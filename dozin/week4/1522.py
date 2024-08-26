string = input()
a_cnt = string.count('a')    # a의 개수
string += string[0:a_cnt-1]    # 원형 처리
min_val = 1001

for i in range(len(string)-(a_cnt-1)):
    # 윈도우 내부의 b와 외부의 a 교환하면 a 모두 연속
    min_val = min(min_val, string[i:i+a_cnt].count('b'))
print(min_val)