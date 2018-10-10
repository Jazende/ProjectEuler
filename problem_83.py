## Dijkstra: https://github.com/mburst/dijkstras-algorithm/blob/master/dijkstras.py
import heapq
import sys

raw_input = """131,673,234,103,18
201,96,342,965,150
630,803,746,422,111
537,699,497,121,956
805,732,524,37,331"""

class Graph:
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, name, edges):
        self.vertices[name] = edges
        # print(f'Name: {name}. Edges: {edges}.')
    
    def shortest_path(self, start, finish):
        # print(self.vertices)
        distances = {} # Distance from start to node
        previous = {}  # Previous node in optimal path from source
        nodes = [] # Priority queue of all nodes in Graph

        for vertex in self.vertices:
            if vertex == start: # Set root node as distance of 0
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None
        
        while nodes:
            smallest = heapq.heappop(nodes)[1] # Vertex in nodes with smallest distance in distances
            if smallest == finish: # If the closest node is our target we're done so print the path
                path = []
                while previous[smallest]: # Traverse through nodes til we reach the root which is 0
                    path.append(smallest)
                    smallest = previous[smallest]
                return path
            if distances[smallest] == sys.maxsize: # All remaining vertices are inaccessible from source
                break
            
            for neighbor in self.vertices[smallest]: # Look at all the nodes that this vertex is attached to
                alt = distances[smallest] + self.vertices[smallest][neighbor] # Alternative path distance
                if alt < distances[neighbor]: # If there is a new shortest path update our priority queue (relax)
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return distances

    def shortest_path_points(self, start, finish):
        path = self.shortest_path(start, finish)
        # neemt eerste waarde van de waarden per punt uit lijst vertices voor elke waarde in het pad behalve start en finish
        points = [[x[1] for x in self.vertices[point].items()][0] for point in [x for x in path if not x == start and not x == finish][::-1]]
        return points, sum(points), path

    def shortest_path_sum(self, start, finish):
        return self.shortest_path_points(start, finish)

    def __str__(self):
        return str(self.vertices)

    def build_from_raw_input(self, raw, go_back=True):
        matrix = [[number for number in line.split(",")] for line in raw_input.strip().split("\n")]
        self.matrix = matrix

        start_sides = {}
        end_sides = {}
        max_side = len(matrix[0])-1

        for h in range(len(matrix)):
            for w in range(len(matrix[0])):
                sides = {}
                if h-1 in range(len(matrix)):
                    sides['{}x{}'.format(h-1, w)] = int(matrix[h][w])
                if h+1 in range(len(matrix)):
                    sides['{}x{}'.format(h+1, w)] = int(matrix[h][w])
                if go_back:
                    if w-1 in range(len(matrix[0])):
                        sides['{}x{}'.format(h, w-1)] = int(matrix[h][w])
                if w+1 in range(len(matrix[0])):
                    sides['{}x{}'.format(h, w+1)] = int(matrix[h][w])
                if w == 0:
                    sides['S'] = int(matrix[h][w])
                if w == max_side:
                    sides['E'] = int(matrix[h][w])
                    
                self.add_vertex('{}x{}'.format(h, w), sides)

        for h in range(len(matrix)):
            start_sides['{}x{}'.format(h, 0)] = 0
            end_sides['{}x{}'.format(h, max_side)] = 0
            
        self.add_vertex('S', start_sides)
        self.add_vertex('E', end_sides)

class TopLeftBotRightGraph(Graph):
    def build_from_raw_input(self, raw):
        matrix = [[number for number in line.split(",")] for line in raw_input.strip().split("\n")]
        self.matrix = matrix

        start_sides = {}
        end_sides = {}
        max_side = len(matrix[0])-1

        for h in range(len(matrix)):
            for w in range(len(matrix[0])):
                sides = {}
                if h-1 in range(len(matrix)):
                    sides['{}x{}'.format(h-1, w)] = int(matrix[h][w])
                if h+1 in range(len(matrix)):
                    sides['{}x{}'.format(h+1, w)] = int(matrix[h][w])
                if w-1 in range(len(matrix[0])):
                    sides['{}x{}'.format(h, w-1)] = int(matrix[h][w])
                if w+1 in range(len(matrix[0])):
                    sides['{}x{}'.format(h, w+1)] = int(matrix[h][w])
                    
                self.add_vertex('{}x{}'.format(h, w), sides)
                
    def shortest_path_points(self, start, finish):
        path = self.shortest_path(start, finish)
        path.append(start)
        points = [[x[1] for x in self.vertices[point].items()][0] for point in path[::-1]]
        return points, sum(points), path
    
    def shortest_path_top_left_bot_right(self):
        top_left = '0x0'
        bot_right = '{}x{}'.format(len(self.matrix)-1, len(self.matrix[0])-1)
        return self.shortest_path_sum(top_left, bot_right)[1]

if __name__ == '__main__':
    with open('p083_matrix.txt', 'r') as g:
        raw_input = g.read().strip()
        
    e = TopLeftBotRightGraph()
    e.build_from_raw_input(raw_input)
    print(e.shortest_path_top_left_bot_right())
