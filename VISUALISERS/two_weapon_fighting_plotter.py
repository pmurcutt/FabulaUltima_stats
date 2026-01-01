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

fig, axes = plt.subplots(4, 4)

for d1index in range(len(dice_sizes)):
    d1size = dice_sizes[d1index]
    for d2index in range(d1index, len(dice_sizes)):
        d2size = dice_sizes[d2index]
        colour = 0
        one_v_two_weap_diff_by_dmg_bonus = {}
        for damage_bonus in weapon_damage:
            one_v_two_weap_diff_by_dmg_bonus[damage_bonus] = []
        for dc in range(len(two_weapon_dmg[d1size][d2size])):
            for damage_bonus in weapon_damage:
                one_atk = two_weapon_dmg[d1size][d2size][dc][damage_bonus]['1 attack']
                two_atk = two_weapon_dmg[d1size][d2size][dc][damage_bonus]['2 attack']
                one_v_two_weap_diff_by_dmg_bonus[damage_bonus].append(one_atk - two_atk)

        for damage_bonus in weapon_damage:
            if damage_bonus in ['4', '6', '8', '10']:
                axes[3-d1index][d2index].plot(np.array(one_v_two_weap_diff_by_dmg_bonus[damage_bonus]),color=colours[colour], label=f'+{damage_bonus}' )
                colour += 1
        axes[3-d1index][d2index].grid()

#plt.legend(loc="lower right")
# plt.grid()

#plt.savefig('dice_odds.png')
plt.show()