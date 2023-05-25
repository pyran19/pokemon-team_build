import mkgraph2
import numpy as np


#全選出パターン
selecs=[]
for k in range(6):
    for j in range(k):
        for i in range(j):
            selecs.append([i,j,k])

class Party():
    def __init__(self,synergy):
        self.synergy=np.array(synergy)
    def mkShape(self,threshold):
        self.shape=self.synergy>=threshold                 
                    
#エッジ数の計算
def calcE(selec,shape):
    count = 0
    for i in range(6):
        for j in range(i):
            if shape[i-1][j] and i in selec and j in selec:
                count += 1
    return count

#エッジが2個ある選出数の計算
def count2edge(shape):
    count=0
    for selec in selecs:
        if calcE(selec,shape) == 2:
            count += 1
    return count

#多様性の計算
def calcZ(beta,shape):
    Z=0
    for selec in selecs:
        Z += 2**(beta*calcE(selec,shape))
    return Z/2**(2*beta)

#構築の総当たり
for i in range(1):
    for j in range(2):
        for k in range(3):
            for l in range(4):
                for m in range(5):
                    synergy=[[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]
                    synergy[0][i]=1
                    synergy[1][j]=1
                    synergy[2][k]=1
                    synergy[3][l]=1
                    synergy[4][m]=1
                    party=Party(synergy)
                    party.mkShape(0.5)
                    #Z=calcZ(1,party.shape)
                    Z=count2edge(party.shape)
                    if Z > 7:
                        print(Z)
                        mkgraph2.draw_hexagon(mkgraph2.mkEdges(party.shape))
                    
 
