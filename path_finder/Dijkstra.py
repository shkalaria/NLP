def dijkstra(graph, src, dest, visited=[], distances={}, predecessors={}):

    # ending condition
    if src == dest:
        path = []
        predecessor = dest
        
        while predecessor != None:

            path.append(predecessor)
            predecessor = predecessors.get(predecessor, None)

        return path

    else :     
        # initializes the distance for the first time
        if not visited: 
            distances[src] = 0

        # visit the neighbors and calculate the distance
        for neighbor in graph[src] :

            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]

                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src

        # mark src as visited
        visited.append(src)

        unvisited = {}
        for key in graph:
            if key not in visited:
                unvisited[key] = distances.get(key,float('inf'))

        node = min(unvisited, key = unvisited.get)
        return dijkstra(graph, node, dest, visited, distances, predecessors)