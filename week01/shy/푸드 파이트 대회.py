'''
[level 1] 푸드 파이트 대회 - 134240
https://school.programmers.co.kr/learn/courses/30/lessons/134240
'''

def solution(food):
    ans1 = "".join([str(idx)*(num//2) for idx, num in enumerate(food)])
    return ans1 + "0" + ans1[::-1]
