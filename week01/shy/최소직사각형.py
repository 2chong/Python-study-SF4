def solution(sizes):
    newsizes = [sorted(i) for i in sizes]
    width = max(i[1] for i in newsizes)
    length = max(i[0] for i in newsizes)
    return width*length