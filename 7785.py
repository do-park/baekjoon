# 7785 회사에 있는 사람

name, access = 0, 1
company = set()
N = int(input())
for tc in range(N):
    log = list(map(str, input().split()))
    if log[access] == 'enter':
        company.add(log[name])
    else:
        company.remove((log[name]))
company = sorted(list(company), reverse=True)
for staff in company:
    print(staff)