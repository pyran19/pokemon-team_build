import pygame
import math
import numpy as np

# ウィンドウサイズ
WIDTH = 800
HEIGHT = 600

# 色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Node:
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y

class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

# 6個のNodeの作成
nodes = [
    Node("0",  400,   40),
    Node("1",  525,  257),
    Node("2",  400,  473),
    Node("3",  150,  473),
    Node("4",   25,  257),
    Node("5",  150,   40)
]

def mkEdges(shape):
    edges=[]
    for i in range(5):
        for j in range(5):
            if shape[i][j]:
                edges.append(Edge(nodes[i+1],nodes[j]))
    return edges

def draw_hexagon(edges):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hexagon")

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill(WHITE)

        # エッジを描画
        for edge in edges:
            pygame.draw.line(screen, BLACK, (edge.node1.x, edge.node1.y), (edge.node2.x, edge.node2.y), 1)

        # ノードを描画
        for edge in edges:
            pygame.draw.circle(screen, RED, (edge.node1.x, edge.node1.y), 15)
            pygame.draw.circle(screen, RED, (edge.node2.x, edge.node2.y), 15)
            
            # ノードの名前を表示
            font = pygame.font.Font(None, 20)
            label1 = font.render(edge.node1.label, True, BLACK)
            label2 = font.render(edge.node2.label, True, BLACK)
            screen.blit(label1, (edge.node1.x - 4, edge.node1.y - 7))
            screen.blit(label2, (edge.node2.x - 4, edge.node2.y - 7))

        pygame.display.flip()
        clock.tick(60)

if __name__=="__main__":
    synergy=[
        [1,0,0,0,0],
        [0,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,0],
        [0,0,0,0,1]
    ]
    synergy=np.array(synergy)
    shape=synergy>0.5
    
    # Edgeの指定
    edges = mkEdges(shape)
    # 図形の描画
    draw_hexagon(edges)


