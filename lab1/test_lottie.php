<?php

/**
 * Простой скрипт для проверки валидации Lottie файлов
 * Проверяет bad_lottie.json и good_lottie.json на наличие отсутствующих свойств 'i' в keyframes
 */

// Путь к файлам (замените на свои пути)
$badLottiePath = './bad_lottie.json';
$goodLottiePath = './good_lottie.json';
$goodLottiePath_1 = './good_lottie_1.json';


// Валидатор keyframes для Lottie файлов
class LottieKeyframeValidator {
    /**
     * Проверяет обязательные свойства в ключевых кадрах анимации Lottie
     *
     * @param mixed[] $decoded_body Декодированная Lottie анимация
     * @return array [проверенный массив, массив критических ошибок]
     */
    public static function validateKeyframes(array $decoded_body): array {
        $errors = [];
        
        // Рекурсивно проверяем структуру lottie
        self::validateKeyframesRecursively($decoded_body, '', $errors);
        
        return [$decoded_body, $errors];
    }
    
    /**
     * Рекурсивно проверяет структуру Lottie на наличие обязательных полей в ключевых кадрах
     * 
     * @param mixed $data Часть Lottie структуры для проверки
     * @param string $path Текущий путь в JSON структуре
     * @param array &$errors Массив для записи критических ошибок
     */
    private static function validateKeyframesRecursively($data, string $path, array &$errors): void {
        if (!is_array($data)) {
            return;
        }

        // Специальная проверка для конкретного формата keyframes из bad_lottie.json
        // Проверяем только путь layers/X/ks/r/k
        if ($path && preg_match('#^layers/\d+/ks/r/k$#', $path)) {
            // Проверяем формат массива как в bad_lottie.json
            if (is_array($data) && self::isAnimationKeyframeArray($data)) {
                foreach ($data as $index => $keyframe) {
                    if (is_array($keyframe) && isset($keyframe['t']) && isset($keyframe['s']) && !isset($keyframe['i'])) {
                        $keyframePath = $path . '/' . $index;
                        $errors[] = "$keyframePath error Base Keyframe must have required property 'i' Base Keyframe";
                    }
                }
            }
        }
        
        // Рекурсивно проверяем все вложенные элементы
        foreach ($data as $key => $value) {
            if (is_array($value)) {
                $newPath = $path ? "$path/$key" : $key;
                self::validateKeyframesRecursively($value, $newPath, $errors);
            }
        }
    }
    
    /**
     * Проверяет, является ли массив набором keyframes в формате как в bad_lottie.json
     * 
     * @param array $array Массив для проверки
     * @return bool True если это массив keyframes требующих 'i'
     */
    private static function isAnimationKeyframeArray(array $array): bool {
        if (empty($array) || !is_array($array)) {
            return false;
        }
        
        // Проверяем, что это массив объектов с t и s
        $hasKeyframeFormat = false;
        foreach ($array as $item) {
            if (!is_array($item)) {
                return false;
            }
            
            // Проверяем формат как в bad_lottie.json - keyframe с t и s
            if (isset($item['t']) && isset($item['s']) && is_array($item['s'])) {
                $hasKeyframeFormat = true;
                
                // Если хотя бы один keyframe имеет 'i', то этот формат не требует обязательного 'i'
                if (isset($item['i'])) {
                    // Это good_lottie.json формат, где 'i' необязательно
                    return false;
                }
            }
        }
        
        // Возвращаем true только если все элементы соответствуют формату keyframes из bad_lottie.json
        return $hasKeyframeFormat;
    }
}

// Функция для чтения и проверки Lottie файла
function validateLottieFile(string $filePath) {
    echo "Проверка файла: $filePath\n";
    
    // Проверяем существование файла
    if (!file_exists($filePath)) {
        echo "Ошибка: Файл не найден!\n";
        return;
    }
    
    // Читаем и декодируем JSON
    $jsonContent = file_get_contents($filePath);
    $lottieData = json_decode($jsonContent, true);
    
    if (json_last_error() !== JSON_ERROR_NONE) {
        echo "Ошибка декодирования JSON: " . json_last_error_msg() . "\n";
        return;
    }
    
    // Запускаем валидацию
    [, $errors] = LottieKeyframeValidator::validateKeyframes($lottieData);
    
    // Выводим результаты
    echo "Результаты проверки:\n";
    if (empty($errors)) {
        echo "✓ Файл не содержит ошибок.\n";
    } else {
        echo "✗ Найдено " . count($errors) . " ошибок:\n";
        foreach ($errors as $error) {
            echo "  - $error\n";
        }
    }
    echo "\n";
}

// Запускаем проверку обоих файлов
echo "=== Валидация Lottie файлов ===\n\n";
validateLottieFile($badLottiePath);
validateLottieFile($goodLottiePath);
validateLottieFile($goodLottiePath_1);
