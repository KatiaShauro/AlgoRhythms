import heapq
from typing import List, Tuple
from collections import deque, defaultdict
from itertools import count

from src.vol3.task25.CubeState import CubeState


class CubePathFinder:
    def __init__(self, grid : List[List[int]], face_values : List[int]):
        self.grid = grid
        self.face_values = face_values
        self.n = len(grid)
        self.m = len(grid[0])
        self.orientations  = self.generate_all_orientations()

    @staticmethod
    def generate_all_orientations():
        orientations = set()
        queue = deque([(1, 2, 3)])
        visited = set()

        while queue:
            top, front, right = queue.popleft()
            orientations.add((top, front, right))

            for new_orient in [
                (front, 7 - top, right),
                (7 - front, top, right),
                (7 - right, front, top),
                (right, front, 7 - top)
            ]:
                if new_orient not in visited:
                    if all(1 <= num <= 6 for num in new_orient):
                        visited.add(new_orient)
                        queue.append(new_orient)

        return list(orientations)

    def calculate_penalty(self, x: int, y: int, face: int) -> int:
        return abs(self.grid[x][y] - self.face_values[face - 1])

    def get_neighbors(self, state: CubeState) -> List[Tuple[CubeState, int, str]]:
        neighbors = []
        directions = [(-1, 0, 'Вверх'), (1, 0, 'Вниз'), (0, -1, 'Влево'), (0, 1, 'Вправо')]

        for dx, dy, dir_symbol in directions:
            nx, ny = state.x + dx, state.y + dy
            if 0 <= nx < self.n and 0 <= ny < self.m:
                if dx == -1:
                    new_orient = (state.front, 7 - state.top, state.right)
                elif dx == 1:
                    new_orient = (7 - state.front, state.top, state.right)
                elif dy == 1:
                    new_orient = (7 - state.right, state.front, state.top)
                else:
                    new_orient = (state.right, state.front, 7 - state.top)

                new_state = CubeState(nx, ny, *new_orient)
                penalty = self.calculate_penalty(nx, ny, new_orient[0])
                neighbors.append((new_state, penalty, dir_symbol))

        return neighbors

    def bfs_find_optimal_path(self, start: Tuple[int, int], end: Tuple[int, int]) -> Tuple[int, List[CubeState]]:
        x1, y1 = start
        x2, y2 = end

        queue = deque()
        visited = set()
        min_penalty = float('inf')
        best_path = []

        for orient in self.orientations:
            initial_state = CubeState(x1, y1, *orient)
            initial_penalty = self.calculate_penalty(x1, y1, orient[0])
            queue.append((initial_state, initial_penalty, [initial_state]))
            visited.add(initial_state)

        while queue:
            current_state, current_penalty, current_path = queue.popleft()

            if current_state.x == x2 and current_state.y == y2:
                if current_penalty < min_penalty:
                    min_penalty = current_penalty
                    best_path = current_path
                continue

            for neighbor_state, transition_penalty, _ in self.get_neighbors(current_state):
                if neighbor_state not in visited:
                    new_penalty = current_penalty + transition_penalty
                    new_path = current_path + [neighbor_state]
                    visited.add(neighbor_state)
                    queue.append((neighbor_state, new_penalty, new_path))

        return min_penalty, best_path if best_path else (float('inf'), [])

    def find_optimal_path(self, start: Tuple[int, int], end: Tuple[int, int]) -> Tuple[int, List[CubeState]]:
        x1, y1 = start
        x2, y2 = end

        dist = defaultdict(lambda: float('inf'))
        prev = {}
        heap = []
        counter = count()

        for orient in self.orientations:
            initial_state = CubeState(x1, y1, *orient)
            initial_penalty = self.calculate_penalty(x1, y1, orient[0])
            dist[initial_state] = initial_penalty
            heapq.heappush(heap, (initial_penalty, next(counter), initial_state))

        while heap:
            current_penalty, _, current_state = heapq.heappop(heap)

            if current_state.x == x2 and current_state.y == y2:
                path = []
                while current_state in prev:
                    path.append(current_state)
                    current_state = prev[current_state]
                path.append(current_state)
                path.reverse()

                total_penalty = sum(
                    self.calculate_penalty(state.x, state.y, state.top)
                    for state in path
                )
                return total_penalty, path

            if current_penalty > dist[current_state]:
                continue

            for neighbor_state, transition_penalty, _ in self.get_neighbors(current_state):
                new_penalty = current_penalty + transition_penalty

                if new_penalty < dist[neighbor_state]:
                    dist[neighbor_state] = new_penalty
                    prev[neighbor_state] = current_state
                    heapq.heappush(heap, (new_penalty, next(counter), neighbor_state))

        return int('inf'), []


    def visualize_path(self, path : List[CubeState]):
        if not path:
            print("Путь не найден")
            return

        print(f"Найден оптимальный путь.")
        print(f"Старт: {path[0]}.\nФиниш: {path[-1]}.\nСуммарный штраф:"
              f" {sum(self.calculate_penalty(s.x, s.y, s.top) for s in path)}")
        print("Полный путь:")
        for i, state in enumerate(path):
            if i < len(path) - 1:
                next_state = path[i + 1]
                direction = ""
                if next_state.x < state.x: direction = "Вверх"
                elif next_state.x > state.x: direction = "Вниз"
                elif next_state.y < state.y: direction = "Влево"
                elif next_state.y > state.y: direction = "Вправо"
                print(f"{i + 1}. {state} | Штраф: {self.calculate_penalty(state.x, state.y, state.top)} | Поворот: {direction}")