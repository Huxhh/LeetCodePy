import numpy as np


def kmeans(X, k, max_iters=100):
    # 随机初始化聚类中心
    centroids = X[np.random.choice(range(X.shape[0]), size=k, replace=False)]

    for _ in range(max_iters):
        # 计算所有点到所有中心的距离
        dists = np.sqrt(((X[:, np.newaxis] - centroids) ** 2).sum(axis=2))

        # 将每个点分配给最近的聚类中心
        labels = dists.argmin(axis=1)

        # 重新计算聚类中心
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])

        # 如果聚类中心没有变化，我们就完成了
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return centroids, labels

# 测试
np.random.seed(42)
X = np.random.rand(100, 2)
centroids, labels = kmeans(X, 3)

print("Centroids:")
print(centroids)
