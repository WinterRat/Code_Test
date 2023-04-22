from sys import stdin

input = stdin.readline
def dfs(graph_dict, start, end):
    visited = set()
    stack = [start]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            if current not in graph_dict:
                continue

            if end in graph_dict[current]:
                return True

            for next in graph_dict[current]:
                if next not in visited:
                    stack.append(next)
    return False

def main():
    n = int(input())
    graph_dict = {}
    p_list = []
    for _ in range(n):
        input_str = input().strip()
        key, value = input_str.split(' is ')
        graph_dict[key] = value
        
    m = int(input())
    for _ in range(m):
        check_str = input().strip()
        start, end = check_str.split(' is ')
        if dfs(graph_dict, start, end):
            p_list.append("T")
        else:
            p_list.append("F")
    for some in p_list:
        print(some)
        
if __name__=="__main__":
    main()