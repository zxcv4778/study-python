
class Graph:
    def bfs(self, data, start):
        visited = []
        queue = [start]

        while queue:
            n = queue.pop(0)
            if n not in visited:
                visited.append(n)
                queue += data[n] - set(visited)

        return visited

    def bfs_path(self, data, start, goal):
        queue = [(start, [start])]
        result = []

        while queue:
            n, path = queue.pop(0)

            if n == goal:
                result.append(path)
            else:
                for m in data[n] - set(path):
                    queue.append((m, path + [m]))

        return result

    def dfs(self, data, start):
        visited = []
        stack = [start]

        while stack:
            n = stack.pop()

            if n not in visited:
                visited.append(n)
                stack += data[n] - set(visited)

        return visited

    def dfs_path(self, data, start, goal):
        stack = [(start, [start])]
        result = []

        while stack:
            n, path = stack.pop()

            if n == goal:
                result.append(path)
            else:
                for m in data[n] - set(path):
                    stack.append((m, path + [m]))

        return result


if __name__ == "__main__":
    gdata = {'A': set(['B', 'C']),
            'B': set(['A', 'E', 'F']),
            'C': set(['B', 'D', 'E']),
            'D': set(['F']),
            'E': set(['B', 'A']),
            'F': set(['D', 'C'])}

    g = Graph()

    print(g.bfs(gdata, 'F'))
    print(g.bfs_path(gdata, 'A', 'F'))
    print(g.dfs(gdata, 'F'))
    print(g.dfs_path(gdata, 'A', 'F'))







