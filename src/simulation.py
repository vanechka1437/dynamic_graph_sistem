def simulate_path_graph(edge_lengths: list[int]) -> tuple[int, list[int]]:
    """
    Симуляция динамической системы на метрическом графе, представляющим собой простой путь

    :param edge_lengths: список из взаимно простых в совокупности длин ребер пути по порядку
    :return: кортеж из времени стабилизации пути и списка времен стабилизации каждого ребра по порядку
    """
    # хранит позицию точки и ее направление, позиция от 0 до sum(edges_lengths)
    # направление 1 или -1 - от начальной вершины и к ней
    points = list()
    # время стабилизации каждого отдельного ребра
    stabilization_times = [-1 for _ in range(len(edge_lengths))]
    # начальная точка
    points.append([0, 1])
    # позиции вершин
    vertex_positions = [0 for _ in range(len(edge_lengths) + 1)]
    for i in range(len(edge_lengths)):
        vertex_positions[i + 1] = vertex_positions[i] + edge_lengths[i]
    # перебираем все тики времени
    t = 1
    while True:
        # передвигаем каждую точку по направлению
        for point in points:
            point[0] += point[1]
        # если точка пришла в вершину, она разворачивается, а также если
        # не в 0 и не в sum(edge_lengths) позициях, то создает новую точку
        # в том же направлении, то есть как бы продолжает движение, но если
        # в одну вершину пришло две точки, то новых вершин не создается и
        # точки как бы просто продолжают движение
        new_points = list()
        for point in points:
            if point[0] == 0 or point[0] == sum(edge_lengths):
                point[1] *= -1
            elif point[0] in vertex_positions and sum([p[0] == point[0] for p in points]) > 1:
                pass
            elif point[0] in vertex_positions:
                new_points.append([point[0], point[1] * (-1)])

        points = points + new_points
        # обновляем время стабилизации каждого отдельного ребра
        for i in range(len(edge_lengths)):
            count = 0
            for point in points:
                if vertex_positions[i] < point[0] < vertex_positions[i + 1]:
                    count += 1
                if vertex_positions[i] == point[0] and point[1] == 1:
                    count += 1
                if vertex_positions[i + 1] == point[0] and point[1] == -1:
                    count += 1
            if count == edge_lengths[i]:
                if stabilization_times[i] == -1:
                    stabilization_times[i] = t
        # условие остановки - достижение количеством вершин максимума
        if len(points) == sum(edge_lengths):
            return t, stabilization_times
        t += 1