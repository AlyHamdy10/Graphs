class Graphs:
    def dfs_stack(self, graph, source):  # depth first traversal using stack
        stack = [source]
        while len(stack) != 0:
            current = stack.pop()
            print(current)
            for neighbour in graph[current]:
                stack.append(neighbour)
