'''
프로그래머스 - lv 2. 교점에 별 만들기 / 구현, 수학(약간)
- https://school.programmers.co.kr/learn/courses/30/lessons/87377
'''

def get_intersection_point(line1, line2):
    A, B, C = line1
    D, E, F = line2
    
    det = A*E - B*D
    if det == 0:
        return None
    
    return (B*F - C*E) / det, (C*D - A*F) / det

def get_min_max(intersection_points):
    min_x, max_x = float('inf'), float('-inf')
    min_y, max_y = float('inf'), float('-inf')
    
    for x, y in intersection_points:
        if min_x > x: min_x = x
        if max_x < x: max_x = x
        if min_y > y: min_y = y
        if max_y < y: max_y = y
    
    return min_x, min_y, max_x, max_y


def get_maps(min_x, min_y, max_x, max_y, intersection_points):
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    
    result = [['.' for _ in range(width)] for _ in range(height)]
    
    for x, y in intersection_points:
        col = x - min_x
        row = max_y - y
        result[row][col] = '*'
    
    return result

def solution(line):
    intersection_points = []
    n = len(line)
    
    for i in range(n):
        for j in range(i+1, n):
            result = get_intersection_point(line[i], line[j])
            if result is None:
                continue
            else:
                x, y = result
                if x == int(x) and y == int(y):
                    intersection_points.append((int(x), int(y)))
    
    # print(intersection_points)
    min_x, min_y, max_x, max_y = get_min_max(intersection_points)
    result = get_maps(min_x, min_y, max_x, max_y, intersection_points)   
    
    answer = []
    for i in range(len(result)):
        answer.append(''.join(result[i]))
    
    return answer
