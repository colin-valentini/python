
def merge_intervals(intervals):
  '''
  Given an array of intervals where intervals[i] = [starti, endi], merge
  all overlapping intervals, and return an array of the non-overlapping 
  intervals that cover all the intervals in the input.

  https://leetcode.com/problems/merge-intervals/
  '''
  sorted_intervals = sorted(intervals)
  covers = [sorted_intervals[0]]
  for interval in sorted_intervals[1:]:
    start, stop = interval
    lastCoverStart, lastCoverStop = covers[-1]
    
    # The current interval overlaps the last covering interval if and only
    # if the stop value of the cover is beyond or the same as the start value
    # of the current interval
    if lastCoverStop >= start:
      # Merge the last covering interval with this current interval
      covers[-1] = [lastCoverStart, max(lastCoverStop, stop)]
    else:
      # Append this inteval to the covering intervals
      covers.append(interval)
  
  return covers

assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert merge_intervals([[1,4],[4,5]]) == [[1,5]]
assert merge_intervals([[1,4],[0,4]]) == [[0,4]]
  