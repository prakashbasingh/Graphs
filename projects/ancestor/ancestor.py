
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

    
    
def earliest_ancestor(ancestors, starting_node):
    # creating a graph
    ancestor_graph = Graph()
    
    for vertex in ancestors:
        # adding 1st and 2nd vertices into the graph
        if vertex[0] not in ancestor_graph.vertices:
            ancestor_graph.add_vertex(vertex[0])
        if vertex[1] not in ancestor_graph.vertices:
            ancestor_graph.add_vertex(vertex[1])
        # adding edges into the graph to connect the vertices
        ancestor_graph.add_edge(vertex[1], vertex[0])
    
    # now creating a queue
    queue = Queue()
    # now adding starting node to remember the path
    queue.enqueue([starting_node])
    # to keep track the path
    path = []
    
    # when queue size is more than 0 
    while queue.size() > 0:
        vertex_path = queue.dequeue()
        # if the current path is qual to the prior path, keep teh smaller value
        if len(vertex_path) == len(path) and vertex_path[-1] < path[-1]:
            path = vertex_path
        # if current path is longer than the prior path, replace it
        if len(vertex_path) > len(path):
            path = vertex_path
        # add neighbor_items to the que       
        for neighbor_items in ancestor_graph.get_neighbors(vertex_path[-1]):
            copy_path = list(vertex_path)
            copy_path.append(neighbor_items)
            queue.enqueue(copy_path)
    # if path has not greater and equal to 1 ,. then there is no parent and return -1       
    if len(path) <= 1:
        return -1
    # if there is parents return the path after finishing the loop
    else:
        return path[-1]
        
        
    