class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {v: set() for v in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    def is_valid_color(self, vertex, color, color_assignment):
        for neighbor in self.graph[vertex]:
            if color_assignment[neighbor] == color:
                return False
        return True

    def graph_coloring_util(self, num_colors, color_assignment, vertex):
        if vertex == self.vertices:
            return True  # All vertices are colored

        for color in range(1, num_colors + 1):
            if self.is_valid_color(vertex, color, color_assignment):
                color_assignment[vertex] = color

                if self.graph_coloring_util(num_colors, color_assignment, vertex + 1):
                    return True

                color_assignment[vertex] = 0  # Backtrack

        return False

    def graph_coloring(self, num_colors):
        color_assignment = [0] * self.vertices

        if not self.graph_coloring_util(num_colors, color_assignment, 0):
            print("No valid coloring exists.")
        else:
            print("Valid coloring:", color_assignment)


# Example usage:
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

num_colors = 3  # You can change the number of colors as needed
graph.graph_coloring(num_colors)
