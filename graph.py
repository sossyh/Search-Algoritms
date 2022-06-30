class node:
    def __init__(self,node):
        self.node = node
        self.adjecencylist = {}

    def add_adjecent_node(self,adjecent, weight=0):
        self.adjecencylist[adjecent] = weight

    def connections(self):
        return self.adjecencylist.keys()

    def weight(self, adjecent):
      return self.adjecencylist[adjecent]
class edge:
    def __init__(self, edge, weight):
        self.edge = edge
        self.weight = weight
    def set_weight(self, weight):
        self.weight = weight
    def get_weight(self):
        return self.weight
class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_node(self, vertex): #adding vertex to the graph
        self.graph[vertex.node] = vertex

    def make_edge(self, node1, node2, weight=0):
        noden1=node(node1)
        noden2=node(node2)
        if node1 not in self.graph:
            self.add_node(noden1)
        if node2 not in self.graph:
            self.add_node(noden2)
        self.graph[node1].add_adjecent_node(self.graph[node2], weight)
    def length(self):
        return len(self.graph)
    def __iter__(self):
        return iter(self.graph.values())
graph = Graph()
def textToGraph():
    with open('file.txt','r',encoding="utf-8") as f:
        lines = f.readlines()
        for li in lines:
            words=li.split(" ")
            graph.make_edge(words[0],words[1],words[2])
         

    for node in graph:
      for edge in node.connections():
        weight=node.weight(edge)
        print('{} <-> {} <-> {}'.format(node.node, edge.node,weight))


textToGraph()
