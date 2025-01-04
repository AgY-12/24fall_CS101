from collections import deque


def bfs(board, start, end):
    w, h = len(board[0]), len(board)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上
    visited = set()  # 使用集合来记录访问过的点 (x, y, prev_dir)
    queue = deque([(*start, 0, None)])  # (x, y, segments, prev_direction)

    while queue:
        x, y, segments, prev_dir = queue.popleft()
        if (x, y) == end:
            return segments

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy

            # 检查是否在板内且未访问过，且当前位置是 'X'
            if 0 <= nx < w and 0 <= ny < h and (nx, ny, i) not in visited and board[ny][nx] == 'X':
                visited.add((nx, ny, i))
                new_segments = segments + (1 if prev_dir != i else 0)
                queue.append((nx, ny, new_segments, i))

            # 允许路径暂时离开矩形板，但必须保证最终能回到板内
            elif not (0 <= nx < w and 0 <= ny < h):
                # 尝试从板外重新进入板内
                for j, (dx2, dy2) in enumerate(directions):
                    nnx, nny = nx + dx2, ny + dy2
                    if 0 <= nnx < w and 0 <= nny < h and (nnx, nny, j) not in visited and board[nny][nnx] == 'X':
                        visited.add((nnx, nny, j))
                        new_segments = segments + (1 if prev_dir != j else 0)
                        queue.append((nnx, nny, new_segments, j))
                        break  # 一旦找到可以进入板内的路径，立即停止尝试其他方向

    return -1


def main():
    board_num = 1
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break

        # 读取原始矩形板，并在其周围添加一圈空格作为保护圈
        board = [[' '] * (w + 2) for _ in range(h + 2)]
        for i in range(1, h + 1):
            row = input().strip()
            for j in range(1, w + 1):
                board[i][j] = row[j - 1]

        pairs = []
        while True:
            x1, y1, x2, y2 = map(int, input().split())
            if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
                break
            pairs.append(((x1, y1), (x2, y2)))

        print(f"Board #{board_num}:")
        for i, (start, end) in enumerate(pairs, 1):
            # 调整坐标，因为板子扩展了一圈
            start = (start[0], start[1])
            end = (end[0], end[1])
            if board[start[1]][start[0]] == 'X' and board[end[1]][end[0]] == 'X':
                segments = bfs(board, start, end)
                if segments != -1:
                    print(f"Pair {i}: {segments} segments.")
                else:
                    print(f"Pair {i}: impossible.")
            else:
                print(f"Pair {i}: impossible.")
        print()
        board_num += 1


if __name__ == "__main__":
    main()
'''
5 4
XXXXX
X   X
X XXX
X   X
2 3 5 3
1 3 4 4
2 3 3 4
0 0 0 0
0 0

Board #1:
Pair 1: impossible.
Pair 2: impossible.
Pair 3: impossible.

'''
