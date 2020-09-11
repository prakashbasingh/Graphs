class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue to hold nodes to visit
        to_visit_queue = Queue()

        # Create a set to hold visited nodes
        visited = set()

        # Initialize: add the starting node to the queue
        to_visit_queue.enqueue(starting_vertex)

        # While queue not empty:
        while to_visit_queue.size() > 0:
            # dequeue first entry
            v = to_visit_queue.dequeue()

            # if not visited:
            if v not in visited:
                # Visit the node (print it out)
                # print(f" The visited node using BFT: {v}")
                print(v)

                # Add it to the visited set
                visited.add(v)

                # enqueue all its neighbors
                for n in self.get_neighbors(v):
                    #print(f"Adding: {n}")
                    to_visit_queue.enqueue(n)        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a queue to hold nodes to visit
        to_visit_queue = Stack()

        # Create a set to hold visited nodes
        visited = set()

        # Initialize: add the starting node to the queue
        to_visit_queue.push(starting_vertex)

        # While queue not empty:
        while to_visit_queue.size() > 0:
            # dequeue first entry
            v = to_visit_queue.pop()

            # if not visited:
            if v not in visited:
                # Visit the node (print it out)
                # print(f" The visited node using DFT: {v}")
                print(v)

                # Add it to the visited set
                visited.add(v)

                # enqueue all its neighbors
                for n in self.get_neighbors(v):
                    #print(f"Adding: {n}")
                    to_visit_queue.push(n)