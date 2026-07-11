class Disjoint:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.size = [1]*n


    def findParent(self,u):
        if self.parent[u] == u:
            return self.parent[u]
        self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]

    def unionByRank(self,u,v):
        up_u = self.findParent(u)
        up_v = self.findParent(v)

        if up_u == up_v:
            return 
        if self.rank[up_u] < self.rank[up_v]:
            self.parent[up_u] = up_v
        elif self.rank[up_v] < self.rank[up_u]:
            self.parent[up_v] = up_u
        else:
            self.parent[up_v] = up_u
            self.rank[up_u] += 1

    def unionBySize(self,u,v):
        up_u = self.findParent(u)
        up_v = self.findParent(v)

        if up_u == up_v:
            return
        
        if self.size[up_u] < self.size[up_v]:
            self.parent[up_u] = up_v
            self.size[up_v] += self.size[up_u]
        else:
            self.parent[up_v] = up_u
            self.size[up_u] += self.size[up_v]


ds = Disjoint(8)

# ds.unionByRank(1,2)
# ds.unionByRank(2,3)
# ds.unionByRank(4,5)
# ds.unionByRank(6,7)
# ds.unionByRank(5,6)
# ds.unionByRank(3,7)


ds.unionBySize(1,2)
ds.unionBySize(2,3)
ds.unionBySize(4,5)
ds.unionBySize(6,7)
ds.unionBySize(5,6)
ds.unionBySize(3,7)

# print("parent:", ds.parent)
print("size:  ", ds.size)



