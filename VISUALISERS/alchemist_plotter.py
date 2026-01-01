import json
import matplotlib.pyplot as plt
import numpy as np

def plot_alchemist_odds(alchemist_odds):

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    axis_count = 0
    for num_d20, data in alchemist_odds.items():
        keys = [key.replace('_', ' ') for key in data]
        vals = [key for key in data.values()]

        num_cols = len(keys) + 1
        cmap = plt.get_cmap('hsv')
        colours = [cmap(i) for i in np.linspace(0, 1, num_cols)]

        axes[axis_count].bar(keys, vals, color=colours)
        vals_short = [round(i, 2) for i in vals]
        axes[axis_count].bar_label(axes[axis_count].containers[0],
                                   labels=vals_short,
                                   label_type='edge',
                                   rotation=90,
                                   color='black',
                                   fontsize=6)
        axis_count += 1

    for ax, row in zip(axes, ['2 x D20', '3 x D20', '4 x D20']):
        ax.set_ylabel(row, size=16)

    plt.xticks(fontsize=6, rotation='vertical', )
    plt.subplots_adjust(left=0.1, right=0.98, bottom=0.27, top=0.95, wspace=0.1, hspace=0.5)
    plt.savefig('../IMG/alchemist.png')
    plt.show()


if __name__ == '__main__':
    with open('../JSON/alchemist_odds.json', 'r') as file:
        alchemist_odds = json.load(file)

    plot_alchemist_odds(alchemist_odds)