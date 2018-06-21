import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import itertools

def graph_BloxPot(graphTitle, data, randomDists, xLabel, yLabel):
    fig, ax1 = plt.subplots(figsize=(10, 6))
    fig.canvas.set_window_title(graphTitle)
    plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

    bp = plt.boxplot(data, notch=0, sym='+', vert=1, whis=1.5)
    plt.setp(bp['boxes'], color='black')
    plt.setp(bp['whiskers'], color='black')
    plt.setp(bp['fliers'], color='red', marker='+')

    # Add a horizontal grid to the plot, but make it very light in color
    # so we can use it for reading data values but not be distracting
    ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                   alpha=0.5)

    # Hide these grid behind plot objects
    ax1.set_axisbelow(True)
    #ax1.set_title('Comparison of IID Bootstrap Resampling Across Five Distributions')
    ax1.set_xlabel(xLabel)
    ax1.set_ylabel(yLabel)

    # Now fill the boxes with desired colors
    boxColors = ['royalblue'] #'darkkhaki', 
    #numBoxes = 5
    numBoxes = 4
    medians = list(range(numBoxes))
    for i in range(numBoxes):
        box = bp['boxes'][i]
        boxX = []
        boxY = []
        #for j in range(5):
        for j in range(4):
            boxX.append(box.get_xdata()[j])
            boxY.append(box.get_ydata()[j])
        boxCoords = list(zip(boxX, boxY))
        # Alternate between Dark Khaki and Royal Blue
        
        #k = i % 2
        #facecolor=boxColors[k]
        
        boxPolygon = Polygon(boxCoords, facecolor='royalblue')
        ax1.add_patch(boxPolygon)
        # Now draw the median lines back over what we just filled in
        med = bp['medians'][i]
        medianX = []
        medianY = []
        for j in range(2):
            medianX.append(med.get_xdata()[j])
            medianY.append(med.get_ydata()[j])
            plt.plot(medianX, medianY, 'k')
            medians[i] = medianY[0]
        # Finally, overplot the sample averages, with horizontal alignment
        # in the center of each box
        plt.plot([np.average(med.get_xdata())], [np.average(data[i])],
                 color='w', marker='*', markeredgecolor='k')

    # Set the axes ranges and axes labels
    #ax1.set_xlim(0.5, numBoxes + 0.5)
    ax1.set_xlim(0.4, numBoxes + 0.4)
    top = max(list(itertools.chain.from_iterable(data)))
    bottom = min(list(itertools.chain.from_iterable(data)))
    ax1.set_ylim(bottom, top)
    xtickNames = plt.setp(ax1, xticklabels=randomDists)
    plt.setp(xtickNames, rotation=45, fontsize=8)

    # Due to the Y-axis scale being different across samples, it can be
    # hard to compare differences in medians across the samples. Add upper
    # X-axis tick labels with the sample medians to aid in comparison
    # (just use two decimal places of precision)
    pos = np.arange(numBoxes) + 1
    upperLabels = [str(np.round(s, 2)) for s in medians]
    weights = ['bold', 'semibold']
    for tick, label in zip(range(numBoxes), ax1.get_xticklabels()):
        k = tick % 2
        ax1.text(pos[tick], top - (top*0.05), upperLabels[tick],
                 horizontalalignment='center', size='x-small', weight=weights[k],
                 color='royalblue')

    # Finally, add a basic legend
    #plt.figtext(0.80, 0.08, str(500) + ' Random Numbers',
    #            backgroundcolor=boxColors[0], color='black', weight='roman',
    #            size='x-small')
    #plt.figtext(0.80, 0.045, 'IID Bootstrap Resample',
                #backgroundcolor=boxColors[1],
                #color='white', weight='roman', size='x-small')
    #plt.figtext(0.80, 0.015, '*', color='white', backgroundcolor='silver',
    #            weight='roman', size='medium')
    #plt.figtext(0.815, 0.013, ' Average Value', color='black', weight='roman',
    #            size='x-small')

    plt.show()

if __name__ == '__main__':
    #Independent Variables
    randomDists = ['ACM','IEEE', 'Scidirect','Springer']
    xLabel = 'Search Engine'

    metamorphic_relations = ['MPTitle', 'MPublished', 'SwapJD', 'Top1Absent']

    if (len(sys.argv) == 1):
        print('Usage: python bloxplot.py relation (\'MPTitle\', \'MPublished\', \'SwapJD\', \'Top1Absent\')')
        sys.exit(-1)

    metamorphic_relation = str(sys.argv[1]) #Metamorphic Relation

    if (metamorphic_relation == 'MPTitle'):
        #MPTitle
        yLabel = '% Fail'

        ACM  = []
        IEEE  = []
        SciDirect = []
        Springer = []
        
    elif (metamorphic_relation == 'MPublished'):
        #MPublished
        yLabel = '% Fail'

        ACM  = []
        IEEE  = []
        SciDirect = []
        Springer = []

    elif (metamorphic_relation == 'SwapJD'):
        #SwapJD
        yLabel = 'Jaccard Similarity Coefficient'

        ACM  = [0.365, 0.398333333, 0.225, 0.341666667, 0.462592593, 0.336666667, 0.343333333, 0.186666667, 0.275, 0.266666667, 0.25, 0.231666667, 0.306666667, 0.34, 0.313333333, 0.303333333, 0.401666667, 0.406666667, 0.166666667, 0.326666667, 0.248333333, 0.261666667, 0.243333333, 0.23, 0.308333333, 0.208333333, 0.285, 0.241111111, 0.32, 0.346666667, 0.243333333, 0.330606061, 0.303333333]
        IEEE  = [0.309333333, 0.421333333, 0.518666667, 0.358666667, 0.328, 0.430666667, 0.393333333, 0.325333333, 0.442666667, 0.425333333, 0.505333333, 0.438666667, 0.484, 0.389333333, 0.432, 0.398666667, 0.505333333, 0.352, 0.54, 0.445333333, 0.444, 0.461333333, 0.424, 0.473333333, 0.705333333, 0.44, 0.389333333, 0.293333333, 0.302666667, 0.310666667, 0.328, 0.498666667, 0.312]
        SciDirect = [0.338666667, 0.306666667, 0.385333333, 0.269333333, 0.318761905, 0.221333333, 0.2, 0.322666667, 0.170666667, 0.372, 0.298111365, 0.348, 0.253333333, 0.361333333, 0.346666667, 0.342666667, 0.402666667, 0.344, 0.330666667, 0.538666667, 0.333333333, 0.264, 0.273333333, 0.410666667, 0.433333333, 0.225894737, 0.336, 0.206666667, 0.182666667, 0.385101449, 0.396592593, 0.365333333, 0.238333333]
        Springer = [0.969210526, 0.987602339, 1, 0.993333333, 0.874187995, 0.984444444, 0.962745098, 0.996666667, 0.961904762, 0.992592593, 0.971520468, 1, 0.921666667, 0.93, 0.996666667, 1, 0.989454191, 0.957777778, 0.966666667, 0.972962963, 0.952807018, 0.921666667, 1, 0.980392157, 0.994736842, 1, 0.93, 0.946410256, 0.982962963, 0.987037037, 0.936246782, 0.964814815, 0.98]

    elif (metamorphic_relation == 'Top1Absent'):
        #Top1Absent
        yLabel = '% Fail'

        ACM  = []
        IEEE  = []
        SciDirect = []
        Springer = []

    data = [ACM, IEEE, SciDirect, Springer]   
    graph_BloxPot(metamorphic_relation, data, randomDists, xLabel, yLabel)    