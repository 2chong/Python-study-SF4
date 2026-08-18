'''
[level 1] 최소직사각형 - 86491
https://school.programmers.co.kr/learn/courses/30/lessons/86491
'''

def solution(sizes):
    newsizes = [sorted(i) for i in sizes]
    width = max(i[1] for i in newsizes)
    length = max(i[0] for i in newsizes)
    return width*length


# return max(max(x) for x in sizes) * max(min(x) for x in sizes)
