import Unit

class Node(Unit):
    def __init__(self, entity, properties):
        super().__init__(entity, properties)
        self.edges = []
        self.inputEdges = []
        self.outputEdges = []

    def unlink(self):
        return

    