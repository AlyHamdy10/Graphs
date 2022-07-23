class Graphs:
    #---------------------------------------------------------------#
    # depth first traversal using stack
    def dfs_stack(self, graph, source):
        stack = [source]
        while len(stack) != 0:
            current = stack.pop()
            print(current)
            for neighbour in graph[current]:
                stack.append(neighbour)
#---------------------------------------------------------------#
    # depth first traversal using recursion

    def dfs_recursion(self, graph, source):
        print(source)
        for neighbour in graph[source]:
            Graphs.dfs_recursion(self, graph, neighbour)
#---------------------------------------------------------------#
    # breadth first traversal using recursion

    def bfs(self, graph, source):
        queue = [source]
        while len(queue) != 0:
            current = queue.pop(0)
            print(current)
            for neighbour in graph[current]:
                queue.append(neighbour)
#---------------------------------------------------------------#
    # returns true if there exists a path from src to dst
    # finds path using dfs

    def has_path_dfs(self, graph, src, dst):
        if src == dst:
            return True
        for neighbour in graph[src]:
            if self.has_path_dfs(self, graph, neighbour, dst):
                return True
        return False
#---------------------------------------------------------------#
    # returns true if there exists a path from src to dst
    # finds path using bfs

    def has_path_bfs(self, graph, src, dst):
        queue = [src]
        while len(queue) != 0:
            current = queue.pop()
            if current == dst:
                return True
            for neighbour in graph[current]:
                queue.append(neighbour)
        return False
