from typing import Optional
from graph_interfaces import IGraph, IVertex
from graph_impl import Graph, Vertex, Edge
import csv
from collections import deque

def read_graph(file_path: str) -> IGraph:  
    """Read the graph from the file and return the graph object.
        Args:
            file_path: The path to the CSV file that contains the graph data.
        Returns:
            An instance of the Graph that is populated with the data from the read in 
            CSV File.
    """
    graph = Graph()
    vertices = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            source = row['source']
            destination = row['destination']
            highway = row['highway']
            distance = float(row['distance'])

            if source not in vertices:
                v_source = Vertex(source)
                vertices[source] = v_source
                graph.add_vertex(v_source)
            if destination not in vertices:
                v_destination = Vertex(destination)
                vertices[destination] = v_destination
                graph.add_vertex(v_destination)

            edge_name = f"{source}->{destination}"
            edge = Edge(edge_name, vertices[destination], distance)
            graph.add_edge(edge)
    return graph

def print_dfs(graph: IGraph, start_vertex: IVertex) -> None: 
    """Print the DFS traversal of the graph starting from the start vertex.
        Note: This is an iterative implementation using a stack.
        
        Args:
            graph: The graph to traverse.
            start_vertex: The vertex to start the DFS from.
        Returns: 
            None

    """
    for v in graph.get_vertices():
        v.set_visited(False)
    stack = [start_vertex]
    result = []
    while stack:
        vertex = stack.pop()
        if not vertex.is_visited():
            result.append(vertex.get_name())
            vertex.set_visited(True)
            neighbors = []
            for edge in vertex.get_edges():
                neighbors.append(edge.get_destination())
            for neighbor in reversed(neighbors):
                if not neighbor.is_visited():
                    stack.append(neighbor)
    print("DFS:", ' -> '.join(result))

def print_bfs(graph: IGraph, start_vertex: IVertex) -> None: 
    """Print the BFS traversal of the graph starting from the start vertex.
        Note: This is an iterative implementation using a queue.
        Args:
            graph: The graph to traverse.
            start_vertex: The vertex to start the BFS from.
        Returns:
            None
    """
    for v in graph.get_vertices():
        v.set_visited(False)
    queue = deque([start_vertex])
    result = []
    start_vertex.set_visited(True)
    while queue:
        vertex = queue.popleft()
        result.append(vertex.get_name())
        for edge in vertex.get_edges():
            neighbor = edge.get_destination()
            if not neighbor.is_visited():
                neighbor.set_visited(True)
                queue.append(neighbor)
    print("BFS:", ' -> '.join(result))


def main() -> None:
    graph: IGraph = read_graph("graph.txt")
    start_vertex_name: str  = input("Enter the start vertex/city name: ")

    # Find the start vertex object
    start_vertex: Optional[IVertex]= next((v for v in graph.get_vertices() if v.get_name() == start_vertex_name), None)

    if start_vertex is None:
        print("Start vertex not found")
        return
    
    print_dfs(graph, start_vertex)
    print_bfs(graph, start_vertex)


if __name__ == "__main__":
    main()