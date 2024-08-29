# def solution(arr):
#     answer = []
#     answer.append(arr[0])
#     for i in range(1, len(arr)):
#         if arr[i] == arr[i-1]:
#             continue
#         else:
#             answer.append(arr[i])
#     return answer

def solution(arr):
    answer = []
    for num in arr:
        if not answer or num != answer[-1]:
            answer.append(num)
    return answer