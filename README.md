Assignment 3: Graphs Pt. 1, DFS & BFS
Name: AJ Tennathur, Jerrick Little

Description of Implementation: 
- Graph Implementation: 
    - Directed graph implementation using an adjacency list structure. 
    - Graph class manages vertices and edges with dictionaries for efficient lookup. 
    - Vertex class keeps the outgoing edges in a dictionary, allowing fast addition and removal by the edge name. 
    - Edge class stores the edge's name, destination vertex, and weight (distance). 
    - All classes (Graph, Vertex, Edge) have docstrings describing purpose and methods. 
- BFS & DFS Implementation
    - Iterative Implementations (for both DFS and BFS)
    - DFS uses stack structure to explore as deep as possible before coming back, marking each vertex as visited, and then prints the order of discovery.
    - BFS uses queue structure to explore all of the neighbors at the current depth and then moving on.
        - Just like DFS, it marks the vertices as visited, and prints the order of discovery. 
    - Note: Both of the traversal methods reset the "visited" status before starting. 

To Run: 
    - Simply have all of the following files loaded: 
        - graph_impl.py
        - graph.txt
        - program.py
    - Run program.py, and you will be prompted to enter the starting vertex/city name. Simply enter the name from the graph.txt file of your choosing, and then run the program.py file to see the results of the DFS and BFS traversals.

- Additional Note: in the Vertex class for the graph implementation, I created a generic type variable: self._data: Optional[V] = None
    - This means that each vertex could store some additional data of any type. 
    - In my current implementation, I did not end up using the self._data, so the V is not being utilized. However, I still included it because it is useful in the future if I want to associate arbitrary data with each vertex.
