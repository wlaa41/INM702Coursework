import packages.grid as grid
import packages.node as node
import packages.path as pth

import sys
sys.path.insert(1, 'D:\AAlearnAA\Study\python')
from rutaul.prnt import pg,pm,pr,py

gridsize = (4, 4)
gridlength,gridwidth = gridsize
visitedlist = [(0, 0)]
d = grid.gridgen(gridsize) # Creating the grid ................
d.fillnaughty()
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
        addup(path)
    if x + 1 < gridlength:
        print('CALLING ADD DOWN')
        adddown(path,x+1,y)

    if y + 1 < gridwidth:
        print('CALLING ADD RIGHT')
        addright(path, x, y+1)

def addup(path: pth):
    # check rules
    # if the agent in the extreme left then NO UP
    if path.currentlocation[1] < gridwidth - 2:
        # if the cell has been visited by the path or in the adjusant locationf
        if path.currentlocation not in path.path2start:
            if path.currentlocation not in path.path2startadjacent:
                py("add up")
                checkiftheagentarrive(tobeaddedtoseedingpath[len(tobeaddedtoseedingpath)-1])


def adddown(path: pth,x,y):
    # check rules
    # if the cell has been visited by the path or in the adjusant locationf
    if (x,y) not in path.path2start:
        if (x, y) not in path.path2startadjacent:
            pr("add DOWN")
            tobeaddedtoseedingpath.append(
                pth.path((x, y), d.grid[x, y], d.grid[x, y], path))
            checkiftheagentarrive(tobeaddedtoseedingpath[len(tobeaddedtoseedingpath)-1])



def addright(path: pth, x, y):
    # check rules
    # if the cell has been visited by the path or in the adjusant locationf
    py(path.path2start)
    if (x, y) not in path.path2start:
        py(path.path2start)
        if (x, y) not in path.path2startadjacent:
            pr("add RIGHT")
            tobeaddedtoseedingpath.append(
                pth.path((x, y), d.grid[x, y], d.grid[x, y], path))
            checkiftheagentarrive(tobeaddedtoseedingpath[len(tobeaddedtoseedingpath)-1])



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
        pr("......  Bingooooooo ......")
        pr("......  Bingooooooo ......")
        pr("......  Bingooooooo ......")
        pr("......  Bingooooooo ......")
        pr("......  Bingooooooo ......")
        pr("......  Bingooooooo ......")
        pr("......  Bingooooooo ......")
        pr("......  Bingooooooo ......")
        pr("......  Bingooooooo ......")
        pr("......  Bingooooooo ......")
        pr("......  Bingooooooo ......")
        pr("......  Bingooooooo ......")

tobeaddedtoseedingpath = []
seedingpath.append(pth.path((0,0),0,0,pth.start(0,0)))
notreachedend = True
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
            else:
                path.tick-=1
            if notreachedend == False:
                break
        seedingpath = seedingpath + tobeaddedtoseedingpath
    pg(Doneseedingpath)
        

def loopforthezeros(path):
    x,y = path.currentlocation
    if  x > 0:
        pass
    if x + 1 < gridlength:
        if d.grid[x+1,y]==0:
            print('CALLING ADD DOWN')
            addzerodown(path,x+1,y)

    if y + 1 < gridwidth:
        if d.grid[x, y+1] == 0:
            print('CALLING ADD RIGHT')
            addzeroright(path, x, y+1)


def addzerodown(path: pth, x, y):
    # check rules
    # if the cell has been visited by the path or in the adjusant locationf
    if (x, y) not in path.path2start:
        pr("add DOWN")
        tobeaddedtoseedingpath.append(
            pth.path((x, y), d.grid[x, y], d.grid[x, y], path))
        checkiftheagentarrive(tobeaddedtoseedingpath[len(tobeaddedtoseedingpath)-1])
        loopforthezeros(tobeaddedtoseedingpath[len(tobeaddedtoseedingpath)-1])

def addzeroright(path: pth, x, y):
    # check rules
    # if the cell has been visited by the path or in the adjusant locationf
    py(path.path2start)
    if (x, y) not in path.path2start:
        py(path.path2start)
        pr("add RIGHT")
        tobeaddedtoseedingpath.append(
            pth.path((x, y), d.grid[x, y], d.grid[x, y], path))
        checkiftheagentarrive(tobeaddedtoseedingpath[len(tobeaddedtoseedingpath)-1])
        loopforthezeros(tobeaddedtoseedingpath[len(tobeaddedtoseedingpath)-1])





start()















