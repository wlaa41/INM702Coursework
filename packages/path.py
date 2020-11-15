
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


        

    def addpath2startAdjacent(self):
        x,y = self.currentlocation
        return [ (x+1,y),(x-1,y),(x,y+1),(x , y -1)]

        
    def __str__(self):
        return f'PATH AT x:{self.currentlocation} is {self.status}'

    def __repr__(self):
        return f'Path @:{self.currentlocation} is {self.status}'
            
