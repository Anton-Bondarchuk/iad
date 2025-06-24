import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd
from itertools import combinations
import random

class CLARA:
    def __init__(self, n_clusters, sample_size=None, n_samples=5, random_state=42):
        self.n_clusters = n_clusters
        self.sample_size = sample_size
        self.n_samples = n_samples
        self.random_state = random_state
        self.best_medoids = None
        self.labels_ = None
        self.cluster_centers_ = None
        
    def _pam_on_sample(self, sample_data):
        n_points = len(sample_data)
        
        np.random.seed(self.random_state)
        medoid_indices = np.random.choice(n_points, self.n_clusters, replace=False)
        medoids = sample_data[medoid_indices]
        
        improved = True
        iteration = 0
        max_iterations = 100
        
        while improved and iteration < max_iterations:
            improved = False
            iteration += 1
            
            distances = np.sqrt(((sample_data[:, np.newaxis] - medoids) ** 2).sum(axis=2))
            labels = np.argmin(distances, axis=1)
            
            for i in range(self.n_clusters):
                cluster_points = sample_data[labels == i]
                if len(cluster_points) == 0:
                    continue
                    
                current_cost = np.sum(np.min(distances, axis=1))
                
                for point in cluster_points:
                    temp_medoids = medoids.copy()
                    temp_medoids[i] = point
                    
                    temp_distances = np.sqrt(((sample_data[:, np.newaxis] - temp_medoids) ** 2).sum(axis=2))
                    temp_cost = np.sum(np.min(temp_distances, axis=1))
                    
                    if temp_cost < current_cost:
                        medoids[i] = point
                        improved = True
                        break
        
        distances = np.sqrt(((sample_data[:, np.newaxis] - medoids) ** 2).sum(axis=2))
        cost = np.sum(np.min(distances, axis=1))
        
        return medoids, cost
    
    def fit(self, X):
        X = np.array(X)
        n_points = len(X)
        
        if self.sample_size is None:
            self.sample_size = min(40 + 2 * self.n_clusters, n_points)
        
        best_cost = float('inf')
        best_medoids = None
        
        for sample_num in range(self.n_samples):
            np.random.seed(self.random_state + sample_num)
            sample_indices = np.random.choice(n_points, min(self.sample_size, n_points), replace=False)
            sample_data = X[sample_indices]
            
            medoids, cost = self._pam_on_sample(sample_data)
            
            if cost < best_cost:
                best_cost = cost
                best_medoids = medoids
        
        self.best_medoids = best_medoids
        self.cluster_centers_ = best_medoids
        
        distances = np.sqrt(((X[:, np.newaxis] - best_medoids) ** 2).sum(axis=2))
        self.labels_ = np.argmin(distances, axis=1)
        
        return self
    
    def predict(self, X):
        X = np.array(X)
        distances = np.sqrt(((X[:, np.newaxis] - self.best_medoids) ** 2).sum(axis=2))
        return np.argmin(distances, axis=1)

def load_data(filename):
    try:
        data = np.loadtxt(filename)
        return data
    except FileNotFoundError:
        print(f"File {filename} not found. Using provided data instead.")
        data = np.array([
            [0.78113008, 2.52359477], [2.33869002, 3.28532404], [3.53563913, 3.29244045],
            [1.03617463, 2.40948153], [2.37348794, 3.41119026], [3.52101489, 3.87102102],
            [0.83382005, 2.35208722], [2.11321877, 2.94555377], [3.61689683, 4.14400681],
            [0.76080354, 2.29836077], [2.44479006, 3.24341460], [4.00920778, 3.26311756],
            [0.62424063, 2.21970969], [2.88085879, 3.36104868], [3.41369460, 3.78243217],
            [0.83966176, 2.74217569], [2.23341947, 3.47695390], [3.75752648, 3.70405224],
            [0.90025615, 2.48720413], [1.98810809, 3.15998146], [3.51998518, 3.46645416],
            [1.21562440, 2.10930619], [2.01472038, 2.88071479], [3.86645530, 3.56931529],
            [0.41663123, 2.69278186], [2.66049099, 3.43324671], [3.58842364, 3.51557323],
            [0.70868786, 2.81770650], [2.57315731, 3.04915755], [3.78867153, 3.83857327],
            [0.82232470, 2.19921285], [2.31399089, 2.68589756], [3.07490873, 4.37813311],
            [0.91276842, 3.23749480], [2.15493592, 3.28354800], [3.82378628, 3.71986751],
            [0.77785155, 2.87841057], [1.96689577, 3.47382759], [3.39363376, 3.99648765],
            [1.18873251, 2.19985176], [2.38782933, 3.54141957], [3.23121696, 3.88206753],
            [0.92332704, 2.08053131], [2.14540134, 3.18343448], [3.22175171, 3.18716959],
            [0.66151685, 2.44714836], [1.71088404, 3.61048823], [3.36669414, 3.15425597],
            [0.96763630, 2.89510626], [2.24383165, 3.28015927], [3.53876078, 3.82550627],
            [1.19901335, 2.50351030], [2.45451963, 3.38397542], [3.58638820, 3.85746464],
            [0.63950876, 2.16559575], [2.22401375, 3.33786863], [3.27841151, 4.01706672],
            [0.96722423, 3.26831517], [2.35125475, 2.83950646], [3.66196610, 3.92328451]
        ])
        return data

def determine_optimal_clusters(data, max_k=8):
    inertias = []
    silhouette_scores = []
    K_range = range(2, max_k + 1)
    
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(data)
        inertias.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(data, kmeans.labels_))
    
    return K_range, inertias, silhouette_scores

def plot_original_data(data):
    plt.figure(figsize=(8, 6))
    plt.scatter(data[:, 0], data[:, 1], alpha=0.7, s=50, c='blue')
    plt.title('Исходные данные (диаграмма рассеяния)', fontsize=14)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_elbow_method(K_range, inertias):
    plt.figure(figsize=(8, 6))
    plt.plot(K_range, inertias, 'bo-', linewidth=2, markersize=8)
    plt.title('Метод локтя', fontsize=14)
    plt.xlabel('Количество кластеров (k)')
    plt.ylabel('Инерция')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_silhouette_analysis(K_range, silhouette_scores):
    plt.figure(figsize=(8, 6))
    plt.plot(K_range, silhouette_scores, 'ro-', linewidth=2, markersize=8)
    plt.title('Анализ силуэта', fontsize=14)
    plt.xlabel('Количество кластеров (k)')
    plt.ylabel('Силуэтный коэффициент')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_clara_clusters(data, clara_model, k):
    plt.figure(figsize=(10, 8))
    
    colors = plt.cm.Set1(np.linspace(0, 1, k))
    
    for i in range(k):
        cluster_points = data[clara_model.labels_ == i]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], 
                   c=[colors[i]], label=f'Кластер {i+1}', alpha=0.7, s=60)
    
    medoids = clara_model.cluster_centers_
    plt.scatter(medoids[:, 0], medoids[:, 1], 
               c='black', marker='x', s=300, linewidths=4, label='Медоиды')
    
    plt.title(f'Результаты кластеризации CLARA (k={k})', fontsize=14)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_clara_boundaries(data, clara_model, k):
    plt.figure(figsize=(10, 8))
    
    colors = plt.cm.Set1(np.linspace(0, 1, k))
    
    x_min, x_max = data[:, 0].min() - 0.5, data[:, 0].max() + 0.5
    y_min, y_max = data[:, 1].min() - 0.5, data[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    
    mesh_points = np.c_[xx.ravel(), yy.ravel()]
    mesh_labels = clara_model.predict(mesh_points)
    mesh_labels = mesh_labels.reshape(xx.shape)
    
    plt.contourf(xx, yy, mesh_labels, alpha=0.3, colors=colors[:k])
    
    for i in range(k):
        cluster_points = data[clara_model.labels_ == i]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], 
                   c=[colors[i]], label=f'Кластер {i+1}', alpha=0.8, s=60)
    
    medoids = clara_model.cluster_centers_
    plt.scatter(medoids[:, 0], medoids[:, 1], 
               c='black', marker='x', s=300, linewidths=4, label='Медоиды')
    
    plt.title(f'Кластеры с границами (k={k})', fontsize=14)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def analyze_clusters(data, K_range, inertias, silhouette_scores):
    diffs = np.diff(inertias)
    diffs2 = np.diff(diffs)
    elbow_k = K_range[np.argmax(diffs2)] if len(diffs2) > 0 else 3
    
    silhouette_k = K_range[np.argmax(silhouette_scores)]
    
    print(f"Рекомендуемое количество кластеров:")
    print(f"  - По методу локтя: {elbow_k}")
    print(f"  - По силуэтному анализу: {silhouette_k}")
    
    return silhouette_k

def print_cluster_info(data, clara_model, k):
    print(f"\n{'='*60}")
    print(f"РЕЗУЛЬТАТЫ КЛАСТЕРИЗАЦИИ CLARA (k={k})")
    print(f"{'='*60}")
    
    medoids = clara_model.cluster_centers_
    
    for i in range(k):
        cluster_points = data[clara_model.labels_ == i]
        cluster_size = len(cluster_points)
        
        print(f"\nКластер {i+1}:")
        print(f"  Медоид (центр): ({medoids[i][0]:.6f}, {medoids[i][1]:.6f})")
        print(f"  Количество точек: {cluster_size}")
        print(f"  Процент от общего: {cluster_size/len(data)*100:.1f}%")
        
        if cluster_size > 0:
            mean_x = np.mean(cluster_points[:, 0])
            mean_y = np.mean(cluster_points[:, 1])
            std_x = np.std(cluster_points[:, 0])
            std_y = np.std(cluster_points[:, 1])
            
            print(f"  Среднее: ({mean_x:.6f}, {mean_y:.6f})")
            print(f"  Стд. отклонение: ({std_x:.6f}, {std_y:.6f})")
    
    if len(set(clara_model.labels_)) > 1:
        sil_score = silhouette_score(data, clara_model.labels_)
        print(f"\nОбщий силуэтный коэффициент: {sil_score:.4f}")

def main():
    print("КЛАСТЕРИЗАЦИЯ МЕТОДОМ CLARA")
    print("="*50)
    
    data = load_data('data2.txt')
    print(f"Загружено {len(data)} точек данных")
    
    print("\n1. Построение диаграммы рассеяния исходных данных...")
    plot_original_data(data)
    
    print("\n2. Анализ оптимального количества кластеров...")
    K_range, inertias, silhouette_scores = determine_optimal_clusters(data)
    
    print("\n3. График метода локтя...")
    plot_elbow_method(K_range, inertias)
    
    print("\n4. График анализа силуэта...")
    plot_silhouette_analysis(K_range, silhouette_scores)
    
    optimal_k = analyze_clusters(data, K_range, inertias, silhouette_scores)
    
    print(f"\n5. Применение алгоритма CLARA с k={optimal_k}...")
    clara = CLARA(n_clusters=optimal_k, n_samples=10, random_state=42)
    clara.fit(data)
    
    print("\n6. Визуализация кластеров...")
    plot_clara_clusters(data, clara, optimal_k)
    
    print("\n7. Визуализация границ кластеров...")
    plot_clara_boundaries(data, clara, optimal_k)
    
    print_cluster_info(data, clara, optimal_k)
    
    print(f"\n8. Сравнение с другими значениями k...")
    for k in [2, 3, 4]:
        if k != optimal_k:
            print(f"\nТестирование k={k}:")
            clara_test = CLARA(n_clusters=k, n_samples=5, random_state=42)
            clara_test.fit(data)
            if len(set(clara_test.labels_)) > 1:
                sil_score = silhouette_score(data, clara_test.labels_)
                print(f"  Силуэтный коэффициент: {sil_score:.4f}")

if __name__ == "__main__":
    main()