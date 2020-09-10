        # # create a set for visited_vertices
        # visited_ver = set()
        # # create a path to begin search
        # curr_path = dfs_path.pop()
        # # if curr_path is None
        # if curr_path == None:
        #     # make current path include the starting vertex
        #     curr_path = [starting_vertex]
        # # check if the last item in list/array/stack is not in the visited_ver
        # if curr_path[-1] not in visited_ver:
        #     # add the last item to visited vertices
        #     visited_ver.add(curr_path[-1])
        #     # get neighbors for the last item,
        #     for neighbor in self.get_neighbors(curr_path[-1]):
        #         # if neighbor is the destination vertex
        #         if neighbor == destination_vertex:
        #             # append neighbor to path
        #             curr_path.append(neighbor)
        #             # return the curr path
        #             return curr_path
        #         # create a copy of the curr path to make a new path
        #         curr_path_copy = curr_path.copy()
        #         # add neighbor to new path
        #         curr_path_copy.append(neighbor)
        #         # push the new path to the master path
        #         dfs_path.push(curr_path_copy)
        #     # and of course re run the function until it doesnt need to anymore
        #     return self.dfs_recursive(starting_vertex, destination_vertex, dfs_path, visited_ver)

# path = "2, 4, 6"
# path2 = []

# path3 = [path]

# print(path3)