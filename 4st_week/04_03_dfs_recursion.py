# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []


def dfs_recursion(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node)
    print("current_node", cur_node, "adjacent_graph[cur_node]", adjacent_graph[cur_node])
    for adjacent_node in adjacent_graph[cur_node]:
        if adjacent_node not in visited_array: ## 인접 노드 중에 방문 하지 않은 조건
            dfs_recursion(adjacent_graph, adjacent_node, visited_array) ## 방문 안했으면 거기서 다시 탐색 시작


    return


dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!