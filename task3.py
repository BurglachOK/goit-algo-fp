import heapq
import random

def dijkstra(graph, start):
    dis = {node: float('inf') for node in graph}
    dis[start] = 0
    queue = [(0, start)]
    while queue:
        curr_dist, curr_node = heapq.heappop(queue)
        if curr_dist > dis[curr_node]:
            continue
        for neighbor, weight in graph[curr_node]:
            distance = curr_dist + weight
            if distance < dis[neighbor]:
                dis[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return dis, start


"Односторонні зв'язки"
graph = {
    'A': [('D', 1), ('X', 5), ('H', 4), ('E', 2)],
    'B': [('X', 9), ('C', 10), ('N', 1), ('A', 2)],
    'C': [('H', 9), ('T', 1)],
    'D': [('G', 9), ('N', 4), ('O', 10), ('I', 1)],
    'E': [('W', 7), ('K', 5)],
    'F': [('G', 6), ('D', 2)],
    'G': [('D', 6), ('L', 10), ('I', 1)],
    'H': [('O', 9), ('D', 7), ('C', 9), ('J', 10)],
    'I': [('S', 4), ('W', 2), ('B', 4)],
    'J': [('C', 4), ('D', 7), ('I', 8)],
    'K': [('L', 6), ('G', 5), ('W', 2)],
    'L': [('U', 3), ('R', 4), ('F', 8), ('M', 5)],
    'M': [('W', 9), ('H', 1), ('Y', 1)],
    'N': [('M', 5), ('C', 4), ('S', 6)],
    'O': [('U', 8), ('M', 8)],
    'P': [('I', 3), ('H', 9)],
    'Q': [('I', 10), ('N', 10), ('M', 6), ('H', 3)],
    'R': [('P', 2), ('Y', 1), ('D', 3), ('U', 3)],
    'S': [('N', 10), ('C', 7), ('M', 10), ('O', 9)],
    'T': [('R', 1), ('V', 9)],
    'U': [('Y', 6), ('D', 5), ('N', 3)],
    'V': [('A', 5), ('Q', 2)],
    'W': [('J', 9), ('T', 4), ('E', 6), ('Y', 3)],
    'X': [('Y', 9), ('A', 2), ('K', 8)],
    'Y': [('J', 4), ('B', 4), ('S', 2)]
}


def get_start(graph):
    start = []
    for i in graph:
        start.append(i)
        
    if len(start) >= 2:
        start_num = random.randint(0, len(start))
        start_node = start[start_num]
    return start_node

shortest_paths, start = dijkstra(graph, get_start(graph))

for node in shortest_paths:
    print(f"Closest distance from {start} to {node}: {shortest_paths[node]}")
