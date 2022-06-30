import heapq
from collections import defaultdict
from collections import deque
from time import time
import math
from time import perf_counter
class node:
    def __init__(self,node):
        self.node = node

    def name(self):
        return self.node


    def __repr__(self):
        return "node()"
    def __str__(self):
        return self.node
class edge:
    def __init__(self, edge, weight):
        self.edge = edge
        self.weight = weight
    def set_weight(self, weight):
        self.weight = weight
    def get_weight(self,start,adjecent):
        return self.weight
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.map1 = defaultdict()

           
    def add_node(self, vertex): #adding vertex to the graph
        self.graph[vertex.node].append(vertex)

    def make_edge(self, node1, node2, weight=0):
        if node1 not in self.map1:
            self.map1[node1] = node(node1)
        if node2 not in self.map1:
            self.map1[node2] = node(node2)
        n1, n2 = node1, node2

        node1 = self.map1[node1]
        node2 = self.map1[node2]
            
        self.graph[self.map1[n1]].append((node2, weight))
        self.graph[self.map1[n2]].append((node1, weight))
        
        

        

    def __iter__(self):
        return iter(self.graph.values())


def breadth_first_search(graph,start):
        start_time=time()*10000
        path=[]
        visited=set()         #inorder to have unrepeated visited nodes
        queue= deque()
        visited.add(start)
        queue.append(start)
        
        while(len(queue)>0):
            visited_node=queue.popleft()
            path.append(visited_node)
            for adjecent_node in graph.graph:
                if adjecent_node.name() not in visited:
                    visited.add(adjecent_node.name())
                    queue.append(adjecent_node.name())
        end_time=time()*10000
        time_required=end_time - start_time
        print(" -> ".join(path))
        print("\n")
        print("$$$$$$ time $$$$$$")
        
        print("required time for breadth first search =",time_required ,"X 10^-4 second")
        print("\n")
        
def depth_first_search(graph,start):
        start_time=time()*10000
        path=[]
        visited=set()        #inorder to have unrepeated visited nodes
        stack= []
        visited.add(start)
        stack.append(start)
        while(len(stack)>0):
            visited_node=stack.pop()
            path.append(visited_node)

            for node in graph.graph[graph.map1[visited_node]]:
                adjecent_node, weight = node
                if adjecent_node.name() not in visited:
                    visited.add(adjecent_node.name())
                    stack.append(adjecent_node.name())  
        
        end_time=time()*10000
        time_required = end_time - start_time
        print(" -> ".join(path))
        print("\n")
        print("$$$$$$ time $$$$$$")
        
        print("required time for depth first search =",time_required ,"X 10^-4 second")
        print("\n")     

    

def dijkastra(graph,start,goal):
   
    visited=set() 
    heap=[(0,start,start)]
    while heap:
        weight,node,path=heapq.heappop(heap)
        
        respective_node = graph.map1[node]
        if respective_node.name()== goal:
            return path
        if node not in visited:
            visited.add(node)            
            for n in graph.graph[respective_node]:
                new_node, w = n
                if new_node.name() not in visited:
                    cost = float(w) + weight
                    newpath=str(path)+"<->"+str(str(new_node))
                   
                    heapq.heappush(heap,(cost,new_node.name(), newpath))



    return []




def heuristic_function(node):
    
    heuristic={}
    with open('heuristic.txt','r',encoding="utf-8") as f:
        lines = f.readlines()
        for li in lines:
            words=li.split(" ")
            result1=math.pow(float(words[1]), 2)+math.pow(float(words[2]), 2)
            result=math.sqrt(result1)
            
            heuristic[words[0]] = result
    return heuristic[node]
    

def A_Star(graph, start, goal):
    
    visited=set()
    initial = heuristic_function(start)
    heap=[(initial,0,start,start)]
    while heap:
        total, weight,node,path=heapq.heappop(heap)
        respective_node = graph.map1[node]
        if respective_node.name()== goal:
            return path
        if node not in visited:
            visited.add(node)            
            for n in graph.graph[respective_node]:
                new_node, w = n
                if new_node.name() not in visited:
                    cost = float(w) + weight
                    new_total = cost + heuristic_function(new_node.name())
                    newpath=str(path)+"<->"+str(str(new_node))
                   
                    heapq.heappush(heap,(new_total, cost,new_node.name(), newpath))
    return []  

graph = Graph()

with open('file.txt','r',encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        words=line.split(" ")
        graph.make_edge(words[0],words[1],words[2])



start="eforie"
end="neamt"
print("breadth first search")
breadth_first_search(graph,start)
print("###############")
print("depth first search")
depth_first_search(graph,start)
print("###############")
print("djkastra ")
start_time = perf_counter()
print(dijkastra(graph,start,end))
end_time=perf_counter()
print("The time requred for dijkastra algorithm",end_time - start_time,"seconds" )
print("\n")
print("###############")

print("A* shortest path search algorithm")
start_time = perf_counter()
print(A_Star(graph,start,end))
end_time=perf_counter()
print("The time requred for A* algorithm",end_time - start_time,"seconds"  )







