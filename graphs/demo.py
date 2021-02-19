#!/usr/bin/env python3

from classes.adjacency_list import AdjacencyList
from classes.graph_traverser import GraphTraverser
from classes.graph_traverser import TraversalOrder

# Create a simple adjacency list to define our graph
edges = AdjacencyList([
  [1,2],
  [3,4],
  [],
  [0],
  [2]
])

# Create a new traverser instance and define a simple callback function
traverser = GraphTraverser(edges)

def call_back(node, edges, visited, order):
  if order == TraversalOrder.PRE_ORDER:
    print(f'[PRE_ORDER] Executed callback for node: {node}')
  elif order == TraversalOrder.POST_ORDER:
    print(f'[POST_ORDER] Executed callback for node: {node}')

# Call the traverser to demo the call back
traverser.apply_depth_first(call_back)