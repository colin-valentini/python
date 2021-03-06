
from classes.visited_status import VisitedStatus

def topological_sort(vertices, edges):
  '''
  Performs a topological sort on the given graph (as defined by the provided vertices and edges)
  and returns the ordering found, or an empty list if no ordering exists

  O(v+e) time | O(v+e) space
  '''
  # Generate a "previous" adjacency map which maps vertices to vertices which point to them
  previous_map = get_previous_map(vertices, edges)

  # Use a visited dictionary to tell us what the current state of a given node in the graph is,
  # we can use an enum to standardize the status values used
  visited = { vertex: VisitedStatus.Unvisited for vertex in vertices}

  # Create a new list to cache our ordering as we go
  ordering = []

  # For each vertex in our graph, if we haven't already visited the vertex, perform a depth
  # first search of pre-vertices and add them to the ordering in a "post-order" traversal
  for vertex in vertices:
    if visited[vertex] != VisitedStatus.Visited:

      # The depth first search function will return True if a cycle has been detected, in
      # which case we want to immediately return an empty array (no topological ordering
      # exists for graphs with directed cycles)
      cycleDetected = depth_first_search(vertex, ordering, visited, previous_map)
      if cycleDetected:
        return []

  return ordering

def depth_first_search(vertex, ordering, visited, previous_map):
  '''
  Search all the pre-vertices of the given vertex, appending the most ancestral
  vertex (in recursive calls) before appending the current vertex to the ordering
  list.

  Returns True if a cycle has been deteced else False. All modifications to the ordering
  list are done in place.

  O(v+e) time | O(v+e) space
  '''
  if visited[vertex] == VisitedStatus.InProgress:
    # Cycle deteced!
    return True

  visited[vertex] = VisitedStatus.InProgress

  for preVertex in previous_map[vertex]:
    if visited[preVertex] != VisitedStatus.Visited:
      
      # We want to make sure we propogate any cycle detection immediately
      cycleDetected = depth_first_search(preVertex, ordering, visited, previous_map)
      if cycleDetected:
        return True

  ordering.append(vertex)
  visited[vertex] = VisitedStatus.Visited
  return False

def get_previous_map(vertices, edges):
  '''
  An O(e) time | O(v+e) space operation to transform out inputs in a "previous" adjacency
  map
  '''
  previous_map = { vertex: [] for vertex in vertices }
  for edge in edges:
    origin, destination = edge
    previous_map[destination].append(origin)

  return previous_map