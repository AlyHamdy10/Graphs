class Graphs:
    def dfs_stack(self, graph, source):  # depth first traversal using stack
        stack = [source]
        while len(stack) != 0:
            current = stack.pop()
            print(current)
            for neighbour in graph[current]:
                stack.append(neighbour)

    def dfs_recursion(self, graph, source):  # depth first traversal using recursion
        print(source)
        for neighbour in graph[source]:
            Graphs.dfs_recursion(self, graph, neighbour)

    def bfs(self, graph, source):
        queue = [source]
        while len(queue) != 0:
            current = queue.pop(0)
            print(current)
            for neighbour in graph[current]:
                queue.append(neighbour)
