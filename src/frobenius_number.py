import heapq


def frobenius_number_nijenhuis(numbers: list[int]) -> int:
    """
    Алгоритм Нийенхуиса быстрого вычисления числа Фробениуса набора
    взаимно простых в совокупности натуральных чисел

    :param numbers: набор взаимно простых в совокупности натуральных чисел
    :return: число Фробениуса переданного набора чисел
    """
    if not numbers:
        return 0
    numbers = sorted(numbers)
    min_num = numbers[0]
    n = min_num
    if min_num == 1:
        return 0
    edges = [[] for _ in range(n)]
    temp_g = [{} for _ in range(n)]
    for i in range(n):
        for num in numbers:
            v = (num + i) % n
            if v not in temp_g[i] or temp_g[i][v] > num:
                temp_g[i][v] = num
    for i in range(n):
        for v, w in temp_g[i].items():
            edges[i].append((v, w))
    INF = float('inf')
    dist = [INF] * n
    dist[0] = 0
    heap = [(0, 0)]
    while heap:
        d_v, v = heapq.heappop(heap)
        if d_v != dist[v]:
            continue
        for u, w in edges[v]:
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
                heapq.heappush(heap, (dist[u], u))
    max_dist = max(dist[1:]) if n > 1 else 0
    return max_dist - n