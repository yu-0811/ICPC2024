import sys
def input():return sys.stdin.readline().rstrip()
if len(sys.argv) == 2: sys.stdin = open(sys.argv[1])

from collections import defaultdict
from bisect import bisect
while True:
  a,b,X,Y,n = map(int,input().split())
  if a==0: exit()
  
  k1 = defaultdict(list) # k1[k] := y=x+k 上にある球の x 座標
  k2 = defaultdict(list) # k2[k] := y=-x+k 上にある球の x 座標
  # コインの座標を入れる
  k1[Y-X].append(X)
  k2[Y+X].append(X)
  XY = [list(map(int,input().split())) for _ in range(n)]
  for x,y in XY:
    k1[y-x].append(x)
    k2[y+x].append(x)
  for k in k1.keys(): k1[k].sort()
  for k in k2.keys(): k2[k].sort()
  OUT = [(0,0),(0,b),(a,0),(a,b)] # 四隅
  vis = set()
  def move(nx,ny):
    x,y,f = nx,ny,0
    while True:
      if f==0:
        ind = bisect(k1[y-x],x)
        # コインにあたるなら True を返す
        if len(k1[y-x])!=0 and ind!=len(k1[y-x]) and y-x==Y-X and k1[y-x][ind]==X: return True
        # 他の障害物にあたるなら False を返す (元の自分の場所に当たらないように注意)
        if ind!=len(k1[y-x]) and not (y-x==ny-nx and k1[y-x][ind]==nx): return False
        # 壁まで移動
        x,y = x+min(a-x,b-y), y+min(a-x,b-y)
        # 向きを変える
        if x==a: f = 1
        elif y==b: f = 3
        
      elif f==1:
        ind = bisect(k2[y+x],x)
        if len(k2[y+x])!=0 and ind!=0 and y+x==Y+X and k2[y+x][ind-1]==X: return True
        if ind!=0 and not (y+x==ny+nx and k2[y+x][ind-1]==nx): return False
        x,y = x-min(x,b-y), y+min(x,b-y)
        if x==0: f = 0
        elif y==b: f = 2
      
      elif f==2:
        ind = bisect(k1[y-x],x)
        if len(k1[y-x])!=0 and ind!=0 and y-x==Y-X and k1[y-x][ind-1]==X: return True
        if ind!=0 and not (y-x==ny-nx and k1[y-x][ind-1]==nx): return False
        x,y = x-min(x,y), y-min(x,y)
        if x==0: f = 3
        elif y==0: f = 1  
      
      elif f==3:
        ind = bisect(k2[y+x],x)
        if len(k2[y+x])!=0 and ind!=len(k2[y+x]) and y+x==Y+X and k2[y+x][ind]==X: return True
        if ind!=len(k2[y+x]) and not (y+x==ny+nx and k2[y+x][ind]==nx): return False
        x,y = x+min(a-x,y), y-min(a-x,y)
        if x==a: f = 2
        elif y==0: f = 0
        
      if (x,y) in OUT: return False
      if (x,y,f) in vis: return False
      vis.add((x,y,f))

  ans = list()
  for i,[x,y] in enumerate(XY): # 球を1つずつ動かす
    if move(XY[i][0],XY[i][1]): ans.append(i+1)
    
  if len(ans)==0: print('No')
  else:
    ans.sort()
    print(*ans)