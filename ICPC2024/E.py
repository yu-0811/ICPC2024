import sys
def input():return sys.stdin.readline().rstrip()
if len(sys.argv) == 2: sys.stdin = open(sys.argv[1])

def c1_equal_cN(ans,C):
  for j in range(len(C)): ans[0][j] = C[N-j-1]
  for i in range(len(C)): ans[i][0] = C[i]
  for i in range(len(C)): ans[i][N-1] = C[N-i-1]
  for j in range(len(C)): ans[N-1][j] = C[j]
  print('Yes')
  for i in range(len(C)): print(*ans[i])

while True:
  N = int(input())
  if N==0: exit()
  C = list(map(int,input().split()))
  ans = [[0]*N for _ in range(N)]
  if C[0]==C[N-1]:
    c1_equal_cN(ans,C)
    continue
  ci,cj = -1,-1
  for i in range(1,N-1):
    if C[i]==C[N-1] and ci==-1: ci = i
    elif C[i]==C[0] and ci!=-1: 
      cj = i
      break
  if ci==-1 or cj==-1:
    print('No')
    continue
  
  for j in range(N): # 南から見たとき
    if j<ci: ans[cj][j] = C[j]
    elif ci<=j<=cj: ans[N-1][j] = C[j]
    elif cj<j: ans[N-ci-1][j] = C[j]
  for i in range(N): # 西から見たとき
    if i<ci: ans[i][N-cj-1] = C[i]
    elif ci<=i<=cj: ans[i][0] = C[i]
    elif cj<i: ans[i][ci] = C[i]
  C = C[::-1]
  for j in range(N): # 北から見たとき
    if j<N-cj-1: ans[ci][j] = C[j]
    elif N-cj-1<=j<=N-ci-1: ans[0][j] = C[j]
    elif N-ci-1<j: ans[N-cj-1][j] = C[j]
  for i in range(N): # 東からみたとき
    if i<N-cj-1: ans[i][N-ci-1] = C[i]
    elif N-cj-1<=i<=N-ci-1: ans[i][N-1] = C[i]
    elif N-ci-1<i: ans[i][cj] = C[i]
  
  print('Yes')
  for i in range(N): print(*ans[i])