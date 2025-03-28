

Метрики расстояния: 1 – Евклидово, 2 – стандартизированное Евклидово, 3 – го-
рода, 4 – Махаланобиса, 5 – Минковского (p = 4), 6 –Чебышева.
** Методы связывания: a – ближнего соседа, b – дальнего соседа, c – средней связи,
d – центроидный, e – медианной связи.


1 - Евклидово
$$
d_2(n_i, n_j) = \left[ \sum_{l=1}^{K} (x_{il} - x_{jl})^2 \right]^{\frac{1}{2}}
$$


3 - метрика города (манхэттенское расстояние)

$S_t$ — дисперсия по $t$-му признаку;

$$
d_H(n_i, n_j) = \sum_{l=1}^K |x_{il} - x_{jl}|;
$$

Оно соответствует перемещению **по осям** (в отличие от евклидового расстояния, которое измеряет кратчайшее прямое расстояние).
    

### **Где используется?**

- В задачах, где передвижение возможно только **по решетке** (например, городские улицы, лабиринты).
    
- В машинном обучении при работе с таксономическими или категориальными данными.
    
- В компьютерном зрении и обработке изображений (например, при расчёте различий между пикселями).




Что такое кофенетический коэффициент?

Кофенетический коэффициент корреляции измеряет степень соответствия между исходными расстояниями между объектами и расстояниями, представленными в дендрограмме иерархической кластеризации. Это важный показатель качества кластеризации.
Как интерпретировать значения:

    0.9-1.0: Отличное соответствие (очень высокое качество кластеризации)
    0.8-0.9: Хорошее соответствие
    0.7-0.8: Среднее соответствие
    <0.7: Слабое соответствие (низкое качество кластеризации)

Анализ представленной таблицы: