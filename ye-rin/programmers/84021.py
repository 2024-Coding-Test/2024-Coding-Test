from typing import List
import copy

def solution(game_board: List[List[int]], table: List[List[int]]) -> int:
    def find_pieces(board: List[List[int]], target: int) -> List[List[List[int]]]:
        """
        주어진 보드에서 연결된 target 값의 조각들을 찾아 반환
        
        Args:
            board: 게임 보드 또는 테이블
            target: 찾고자 하는 값 (0: 빈 공간, 1: 퍼즐 조각)
        
        Returns:
            찾은 조각들의 리스트. 각 조각은 좌표 리스트로 표현됩니다.
        """
        pieces = []
        visited = [[False] * len(board) for _ in range(len(board))]
        
        def dfs(x: int, y: int, piece: List[List[int]]) -> None:
            """
            DFS를 사용하여 연결된 조각 탐색
            
            Args:
                x, y: 현재 위치
                piece: 현재까지 찾은 조각의 좌표 리스트
            """
            # 보드 범위를 벗어나거나, 이미 방문했거나, target 값이 아니면 종료
            if x < 0 or x >= len(board) or y < 0 or y >= len(board) or visited[x][y] or board[x][y] != target:
                return
            
            visited[x][y] = True
            piece.append([x, y])
            
            # 상하좌우 네 방향으로 탐색 진행
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(x + dx, y + dy, piece)
        
        # 보드의 모든 위치에 대해 DFS 수행
        for i in range(len(board)):
            for j in range(len(board)):
                if not visited[i][j] and board[i][j] == target:
                    piece = []
                    dfs(i, j, piece)
                    if piece:
                        pieces.append(piece)
        
        return pieces

    def normalize_piece(piece: List[List[int]]) -> List[List[int]]:
        """
        조각의 좌표를 (0,0)을 기준으로 정규화
        
        Args:
            piece: 정규화할 조각의 좌표 리스트
        
        Returns:
            정규화된 조각의 좌표 리스트
        """
        min_x = min(p[0] for p in piece)
        min_y = min(p[1] for p in piece)
        return [[x - min_x, y - min_y] for x, y in piece]

    def rotate_piece(piece: List[List[int]]) -> List[List[int]]:
        """
        조각을 90도 시계 방향으로 회전
        
        Args:
            piece: 회전시킬 조각의 좌표 리스트
        
        Returns:
            회전된 조각의 좌표 리스트
        """
        return [[y, -x] for x, y in piece]

    def fit_piece(board: List[List[int]], piece: List[List[int]]) -> bool:
        """
        주어진 조각을 게임 보드의 빈 공간에 맞출 수 있는지 확인
        
        Args:
            board: 게임 보드
            piece: 맞춰볼 조각의 좌표 리스트
        
        Returns:
            조각을 맞출 수 있으면 True, 아니면 False
        """
        for i in range(len(board)):
            for j in range(len(board)):
                if can_place_piece(board, piece, i, j):
                    place_piece(board, piece, i, j, 1)  # 조각을 보드에 배치
                    return True
        return False

    def can_place_piece(board: List[List[int]], piece: List[List[int]], start_x: int, start_y: int) -> bool:
        """
        특정 위치에 조각을 놓을 수 있는지 확인
        
        Args:
            board: 게임 보드
            piece: 맞춰볼 조각의 좌표 리스트
            start_x, start_y: 조각을 놓기 시작할 위치
        
        Returns:
            조각을 놓을 수 있으면 True, 아니면 False
        """
        for x, y in piece:
            nx, ny = start_x + x, start_y + y
            # 보드 범위를 벗어나거나 이미 채워진 칸이면 False
            if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board) or board[nx][ny] != 0:
                return False
            
            # 인접한 칸 확인 (빈 칸이 있으면 안 됨)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ax, ay = nx + dx, ny + dy
                if 0 <= ax < len(board) and 0 <= ay < len(board):
                    if board[ax][ay] == 0 and [ax - start_x, ay - start_y] not in piece:
                        return False
        return True

    def place_piece(board: List[List[int]], piece: List[List[int]], start_x: int, start_y: int, value: int) -> None:
        """
        조각을 보드에 배치
        
        Args:
            board: 게임 보드
            piece: 배치할 조각의 좌표 리스트
            start_x, start_y: 조각을 놓기 시작할 위치
            value: 채울 값 (1: 퍼즐 조각)
        """
        for x, y in piece:
            board[start_x + x][start_y + y] = value

    # 게임 보드의 빈 공간 찾기
    empty_spaces = find_pieces(game_board, 0)
    empty_spaces = [normalize_piece(piece) for piece in empty_spaces]

    # 테이블의 퍼즐 조각 찾기
    puzzle_pieces = find_pieces(table, 1)
    puzzle_pieces = [normalize_piece(piece) for piece in puzzle_pieces]

    filled_count = 0
    used_pieces = [False] * len(puzzle_pieces)

    # 각 빈 공간에 대해 맞는 퍼즐 조각 찾기
    for space in empty_spaces:
        for i, piece in enumerate(puzzle_pieces):
            if used_pieces[i]:
                continue
            
            # 조각을 4번 회전시키며 맞춰보기
            for _ in range(4):
                if sorted(space) == sorted(piece):
                    filled_count += len(space)
                    used_pieces[i] = True
                    break
                piece = normalize_piece(rotate_piece(piece))
            
            if used_pieces[i]:
                break

    return filled_count