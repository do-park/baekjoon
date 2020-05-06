# BOJ 17136 색종이 붙이기
# 예제 5번 오답
# 하드 코딩 말고...

maps = [list(map(int, input().split())) for _ in range(10)]
paper = [0, 5, 5, 5, 5, 5]
visited = [[False] * 10 for _ in range(10)]
count = 0
for i in range(10):
    for j in range(10):
        if maps[i][j] and not visited[i][j]:
            print(f'maps[{i}][{j}]')
            visited[i][j] = True
            total = 1
            max_p = 1
            if i + 1 < 10 and j + 1 < 10:
                total += maps[i + 1][j] + maps[i][j + 1] + maps[i + 1][j + 1]
                if total == 4:
                    max_p = 2
                    visited[i + 1][j] = visited[i][j + 1] = visited[i + 1][j + 1] = True
            if i + 2 < 10 and j + 2 < 10 and max_p == 2:
                total += maps[i + 2][j] + maps[i + 2][j + 1] + maps[i + 2][j + 2] + maps[i][j + 2] + maps[i + 1][j + 2]
                if total == 9:
                    max_p = 3
                    visited[i + 2][j] = visited[i + 2][j + 1] = visited[i + 2][j + 2] = visited[i][j + 2] = visited[i + 1][j + 2] = True
            if i + 3 < 10 and j + 3 < 10 and max_p == 3:
                total += maps[i + 3][j] + maps[i + 3][j + 1] + maps[i + 3][j + 2] + maps[i + 3][j + 3] + maps[i + 2][j + 3] + maps[i + 1][j + 3] + maps[i][j + 3]
                if total == 16:
                    max_p = 4
                    visited[i + 3][j] = visited[i + 3][j + 1] = visited[i + 3][j + 2] = visited[i + 3][j + 3] = visited[i + 2][j + 3] = visited[i + 1][j + 3] = visited[i][j + 3] = True
            if i + 4 < 10 and j + 4 < 10 and max_p == 4:
                total += maps[i + 4][j] + maps[i + 4][j + 1] + maps[i + 4][j + 2] + maps[i + 4][j + 3] + maps[i + 4][j + 4] + maps[i + 3][j + 4] + maps[i + 2][j + 4] + maps[i + 1][j + 4] + maps[i][j + 4]
                if total == 25:
                    max_p = 5
                    visited[i + 4][j] = visited[i + 4][j + 1] = visited[i + 4][j + 2] = visited[i + 4][j + 3] = visited[i + 4][j + 4] = visited[i + 3][j + 4] = visited[i + 2][j + 4] = visited[i + 1][j + 4] = visited[i][j + 4] = True
            print(max_p)
            if paper[max_p]:
                paper[max_p] -= 1
                count += 1
            else:
                if max_p == 3:
                    if paper[2] and paper[1] >= 5:
                        paper[2] -= 1
                        paper[1] -= 5
                        count += 6
                    else:
                        count = -1
                        break
                if max_p == 2:
                    if paper[1] >= 4:
                        paper[1] -= 4
                        count += 4
                    else:
                        count = -1
                        break
                count = -1
                break
    if count == -1:
        break
for i in range(10):
    print(visited[i])
print()
print(count)
print()
print(paper)