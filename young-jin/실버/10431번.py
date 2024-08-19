def sorting(students):
    answer = 0
    result = [] # 정렬된 리스트를 따로 생성. 리스트를 따로 생성하지 않고 기존의 리스트에서 각 숫자와 그 숫자 뒤에 있는 모든 숫자들을 비교해도 됨
    result.append(students[0])

    for i in range(1,20):
        student = students[i]
        for j in range(i-1, -1, -1): # 앞에 있는 숫자와 비교
            if students[j] > student:
                result.insert(j, student) # students[i], students[j] = students[j], students[i]
                answer += 1

    return answer

p = int(input())
for _ in range(p):
    t, *students = list(map(int,input().split()))
    ans = sorting(students)
    print(t, ans)