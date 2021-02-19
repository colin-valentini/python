#!/usr/bin/env python3

class AdjacencyList:
  def __init__(self, edges):
    self.num_vertices = len(edges)
    self.edges = edges
    self.__validate()
  
  def __len__(self):
    return self.num_vertices
  
  def __contains__(self, vertex):
    return 0 <= vertex and vertex <= self.__len__()

  def __getitem__(self, vertex):
    if not vertex in self:
      raise IndexError(f"Vertex '{vertex}' is not a valid vertex")
    return self.edges[vertex]
  
  def __validate(self):
    if self.num_vertices == 0:
      raise Exception("Constructor arg 'edges' cannot be empty")
    if not isinstance(self.edges, list):
      raise TypeError("Constructor arg 'edges' must be an instance of type list")
  
  def has_edge_to(self, origin, destination):
    if not self.__contains__(origin) or not self.__contains__(destination):
      return False
    
    return destination in self.edges[origin]

  