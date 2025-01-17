def solution(board, moves):
    bucket = []
    answer = 0

    for move in moves:
        index = move - 1

        for row in board:
            if row[index] !=0:
                bucket.append(row[index])
                row[index] = 0
                if len(bucket) > 1 and bucket[-1] == bucket[-2]:
                    answer+=2
                    bucket.pop()
                    bucket.pop()
                break

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(f"answer is {solution(board, moves)}")
