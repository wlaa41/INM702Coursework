import packages.grid as grid
import packages.node as node
import numpy as np
import pdb
import packages.path as pth
import sys
import copy as copy
sys.path.insert(1, 'D:\AAlearnAA\Study\python')

from rutaul.prnt import pg, pm, pr, py, pb

# ------------------- Creating the random grid
gridsize = (3, 3)
gridlength, gridwidth = gridsize
visitedlist = [(0, 0)]
d = grid.gridgen(gridsize)  # Creating the grid ................
d.reachedpointgrid = 9999 * np.ones(gridsize).astype(int)

pr(d.reachedpointgrid)
# d.fillnaughty()
# d.fillreallynaughty()D
# d.fillreallynaughtyLEFTUP()
# d.grid = np.ones(gridsize)
d.easytest()
pg(d.grid)

# ---------------------------------------------

# ------------- Creating lists to hold data
reachednodes = [(0, 0)]
WEIGHTreachednodes = []
DONEseedingpath = []
seedingpath = []
terminatedpath = []
to_be_added2seedingpath = []  # This list is created because while
# we iterate through seeding list we save all the next seeding paths
# ---------------------------------------------

# ------------- Global var for all functions to mainpulate
notreachedend = True
# ---------------------------------------------


# ----------- Creating a path at any node and examin
# one of the adjacent direction UP DOWN LEFT RIGHT
def createpath(path: pth):
    x, y = path.currentlocation
    # pdb.set_trace()
    if x - 1 >= 0:  # -- CHECK THE GRID DIMENESION
        pg('CALLING ADD UP')
        addup(path, x-1, y)
    if x + 1 < gridlength:  # -- CHECK THE GRID DIMENESION
        pg('CALLING ADD DOWN')
        adddown(path, x+1, y)

    if y + 1 < gridwidth:  # -- CHECK THE GRID DIMENESION
        pg('CALLING ADD RIGHT')
        addright(path, x, y+1)

    if y - 1 >= 0:  # -- CHECK THE GRID DIMENESION
        pg('CALLING ADD LEFT')
        addleft(path, x, y-1)


def addup(path: pth, x, y):
    # check rules FOR UP
    # if the agent in the extreme left then NO UP
    if path.currentlocation[1] < gridwidth - 2:
        # if the cell has been visited by the path or in the adjusant locationf
        if (x, y) not in path.path2start:
            if (x, y) not in path.path2startadjacent:
                # pr("add UP")
                tobeaddedThencheckiftheagentarrive(path, x, y)


def adddown(path: pth, x, y):
    # check rules FOR DOWN
    # if the cell has been visited by the path or in the adjusant locationf
    if (x, y) not in path.path2start:
        if (x, y) not in path.path2startadjacent:
            # pr("add DOWN")
            tobeaddedThencheckiftheagentarrive(path, x, y)


def addright(path: pth, x, y):
    # check rules
    # if the cell has been visited by the path or in the adjusant locationf
    if (x, y) not in path.path2start:
        if (x, y) not in path.path2startadjacent:
            # pr("add RIGHT")
            tobeaddedThencheckiftheagentarrive(path, x, y)


def addleft(path: pth, x, y):
    # check rules
    if path.currentlocation[0] < gridlength - 2:
        # if the cell has been visited by the path or in the adjusant locationf
        if (x, y) not in path.path2start:
            if (x, y) not in path.path2startadjacent:
                # pr("add LEFT")
                tobeaddedThencheckiftheagentarrive(path, x, y)

# While iterating in the seeding paths "seedingpath list" we add the braches in this array
# To avoid adding whilt iterating


def tobeaddedThencheckiftheagentarrive(path: pth, x, y):
    """Adding to the seeding path but through mid list To avoid adding whilt iterating 

    Args:
        path (pth): Father path
        x (int): New point coordinate column number "Child path"
        y (int): New point coordinate column number "Child path"
    """
    # Checking if the cell has been visited by another path in shorter time
    # if yes then no path will be created
    if path.weight + d.grid[x, y] < d.reachedpointgrid[x, y]:
        d.reachedpointgrid[x, y] = path.weight + d.grid[x, y]
        to_be_added2seedingpath.append(
            pth.path((x, y), d.grid[x, y], d.grid[x, y], path))
        checkiftheagentarrive(
            to_be_added2seedingpath[len(to_be_added2seedingpath)-1])


# Check if one of the pathes reachs the end point
def checkiftheagentarrive(path):
    x, y = path.currentlocation
    if (x, y) == (gridlength-1, gridwidth-1):
        global notreachedend
        notreachedend = False
        pr('...............................................................')
        pg(f' {d.grid}')
        pg(f' {path.path2start}  W: {path.weight}')
        pr('...............................................................')
        pr("               .........  Bingooooooo .........")
        pr("               .........  Bingooooooo .........")
        pr("               .......                  .......")
        pr('               .....         \(")/        .....')
        pr("               .....         -( )-        .....")
        pr("               .....         /(_)\        .....")
        pr("               .......                  .......")
        pr("               .........  Bingooooooo .........")
        pr("               .........  Bingooooooo .........")
        pr('...............................................................')
        pb('        .__                       __                     __    ')
        pb('  ______|  |__    ____  _______ _/  |_   ____    _______/  |_  ')
        pb(' /  ___/|  |  \  /  _ \ \_  __ \\   __\_/ __ \  /  ___/\   __\ ')
        pb(' \___ \ |   Y  \(  <_> ) |  | \/ |  |  \  ___/  \___ \  |  |   ')
        pb('/____  >|___|  / \____/  |__|    |__|   \___  >/____  > |__|   ')
        pb('     \/      \/                             \/      \/         ')
        # print(f' {path.path2start}  W: {path.weight}')
        pr('...............................................................')


# Looking in one of the four direction for zeros nodes so we can add the braches of those nodes
# right away as zero stand for no time the function berform test then call addzero function
def loopforthezeros(path):
    x, y = path.currentlocation
    if x > 0:
        pass
    if x + 1 < gridlength:
        if d.grid[x+1, y] == 0:
            # py('ADD Zero DOWN')
            addzeroPATH(path, x+1, y)

    if y + 1 < gridwidth:
        if d.grid[x, y+1] == 0:
            # py('ADD Zero RIGHT')
            addzeroPATH(path, x, y+1)

    if x - 1 >= 0:
        if d.grid[x-1, y] == 0:
            # py('ADD Zero UP')
            addzeroPATH(path, x-1, y)

    if y - 1 >= 0:
        if d.grid[x, y-1] == 0:
            # py('ADD Zero LEFT')
            addzeroPATH(path, x, y-1)


def addzeroPATH(path: pth, x, y):
    # check rules
    # if the cell has been visited by the path or in the adjusant locationf
    if (x, y) not in path.path2start:
        # pr("add ZERO D")
        tobeaddedThencheckiftheagentarrive(path, x, y)
        loopforthezeros(
            to_be_added2seedingpath[len(to_be_added2seedingpath)-1])


#################################################################################################
#############################                                     ###############################
#############################   Starting the search from a[0,0]   ###############################
#############################                                     ###############################
#################################################################################################

to_be_added2seedingpath.append(pth.path((0, 0), 0, 0, pth.start(0, 0)))
loopforthezeros(to_be_added2seedingpath[0])
d.reachedpointgrid[0, 0] = 0
seedingpath = to_be_added2seedingpath.copy()
py(f'Before looping seedignpath : {seedingpath}')


py(f'After seedignpath : {seedingpath}')

# val = input("Enter your value: ")
Tick = 0


def start():

    global notreachedend
    global Tick
    while(notreachedend):
        global to_be_added2seedingpath
        global seedingpath

        pr(d.grid)
        pb(d.reachedpointgrid)
        pr(f'Global Time: {Tick}')
        py(f'After seedignpath : {seedingpath}')
        py(f'Number of seedignpath : {len(seedingpath)}')

        # pg(seedingpath)
        for path in seedingpath:
            # py(path.tick)
            if path.tick == 0:
                # pg(seedingpath)
                pdb.set_trace()
                createpath(path)
                path.status = "DONE Seeding"

                DONEseedingpath.append(path)
                to_be_added2seedingpath.remove(path)
                pdb.set_trace()
                loopforthezeros(path)
                # pm(f'Before adding adj adj:{path.path2startadjacent}')
                # a method to add the neighboring cells in the path to avoid looking for a path that is not neccesory
                path.addadjacentcellasNOGO(gridsize)
                # pm(f'After adding adj adj:{path.path2startadjacent}')
            else:
                path.tick -= 1
                to_be_added2seedingpath.append(path)
            if notreachedend == False:
                break

        seedingpath = to_be_added2seedingpath.copy()
        to_be_added2seedingpath = []

        Tick += 1
    # pg(DONEseedingpath)


start()
