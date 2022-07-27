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
#---------------------------------------------------------------#
    # returns true if there exists a path from src to dst
    # finds path using recursion
    # handles cyclic graph

    def has_path(self, graph, src, dst, visited=set()):
        if src in visited:
            return False
        visited.add(src)
        if src == dst:
            return True
        for neighbour in graph[src]:
            if self.hasPath(self, graph, neighbour, dst, visited) == True:
                return True
        return False
#---------------------------------------------------------------#
    # builds undirected graph given the edges in parameter

    def build_graph(self, edges):
        graph = dict()
        for edge in edges:
            [a, b] = edge
            if not (a in graph):
                graph[a] = []
            if not (b in graph):
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
        return graph
#---------------------------------------------------------------#
    # returns true if there exists a path between nodeA and nodeB
    # the function is given a list of edges present
    # a graph is built according to the list of edges given

    def has_path_undirected_graph(self, edges, nodeA, nodeB):
        graph = self.build_graph(self, edges)
        return self.hasPath(self, graph, nodeA, nodeB)
#---------------------------------------------------------------#
    # returns true if a new unvisited component is found

    def explore(self, graph, current, visited):
        if current in visited:
            return False
        visited.add(current)
        for neighbour in graph[current]:
            self.explore(self, graph, neighbour, visited)
        return True
#---------------------------------------------------------------#
    # returns number of connected components in graph

    def count_connected_components(self, graph):
        visited = set()
        count = 0
        for node in graph:
            if self.explore(self, graph, node, visited):
                count += 1
        return count
#---------------------------------------------------------------#
    # returns the size of the largest component in graph
    # uses function explore_size

    def largest_component(self, graph):
        visited = set()
        largest = 0
        for node in graph:
            size = self.explore_size(self, graph, node, visited)
            if size > largest:
                largest = size
        return largest
#---------------------------------------------------------------#
    # returns the number of neighbours of the node sent in parameter
    # integer returned includes the node sent itself

    def explore_size(self, graph, node, visited):
        if node in visited:
            return 0
        visited.add(node)
        size = 1
        for neighbour in graph[node]:
            size += self.explore_size(self, graph, neighbour, visited)
        return size
