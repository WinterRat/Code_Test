from sys import stdin
from collections import deque

def dfs(tree, start_node):
    visited = [False] * len(tree)
    dist = [0] * len(tree)
    need_visited = [start_node]

    while need_visited:
        current_node = need_visited.pop()
        visited[current_node] = True

        for next_node, leng in tree[current_node]:
            if not visited[next_node]:
                dist[next_node] = dist[current_node] + leng
                need_visited.append(next_node)

    return dist

def main():
    V = int(input())
    tree =[[] for _ in range(V+1)]
    for i in range(1,V+1) :
        input_list = list(map(int, input().split())) # 0부터임
        l = (len(input_list)-2) // 2 # 1 1 2 3 1
        if(l==1) : # 출발점이 안정해져서 연결 노드가 1인 제일 먼 애들 후보로 저장해놓기
            start_hubo = i
            
        for idx in range(l): # 0 1 > 1 3 2 4
            tree[input_list[0]].append((input_list[2*idx+1],input_list[(idx+1)*2]))
            
    # 임의의 시작 후 여기서 나온 값 중 가장 큰애를 시작 노드로 설정 1 2 5 시작 노드중 1, 5 는 11나오는데 2 는 10나옴 
    distance_list = dfs(tree, start_hubo)
    start = distance_list.index(max(distance_list))
    longest_tree = dfs(tree, start)
    diameter = max(longest_tree)
    
    print(diameter)

    
if __name__=="__main__":
    main()