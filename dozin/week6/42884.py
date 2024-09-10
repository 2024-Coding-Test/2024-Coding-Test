def solution(routes):
    camera = -30001
    routes.sort(key=lambda x: x[1])
    cameraCount = 0
    for route in routes:
        if route[0] > camera:
            cameraCount += 1
            camera = route[1]
    print(routes)
    return cameraCount