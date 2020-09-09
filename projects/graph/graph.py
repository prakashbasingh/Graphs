"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

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
                print(f" The visited node using BFT: {v}")

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
                print(f" The visited node using DFT: {v}")

                # Add it to the visited set
                visited.add(v)

                # enqueue all its neighbors
                for n in self.get_neighbors(v):
                    #print(f"Adding: {n}")
                    to_visit_queue.push(n) 

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # making current node as visited
        if visited == None:
            visited = set()
            
        visited.add(starting_vertex)
        print(f" these are starting vertices, the dft_recursive way: {starting_vertex}")
        
        # saving current node neighbor to a variable name neighbors
        neighbors = self.get_neighbors(starting_vertex)
        
        # while current node has the neighbor
        while len(neighbors) > 0:
            for node in neighbors: # for each neighbor
                if node not in visited: # if neighbor has not been visited
                    self.dft_recursive(node, visited) # making the neighbor current node in recursive way
                else: # if neighbor has been visited
                    return
                
       

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        
        # Create a Set to store visited vertices
        # While the queue is not empty...
            # Dequeue the first PATH
            # Grab the last vertex from the PATH
            # If that vertex has not been visited...
                # CHECK IF IT'S THE TARGET
                # IF SO, RETURN PATH
                # Mark it as visited...
                # Then add A PATH TO its neighbors to the back of the queue
                # COPY THE PATH
                # APPEND THE NEIGHBOR TO THE BACK

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
