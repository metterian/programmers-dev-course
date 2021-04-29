# DFS : Depth First Search - 깊이 우선 탐색(Stack, Recursive)


def nQueen(lst, row, n):
    """
    lst : 어떤 열에 담았는지 두는 List
    row : 현재 행
    n   : 체스판 사이즈(N*N)
    """
    count = 0
    if row == n:
        return

    for col in range(n):
        lst[row] = col # 인덱스 : row, 값 : col
        # 열(column) 체크
        for i in range(row): # 0 ~ 바로 전까지!
            if

        # 대각 선 체그

    return count


def solution(n):
    sols = [-1] * n
    return nQueen(sols, 0, n)







# 좌상향

# 우상향

# 같은 열

