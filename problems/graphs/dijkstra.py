
def dijkstra_shortest_path(start, edges):
  num_vertices = len(edges)
  min_distances = [float('inf') for _ in range(num_vertices)]
  min_distances[start] = 0

  priority_queue = PriorityQueue([Vertex(node_id) for node_id in range(num_vertices)])
  priority_queue.update(start, 0)

  while not priority_queue.is_empty():
    origin = priority_queue.remove()
    distance_to_origin = origin.distance

    if distance_to_origin == float('inf'):
      break

    for destination, distance_to_destination in edges[origin.node_id]:
      path_distance = distance_to_origin + distance_to_destination
      min_distance_to_destination = min_distances[destination]
      if path_distance < min_distance_to_destination:
        min_distances[destination] = path_distance
        priority_queue.update(destination, path_distance)

  return min_distances

class PriorityQueue():
  def __init__(self, vertices):
    self.vertex_map = {i:i for i in range(len(vertices))}
    self.heap = self.build_heap(vertices)
  
  def is_empty(self):
    return not len(self.heap)
  
  def build_heap(self, vertices):
    first_parent_index = (len(vertices) - 2) // 2
    for index in reversed(range(first_parent_index + 1)):
      self.sift_down(index, len(vertices) - 1, vertices)
    return vertices
  
  def sift_down(self, start_index, end_index, heap):
    curr_index = start_index
    left_index = curr_index * 2 + 1
    while left_index <= end_index:
      right_index = curr_index * 2 + 2 if curr_index * 2 + 2 <= end_index else -1
      
      if right_index != -1 and heap[right_index].distance < heap[left_index].distance:
        index_to_swap = right_index
      else:
        index_to_swap = left_index
      
      if heap[index_to_swap].distance < heap[curr_index].distance:
        self.swap(curr_index, index_to_swap, heap)
        curr_index = index_to_swap
        left_index = curr_index * 2 + 2
      else:
        return
  
  def sift_up(self, start_index, heap):
    curr_index = start_index
    parent_index = (curr_index - 1) // 2
    while curr_index > 0 and heap[curr_index].distance < heap[parent_index].distance:
      self.swap(curr_index, parent_index, heap)
      curr_index = parent_index
      parent_index = (curr_index - 1) // 2
  
  def remove(self):
    if self.is_empty():
      return
    
    self.swap(0, len(self.heap) - 1, self.heap)
    vertex = self.heap.pop()
    self.vertex_map.pop(vertex.node_id)
    self.sift_down(0, len(self.heap) - 1, self.heap)

    return vertex

  def swap(self, i, j, heap):
    self.vertex_map[heap[i].node_id] = j
    self.vertex_map[heap[j].node_id] = i
    heap[i], heap[j] = heap[j], heap[i]
  
  def update(self, node_id, distance):
    self.heap[self.vertex_map[node_id]] = Vertex(node_id, distance)
    self.sift_up(self.vertex_map[node_id], self.heap)

class Vertex():
  def __init__(self, node_id, distance=float('inf')):
    self.node_id = node_id
    self.distance = distance

edges = [
  [
    [1, 7]
  ],
  [
    [2, 6],
    [3, 20],
    [4, 3]
  ],
  [
    [3, 14]
  ],
  [
    [4, 2]
  ],
  [],
  []
]
print(dijkstra_shortest_path(0, edges))