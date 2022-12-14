import matplotlib.pyplot as plt


def plot(data):
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
    plt.savefig(f'./static/{sector}.jpg')
