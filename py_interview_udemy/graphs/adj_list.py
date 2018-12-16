class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVert = 0

    def addVertex(self, key):
        self.numVert += 1
        newVert = Vertex(key)
        self.vertList[key] = newVert
        return newVert 

    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def getAllVerts(self):
        return self.vertList.keys()

    def __contains__(self, key):
        return key in self.vertList

    def addEdge(self, fromVert, toVert, weight = 0):
        if fromVert not in self.vertList:
            newVert = self.addVertex(fromVert)
        
        if toVert not in self.vertList:
            newVert = self.addVertex(toVert)

        self.vertList[fromVert].addNeighbor(self.vertList[toVert], weight)

    def  __iter__(self):
        return iter(self.vertList.values())
