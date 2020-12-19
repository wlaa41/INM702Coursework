import packages.grid as grid
import packages.node as node
import packages.drawpath as drw
import packages.antpath as pth
import numpy as np

import pdb

import sys
sys.path.insert(1, 'D:\AAlearnAA\Study\python')
from rutaul.prnt import pg, pm, pr, py, pb



def addup(path: pth, x, y):
    # check rules FOR UP
    # if the agent in the extreme left then NO UP
    if path.currentlocation[1] < gridwidth - 2:
        # if the cell has been visited by the path or in the adjusant locationf
                # pr("add UP")
                tobeaddedThencheckiftheagentarrive(path, x, y)


def adddown(path: pth, x, y):
    # check rules FOR DOWN
    # if the cell has been visited by the path or in the adjusant locationf
            # pr("add DOWN")
            tobeaddedThencheckiftheagentarrive(path, x, y)


def addright(path: pth, x, y):
    # check rules
    # if the cell has been visited by the path or in the adjusant locationf
            # pr("add RIGHT")
            tobeaddedThencheckiftheagentarrive(path, x, y)


def addleft(path: pth, x, y):
    # check rules
    if path.currentlocation[0] < gridlength - 2:
        # if the cell has been visited by the path or in the adjusant locationf
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
    if (x, y) not in path.path2start:
        if (x, y) not in path.path2startadjacent:
            d.reachedpointgrid[x, y] = path.weight + d.grid[x, y]
            temp = pth.path((x, y), d.grid[x, y], gridsize, incomingcell=path)
            # pdb.set_trace()
            if d.grid[temp.currentlocation[0]][temp.currentlocation[1]] == 0:
                zeronodes.append(temp)
                loopforthezeros(
                    zeronodes[len(zeronodes)-1])
            else:
                seedingpath.append(temp)






# ------------- Global var for all functions to mainpulate
notreachedend = True
# ---------------------------------------------


def createNONzeropath(path: pth):
    x, y = path.currentlocation
    if x - 1 >= 0 :  # -- CHECK THE GRID DIMENESION
        # pg('CALLING ADD UP')
        if path.currentlocation[1] < gridwidth - 2:
            addNoN0(path, x-1, y)
    if x + 1 < gridlength:  # -- CHECK THE GRID DIMENESION
        # pg('CALLING ADD DOWN')
        addNoN0(path, x+1, y)

    if y + 1 < gridwidth:  # -- CHECK THE GRID DIMENESION
        # pg('CALLING ADD RIGHT')
        addNoN0(path, x, y+1)

    if y - 1 >= 0:  # -- CHECK THE GRID DIMENESION
        # pg('CALLING ADD LEFT')
        if path.currentlocation[0] < gridlength - 2:
            addNoN0(path, x, y-1)


def addNoN0(path: pth, x, y):
    if (x, y) not in path.path2start:
        if (x, y) not in path.path2startadjacent:
            if d.grid[x][y] != 0:
                if (x, y) not in listofoption:

                    listofoption.append((x,y))
                    d.reachedpointgrid[x, y] = path.weight + d.grid[x, y]





def choose_move(path,list0 ,options):
    p_option = np.array([]) # The probibilty of each option 
    for x,y in options:
        p = (((beta_plus/d.grid[x][y]) ** beta) + (tau[x][y] ** alpha))
        # py(f'{d.grid[x][y]} at {x},{y} -> {p}')
        p_option = np.append(p_option,  p   )

    probablity = p_option/sum(p_option)
    # pr(probablity)
    probablity = np.cumsum( probablity)
    # pr(probablity)
    import random
    random.uniform(0, 1)
    choices = np.array([]).astype(int)
    for i in range(0,path.antscount):
        ran = random.uniform(0, 1)
        choices = np.append(choices, np.where(probablity > ran)[0][0])
    # calculating the probeblity of each path
    # pg(choices)
    templst = []
    
    for i in range(0, len(probablity)):
        x, y = options[i]
        ants = len(np.where(choices == i)[0])
        temp = pth.path(options[i], d.grid[x][y], gridsize, path, ants)
        # pr(f'path: {temp.currentlocation}  got             {ants} ants ')
        temp.path2start = temp.path2start + list0 + options 
        if(temp.antscount>0):
            if (x, y) == (gridlength-1, gridwidth-1):
                reachedpath.append(
                    pth.path((x, y), d.grid[x][y], gridsize, path, antscount=ants))
                # pb(f'{path.antscount} ant has reached')
            else:
                seedingpath.append(temp)
    
    
def loopforthezeros(path):
    x, y = path.currentlocation

    # pdb.set_trace()#
    if x + 1 < gridlength:
        if d.grid[x+1, y] == 0:
            # py('ADD Zero DOWN')
            addzeroPATH(path, x+1, y, 'down')

    if y + 1 < gridwidth:
        if d.grid[x, y+1] == 0:
            # pdb.set_trace()#
            # py('ADD Zero RIGHT')
            addzeroPATH(path, x, y+1, 'right')

    if x - 1 >= 0:
        if d.grid[x-1, y] == 0:
            # py('ADD Zero UP')
            addzeroPATH(path, x-1, y, 'up')

    if y - 1 >= 0:
        if d.grid[x, y-1] == 0:
            # py('ADD Zero LEFT')
            addzeroPATH(path, x, y-1, 'left')
    # # pdb.set_trace()#

def addzeroPATH(path: pth, x, y, info):
    # check rules
    # if the cell has been visited by the path or in the adjusant locationf

    if (x, y) not in path.path2start:
        # pr(f'add ZERO {info}')
        tobeaddedThencheckiftheagentarrive(path, x, y)


def updatephromones(reachedpath):
    global tau
    # tau = tau + Q / pathweight  Q is a constant 
    for path in reachedpath:
        pointer = path
        weight = path.weight
        # pg(tau)

        while(pointer.currentlocation != (0,0)):
            x,y = pointer.currentlocation

            tau[x][y] = tau[x][y] + (Q/weight)

            # pb(f'x = { x}  y = {y} newV { tau[x][y]}  =  old {tau[x][y]  }  plus   {(Q/weight)}')


            pointer = pointer.incomingcell
        # import pdb; pdb.set_trace()


    # Evaboration ..................................
    tau = tau * Evaporate


def resetparameter():
    
    seedingpath.clear()
    terminatedpath.clear()
    reachedpath.clear()
    zeronodes.clear()
    listof0nodelocation.clear()
    listofoption.clear()


def start(repeatation = 5):
    global seedingpath

    for i in range(0,repeatation):
        print(tau)
        resetparameter()



        tem = pth.path((0, 0), 0,gridsize, incomingcell=pth.start(
            0, 0,incomingcell=pth.start(0,0)),  antscount=colonyantcount)
        seedingpath.append(tem)
        

        
        while(len(seedingpath) !=0):
            global listofoption
            # pb(f'@@@@@@starting  while loop the nodes seedingpath: {seedingpath}')
            global zeronodes

            templist4iteration = seedingpath.copy()
            seedingpath = []

            for path in templist4iteration:
                # print(f'.......................  strtiin for loop path: {path}')
                listof0nodelocation = []
                listofoption = []
                # print(f'before...................  optoins: {listofoption}')

                zeronodes.append(path)
                d.reachedpointgrid[0, 0] = 0
                loopforthezeros(path)

                for zero in zeronodes:
                    
                    listof0nodelocation.append(zero.currentlocation)
                    createNONzeropath(zero)
                zeronodes = []
                # print(f'after ..................  optoins: {listofoption}')
                # print(f'after ..................    zeros: {listof0nodelocation}')

                # pdb.set_trace()
                if (gridlength-1, gridwidth-1) in listof0nodelocation:
                    # pb(f'{path.antscount} ant has reached through zeros')
                    reachedpath.append(
                        pth.path((gridlength-1, gridwidth-1), d.grid[gridlength-1][gridwidth-1], gridsize, incomingcell=path, antscount=path.antscount))
                    
                else:
                    if len(listofoption) == 0:
                        # pr(f'{path.antscount} ant has been terminated')
                        terminatedpath.append(path)
                    else:
                        choose_move(path, listof0nodelocation, listofoption)
                
                # pm('.............................................c')

                # pdb.set_trace() 



        
        # import pdb; pdb.set_trace()
        pg('...........................................................')
        pb(gridsize)
        drw.drawgraph(reachedpath,gridsize,i)

        updatephromones(reachedpath)


# ------------------- Creating the random grid
gridsize = (10, 15)

d = grid.gridgen(gridsize)  # Creating the grid ................

# d.grid = d.fillgridMOREZeros(morezeroby=8)
# gridsize = d.fillava()
# gridsize = d.fillnaughty()

pb(d.grid)
gridlength, gridwidth = gridsize
colonyantcount = 15
tau = 4 * np.ones(gridsize)  # we intiate phormone at the mean almost 0-9

# tau =np.asarray( [   [9., 9., 9.]
#                     ,[1., 1., 9.]
#                     ,[1., 1., 9.]
#                     ,[1., 1., 9.]])


d.reachedpointgrid = 999 * np.ones(gridsize).astype(int)
alpha = 1
beta = .5
beta_plus = 1
Q = (gridlength + gridwidth )
Evaporate = .9
# ---------------------------------------------

# ------------- Creating lists to hold data

seedingpath = []
terminatedpath = []
reachedpath = []
zeronodes = []
listof0nodelocation = []
listofoption = []

# ---------------------------------------------
pb(gridsize)
pr('..............................................................cc')
start(2)
# pointer = reachedpath[0]
import pdb; pdb.set_trace()

drw.drawgraph(terminatedpath,gridsize)

pointer = reachedpath[0]
drw.drawgraph([pointer],gridsize)
