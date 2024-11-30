def init_tree(arr, tree, node, start, end):
    if start == end:  # 리프 노드에 도달했을 때
        tree[node] = arr[start]  # 배열의 값을 트리에 저장
        return tree[node]
    mid = (start + end) // 2  # 구간을 반으로 나눔
    # 왼쪽 자식과 오른쪽 자식을 재귀적으로 초기화하고 그 합을 현재 노드에 저장
    tree[node] = init_tree(arr, tree, node*2, start, mid) + init_tree(arr, tree, node*2+1, mid+1, end)
    return tree[node]

def update_tree(tree, node, start, end, index, diff):
    if index < start or index > end:  # 업데이트할 인덱스가 현재 구간을 벗어난 경우
        return
    tree[node] += diff  # 현재 노드의 값을 변경
    if start != end:  # 리프 노드가 아니면 자식 노드도 업데이트
        mid = (start + end) // 2
        update_tree(tree, node*2, start, mid, index, diff)  # 왼쪽 자식
        update_tree(tree, node*2+1, mid+1, end, index, diff)  # 오른쪽 자식

def binary_search(tree, n, target):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        # 현재 mid까지의 합이 target보다 크거나 같으면 
        # 답이 더 왼쪽에 있을 수 있으므로 오른쪽 범위를 줄임
        if get_sum(tree, 1, 0, n-1, 0, mid-1) >= target:
            right = mid
        else:
            left = mid + 1
    return left

def get_sum(tree, node, start, end, left, right):
    if left > end or right < start:  # 구하려는 구간과 현재 구간이 겹치지 않는 경우
        return 0
    if left <= start and end <= right:  # 구하려는 구간이 현재 구간을 완전히 포함하는 경우
        return tree[node]
    # 구간이 일부만 겹치는 경우 왼쪽, 오른쪽 자식의 합을 재귀적으로 계산
    mid = (start + end) // 2
    return get_sum(tree, node*2, start, mid, left, right) + get_sum(tree, node*2+1, mid+1, end, left, right)

N = int(input())
army = list(map(int, input().split()))
M = int(input())
orders = [list(map(int, input().split())) for _ in range(M)]

# Initialize segment tree
size = 1
while size < N:
    size *= 2
tree = [0] * (2 * size)
init_tree(army, tree, 1, 0, N-1)

# Process queries
for order in orders:
    if order[0] == 1:  # Update operation
        idx = order[1] - 1
        diff = order[2]
        army[idx] += diff
        update_tree(tree, 1, 0, N-1, idx, diff)
    else:  # Query operation
        target = order[1]
        result = binary_search(tree, N, target)
        print(result)