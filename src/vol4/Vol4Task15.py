from collections import deque


def is_bipartite(n, adj):
    color = [-1] * (n + 1)

    for i in range(1, n + 1):
        if color[i] == -1:
            queue = deque([i])
            color[i] = 0

            while queue:
                v = queue.popleft()
                for u in adj[v]:
                    if color[u] == -1:
                        color[u] = color[v] ^ 1
                        queue.append(u)
                    elif color[u] == color[v]:
                        return False, None
    return True, color


def solve():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    bipartite, color = is_bipartite(n, adj)

    if not bipartite:
        print("Система магистралей является четно-нечетной")
    else:
        print("Система магистралей НЕ является четно-нечетной")

        subset0 = [i for i in range(1, n + 1) if color[i] == 0]
        subset1 = [i for i in range(1, n + 1) if color[i] == 1]

        # Выбираем большую долю
        max_subset = subset0 if len(subset0) > len(subset1) else subset1
        print(f"Максимальное подмножество: {max_subset}")
        print(f"Размер подмножества: {len(max_subset)}")


if __name__ == "__main__":
    solve()