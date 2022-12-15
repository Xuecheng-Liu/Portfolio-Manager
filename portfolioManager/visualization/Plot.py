'''
This is the visualization module for plotting sector forecasting bar graph.
'''
import sys
import matplotlib.pyplot as plt


def plot(data, path = None):
    '''
    Given the dataframe that contains sectors forecasting infomation, generate
    bar graphs to visualizate forecasting.
    Parameters:
        data: the sector forecasting dataframe
        path: optional parameter for giving the save path during testing.
    Return:
        generate bar graph that red and green indicate loss and gain.
    '''
    plt.clf()
    x = data.columns.values.tolist()
    y = data.values.reshape(5, ).tolist()
    sector = data.index.values[0]
    color = ['g' if x > 0 else 'r' for x in y]
    plt.bar(x, y, color=color)
    for a, b in zip(x, y):
        plt.text(a, b, '%.3f' % b, ha='center', va='bottom')

    plt.ylim(-3, 3)
    plt.ylabel('Return %')
    plt.title(sector)

    if path == None:
        path = sys.path[0]+"/static"
        plt.savefig(f'{path}/{sector}.jpg')
    else:
        plt.savefig(path + '/sector_test.jpg')

