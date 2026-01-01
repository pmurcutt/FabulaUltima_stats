import json
import matplotlib.pyplot as plt
import numpy as np

with open('../JSON/FabUlt_2_weapon_fighting.json', 'r') as file:
    two_weapon_dmg = json.load(file)

# TODO: lift this from JSON...
dice_sizes = ['6', '8', '10', '12']
weapon_damage = [str(i) for i in range(25)]


#num_colours = len(two_weapon_dmg['6']['6'])
num_colours = 5
cmap = plt.get_cmap('hsv')
colours = [cmap(i) for i in np.linspace(0, 1, num_colours)]

fig, axes = plt.subplots(4, 4, sharex=True, sharey=True)

for d1index in range(len(dice_sizes)):
    d1size = dice_sizes[d1index]
    for d2index in range(len(dice_sizes)):
        if d2index < d1index:
            axes[d1index][d2index].spines['left'].set_color('white')
            axes[d1index][d2index].spines['right'].set_color('white')
            axes[d1index][d2index].spines['top'].set_color('white')
            axes[d1index][d2index].spines['bottom'].set_color('white')
            axes[d1index][d2index].tick_params(axis='y', colors='white', which='both')
            axes[d1index][d2index].tick_params(axis='x', colors='white', which='both')
        else:
            d2size = dice_sizes[d2index]
            colour = 0
            one_v_two_weap_diff_by_dmg_bonus = {}
            for damage_bonus in weapon_damage:
                one_v_two_weap_diff_by_dmg_bonus[damage_bonus] = []
            for dc in range(len(two_weapon_dmg[d1size][d2size])):
                for damage_bonus in weapon_damage:
                    one_atk = two_weapon_dmg[d1size][d2size][dc][damage_bonus]['1 attack']
                    two_atk = two_weapon_dmg[d1size][d2size][dc][damage_bonus]['2 attack']
                    # one_v_two_weap_diff_by_dmg_bonus[damage_bonus].append(one_atk)
                    # one_v_two_weap_diff_by_dmg_bonus[damage_bonus].append(two_atk)
                    one_v_two_weap_diff_by_dmg_bonus[damage_bonus].append(two_atk - one_atk)

            for damage_bonus in weapon_damage:
                if damage_bonus in ['4', '6', '8', '10']:
                    axes[d1index][d2index].plot(np.array(one_v_two_weap_diff_by_dmg_bonus[damage_bonus]),
                                                  color=colours[colour],
                                                  label=f'+{damage_bonus}')
                    colour += 1

            axes[d1index][d2index].set_xlim([0, 25])
            # axes[d1index][d2index].set_ylim([0, 20])
            axes[d1index][d2index].set_ylim([-10, 10])
            axes[d1index][d2index].set_xticks(np.arange(0, 26, 5))
            axes[d1index][d2index].set_xticks(np.arange(0, 26, 1), minor=True)
            # axes[d1index][d2index].set_yticks(np.arange(0, 20, 5))
            axes[d1index][d2index].set_yticks(np.arange(-10, 10, 5))
            axes[d1index][d2index].grid(which='major', alpha=0.8)
            axes[d1index][d2index].grid(which='minor', alpha=0.2)
            if d1index == 0 and d2index == 3:
                axes[d1index][d2index].legend(loc="upper right", fontsize=5)



fig.suptitle('Two weapon fighting advantage for each dice combo', fontsize='x-large')
for ax, col in zip(axes[0, :], ['D6', 'D8', 'D10', 'D12']):
    ax.set_title(col, size=16)
for ax, row in zip(axes[:, 0], ['D6', 'D8', 'D10', 'D12']):
    ax.set_ylabel(row, size=16)

plt.savefig('../IMG/two_weapon_fighting_2atak.png', dpi=500)
plt.show()