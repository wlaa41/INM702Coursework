import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive
import math
import sys
sys.path.insert(1, 'D:\AAlearnAA\Study\python')
from rutaul.prnt import pg, pm, pr, py, pb



def drawgraph(seedingpath,gridsize,iteration = 1):
    # import pdb; pdb.set_trace()
    nodesDot = []
    labels = []
    gridlength, gridwidth = gridsize
    for x in range(0, gridlength):
        for y in range(0, gridwidth):
            nodesDot.append([x, y])

    nodesDot = np.asarray(nodesDot)
    plt.scatter(nodesDot[..., 1], nodesDot[..., 0])
    weights = []

    for path in seedingpath:
        tothestartnode = True
        pointer = path
        weights = weights + [path.weight]
        while(tothestartnode):
            if pointer.incomingcell.currentlocation == (0, 0):
                tothestartnode = False

            temp = np.asarray(
                [pointer.currentlocation, pointer.incomingcell.currentlocation])
            # print(temp[..., 1])
            # print(temp[..., 0])
            # plt.plot(temp[..., 1],  gridlength - 1 -
            #          temp[..., 0], 'g-', linewidth=5)
            lbl = ''
            if str(pointer.antscount) not in labels:
                lbl = str(pointer.antscount)
                labels = labels + [lbl]

            # pr(pointer.antscount)
            # pr( math.log(pointer.antscount))
            # pr((.1 * math.log(pointer.antscount)))
            plt.plot(temp[..., 1], gridlength - 1 - temp[..., 0],
                     'g', linewidth=5, alpha=.6,label=lbl)

            pointer = pointer.incomingcell
    # pr(labels)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    # pb(f'total path reached {len(weights)}  they are {weights}')
    # plt.figure(num=f'The   {iteration}   iteration')
    plt.title(f'The   {iteration}   iteration')
    plt.show()


if __name__ == "__main__":
    gridsize = (5, 5)
    import antpath as pth
    incom = pth.path((0, 0), 3,gridsize, pth.start((0, 0), 0))
    temp = pth.path((0, 1), 4, gridsize, incom, antscount=4)
    temp = pth.path((1, 1), 4, gridsize, temp, antscount=4)
    temp = pth.path((2, 1), 4, gridsize, temp, antscount=4)
    temp = pth.path((2, 2), 4, gridsize, temp, antscount=4)
    temp.path2start = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]

    drawgraph([temp], gridsize)

# interactive_plot = interactive(drawgraph, iter=columns)
# interactive_plot
