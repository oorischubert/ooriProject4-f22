    def dfs(self,node): 
        self.vertices[node].visited=True 
        print(self.vertices[node]) 
        mystack=Stack() 
        mystack.push(node)
        while not mystack.isEmpty():
            j=self.getAdjUnvisitedNode(mystack.peek()) 
            if j is None:
                mystack.pop() 
            else:
                self.vertices[j].visited=True 
                print(self.vertices[j]) 
                mystack.push(j)
        for n in self.vertices: n.visited=False

    def getAdjUnvisitedNode(self,v): 
        for i in range(len(self.vertices)):
            if (self.adjMatrix[v][i]!=0) and (self.vertices[i].visited==False): 
                return i # found neighbor
        return None #no such node

    def bfs(self,node): 
        self.vertices[node].visited=True 
        print(self.vertices[node]) 
        myqueue=Queue() 
        myqueue.enqueue(node)
        while not myqueue.isEmpty():
            k=myqueue.dequeue() 
            while True:
                j=self.getAdjUnvisitedNode(k) 
                if j is None: break 
                self.vertices[j].visited=True 
                print(self.vertices[j]) 
                myqueue.enqueue(j)
        for n in self.vertices: n.visited=False