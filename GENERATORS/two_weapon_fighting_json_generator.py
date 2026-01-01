import json

# damage with 1 weapon = average hr vs DC + weapon dmg base dmg
# damage with two weapon fighting = odds of hitting DC * weapon dmg base dmg * 2
# axes are:
# DC
# Odds of hitting DC -> Dice pair used
# weapon damage

DICE_SIZES = ['6', '8', '10', '12']

def generate_two_weapon_fighting_damage(dice_sizes, cumulative_probability, avg_hr):
    weapon_damage = [i for i in range(25)]
    avg_weapon_dmg = {}

    for d1index in range(len(dice_sizes)):
        d1size = dice_sizes[d1index]
        avg_weapon_dmg[d1size] = {}
        for d2index in range(d1index, len(dice_sizes)):
            d2size = dice_sizes[d2index]
            avg_weapon_dmg[d1size][d2size] = [0 for i in range(len(avg_hr[d1size][d2size]))]
            for dc in range(len(avg_hr[d1size][d2size])):
                avg_weapon_dmg[d1size][d2size][dc] = {}
                for damage_bonus in weapon_damage:
                    avg_weapon_dmg[d1size][d2size][dc][damage_bonus] = {}
                    avg_weapon_dmg[d1size][d2size][dc][damage_bonus]['1 attack'] = \
                        avg_hr[d1size][d2size][dc] + damage_bonus
                    avg_weapon_dmg[d1size][d2size][dc][damage_bonus]['2 attack'] = \
                        cumulative_probability[d1size][d2size][dc] * damage_bonus * 2

    with open('../JSON/FabUlt_2_weapon_fighting.json', 'w') as file:
        json.dump(avg_weapon_dmg, file, indent=4)


if __name__ == '__main__':
    with open('../JSON/FabUlt_dice_cumulative.json', 'r') as file:
        cumulative_probability = json.load(file)

    with open('../JSON/FabUlt_dice_avg_hr_by_dc.json', 'r') as file:
        avg_hr = json.load(file)

    generate_two_weapon_fighting_damage(DICE_SIZES, cumulative_probability, avg_hr)

