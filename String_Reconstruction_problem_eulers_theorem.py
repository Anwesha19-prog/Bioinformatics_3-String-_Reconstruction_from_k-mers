# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 14:11:25 2025

@author: DELL
"""

from collections import defaultdict, deque

def parse_input(file_name):
    with open(file_name, 'r') as f:
        k = int(f.readline().strip())
        patterns = f.read().strip().split()
    return k, patterns

def build_de_bruijn_graph(kmers):
    graph = defaultdict(deque)
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph[prefix].append(suffix)
    return graph

def find_start_node(graph):
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)

    nodes = set(graph.keys())
    for u in graph:
        out_deg[u] += len(graph[u])
        for v in graph[u]:
            in_deg[v] += 1
            nodes.add(v)

    start = None
    for node in nodes:
        if out_deg[node] - in_deg[node] == 1:
            return node
    return next(iter(graph))

def find_eulerian_path(graph):
    graph_copy = {u: deque(v) for u, v in graph.items()}
    start_node = find_start_node(graph)
    stack = [start_node]
    path = []

    while stack:
        current = stack[-1]
        if graph_copy.get(current):
            next_node = graph_copy[current].popleft()
            stack.append(next_node)
        else:
            path.append(stack.pop())
    return path[::-1]

def reconstruct_string_from_path(path):
    text = path[0]
    for node in path[1:]:
        text += node[-1]
    return text

if __name__ == "__main__":
    # 🔽 Input and Output file names
    input_file = "dataset_30187_7.txt"
    output_file = "output.txt"

    k, kmers = parse_input(input_file)
    graph = build_de_bruijn_graph(kmers)
    path = find_eulerian_path(graph)
    result = reconstruct_string_from_path(path)

    with open(output_file, 'w') as f:
        f.write(result)

    print("Reconstructed string written to", output_file)
