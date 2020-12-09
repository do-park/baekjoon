# 7785 회사에 있는 사람

from sys import stdin

name, access = 0, 1
company = set()
N = int(stdin.readline())
for tc in range(N):
    log = list(map(str, stdin.readline().split()))
    if log[access] == 'enter':
        company.add(log[name])
    else:
        company.remove((log[name]))
print('\n'.join(sorted(list(company), reverse=True)))