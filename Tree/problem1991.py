import sys
from collections import defaultdict
input = sys.stdin.readline

# input
graph = defaultdict(list)

N = int(input())
for _ in range(N):
    a, b, c = input().split()
    graph[a].append(b)
    graph[a].append(c)

# logic
def preorder(node):
    if node == ".":
        return
    
    print(node, end="")
    preorder(graph[node][0])
    preorder(graph[node][1])


def inorder(node):
    if node == ".":
        return
    
    inorder(graph[node][0])
    print(node, end="")
    inorder(graph[node][1])


def postorder(node):
    if node == ".":
        return
    
    postorder(graph[node][0])
    postorder(graph[node][1])
    print(node, end="")

# output
preorder("A")
print()
inorder("A")
print()
postorder("A")