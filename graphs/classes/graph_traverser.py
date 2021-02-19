#!/usr/bin/env python3

from enum import Enum

class TraversalOrder(Enum):
  PRE_ORDER = -1
  POST_ORDER = 1

class GraphTraverser:
  def __init__(self, edges):
    self.edges = edges
  
  def __reset_visited(self):
    self.visited = [False] * len(self.edges)

  def apply_depth_first(self, call_back):
    self.__reset_visited()
    self.__set_call_back(call_back)
    self.__traverse_depth_first(0)
  
  def __set_call_back(self, call_back):
    self.call_back = call_back

  def __traverse_depth_first(self, origin):
    if self.visited[origin]:
      return

    self.call_back(origin, self.edges, self.visited, TraversalOrder.PRE_ORDER)
    
    self.visited[origin] = True
    for destination in self.edges[origin]:
      self.__traverse_depth_first(destination)
    
    self.call_back(origin, self.edges, self.visited, TraversalOrder.POST_ORDER)
