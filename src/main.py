from CubeProblemGenerator import CubeProblemGenerator
from CubePathFinder import CubePathFinder
from CubeProblemVisualizer import CubeProblemVisualizer

def main():
    while True:
        problem = CubeProblemGenerator.CubeProblemGenerator.generate_problem(
            min_size=7,
            max_size=10,
            min_val=1,
            max_val=9
        )

        CubeProblemVisualizer.CubeProblemVisualizer.display_problem(problem)

        print("\nВычисление оптимального пути...")
        finder = CubePathFinder.CubePathFinder(problem.grid, problem.face_values)
        total_penalty, optimal_path = finder.find_optimal_path(problem.start_pos, problem.end_pos)

        CubeProblemVisualizer.CubeProblemVisualizer.display_solution(optimal_path, total_penalty)

        try:
            start_another_time = int(input("\nЖелаете продолжить программу?(1/0)"))
            if start_another_time:
                continue
            break
        except ValueError:
            print("Некорректные вводимые данные.")

if __name__ == "__main__":
    main()
