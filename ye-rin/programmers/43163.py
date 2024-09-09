from collections import deque

def solution(begin, target, words):
    # 목표 단어가 단어 목록에 없으면 변환 불가능
    if target not in words:
        return 0
    
    def compare_words(word1, word2):
        """
        두 단어가 한 글자만 다른지 확인하는 함수
        :param word1: 첫 번째 단어
        :param word2: 두 번째 단어
        :return: 한 글자만 다르면 True, 그렇지 않으면 False
        """
        # zip으로 두 단어의 문자를 쌍으로 만들고, 다른 문자의 개수를 세어 1인 경우 True 반환
        return sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1
    
    # BFS를 위한 큐 초기화: (단어, 변환 단계) 튜플을 저장
    queue = deque([(begin, 0)])
    # 방문한 단어를 기록하는 집합
    visited = set([begin])
    
    while queue:
        # 큐에서 현재 단어와 변환 단계를 가져옴
        current_word, steps = queue.popleft()
        
        # 현재 단어가 목표 단어와 같으면 현재까지의 변환 단계 반환
        if current_word == target:
            return steps
        
        # 단어 목록의 모든 단어에 대해 검사
        for word in words:
            # 아직 방문하지 않은 단어이고, 현재 단어와 한 글자만 다른 경우
            if word not in visited and compare_words(current_word, word):
                # 방문 처리
                visited.add(word)
                # 큐에 새 단어와 증가된 변환 단계를 추가
                queue.append((word, steps + 1))
    
    # 모든 가능한 변환을 시도했지만 목표 단어에 도달하지 못한 경우
    return 0