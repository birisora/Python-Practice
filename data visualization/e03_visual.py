import matplotlib.pyplot as plt 

from e03_randomWalk import RandomWalk

# make a random walk and plot points as long program active
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # set size of plotting window
    # figure() controls w, h, resolution, and background color of plot
    # figsize takes tuple that tells matplotlib dimensions of plotting window
    # in inches.
    plt.figure(dpi=128, figsize=(10,6))

    # use range to generate nums = to num of points in walk
    point_numbers = list(range(rw.num_points))
    # feed random walk's x and y val to scatter
    # pass point_numbers to c arg, use blue colormap and use edgecolor=none
    # to remove black outline
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
        edgecolor='none', s=1)
    # color the starting point green and in larger size
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    # color ending point red and in larger size
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100)

    # removing the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.savefig('e03_randomWalk.png', bbox_inches='tight')
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break


