# BOJ 14501 퇴사

T, P = 0, 1

def schedule(day, profit):
    global result
    if day > N:
        return
    if day == N:
        result = max(result, profit)
        return
    schedule(day+1, profit)
    schedule(day+timetable[day][T], profit+timetable[day][P])


N = int(input())
timetable = [list(map(int, input().split())) for _ in range(N)]
result = 0
schedule(0, 0)
print(result)