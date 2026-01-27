import math
from random import randint as rand, choice, choices 
import networkx as nx
import matplotlib.pyplot as plt


class Mesh(nx.Graph):
    """
    A mesh network graph where nodes are randomly connected with weighted edges.
    
    Attributes:
        size (int): Number of nodes in the mesh
        max_connections (int): Maximum number of connections per node
        max_weight (int): Maximum weight value for edges
        start_nodes (list): List of starting nodes for pathfinding
        end_node (int): The destination node
    """
    size: int
    max_connections: int
    max_weight: int
    
    def __init__(self, size: int, max_connections: int = 5, max_weight: int = 10) -> None:
        """
        Initializes the mesh with random nodes and edges.
        
        :param size: Number of nodes to create
        :param max_connections: Maximum connections per node (default: 5)
        :param max_weight: Maximum weight for edges (default: 10)
        """
        super().__init__()

        # Create nodes numbered from 0 to size-1
        self.add_nodes_from(range(size))
        
        # Randomly connect nodes to create edges with random weights
        for n in self.nodes:
            other_nodes = [node for node in self.nodes if node != n]
            # Randomly select between 1 and max_connections nodes to connect to
            connections = choices(other_nodes, k=rand(1, max_connections))
            for connection in connections:
                # Add edge with random weight between 1 and max_weight
                self.add_edge(n, connection, weight=rand(1, max_weight))
    

    def select_start_end(self, n_start: int = 1) -> None:
        """
        Randomly selects start and end nodes for pathfinding.
        
        :param n_start: Number of start nodes to select (default: 1)
        :raises ValueError: If n_start is invalid
        """
        # Validate input
        if n_start + 1 > len(self.nodes):
            raise ValueError("n_start is too high for the number of nodes in the mesh")
        if n_start < 1:
            raise ValueError("n_start must be at least 1")
        
        # Select start and end nodes
        if n_start == 1:
            self.start_nodes = [choice(self.nodes)]
            self.end_node = choice([node for node in self.nodes if node != self.start_nodes[0]])
        else:
            self.start_nodes = choices(self.nodes, k=n_start)
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
        nx.draw_spring(self,
                       with_labels=False,
                       width=[self[u][v]['weight'] * 0.5 for u, v in self.edges],
                       node_color=color_map
                       )
        plt.show()


# Create a mesh with 25 nodes and maximum 5 connections per node
m = Mesh(25, 5)
# Select 2 random start nodes and 1 end node
m.select_start_end(2)
# Display the mesh
m.show()