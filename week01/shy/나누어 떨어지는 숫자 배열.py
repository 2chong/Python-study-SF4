def solution(arr, divisor):
    answer = [i for i in arr if i%divisor == 0]
    if not answer:
        return [-1]
    return sorted(answer)
