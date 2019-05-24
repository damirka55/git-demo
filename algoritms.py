# Algotitms from book.

# Binary search.
def binary_search(work_list, item):
    low = 0
    high = len(work_list) - 1
    
    while low <= high:
        middle = int((low+high)/2)
        value = work_list[middle]
        
        if value == item:
            return middle
            
        elif value > item:
            high = middle - 1
            
        else:
            low = middle + 1
    
    return None
    
# Selection sort.
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    
    return smallest_index
    
def selection_sort(arr):
    new_arr = []
    
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
        
    return new_arr

# Recursion and factorial.
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)

# Divide et impera.
def summ(arr):
    if arr == []:
        return 0
        
    x = arr.pop(0)
    return x + summ(arr)
        
def count(arr):
    if arr == []:
        return 0
    
    return 1 + count(arr[1:])
    
def find_biggest(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]
    if arr[0] > find_biggest(arr[1:]):
        return arr[0]
    else:
        return find_biggest(arr[1:])

# Quick sort.
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
            
    return quick_sort(less) + [arr[0]] + quick_sort(greater)

# Breadth first serach.
def person_is_seller(name):
    return name[0] == 'm' 

from collections import deque
def breadth_first_serach(name, graph):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                return person
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
    
# Dijkstra`s algorithm.
def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    
    return lowest_cost_node
    
def dijkstra_algoritm(graph, costs, parents, processed = []):
    node = find_lowest_cost_node(costs, processed)
    
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
        
    return parents
    
