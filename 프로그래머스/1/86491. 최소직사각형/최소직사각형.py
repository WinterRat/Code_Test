def solution(sizes):
    answer = 0
    nx = 0
    ny = 0
    for size in sizes:
        x,y = sorted(size)
        nx = max(nx,x)
        ny = max(ny,y)
    
    answer = nx * ny
    return answer