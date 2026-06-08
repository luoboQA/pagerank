import numpy as np

def pagerank(M, d=0.85):
    """PageRank算法实现"""
    N = M.shape[1]
    w = np.ones(N) / N  # 初始概率分布
    M_hat = d * M + (1-d) / N  # Google矩阵
    v = M_hat @ w + (1-d)/N
  
    # 迭代直到收敛
    while np.linalg.norm(w - v) >= 1e-10:
        w = v
        v = M_hat @ w + (1-d)/N
  
    return v
