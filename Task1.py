import packages.grid as grid
import packages.node as node
import numpy as np
import packages.path as pth
import pdb
import sys
sys.path.insert(1, 'D:\AAlearnAA\Study\python')
from rutaul.prnt import pg,pm,pr,py,pb



# ------------------- Creating the random grid
gridsize = (15, 11)

d = grid.gridgen(gridsize) # Creating the grid ................

# pr(d.reachedpointgrid )
# # d.fillnaughty()
# gridsize = d.fillmaddness()
gridsize = d.jiktest()
gridsize = d.fillreallynaughtyLEFTUP()
# gridlength,gridwidth = gridsize
# d.reachedpointgrid = 999 * np.ones(gridsize).astype(int)
# d.fillreallynaughtyLEFTUP()
# d.fillreallynaughtyLEFTUP()
# d.grid = np.ones(gridsize)
# d.grid = d.fillgridMOREZeros(morezeroby=7)
# d.easytest()
# pg(d.grid)
gridlength, gridwidth = gridsize
visitedlist = [(0, 0)]
d.reachedpointgrid = 999 * np.ones(gridsize).astype(int)

# ---------------------------------------------

# ------------- Creating lists to hold data
reachednodes = [(0, 0)]
WEIGHTreachednodes = []
DONEseedingpath = []
seedingpath = []
terminatedpath = []
to_be_added2seedingpath = [] # This list is created because while
# we iterate through seeding list we save all the next seeding paths
# ---------------------------------------------

# ------------- Global var for all functions to mainpulate 
notreachedend = True
# ---------------------------------------------


def loopforthezeros(path):
    x, y = path.currentlocation

    # pdb.set_trace()#
    if x + 1 < gridlength:
        if d.grid[x+1, y] == 0:
            py('ADD Zero DOWN')
            addzeroPATH(path, x+1, y, 'down')

    if y + 1 < gridwidth:
        if d.grid[x, y+1] == 0:
            # pdb.set_trace()#
            py('ADD Zero RIGHT')
            addzeroPATH(path, x, y+1,'right')

    if x - 1 >= 0:
        if d.grid[x-1, y] == 0:
            py('ADD Zero UP')
            addzeroPATH(path, x-1, y, 'up')

    if y - 1 >= 0:
        if d.grid[x, y-1] == 0:
            py('ADD Zero LEFT')
            addzeroPATH(path, x, y-1, 'left')
    # # pdb.set_trace()#


def addzeroPATH(path: pth, x, y,info):
    # check rules
    # if the cell has been visited by the path or in the adjusant locationf
    if path.weight + d.grid[x, y] < d.reachedpointgrid[x, y]:
        pm('            addzeroPATH')
        # pdb.set_trace()#

        if (x, y) not in path.path2start:
            pr(f'add ZERO {info}')
            tobeaddedThencheckiftheagentarrive(path, x, y)
            loopforthezeros(
                to_be_added2seedingpath[len(to_be_added2seedingpath)-1])

# ----------- Creating a path at any node and examin
# one of the adjacent direction UP DOWN LEFT RIGHT
def createpath(path: pth ):
    x,y = path.currentlocation
    print(f'                                                    path  {path.currentlocation}')
    if  x- 1 >= 0: # -- CHECK THE GRID DIMENESION
        pg('CALLING ADD UP')
        addup(path, x-1,y)
    if x + 1 < gridlength:# -- CHECK THE GRID DIMENESION
        pg('CALLING ADD DOWN')
        adddown(path,x+1,y)

    if y + 1 < gridwidth:# -- CHECK THE GRID DIMENESION
        pg('CALLING ADD RIGHT')
        addright(path, x, y+1)
    
    if y - 1 >= 0:  # -- CHECK THE GRID DIMENESION
        pg('CALLING ADD LEFT')
        addleft(path, x, y-1)

def addup(path: pth,x,y):
    # check rules FOR UP 
    # if the agent in the extreme left then NO UP
    if path.currentlocation[1] < gridwidth - 2:
        # if the cell has been visited by the path or in the adjusant locationf
        if (x,y) not in path.path2start:
            if (x, y) not in path.path2startadjacent:
                # pr("add UP")
                tobeaddedThencheckiftheagentarrive(path  , x, y)


def adddown(path: pth,x,y):
    # check rules FOR DOWN
    # if the cell has been visited by the path or in the adjusant locationf
    if (x,y) not in path.path2start:
        if (x, y) not in path.path2startadjacent:
            # pr("add DOWN")
            tobeaddedThencheckiftheagentarrive(path  , x, y)

def addright(path: pth, x, y):
    # check rules
    # if the cell has been visited by the path or in the adjusant locationf
    if (x, y) not in path.path2start:
        if (x, y) not in path.path2startadjacent:
            # pr("add RIGHT")
            tobeaddedThencheckiftheagentarrive(path  , x, y)


def addleft(path: pth, x, y):
    # check rules
    if path.currentlocation[0] < gridlength - 2 :
        # if the cell has been visited by the path or in the adjusant locationf
        if (x, y) not in path.path2start:
            if (x, y) not in path.path2startadjacent:
                pr("add LEFT")
                tobeaddedThencheckiftheagentarrive(path  , x, y)

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
    # pdb.set_trace()#
    if path.weight + d.grid[x, y] < d.reachedpointgrid[x,y]:
        d.reachedpointgrid[x,y] = path.weight + d.grid[x,y] 
        temp = pth.path((x, y), d.grid[x, y], d.grid[x, y], path)

        to_be_added2seedingpath.append( temp)
        checkiftheagentarrive(temp)
        # loopforthezeros(temp)
        

# Check if one of the pathes reachs the end point
def checkiftheagentarrive(path):
    x,y = path.currentlocation
    
    if (x, y) == (gridlength-1,gridwidth-1):
    
        arrivingweight = path.weight# + d.grid[x, y]
        d.reachedpointgrid[x,y]
        global notreachedend 
        notreachedend = False
        pr('...............................................................')
        pr(d.grid)
        pb(d.reachedpointgrid)
        pg(f' {path.path2start}  W: {arrivingweight}')
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
        drawpath(path)
# Looking in one of the four direction for zeros nodes so we can add the braches of those nodes 
# right away as zero stand for no time the function berform test then call addzero function

def drawpath(path):
    grid = d.grid.tolist()
    z = np.ones(gridsize).astype(int)

    import matplotlib
    import matplotlib.pyplot as plt
    from matplotlib.colors import BoundaryNorm
    from matplotlib.ticker import MaxNLocator
    t = 0
    for cell in path.path2start:
        grid[cell[0]][cell[1]] = '-'
        z[gridlength- 1- cell[0]][cell[1]] = t
        # t+=1
 
 
    x = np.arange(-.5, gridlength+.5, 1)  # len = 11
    y = np.arange(-.5, gridwidth+.5, 1)  # len = 7
    cmap = plt.get_cmap('Spectral')  #
    plt.axis('off')
    # pdb.set_trace()

    plt.style.use('dark_background')
    z.reshape(gridwidth,gridlength)
    plt.pcolormesh(y, x, z, cmap=cmap, edgecolor='black',snap= True)

    # pdb.set_trace()

    for row in range(0, gridlength):
        for cell in range(0, gridwidth):
            # if row != 0 or cell !=0 :
            #     if row != gridlength -1 or cell != gridwidth -1:

            plt.text(cell, row, d.grid[gridlength - row-1][cell], color='white', ha='center', va='center', fontsize=10)
    # pdb.set_trace()

    # plt.text(gridlength-1, 0, 'End', color='white',
    #          ha='center', va='center',alpha = .5, fontsize=8)
    # plt.text(0, gridwidth-1, 'Start', color='white',
    #          ha='center', va='center',alpha = .5, fontsize=8)

    # pg('\n'.join(['  '.join([str(cell) for cell in row]) for row in grid]))
    # print('')
    # print('\n'.join(['  '.join([str(cell) for cell in row]) for row in d.grid]))







    plt.show()


    



#################################################################################################
#############################                                     ###############################
#############################   Starting the search from a[0,0]   ###############################
#############################                                     ###############################
#################################################################################################

seedingpath.append(pth.path((0, 0), 0, 0, pth.start(0, 0)))
d.reachedpointgrid[0, 0] = 0
loopforthezeros(seedingpath[0])

py(f'Before looping seedignpath : {seedingpath}')

seedingpath = seedingpath + to_be_added2seedingpath

py(f'After seedignpath : {seedingpath}')

Tick = 0



def start():
    
    global notreachedend
    global Tick
    while(notreachedend):
        global to_be_added2seedingpath
        to_be_added2seedingpath = []
        global seedingpath

        pr(d.grid)
        pb(d.reachedpointgrid)
        pr(f'Global Time: {Tick}')
        py(f'After seedignpath : {seedingpath}')
        py(f'Number of seedignpath : {len(seedingpath)}')
        # pg(seedingpath)
        if len(seedingpath) == 0:
            notreachedend = False
        templist4iteration = seedingpath.copy()
        for path in templist4iteration:
            # py(path.tick)
            if path.tick == 0:
                # pg(seedingpath)
                # pdb.set_trace()
                createpath(path)
                loopforthezeros(path)  
                # pdb.set_trace()#

                path.status="DONE Seeding"
                DONEseedingpath.append(path)
                seedingpath.remove(path)
                
                # pdb.set_trace()#
                # pm(f'Before adding adj adj:{path.path2startadjacent}')
                path.addadjacentcellasNOGO(gridsize) # a method to add the neighboring cells in the path to avoid looking for a path that is not neccesory
                # pm(f'After adding adj adj:{path.path2startadjacent}')
            else:
                path.tick-=1
                Tick += 1
            if notreachedend == False:
                break
        seedingpath = seedingpath + to_be_added2seedingpath
        
    # pg(DONEseedingpath)
        





start()















