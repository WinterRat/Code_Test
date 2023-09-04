import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(u, parent, weight):
    if u == parent[u]:
        return u
    root = find(parent[u], parent, weight)
    weight[u] += weight[parent[u]]
    parent[u] = root
    return root

def merge(u, v, w, parent, weight):
    rootU = find(u, parent, weight)
    rootV = find(v, parent, weight)
    if rootU == rootV:
        return
    weight[rootU] = weight[v] - weight[u] + w
    parent[rootU] = rootV

def main():
    result = []
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break

        parent = [i for i in range(N+1)]
        weight = [0 for _ in range(N+1)]

        for _ in range(M):
            cmd, *data = input().split()
            if cmd == '!':
                u, v, w = map(int, data)
                merge(u, v, w, parent, weight)
            else:
                u, v = map(int, data)
                if find(u, parent, weight) != find(v, parent, weight):
                    result.append("UNKNOWN")
                else:
                    result.append(weight[u] - weight[v])
                    
    print(*result,sep='\n')

if __name__ == "__main__":
    main()