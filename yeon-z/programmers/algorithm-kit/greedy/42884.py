# 단속 카메라
# 현재 코드
def solution(routes):
    routes.sort(key=lambda x: x[0])
    answer = 0
    camera = -30001

    for s, e in routes:
        if s > camera:
            camera = e
            answer += 1
        else:
            camera = min(camera, e)
    return answer

# 이전 코드
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[0])
    camera = -30001

    for s, e in routes:
        print(s, e, camera, answer)
        if s > camera:
            camera = e
            answer += 1
        camera = min(camera, e)

    return answer