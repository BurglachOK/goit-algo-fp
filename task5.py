import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree_dynamic(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.pause(0.7)


def hex_color_gradient(start_color, end_color, steps):
    start = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    gradient = []

    for i in range(steps):
        ratio = i / max(steps - 1, 1)
        rgb = tuple(int(start[j] + (end[j] - start[j]) * ratio) for j in range(3))
        gradient.append('#{:02x}{:02x}{:02x}'.format(*rgb))
    return gradient


def dfs_visualize(root):
    stack = [root]
    visited = []
    all_nodes = collect_all_nodes(root)
    colors = hex_color_gradient("#004B96", "#99ccff", len(all_nodes))

    index = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            node.color = colors[index]
            index += 1
            visited.append(node)
            draw_tree_dynamic(root)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


def bfs_visualize(root):
    queue = deque([root])
    visited = []
    all_nodes = collect_all_nodes(root)
    colors = hex_color_gradient("#900000", "#ff9999", len(all_nodes))

    index = 0
    while queue:
        node = queue.popleft()
        if node not in visited:
            node.color = colors[index]
            index += 1
            visited.append(node)
            draw_tree_dynamic(root)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def collect_all_nodes(root):
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node not in result:
            result.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result


def tree_from_heap(arr):
    heapq.heapify(arr)
    nodes = [Node(key) for key in arr]
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
    return nodes[0] if nodes else None


elements = [0, 4, 5, 10, 1, 3]
root = tree_from_heap(elements)
print("DFS Visualization:")
dfs_visualize(root)
for node in collect_all_nodes(root):
    node.color = "skyblue"
print("BFS Visualization:")
bfs_visualize(root)
plt.show()