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


#1. Create the class Vertex using two attributes i,j as inputs that represents the coor- dinate system. Do not forget to include the visited attribute (set to False) and a
#str method.
#2. A constructor for the class Graph that instantiate a rectangular grid graph. Create
#the list of vertices and initialize the adjacency matrix of size nx∗ny to 0.
#3. Implement form2DGrid method that sets the adjacency matrix by adding edges to the Graph to form the 2D grid (all with a weight of 1). Hint: only the first neighbors of each vertex are connected, you may need to know how to map local and global coordinates, you also need to define the method addEdge.
#4. The displayInfoGraph method, provides information about the graph. Your output should be similar to the example above. The method returns also the total weight of the graph.
#5. The displayAdjMatrix method, provides the matrix. Your output should be similar to the example above. You also need to implement the simple getnVertex method used to return the value of nVertex in the main code.
#6. Implement the plot method using Tkinter. Multiple Tips: 􏰀 Start your plot method by root=Tk().
#􏰀 You will consider a white canvas of size w=80*nx and h=80*ny.
#3
#􏰀 To migrate from your real math coordinate system to the Tkinter coordinate system, you can use the provided static method toTkinter. For example, if you want to know the i,j pixel Tkinter coordinates of the grid point (2,3) you could do the following :
#         i,j=Graph.toTkinter(2,3,-1,nx,-1,ny,w,h)
#􏰀 Vertices are represented by circle (oval) of radius 10 pixels (and user input color)
#􏰀 Edges are represented by line of width 3 times the weight of the connection (so
#3*1=3 here).
#􏰀 End your plot method by root.mainloop()
#The first part is similar to App1, but you can continue the execution of the code by selecting a search algorithms (DFS or BFS) and a starting global node for performing the search.
#As a result, a new MST graph will be created.
#Remark: Depending on the starting point, the MST is not unique since all the weights are the same. You will display the information about the new graph as well (edges connec- tions, total weights, and matrix for small systems).
#Here is what happens if we continue the execution using DFS with Vertex 0:

#1. The dfs method to perform the depth first search and return a new MST graph. Your output should be similar to the example above. You need the class Stack, provided here. You need to implement the getAdjUnvisitedNode method.
#6
#  
#2. You need to implement the bfs method to perform the breadth first search. Your output should be similar to the example above. You need the class Queue, provided here.


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
        
    def plot(self,color):
        root=Tk()
        w=80*self.nx
        h=80*self.ny
        canvas=Canvas(root,width=w,height=h,bg="white")
        canvas.pack()
        for i in range(self.nVertex):
            #onlu display circle if 
            if not self.vertices[i].visited:
                i,j=Graph.toTkinter(self.vertices[i].i,self.vertices[i].j,-1,self.nx,-1,self.ny,w,h)
                canvas.create_oval(i-10,j-10,i+10,j+10,fill=color)
            
        for i in range(self.nVertex):
            for j in range(i+1,self.nVertex):
                if self.adjMatrix[i][j]>0:
                    if self.adjMatrix[i][j]==1:
                        i1,j1=Graph.toTkinter(self.vertices[i].i,self.vertices[i].j,-1,self.nx,-1,self.ny,w,h)
                        i2,j2=Graph.toTkinter(self.vertices[j].i,self.vertices[j].j,-1,self.nx,-1,self.ny,w,h)
                        canvas.create_line(i1,j1,i2,j2,width=3*self.adjMatrix[i][j],fill=color)
        root.mainloop()

#The first part is similar to App1, but you can continue the execution of the code by selecting a search algorithms (DFS or BFS) and a starting global node for performing the search.
#As a result, a new MST graph will be created.
#remark: Depending on the starting point, the MST is not unique since all the weights are the same. You will display the information about the new graph as well (edges connec- tions, total weights, and matrix for small systems).
#The dfs method to perform the depth first search and return a new MST graph. Your output should be similar to the example above. You need the class Stack, provided here. You need to implement the getAdjUnvisitedNode method.
    #App 2 Code
#Welcome to Graph App 2
#========================
#Enter Total Grid Size Nx and Ny: 3 3
#List of edges + weights:
#(0,0) <==> (1,0) 1
#(0,0) <==> (0,1) 1
#(1,0) <==> (2,0) 1
#(1,0) <==> (1,1) 1
#(2,0) <==> (2,1) 1
#(0,1) <==> (1,1) 1
#(0,1) <==> (0,2) 1
#(1,1) <==> (2,1) 1
#(1,1) <==> (1,2) 1
#(2,1) <==> (2,2) 1
#(0,2) <==> (1,2) 1
#(1,2) <==> (2,2) 1
#Total weight: 12
#5
#Matrix: 010100000 101010000 010001000 100010100 010101010 001010001 000100010 000010101 000001010
#Perform: 1-DFS or 2-BFS? 2
#Choose the starting node number: 0
#List of edges + weights:
#(0,0) <==> (1,0) 1
#(0,0) <==> (0,1) 1
#(1,0) <==> (2,0) 1
#(1,0) <==> (1,1) 1
#(2,0) <==> (2,1) 1
#(0,1) <==> (0,2) 1
#(1,1) <==> (1,2) 1
#(2,1) <==> (2,2) 1
#Total weight: 8

    def dfs3(self, node):
        stack = Stack()
        stack.push(node)
        newGraph = Graph(self.nx, self.ny)
        while not stack.isEmpty():
            node = stack.pop()
            if not self.vertices[node].visited: # type: ignore
                self.vertices[node].visited = True # type: ignore
                for i in range(self.nVertex):
                    if self.adjMatrix[node][i] > 0 and not self.vertices[i].visited: # type: ignore
                        stack.push(i)
                        newGraph.addEdge(node, i, 1)
        return newGraph
    
    def bfs3(self, node):
        queue = Queue()
        queue.enqueue(node)
        newGraph = Graph(self.nx, self.ny)
        while not queue.isEmpty():
            node = queue.dequeue()
            if not self.vertices[node].visited: # type: ignore
                self.vertices[node].visited = True # type: ignore
                for i in range(self.nVertex):
                    if self.adjMatrix[node][i] > 0 and not self.vertices[i].visited: # type: ignore
                        queue.enqueue(i)
                        newGraph.addEdge(node, i, 1)
        return newGraph

    def getAdjUnvisitedNode(self, node):
        for i in range(self.nVertex):
            if self.adjMatrix[node][i] > 0 and not self.vertices[i].visited:  # type: ignore
                return i

    def dfs(self, node):
        newGraph = Graph(self.nx, self.ny)
        self.vertices[node].visited = True # type: ignore
        for i in range(self.nVertex):
            if self.adjMatrix[node][i] > 0 and not self.vertices[i].visited: # type: ignore
                newGraph.addEdge(node, i, 1)
                self.dfs(i)
        return newGraph
    
    def bfs(self, node):
        newGraph = Graph(self.nx, self.ny)
        queue = Queue()
        queue.enqueue(node)
        while not queue.isEmpty():
            node = queue.dequeue()
            if not self.vertices[node].visited: # type: ignore
                self.vertices[node].visited = True # type: ignore
                for i in range(self.nVertex):
                    if self.adjMatrix[node][i] > 0 and not self.vertices[i].visited: # type: ignore
                        queue.enqueue(i)
                        newGraph.addEdge(node, i, 1)
        return newGraph

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