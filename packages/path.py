
import copy as c
class start():
    def __init__(self,currentlocation=0, currentcellweight=0 ,incomingcell = None , status="seeding", rightmoving = 0,downmoving= 0):
        self.path2start = []
        self.path2startadjacent = []
        self.weight =0
        self.status = "start"
        self.incomingcell = None
        self.path2startadjacent = []
        self.currentcellweight = 0
        self.currentlocation = (0,0)
    def updateadjacent(self): 
        # def addpath2startAdjacent(self):
        pass


class path():
    def __init__(self,currentlocation, currentcellweight , tick ,incomingcell = None , status="seeding", rightmoving = 0,downmoving= 0):
        self.path2start = []
        self.path2startadjacent = []
        self.tick = tick
        # self.path2start = c.copy(incomingcell.path2start)
        # self.path2startad = c.copy(incomingcell.path2start)
        self.currentlocation = currentlocation
        self.incomingcell = incomingcell
        self.currentcellweight = currentcellweight
        self.status = status
        self.updatepathvar()
        self.rightmoving = rightmoving
        self.downmoving = downmoving

    def updatepathvar(self):
        self.weight = self.incomingcell.weight + self.currentcellweight
        self.path2start = [self.currentlocation] + self.incomingcell.path2start

    def addadjacentcellasNOGO(self,gridsize):
        # print('.........................................................................')
        # print(f'      Path ID: {id(self.incomingcell)} --> Branch ID: {id(self)}')
        # print('.........................................................................')
        # print(f'incomingcell.path2startadjacent {self.incomingcell.path2startadjacent}')
        self.path2startadjacent = self.path2startadjacent + self.incomingcell.path2startadjacent
        for point in self.addpath2startAdjacent(gridsize):
            # print(f'      {id(self)} point:{point} path2start:{self.path2start} CON {point not in self.path2start}')
            
            if point not in self.path2start:
                if point not in self.path2startadjacent:
                    self.path2startadjacent.append(point)
        # print(f'path: {self.path2start}')
        # print(f'adj: {self.path2startadjacent}')
                
        

    def addpath2startAdjacent(self,gridsize):
        x,y = self.incomingcell.currentlocation
        n,m = gridsize
        adjacent = []
        if x-1 > 0:
            adjacent.append((x-1, y))
        if y-1 > 0:
            adjacent.append((x, y-1))
        if x+1 < n:
            adjacent.append((x+1, y))
        if y+1 < m:
            adjacent.append((x, y+1))
        return adjacent

        
    def __str__(self):
        return f'PATH AT x:{self.currentlocation} is {self.status}'

    def __repr__(self):
        return f'Path @:{self.currentlocation} is {self.status} time: {self.tick}'
        
            
