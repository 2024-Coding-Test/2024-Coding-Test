import sys
import heapq

numbers = int(input())  # 처리할 명령의 수를 입력받음
heap = []  # 힙을 저장할 빈 리스트 초기화

for _ in range(numbers):
    num = int(sys.stdin.readline())  # 각 명령어(숫자)를 입력받음
    if num != 0:
        heapq.heappush(heap, num)  # 0이 아닌 경우, 힙에 숫자를 추가 (최소 힙 유지)
    else:
        try:
            print(heapq.heappop(heap))  # 0인 경우, 힙에서 가장 작은 수를 꺼내 출력
        except:
            print(0)  # 힙이 비어 있는 경우, 0을 출력