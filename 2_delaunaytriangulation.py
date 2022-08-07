from queue import PriorityQueue

input_filename = "2_inputTriangulation.txt"
output_filename = "2_outputTriangulation.txt"


class Edge:
    def __init__(self, x, y):
        self.x = x  # vertex 1
        self.y = y  # vertex 2
        self._opposing_points = None

    @property
    def opposing_points(self):
        return self._opposing_points

    @opposing_points.setter
    def opposing_points(self, opposing_point):
        if self._opposing_points is None:
            self._opposing_points = [opposing_point]
        elif (
            isinstance(self._opposing_points, list) and len(self._opposing_points) == 1
        ):
            self._opposing_points.append(opposing_point)
        elif isinstance(self._opposing_points, list) and len(self._opposing_points) > 1:
            raise Exception(
                "Trying to add opposing point to edge that already has 2 opposing points"
            )

    def __hash__(self):
        return hash((min(self.x, self.y), max(self.x, self.y)))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (min(self.x, self.y), max(self.x, self.y)) == (
                min(other.x, other.y),
                max(other.x, other.y),
            )
        else:
            raise Exception("Trying to compare equality on different instance types")

    def __lt__(self, other):
        if min(self.x, self.y) < min(other.x, other.y):
            return True
        elif max(self.x, self.y) < max(other.x, other.y):
            return True
        else:
            return False

    def __str__(self):
        return (
            "Edge has vertex 1 of {} and vertex 2 {}, with opposing_points {}".format(
                self.x, self.y, self._opposing_points
            )
        )


def get_edges_from_triangle(index_list):
    edge_1 = Edge(index_list[0], index_list[1])
    edge_1.opposing_points = index_list[2]
    edge_2 = Edge(index_list[1], index_list[2])
    edge_2.opposing_points = index_list[0]
    edge_3 = Edge(index_list[2], index_list[0])
    edge_3.opposing_points = index_list[1]
    return [edge_1, edge_2, edge_3]


if __name__ == "__main__":

    vertex_dict = {}
    edge_dict = {}
    edge_queue = 0
    with open("./{}".format(input_filename), "r") as f:
        text = f.readlines()
        line_count = 0
        number_of_points = 0
        number_of_triangles = 0
        for line in text:
            if line_count == 0:
                number_of_points = int(line.split()[0])
                number_of_triangles = int(line.split()[1])
            elif line_count > 0 and line_count <= number_of_points:
                # creating vertices
                vertex_idx = line.split()[0]
                vertex_x = line.split()[1]
                vertex_y = line.split()[2]
                vertex_dict[vertex_idx] = (vertex_x, vertex_y)
            elif (
                line_count > number_of_points
                and line_count <= number_of_points + number_of_triangles
            ):
                # creating triangles
                edges = get_edges_from_triangle(line.split())
                for edge in edges:
                    if edge in edge_dict:
                        edge_dict[edge].opposing_points = edge.opposing_points[0]
                    else:
                        edge_dict[edge] = edge

            else:
                raise Exception("Text shouldn't have additional row")
            line_count += 1
    pq = PriorityQueue()
    for edge in edge_dict:
        pq.put(edge)
    while not pq.empty():
        print(pq.get())
