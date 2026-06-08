import random

N = 4          # 网页数量
d = 0.85       # 阻尼因子
delt = 0.00001 # 收敛阈值


def matrix_multi(A, B):
    """矩阵乘法 A * B"""
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])
    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            total = 0
            for k in range(cols_A):
                total += A[i][k] * B[k][j]
            result[i][j] = total
    return result


def matrix_multiN(n, A):
    """矩阵每个元素乘以常数 n"""
    rows = len(A)
    cols = len(A[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = n * A[i][j]
    return result


def matrix_add(A, B):
    """矩阵加法"""
    rows = len(A)
    cols = len(A[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]
    return result


def pageRank(M):
    """
    计算 PageRank
    M: 转移概率矩阵（已转置）
    """
    e = [1] * N
    r = [[(1 - d) * 1.0 / N] for _ in e]  # (1-d)/n 向量

    # 初始化 P 为随机列向量
    P = [[random.random()] for _ in range(N)]

    norm = float('inf')
    while norm > delt:
        new_P = matrix_add(r, matrix_multiN(d, matrix_multi(M, P)))
        # 计算一阶范数差
        norm = sum(abs(new_P[i][0] - P[i][0]) for i in range(N))
        P = new_P

    # 输出结果
    for i, val in enumerate(P):
        print(f"PageRank of page {i + 1}: {val[0]:.6f}")


def tran_and_convert(A):
    """
    根据邻接矩阵求转移概率矩阵并转置
    """
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        row_sum = sum(A[i])
        if row_sum == 0:
            # 如果某行全为0，则均匀跳转
            for j in range(n):
                result[i][j] = 1.0 / n
        else:
            for j in range(n):
                result[i][j] = A[i][j] / row_sum
    # 转置
    return [[result[j][i] for j in range(n)] for i in range(n)]


def main():
    A = [[0, 1, 1, 0], # 行0: 页面0 → 页面1, 页面2
         [1, 0, 0, 1], # 行1: 页面1 → 页面0, 页面3
         [1, 0, 0, 1], # 行2: 页面2 → 页面0, 页面3
         [1, 1, 0, 0]] # 行3: 页面3 → 页面0, 页面1
    M = tran_and_convert(A)
    pageRank(M)


if __name__ == '__main__':
    main()
