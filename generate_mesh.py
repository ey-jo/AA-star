class Node:
    id: int
    incoming: dict[int]
    outgoing: dict[int: int]


    def __init__(self, id: int):
        self.id = id


class Mesh:
    def __init__(self):
        pass
        


def create_mesh(size: int, max_connections: int) -> Mesh:
    """
    Creates the Mesh
    
    :param size: Number of Nodes inside Mesh
    :type size: int
    :param max_connections: Maximum amount of connections per node
    :type max_connections: int
    """
    pass