from Unit import Unit

class Node(Unit):
    """
        Parameters:
            String entity: entity type (person for example)
            Dic properties: entity properties
    """
    def __init__(self, entity, properties):
        super().__init__(entity, properties)
        self.edges = []
        self.inputEdges = []
        self.outputEdges = []

    def unlink(self):
        edges = self.edges

        for i in edges:
            i.unlink()

    def bfs(self, visited, graph, node):
        queue = []
        visited = []
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0) 
            print(s, end = " ") 

            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
