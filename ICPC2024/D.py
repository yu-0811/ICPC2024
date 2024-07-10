import sys
def input():return sys.stdin.readline().rstrip()
if len(sys.argv) == 2: sys.stdin = open(sys.argv[1])

from collections import defaultdict
while True:
  n = int(input())
  if n==0: exit()
  a,b,d = map(int,input().split())
  XY = set() # 障害物がある場所を記録
  for _ in range(n):
    x,y = map(int,input().split())
    XY.add((x,y))
  f = 0 # 進行方向 0が左向き
  DXY = [(1,0),(0,1),(-1,0),(0,-1)] # 移動時の座標変化
  dist = defaultdict(int)
  SUM = 0 # 初期位置からの移動距離

  # 現在地(a,b)
  while d>0:
    if a<0 or a>100 or b<0 or b>100:
      a += DXY[f][0] * d
      b += DXY[f][1] * d
      break
    # 移動先に障害物があるなら方向転換
    while (a+DXY[f][0],b+DXY[f][1]) in XY:
      f += 1
      f %= 4
    a += DXY[f][0]
    b += DXY[f][1]
    SUM += 1
    d -= 1
    if dist[(a,b,f)]==0: # 初めて訪れたなら
      dist[(a,b,f)] = SUM
    else: # ループしているなら
      roop_distance = SUM - dist[(a,b,f)]
      d %= roop_distance

  print(a,b) # 解答出力