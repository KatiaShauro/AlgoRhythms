from typing import List, Tuple


class task34_vol2:
    def dp_solution(self, arr: List[Tuple[int, int]]) -> Tuple[int, int]:
        delta = []
        d = 0
        for t in arr:
            a, b = t
            delta.append(a - b)
            d += (a - b)
        dp = {}
        dp[d] = 0
        min_d = d
        for i in delta:
            diff = -2 * i
            new_entries = {}
            for d, value in dp.items():
                d_new = d + diff
                new_entries[d_new] = min(dp.get(d_new, float('inf')),
                                         value + 1)
                if abs(d_new) < abs(min_d):
                    min_d = d_new
            dp.update(new_entries)
            print(dp)

        v1 = dp.get(min_d, float('inf'))
        v2 = dp.get(-min_d, float('inf'))

        if v1 < v2:
            return v1, abs(min_d)
        else:
            return v2, abs(-min_d)


if __name__ == "__main__":
    task = task34_vol2()
    lst = []
    ans = task.dp_solution(lst)
    print(f'Количество перестановок: {ans[0]}, минимальная разность: {ans[1]}')
