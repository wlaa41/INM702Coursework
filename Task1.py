import packages.grid as grid
import packages.node as node
import packages.path as pth

import sys
sys.path.insert(1, 'D:\AAlearnAA\Study\python')
from rutaul.prnt import pg,pm,pr,py

gridsize = (5, 5)
gridlength,gridwidth = gridsize
visitedlist = [(0, 0)]
d = grid.gridgen(gridsize) # Creating the grid ................
# d.fillnaughty()
# d.fillreallynaughty()
d.fillreallynaughtyLEFTUP()
pg(d.grid)
pm(d.grid[0, 1])
pm(d.grid[1, 0])


reachednodes = [(0, 0)]
connectednodes = []
Doneseedingpath = []
seedingpath = []
terminatedpath = []



def createpath(path: pth ):
    x,y = path.currentlocation
    if  x- 1 >= 0:
        print('CALLING ADD UP')
        addup(path, x-1,y)
    if x + 1 < gridlength:
        print('CALLING ADD DOWN')
        adddown(path,x+1,y)

    if y + 1 < gridwidth:
        print('CALLING ADD RIGHT')
        addright(path, x, y+1)
    
    if  y - 1 >= 0:
        print('CALLING ADD LEFT')
        addleft(path, x, y-1)

def addup(path: pth,x,y):
    # check rules
    # if the agent in the extreme left then NO UP
    if path.currentlocation[1] < gridwidth - 2:
        # if the cell has been visited by the path or in the adjusant locationf
        if (x,y) not in path.path2start:
            if (x, y) not in path.path2startadjacent:
                pr("add UP")
                tobeaddedThencheckiftheagentarrive(path  , x, y)


def adddown(path: pth,x,y):
    # check rules
    # if the cell has been visited by the path or in the adjusant locationf
    if (x,y) not in path.path2start:
        if (x, y) not in path.path2startadjacent:
            pr("add DOWN")
            tobeaddedThencheckiftheagentarrive(path  , x, y)




def addright(path: pth, x, y):
    # check rules
    # if the cell has been visited by the path or in the adjusant locationf
    if (x, y) not in path.path2start:
        if (x, y) not in path.path2startadjacent:
            pr("add RIGHT")
            tobeaddedThencheckiftheagentarrive(path  , x, y)

def addleft(path: pth, x, y):
    # check rules
    if path.currentlocation[0] < gridlength - 2 :
        # if the cell has been visited by the path or in the adjusant locationf
        if (x, y) not in path.path2start:
            if (x, y) not in path.path2startadjacent:
                pr("add LEFT")
                tobeaddedThencheckiftheagentarrive(path  , x, y)


def tobeaddedThencheckiftheagentarrive(path: pth, x, y):
    tobeaddedtoseedingpath.append(
        pth.path((x, y), d.grid[x, y], d.grid[x, y], path))
    checkiftheagentarrive(
        tobeaddedtoseedingpath[len(tobeaddedtoseedingpath)-1])

def checkiftheagentarrive(path):
    x,y = path.currentlocation
    if (x, y) == (gridlength-1,gridwidth-1):
        global notreachedend 
        notreachedend = False
        pr('..................................................')
        print(f' {d.grid}')
        print(f' {path.path2start}  W: {path.weight}')
        pr('..................................................')
        pr("......  Bingooooooo ......")
        pr("......  Bingooooooo ......")
        pr("....                  ....")
        pr('..         \(")/        ..')
        pr("..         -( )-        ..")
        pr("..         /(_)\        ..")
        pr("....                  ....")
        pr("......  Bingooooooo ......")
        pr("......  Bingooooooo ......")


def loopforthezeros(path):
    x, y = path.currentlocation
    if x > 0:
        pass
    if x + 1 < gridlength:
        if d.grid[x+1, y] == 0:
            py('ADD Zero DOWN')
            addzeroPATH(path, x+1, y)

    if y + 1 < gridwidth:
        if d.grid[x, y+1] == 0:
            py('ADD Zero RIGHT')
            addzeroPATH(path, x, y+1)

    if x - 1 >= 0:
        if d.grid[x-1, y] == 0:
            py('ADD Zero UP')
            addzeroPATH(path, x-1, y)

    if y - 1 >= 0:
        if d.grid[x, y-1] == 0:
            py('ADD Zero LEFT')
            addzeroPATH(path, x, y-1)


def addzeroPATH(path: pth, x, y):
    # check rules
    # if the cell has been visited by the path or in the adjusant locationf
    if (x, y) not in path.path2start:
        pr("add ZERO D")
        tobeaddedThencheckiftheagentarrive(path  , x, y)
        loopforthezeros(tobeaddedtoseedingpath[len(tobeaddedtoseedingpath)-1])


tobeaddedtoseedingpath = []
seedingpath.append(pth.path((0,0),0,0,pth.start(0,0)))

notreachedend = True
loopforthezeros(seedingpath[0])
def start():
    
    global notreachedend
    while(notreachedend):
        global tobeaddedtoseedingpath
        tobeaddedtoseedingpath = []
        global seedingpath

        pm(seedingpath)
        for path in seedingpath:
            py(path.tick)
            if path.tick == 0:
                pg(seedingpath)
                createpath(path)
                path.status="DONE Seeding"
              
                Doneseedingpath.append(path)
                seedingpath.remove(path)
                loopforthezeros(path)
                pm(f'Before adding adj adj:{path.path2startadjacent}')
                path.addadjacentcellasNOGO(gridsize) # a method to add the neighboring cells in the path to avoid looking for a path that is not neccesory
                pm(f'After adding adj adj:{path.path2startadjacent}')
            else:
                path.tick-=1
            if notreachedend == False:
                break
        seedingpath = seedingpath + tobeaddedtoseedingpath
    pg(Doneseedingpath)
        





start()















