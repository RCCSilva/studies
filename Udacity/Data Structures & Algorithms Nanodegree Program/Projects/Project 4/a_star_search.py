import heapq
from typing import List
from collections import defaultdict
import math

def shortest_path(M, start: int, goal: int) -> List[int]:
    border = []
    visited = defaultdict(lambda: (float('inf'), None))    
    
    border.append((0, 0, [start], start))
    
    while len(border) > 0:
        total_cost, path_cost, path, inter = heapq.heappop(border)
        
        # intersection
        current_cost, _ = visited[inter]
        if path_cost > current_cost:
            continue
            
        visited[inter] = (path_cost, path)

        # child
        for child_inter in M.roads[inter]:
            new_path = path + [child_inter]

            child_path_cost = get_path_cost(M.intersections, inter, child_inter)
            child_goal_cost = get_goal_cost(M.intersections, child_inter, goal)
            child_total_cost = child_path_cost + child_goal_cost
            
            heapq.heappush(border, (child_total_cost, path_cost + child_path_cost, new_path, child_inter))

    cost, path = visited[goal]
    
    if path:
        return path
    else:
        return []
    
def get_path_cost(intersections, current_node, next_node) -> float:
    return euclidean_distance(intersections[current_node], intersections[next_node])

def get_goal_cost(intersections, next_node, goal_node) -> float:
    return euclidean_distance(intersections[next_node], intersections[goal_node])

def is_exhausted(visited: set, roads: List[List[int]], goal: int) -> int:
    not_visited = set(roads[goal]) - visited
    return len(not_visited) == 0

def euclidean_distance(a: list, b: list) -> int:
    return math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))

def measure_path_distance(path):
    d = 0

    for i in range(len(path) - 1):
        d += euclidean_distance(path[i], path[i + 1])

    return d
