### Your NAMES:
###Oori Schubert
###Wesley Gilpin

from tkinter import *
from Stack import *
from Queue import *
from Heap import *
import sys


#The code creates a regular grid where all first neighbors are connected. The size of the grid is set by the user. The weights are uniformly equal to 1 for all edges. The code returns some information about the graph (such as connecting edges, total weight and adjacency matrix for small systems).

#1. Create the class Vertex using two attributes i,j as inputs that represents the coor- dinate system. Do not forget to include the visited attribute (set to False) and a
#str method.
#2. A constructor for the class Graph that instantiate a rectangular grid graph. Create
#the list of vertices and initialize the adjacency matrix of size nx∗ny to 0.
#3. Implement form2DGrid method that sets the adjacency matrix by adding edges to the Graph to form the 2D grid (all with a weight of 1). Hint: only the first neighbors of each vertex are connected, you may need to know how to map local and global coordinates, you also need to define the method addEdge.
#. The displayInfoGraph method, provides information about the graph. Your output should be similar to the example above. The method returns also the total weight of the graph.
#5. The displayAdjMatrix method, provides the matrix. Your output should be similar to the example above. You also need to implement the simple getnVertex method used to return the value of nVertex in the main code.
#6. Implement the plot method using Tkinter. Multiple Tips: 􏰀 Start your plot method by root=Tk().
#􏰀 You will consider a white canvas of size w=80*nx and h=80*ny.
#3
# 
#􏰀 To migrate from your real math coordinate system to the Tkinter coordinate system, you can use the provided static method toTkinter. For example, if you want to know the i,j pixel Tkinter coordinates of the grid point (2,3) you could do the following :
#         i,j=Graph.toTkinter(2,3,-1,nx,-1,ny,w,h)
#􏰀 Vertices are represented by circle (oval) of radius 10 pixels (and user input color)
#􏰀 Edges are represented by line of width 3 times the weight of the connection (so
#3*1=3 here).
#􏰀 End your plot method by root.mainloop()

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
    def toTkinter(i,j,imin,imax,jmin,jmax,w,h):
        return (i-imin)/(imax-imin)*w,(j-jmin)/(jmax-jmin)*h

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
                    canvas.create_line(i1,j1,i2,j2,width=3*self.adjMatrix[i][j],fill="blue")
        root.mainloop()
    


