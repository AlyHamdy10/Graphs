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
