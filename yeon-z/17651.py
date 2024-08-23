# 볼 모으기
# 1. 바로 옆에 다른 색깔의 볼이 있으면 그 볼을 모두 뛰어 넘어 옮길 수 있다.
# 즉, 빨간색 볼은 옆에 있는 파란색 볼 무더기를 한 번에 뛰어 넘어 옮길 수 있다.
# 2. 옮길 수 있는 볼의 색깔은 한 가지이다. 즉, 빨간색 볼을 처음에 옮겼으면 다음에도 빨간색 볼만 옮길 수 있다.

# 문제 풀이 접근 방법
# 1. 빨간 공을 왼쪽 끝으로 모으는 경우
# 2. 빨간 공을 오른쪽 끝으로 모으는 경우
# 3. 파란 공을 왼쪽 끝으로 모으는 경우
# 4. 파란 공을 오른쪽 끝으로 모으는 경우
# 위 네가지 중 최소 이동 횟수를 구하면 된다.

# 1. 왼쪽 끝부터 연속된 같은 색 공은 이미 모여있으므로 건너뛴다.
# 2. 그 다움부터 목표 색깔의 공이 나올 때마다 이동 횟수를 1씩 증가시킨다.


from sys import stdin

n = int(stdin.readline())
balls = stdin.readline().strip()

r_count = balls.count('R') # Red ball count
b_count = balls.count('B') # Blue ball count

move_r_left = balls.lstrip('R').count('R')
move_r_right = balls.rstrip('R').count('R')
move_b_left = balls.lstrip('B').count('B')
move_b_right = balls.rstrip('B').count('B')

print(min(move_r_right, move_b_right, move_b_left, move_r_left))