from random import randint as rand, choice, choices 
import networkx as nx
import matplotlib.pyplot as plt


class Mesh(nx.Graph):
    """
    A mesh network graph where nodes are randomly connected with weighted edges.
    
    Attributes:
        start_nodes (list): List of starting nodes for pathfinding
        end_node (int): The destination node
        mesh_size (int): Number of nodes in the mesh
    """
    start_nodes: list
    end_node: int
    mesh_size: int

    def generate_mesh(self, max_connections: int, max_weight: int) -> None:
        """
        Generates a random mesh network with nodes and weighted edges.

        :param max_connections: Maximum connections per node
        :param max_weight: Maximum weight for edges
        """
        for n in self.nodes:
            other_nodes = [node for node in self.nodes if node != n]
            # Randomly select between 1 and max_connections nodes to connect to
            connections = choices(other_nodes, k=rand(1, max_connections))
            for connection in connections:
                # Add edge with random weight between 1 and max_weight
                self.add_edge(n, connection, weight=rand(1, max_weight))


    def genearte_planar_mesh(self, max_connections: int, max_weight: int) -> None:
        """
        Generates a planar mesh network.

        :param max_connections: Maximum connections per node
        :param max_weight: Maximum weight for edges
        """


        for n in self.nodes:
            other_nodes = [node for node in self.nodes if node != n]
            # Randomly select between 1 and max_connections nodes to connect to
            connections = choices(other_nodes, k=rand(1, max_connections))
            for connection in connections:
                # Add edge with random weight between 1 and max_weight
                self.add_edge(n, connection, weight=rand(1, max_weight))
                if not nx.is_planar(self):
                    self.remove_edge(n, connection)

        

        #for node in self.nodes:

        #    for i in range(rand(1,4)):
        #        self.add_edge(node, list(self.nodes)[(node + i + 1) % self.mesh_size], weight=rand(1, max_weight))

    
    def __init__(self, size: int, planar: bool = False, max_connections: int = 5, max_weight: int = 10) -> None:
        """
        Initializes the mesh with random nodes and edges.
        
        :param size: Number of nodes to create
        :param planar: Whether to generate a planar mesh (default: False)
        :param max_connections: Maximum connections per node (default: 5)
        :param max_weight: Maximum weight for edges (default: 10)
        """
        super().__init__()

        # Create nodes numbered from 0 to size-1
        self.mesh_size = size
        self.add_nodes_from(range(size))
        
        # Randomly connect nodes without overlapping to create edges with random weights
        self.planar = planar
        if planar:
            self.genearte_planar_mesh(max_connections, max_weight)
        else:
            self.generate_mesh(max_connections, max_weight)
    

    def select_start_end(self, n_start: int = 1, min_distance: int = 1) -> None:
        """
        Randomly selects start and end nodes for pathfinding.
        
        :param n_start: Number of start nodes to select (default: 1)
        :param min_distance: Minimum distance between start and end nodes (default: 1)
        :raises ValueError: If n_start is invalid
        """

        # Validate input
        if n_start + 1 > len(self.nodes):
            raise ValueError("n_start is too high for the number of nodes in the mesh")
        if n_start < 1:
            raise ValueError("n_start must be at least 1")
        
        # Select start and end nodes
        if n_start == 1:
            self.start_nodes = [choice(list(self.nodes))]
            self.end_node = choice([node for node in self.nodes if node != self.start_nodes[0]])
        else:
            self.start_nodes = choices(list(self.nodes), k=n_start)
            self.end_node = choice([node for node in self.nodes if node not in self.start_nodes])


    def show(self) -> None:
        """
        Displays the mesh graph with nodes and edges, coloring start nodes (green) 
        and end node (red), and edge thickness based on weight.
        """
        print(self.nodes)
        print(self.edges)

        # Create color map for visualization
        if hasattr(self, 'start_nodes') and hasattr(self, 'end_node'):
            color_map = []
            for node in self.nodes:
                if node in self.start_nodes:
                    color_map.append('green')
                elif node == self.end_node:
                    color_map.append('red')
                else:
                    color_map.append('lightblue')

        # Draw network with edge thickness based on weight
        if self.planar:
            nx.draw_planar(self,
                       with_labels=False,
                       width=[self[u][v]['weight'] * 0.5 for u, v in self.edges],
                       node_color=color_map
                       )
            plt.show()
        else:
            nx.draw_spring(self,
                       with_labels=False,
                       width=[self[u][v]['weight'] * 0.5 for u, v in self.edges],
                       node_color=color_map
                       )
            plt.show()
    

class Node:
    id: int
    parent: Node | None
    cost: int
    heuristic: int

    def __init__(self, id: int, parent: Node | None = None, cost: int = 0, heuristic: int = 0) -> None:
        self.id = id
        self.cost = cost
        self.parent = parent
        self.heuristic = heuristic

def a_star(mesh: Mesh) -> list:
    return []

def dijkstra(mesh: Mesh) -> list:
    queue = []
    queue.append((0, mesh.start_nodes[0], None))


    return []

# Create a mesh
m = Mesh(20, planar=True, max_connections=4, max_weight=5)
# Select 2 random start nodes and 1 end node
m.select_start_end(1)
# Display the mesh
m.show()