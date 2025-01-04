import heapq
from math import inf

# 四个基本方向：右、下、左、上
DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def find_shortest_path(grid, start, end, dimensions, cycle_length):
    """
    寻找从起点到终点的最短路径。

    :param grid: 地图信息（0为空地，1为石头）
    :param start: 起点坐标 (x, y)
    :param end: 终点坐标 (x, y)
    :param dimensions: 地图尺寸 (rows, cols)
    :param cycle_length: 穿过石头的时间周期
    :return: 最短时间或 "Oop!" 表示无法到达
    """
    rows, cols = dimensions
    visited = [[[False] * cols for _ in range(rows)] for _ in range(cycle_length)]
    priority_queue = [(0,) + start]  # 初始时间为0加上起点坐标

    while priority_queue:
        time, x, y = heapq.heappop(priority_queue)
        if (x, y) == end:  # 到达终点
            return time

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            new_time = time + 1

            if not (0 <= nx < rows and 0 <= ny < cols):  # 检查是否在地图内
                continue

            if grid[nx][ny] == 1 and new_time % cycle_length == 0 and not visited[new_time % cycle_length][nx][
                ny]:  # 穿石头
                visited[new_time % cycle_length][nx][ny] = True
                heapq.heappush(priority_queue, (new_time, nx, ny))
            elif grid[nx][ny] == 0 and not visited[new_time % cycle_length][nx][ny]:  # 普通空地
                visited[new_time % cycle_length][nx][ny] = True
                heapq.heappush(priority_queue, (new_time, nx, ny))

    return "Oop!"


def main():
    test_cases = int(input())
    results = []

    for _ in range(test_cases):
        rows, cols, cycle_length = map(int, input().split())
        grid = []
        start = None
        end = None

        for i in range(rows):
            line = input()
            row = []
            for j, char in enumerate(line):
                if char == "S":
                    start = (i, j)
                    row.append(0)  # 起点当空地
                elif char == "E":
                    end = (i, j)
                    row.append(0)  # 终点当空地
                elif char == "#":
                    row.append(1)  # 石头
                else:
                    row.append(0)  # 空地
            grid.append(row)

        result = find_shortest_path(grid, start, end, (rows, cols), cycle_length)
        results.append(result)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()