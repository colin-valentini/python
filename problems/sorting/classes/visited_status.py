from enum import Enum

class VisitedStatus(Enum):
  Unvisited = -1
  InProgress = 0
  Visited = 1