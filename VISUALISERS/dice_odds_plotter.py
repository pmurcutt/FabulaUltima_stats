import json
import matplotlib.pyplot as plt
import numpy as np


def plot_dice_combos_by_odds_v_dc():
    with open('../JSON/FabUlt_dice_cumulative.json', 'r') as file:
        cumulative_probability = json.load(file)

    # TODO: lift this from JSON...
    dice_sizes = ['6', '8', '10', '12']

    num_colours = round(0.5 * (len(dice_sizes) ** 2 + len(dice_sizes))) + 1
    cmap = plt.get_cmap('hsv')
    colours = [cmap(i) for i in np.linspace(0, 1, num_colours)]

    colour = 0
    for d1index in range(len(dice_sizes)):
        d1size = dice_sizes[d1index]
        for d2index in range(d1index, len(dice_sizes)):
            d2size = dice_sizes[d2index]
            plt.plot(np.array(cumulative_probability[d1size][d2size]), color=colours[colour], label=f'D{d1size} x D{d2size}')
            colour += 1
            print(f'D{d1size} x D{d2size}:', cumulative_probability[d1size][d2size])


    plt.legend(loc="upper right")
    plt.grid()

    plt.xticks(np.arange(0, 25, 5))
    plt.xticks(np.arange(0, 25, 1), minor=True)
    plt.yticks(np.arange(0, 1, 0.1))
    plt.grid(which='major', alpha=0.8)
    plt.grid(which='minor', alpha=0.2)
    plt.xlim([0, 24])
    plt.ylim([0, 1])
    plt.title("Target vs Chance to pass")
    plt.xlabel("Target")
    plt.ylabel("Chance")

    plt.savefig('../IMG/dice_odds.png')
    plt.show()

if __name__ == '__main__':
    plot_dice_combos_by_odds_v_dc()