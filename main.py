import numpy as np
from matplotlib import pyplot as plt

x = []
y = []

numInCircle = 0
numTotal = 1000
frame = 1


fig, ax = plt.subplots()
box = dict(boxstyle='round', facecolor='#f0f9e8', alpha=0.5)


# 1000 Random Plot Points.
# THIS WORKS
def set_randoms():
    i = 0
    while i < numTotal:
        x.append(np.random.uniform(0, 1))
        y.append(np.random.uniform(0, 1))
        i += 1
    # Initializes the two lists of random numbers


def init_scatter():
    circle = plt.Circle((.5, .5), .5, alpha=0.3, facecolor='#7bccc4', edgecolor='#43a2ca')
    ax.set_aspect(1)
    ax.add_artist(circle)
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    # Creates circle, sets figure aspect ratio to 1:1, adds circle drawing, limits axes from 0-1


def calc_in_circle(i):
    global numInCircle
    if 1 / 4 > np.square(x[i - 1] - 1 / 2) + np.square(y[i - 1] - 1 / 2):
        numInCircle += 1
    # increments numInCircle  if the point lies inside the circle


def plot_point(i):
    ax.scatter(x[0:i], y[0:i], color='#0868ac')

    calc_in_circle(i)
    picalc = (numInCircle/i) * 4
    text = '\n'.join((
        r'$\pi = {}$'.format(picalc),
        r'no. of points = {}'.format(int(np.round(i)))))
    for txt in ax.texts:
        txt.set_visible(False)
    ax.text(0.05, 1.2, text, transform=ax.transAxes, fontsize=12, verticalalignment='top', bbox=box)

    plt.show()
    fig.savefig('./pics/{}.png'.format(i), bbox_inches='tight')





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    set_randoms()
    init_scatter()

    while frame <= numTotal:
        plot_point(frame)
        frame += 1
    print("done")
    print(numInCircle)
    print(numTotal)

