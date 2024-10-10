def min_length_subarray(s, arr):
    n = len(arr)  # 배열의 크기
    min_length = float('inf')  # 최소 길이를 무한대로 초기화
    left = 0  # 왼쪽 포인터 초기화
    current_sum = 0  # 현재 합 초기화

    # 오른쪽 포인터를 통해 배열을 순회
    for right in range(n):
        current_sum += arr[right]  # 현재 오른쪽 포인터의 값을 합산

        # 현재 합이 s를 초과할 때
        while current_sum > s:
            min_length = min(min_length, right - left + 1)  # 최소 길이 갱신
            current_sum -= arr[left]  # 왼쪽 포인터의 값을 빼고
            left += 1  # 왼쪽 포인터 이동

    return min_length if min_length != float('inf') else 0  # 결과 반환


n, s = map(int, input().split())  # 배열의 크기 n과 합 s
arr = list(map(int, input().split()))

result = min_length_subarray(s, arr)

print(result)