### Your NAMES:
###Oori Schubert
###Wesley Gilpin

from tkinter import *
from Stack import *
from Queue import *
from Heap import *
import sys

class Vertex:
    def __init__(self,i,j):
        self.i=i
        self.j=j
        self.visited=False

    def __str__(self) -> str:
        return "("+str(self.i)+","+str(self.j)+")"

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __lt__(self, other) -> bool:
        return self.weight < other.weight

    def __gt__(self, other) -> bool:
        return self.weight > other.weight

    def __str__(self) -> str:
        return str(self.src) + " " + str(self.dest) + " " + str(self.weight)

class Graph:
    def __init__(self,nx,ny):
        self.nx=nx
        self.ny=ny
        self.nVertex=nx*ny # number of vertices
        self.vertices=[]
        self.adjMatrix=[[0 for i in range(self.nVertex)] for j in range(self.nVertex)] # adjacency matrix
        for i in range(nx):
            for j in range(ny):
                self.vertices.append(Vertex(i,j))

    def addEdge(self,i,j,size=1) -> None:
        self.adjMatrix[i][j]=size
        self.adjMatrix[j][i]=size

    def form2DGrid(self) -> None:
        for i in range(self.nx):
            for j in range(self.ny):
                if i<self.nx-1:
                    self.addEdge(i*self.ny+j,(i+1)*self.ny+j)
                if j<self.ny-1:
                    self.addEdge(i*self.ny+j,i*self.ny+j+1)
                    
    def displayInfoGraph(self) -> None:
        print("List of edges + weights:")
        for i in range(self.nVertex):
            for j in range(i+1,self.nVertex):
                if self.adjMatrix[i][j]>0:
                    print(self.vertices[i],"<==>",self.vertices[j],self.adjMatrix[i][j])
        print("Total weight:",self.getWeight())
        print()
    
    def getWeight(self) -> int:
        weight = 0
        for i in range(self.nVertex):
            for j in range(i+1,self.nVertex):
                if self.adjMatrix[i][j]>0:
                    weight += self.adjMatrix[i][j]
        return weight

    def displayAdjMat(self) -> None:
        print("Matrix:")
        for i in range(self.nVertex):
            for j in range(self.nVertex):
                print(self.adjMatrix[i][j],end=" ")
            print()
    
    @staticmethod
    def toTkinter(x,y,xmin,xmax,ymin,ymax,width,height):
        i=int((x-xmin)*(width)/(xmax-xmin))
        j=int((ymax-y)*(height)/(ymax-ymin))
        return i,j

    def getnVertex(self) -> int:
        return self.nVertex

    def plot(self,color) -> None:
        root=Tk()
        w=80*self.nx
        h=80*self.ny
        canvas=Canvas(root,width=w,height=h,bg="white")
        canvas.pack()
        for i in range(self.nVertex):
                i,j=Graph.toTkinter(self.vertices[i].i,self.vertices[i].j,-1,self.nx,-1,self.ny,w,h)
                canvas.create_oval(i-10,j-10,i+10,j+10,fill=color)
            
        for i in range(self.nVertex):
            for j in range(i+1,self.nVertex):
                    if self.adjMatrix[i][j] != 0:
                        i1,j1=Graph.toTkinter(self.vertices[i].i,self.vertices[i].j,-1,self.nx,-1,self.ny,w,h)
                        i2,j2=Graph.toTkinter(self.vertices[j].i,self.vertices[j].j,-1,self.nx,-1,self.ny,w,h)
                        canvas.create_line(i1,j1,i2,j2,width=3*self.adjMatrix[i][j],fill=color)
        root.mainloop()

    def dfs(self, node) -> "Graph":
        stack = Stack()
        self.vertices[node].visited = True 
        stack.push(node)
        newGraph = Graph(self.nx, self.ny)
        while not stack.isEmpty():
            j=self.getAdjUnvisitedNode(stack.peek())
            if j is None:
                stack.pop()
            else:
                self.vertices[j].visited = True # type: ignore
                newGraph.addEdge(stack.peek(), j, self.adjMatrix[stack.peek()][j]) # type: ignore
                stack.push(j)
        for n in self.vertices: n.visited = False
        return newGraph
            
    
    def bfs(self, node) -> "Graph":
        queue = Queue()
        self.vertices[node].visited = True 
        queue.enqueue(node)
        newGraph = Graph(self.nx, self.ny)
        while not queue.isEmpty():
            node = queue.dequeue()
            while True:
                j = self.getAdjUnvisitedNode(node)
                if j is None: break
                self.vertices[j].visited = True
                newGraph.addEdge(j, node, self.adjMatrix[j][node]) # type: ignore
                queue.enqueue(j)
                        
        for n in self.vertices: n.visited = False
        return newGraph

    def getAdjUnvisitedNode(self, node):
        for i in range(self.nVertex):
            if self.adjMatrix[node][i] != 0 and not self.vertices[i].visited:  # type: ignore
                return i
        return None

    # The method load2Dgrid that reads the edge info from the file and initialize the matrix with weights. If a file does not exist, the code should stop executing without bug (while displaying some info saying the file does not exist)
    #The file contains the list of edges making the connections between two vertices (in global coordinates) associated with a given weight
    #needs to work for rectangular matrices as well as square ones
    
    def load2DGrid(self, file):
        try: grid = open(file, "r")
        except:
                print("File " + file + " does not exist!")
                sys.exit(0)
        lines = grid.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
            lines[i] = lines[i].split(" ") # type: ignore #
            self.addEdge(int(lines[i][0]), int(lines[i][1]), int(lines[i][2]))
        grid.close()


    def mstw(self,node) -> "Graph":
        heap = Heap()
        newGraph = Graph(self.nx, self.ny)
        self.vertices[node].visited = True
        for i in range(self.nVertex):
            if self.adjMatrix[node][i] != 0:
                heap.insert(Edge(node, i, self.adjMatrix[node][i])) # type: ignore
        while not heap.isEmpty():
            edge = heap.remove()
            if not self.vertices[edge.dest].visited: # type: ignore
                self.vertices[edge.dest].visited = True # type: ignore
                newGraph.addEdge(edge.src, edge.dest, edge.weight) # type: ignore
                for i in range(self.nVertex):
                    if self.adjMatrix[edge.dest][i] != 0 and not self.vertices[i].visited: # type: ignore
                        heap.insert(Edge(edge.dest, i, self.adjMatrix[edge.dest][i])) # type: ignore
        for n in self.vertices: n.visited = False
        return newGraph


        
        
    