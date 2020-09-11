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

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # making current node as visited
        if visited == None:
            visited = set()
        # adding starting_vertex to the visited    
        visited.add(starting_vertex)
        # print(f" these are starting vertices, the dft_recursive way: {starting_vertex}")
        print(starting_vertex)
        
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
        queue_before_search = Queue()
        queue_before_search.enqueue([starting_vertex])
        
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while queue_before_search.size() > 0:
            # Dequeue the first PATH
            current_path = queue_before_search.dequeue()
            # Grab the last vertex from the PATH
            last_vertex = current_path[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vertex == destination_vertex:
                    # IF SO, RETURN PATH
                    return current_path
                # if it is not teh target
                else:
                    # Mark it as visited...
                    visited.add(last_vertex)
                    # Then add A PATH TO its neighbors to the back of the queue
                    for node in self.get_neighbors(last_vertex):
                        # COPY THE PATH
                        copy_current_path = current_path[:]
                        # APPEND THE NEIGHBOR TO THE BACK
                        copy_current_path.append(node)
                        # and add copied current path to the queue
                        queue_before_search.enqueue(copy_current_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        queue_before_search = Stack()
        queue_before_search.push([starting_vertex])
        
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while queue_before_search.size() > 0:
            # Dequeue the first PATH
            current_path = queue_before_search.pop()
            # Grab the last vertex from the PATH
            last_vertex = current_path[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vertex == destination_vertex:
                    # IF SO, RETURN PATH
                    return current_path
                # if it is not teh target
                else:
                    # Mark it as visited...
                    visited.add(last_vertex)
                    # Then add A PATH TO its neighbors to the back of the queue
                    for node in self.get_neighbors(last_vertex):
                        # COPY THE PATH
                        copy_current_path = current_path[:]
                        # APPEND THE NEIGHBOR TO THE BACK
                        copy_current_path.append(node)
                        # and add copied current path to the queue
                        queue_before_search.push(copy_current_path)

    # def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.

    #     This should be done using recursion.
    #     """
    #     # making current node as visited
    #     if visited == None:
    #         visited = set()
    #     # adding starting_vertex to the visited    
    #     visited.add(starting_vertex)
    #     # print(f" these are starting vertices, the dft_recursive way: {starting_vertex}")
    #     # print(starting_vertex)
    #     # keeping track of path
    #     if path is None:
    #         path = [starting_vertex]
    #     # making current_path equal path plus starting vertex
    #     path = path + [starting_vertex]
    #     # checking starting vertex as destination
    #     if starting_vertex == destination_vertex:
    #         return path
        
    #     for new_starting_vertex in self.get_neighbors(starting_vertex):
    #         # checking each new_starting_vertex are visited
    #         if new_starting_vertex not in visited:
    #             #repeat teh previous process above
    #             new_path = self.dfs_recursive(new_starting_vertex, destination_vertex, visited, path)
    #             # if no new_starting_vertex path then return neighbor path
    #             if new_path is None:
    #                 return new_path
    #     return None
    
    def dfs_recursive(self, starting_vertex, destination_vertex, dfs_path=Stack(), visited_ver=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        # create a set for visited_vertices
        visited_ver = set()
        # create a path to begin search
        curr_path = dfs_path.pop()
        # if curr_path is None
        if curr_path == None:
            # make current path include the starting vertex
            curr_path = [starting_vertex]
        # check if the last item in list/array/stack is not in the visited_ver
        if curr_path[-1] not in visited_ver:
            # add the last item to visited vertices
            visited_ver.add(curr_path[-1])
            # get neighbors for the last item,
            for neighbor in self.get_neighbors(curr_path[-1]):
                # if neighbor is the destination vertex, end this
                if neighbor == destination_vertex:
                    # append neighbor to path
                    curr_path.append(neighbor)
                    # return the curr path
                    return curr_path
                # create a copy of the curr path to make a new path
                curr_path_copy = curr_path.copy()
                # add neighbor to new path
                curr_path_copy.append(neighbor)
                # push the new path to the master path
                dfs_path.push(curr_path_copy)
            # and of course re run the function until it doesnt need to anymore
            return self.dfs_recursive(starting_vertex, destination_vertex, dfs_path, visited_ver)
        

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
