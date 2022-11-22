
def solution(board,moves):
    lst = []
    count = 0

    for move in moves:
        move -= 1
        for i in range(len(board)):
            if board[i][move] != 0:
                lst.append(board[i][move])
                board[i][move] = 0
                break
        if len(lst) > 1:
            for sel in range(len(lst)-1):
                if lst[sel] == lst[sel+1]:
                    del lst[sel]
                    del lst[sel]
                    count += 2
    return count

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))
