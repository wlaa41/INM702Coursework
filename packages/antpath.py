

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

    def addpath2startAdjacent(self):
        return []


class path():
    def __init__(self, currentlocation, currentcellweight, gridsize, incomingcell=None,
    antscount = 0 ,reached = False, status="seeding", rightmoving = 0,downmoving= 0 ):
        self.path2start = []
        self.path2startadjacent = []
        self.antscount = antscount
        self.currentlocation = currentlocation
        self.incomingcell = incomingcell
        self.currentcellweight = currentcellweight
        self.status = status
        self.updatepathvar()
        self.rightmoving = rightmoving
        self.downmoving = downmoving
        self.gridsize = gridsize

    def updatepathvar(self):
        self.weight = self.incomingcell.weight + self.currentcellweight
        self.path2start =  self.incomingcell.path2start + [self.currentlocation] 

    def addadjacentcellasNOGO(self):
        
        self.path2startadjacent = self.incomingcell.incomingcell + self.incomingcell.addpath2startAdjacentJ() 
        # print('.........................................................................')
        # print(f'      Path ID: {id(self.incomingcell)} --> Branch ID: {id(self)}')
        # print('.........................................................................')
        # print(f'incomingcell.path2startadjacent {self.incomingcell.path2startadjacent}')
        # self.path2startadjacent = self.path2startadjacent + self.incomingcell.path2startadjacent
        # for point in self.addpath2startAdjacent(self.gridsize):
        #     if point not in self.path2start:
        #         if point not in self.path2startadjacent:
        #             self.path2startadjacent.insert(0, point)
        

    def addpath2startAdjacent(self):
        x,y = self.incomingcell.currentlocation
        n,m = self.gridsize
        adjacent = []
        # if x-1 > 0:
        adjacent.append((x-1, y))
        # if y-1 > 0:
        adjacent.append((x, y-1))
        # if x+1 < n:
        adjacent.append((x+1, y))
        # if y+1 < m:
        adjacent.append((x, y+1))
        return adjacent

        
    def __str__(self):
        return f'PATH AT x:{self.currentlocation} is {self.status} ants: {self.antscount}'

    def __repr__(self):
        return f'Path @:{self.currentlocation} is {self.status} ants: {self.antscount}'
        
            
