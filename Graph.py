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
    def __str__(self):
        return "("+str(self.i)+","+str(self.j)+")"

class Graph:
    def __init__(self,nx,ny):
        self.nx=nx
        self.ny=ny
        self.nVertex=nx*ny
        self.vertices=[]
        self.adjMatrix=[[0 for i in range(self.nVertex)] for j in range(self.nVertex)]
        for i in range(nx):
            for j in range(ny):
                self.vertices.append(Vertex(j,i))

    def addEdge(self,i,j,w):
        self.adjMatrix[i][j]=w
        self.adjMatrix[j][i]=w

    def form2DGrid(self):
        for i in range(self.nx):
            for j in range(self.ny):
                if i<self.nx-1:
                    self.addEdge(i*self.ny+j,(i+1)*self.ny+j,1)
                if j<self.ny-1:
                    self.addEdge(i*self.ny+j,i*self.ny+j+1,1)
                    
    def displayInfoGraph(self):
        print("List of edges + weights:")
        for i in range(self.nVertex):
            for j in range(i+1,self.nVertex):
                if self.adjMatrix[i][j]>0:
                    print(self.vertices[i],"<==>",self.vertices[j],self.adjMatrix[i][j])
        print("Total weight:",self.nx*self.ny*2-self.nx-self.ny)
        print()
        #return self.nx*self.ny*2-self.nx-self.ny

    def displayAdjMat(self):
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

    def getnVertex(self):
        return self.nVertex

    def plot(self,color):
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
                if self.adjMatrix[i][j]>0:
                    i1,j1=Graph.toTkinter(self.vertices[i].i,self.vertices[i].j,-1,self.nx,-1,self.ny,w,h)
                    i2,j2=Graph.toTkinter(self.vertices[j].i,self.vertices[j].j,-1,self.nx,-1,self.ny,w,h)
                    canvas.create_line(i1,j1,i2,j2,width=3*self.adjMatrix[i][j],fill=color)
        
        root.mainloop()

#The first part is similar to App1, but you can continue the execution of the code by selecting a search algorithms (DFS or BFS) and a starting global node for performing the search.
#As a result, a new MST graph will be created.
#remark: Depending on the starting point, the MST is not unique since all the weights are the same. You will display the information about the new graph as well (edges connec- tions, total weights, and matrix for small systems).
#The dfs method to perform the depth first search and return a new MST graph. Your output should be similar to the example above. You need the class Stack, provided here. You need to implement the getAdjUnvisitedNode method.
    #App 2 Code

    def dfs(self, node):
        stack = Stack()
        stack.push(node)
        newGraph = Graph(self.nx, self.ny)
        while not stack.isEmpty():
            node = stack.pop()
            if not self.vertices[node].visited:  # type: ignore
                self.vertices[node].visited = True  # type: ignore
                for i in range(self.nVertex):
                    if self.adjMatrix[node][i] > 0 and not self.vertices[i].visited:  # type: ignore
                        stack.push(i)
                        newGraph.addEdge(node, i, 1)
        return newGraph
    
    def bfs(self, node):
        queue = Queue()
        queue.enqueue(node)
        newGraph = Graph(self.nx, self.ny)
        while not queue.isEmpty():
            node = queue.dequeue()
            if not self.vertices[node].visited:  # type: ignore
                self.vertices[node].visited = True  # type: ignore
                for i in range(self.nVertex):
                    if self.adjMatrix[node][i] > 0 and not self.vertices[i].visited:  # type: ignore
                        queue.enqueue(i)
                        newGraph.addEdge(node, i, 1)
        return newGraph

    def getAdjUnvisitedNode(self, node):
        for i in range(self.nVertex):
            if self.adjMatrix[node][i] > 0 and not self.vertices[i].visited:  # type: ignore
                return i