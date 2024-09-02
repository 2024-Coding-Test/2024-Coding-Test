def solution(sizes):
    for i in sizes:
        i.sort(reverse=True)
        print(i)
    
    width = max(size[0] for size in sizes)
    height = max(size[1] for size in sizes)
    
    answer = width * height
    return answer


def solution(sizes):
    max_width = 0
    max_height = 0
    
    for size in sizes:
        width, height = max(size), min(size)
        
        max_width = max(max_width, width)
        max_height = max(max_height, height)
        
    return max_width * max_height