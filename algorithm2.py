import numpy as np

# 邻接矩阵
a = np.array([[0, 1, 1, 0],
              [1, 0, 0, 1],
              [1, 0, 0, 1],
              [1, 1, 0, 0]], dtype=float)


def graph_move(a):
    """
    构造转移概率矩阵并转置
    """
    n = a.shape[0]
    # 计算每个节点的出度
    out_degree = a.sum(axis=1)
    M = np.zeros_like(a)
    for i in range(n):
        if out_degree[i] == 0:
            M[i, :] = 1.0 / n  # 悬空节点均匀跳转
        else:
            M[i, :] = a[i, :] / out_degree[i]
    return M.T  # 转置


def first_pr(M):
    """初始化 PageRank 向量"""
    n = M.shape[0]
    return np.ones((n, 1)) / n


def page_rank(p, M, v, tol=1e-6, max_iter=1000):
    """
    迭代计算 PageRank
    p: 阻尼因子
    M: 转移概率矩阵（已转置）
    v: 初始 PR 向量
    """
    n = len(v)
    ones = np.ones((n, 1)) / n  # 均匀向量
    for _ in range(max_iter):
        new_v = p * M @ v + (1 - p) * ones
        if np.linalg.norm(new_v - v, ord=1) < tol:
            break
        v = new_v
    return v


if __name__ == "__main__":
    M = graph_move(a)
    pr = first_pr(M)
    p = 0.85
    result = page_rank(p, M, pr)
    for i, val in enumerate(result):
        print(f"PageRank of page {i + 1}: {val[0]:.6f}")