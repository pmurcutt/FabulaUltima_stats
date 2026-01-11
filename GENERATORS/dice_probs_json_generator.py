from copy import deepcopy
import json

DICE_SIZES = [6, 8, 10, 12]
DICE_SIZES_STR = ['6', '8', '10', '12']

def generate_FabUlt_dice_odds(dice_sizes):

    # Create each combination of die sizes
    results_probability = {}

    for d1index in range(len(dice_sizes)):
        d1size = dice_sizes[d1index]
        results_probability[d1size] = {}
        for d2index in range(d1index, len(dice_sizes)):
            d2size = dice_sizes[d2index]
            # create a 2d dict of dice sizes
            # containing a list of result values (0 = fumble, 25 = crit)
            results_probability[d1size][d2size] = \
                [0 for k in range(26)]

            increment = 1/(d1size * d2size)
            # iterate over all possible rolls, incrementing associated result
            for i in range(1, d1size+1):
                for j in range(1, d2size+1):
                    if i == j and i >= 6:
                        results_probability[d1size][d2size][25] += increment
                    elif i == 1 and j == 1:
                        results_probability[d1size][d2size][0] += increment
                    else:
                        results_probability[d1size][d2size][i + j] += increment

    with open('../JSON/FabUlt_dice.json', 'w') as file:
        json.dump(results_probability, file, indent=4)

    # Convert to cumulative
    cumulative_probability = deepcopy(results_probability)

    for d1index in range(len(dice_sizes)):
        d1size = dice_sizes[d1index]
        for d2index in range(d1index, len(dice_sizes)):
            d2size = dice_sizes[d2index]
            roll_sum = 0
            # 25 guarantees any value, so put it at the front so that
            # it accumulates first
            # 0 is always a fail so remove it from accumulator
            cumulative_probability[d1size][d2size][0] = cumulative_probability[d1size][d2size][25]
            cumulative_probability[d1size][d2size][25] = 0
            for i in range(len(results_probability[d1size][d2size])):
                cumulative_probability[d1size][d2size][i] = 1 - roll_sum
                roll_sum += results_probability[d1size][d2size][i]

    with open('../JSON/FabUlt_dice_cumulative.json', 'w') as file:
        json.dump(cumulative_probability, file, indent=4)

def generate_FabUlt_dice_hr(dice_sizes):

    hr_accumulator = {}
    hr_count = {}
    avg_hr_vs_dc = {}

    # Create each combination of die sizes
    for d1index in range(len(dice_sizes)):
        d1size = dice_sizes[d1index]
        hr_accumulator[d1size] = {}
        hr_count[d1size] = {}
        avg_hr_vs_dc[d1size] = {}
        for d2index in range(d1index, len(dice_sizes)):
            d2size = dice_sizes[d2index]
            # create a 2d dict of dice sizes
            # containing a list of result values (0 = fumble, 25 = crit)
            hr_accumulator[d1size][d2size] = [0 for k in range(26)]
            hr_count[d1size][d2size] = [0 for k in range(26)]
            avg_hr_vs_dc[d1size][d2size] = [0 for k in range(26)]

            for i in range(1, d1size + 1):
                for j in range(1, d2size + 1):
                    total = 0
                    hr = 0
                    if i == j and i >= 6:
                        hr = i
                        total = 25
                    elif i == 1 and j == 1:
                        continue
                    else:
                        hr = max(i, j)
                        total = i + j
                    for k in range(total + 1):
                        hr_accumulator[d1size][d2size][k] += hr
                        hr_count[d1size][d2size][k] += 1

    # Generate average HR
    for d1index in range(len(dice_sizes)):
        d1size = dice_sizes[d1index]
        for d2index in range(d1index, len(dice_sizes)):
            d2size = dice_sizes[d2index]
            for i in range(len(hr_accumulator[d1size][d2size])):
                if hr_count[d1size][d2size][i] > 0:
                    avg_hr_vs_dc[d1size][d2size][i] = hr_accumulator[d1size][d2size][i] / hr_count[d1size][d2size][i]

    with open('../JSON/FabUlt_dice_avg_hr_passing_dc.json', 'w') as file:
        json.dump(avg_hr_vs_dc, file, indent=4)

def generate_FabUlt_dice_avg_hr(dice_sizes_str, cumulative_avg_hr, cumulative_dice_odds):
    avg_dmg = {}

    # Create each combination of die sizes
    for d1index in range(len(dice_sizes_str)):
        d1size = dice_sizes_str[d1index]
        avg_dmg[d1size] = {}
        for d2index in range(d1index, len(dice_sizes_str)):
            d2size = dice_sizes_str[d2index]
            avg_dmg[d1size][d2size] = \
                [cumulative_avg_hr[d1size][d2size][i] * cumulative_dice_odds[d1size][d2size][i]
                 for i in range(26)]

    with open('../JSON/FabUlt_dice_avg_hr_by_dc.json', 'w') as file:
        json.dump(avg_dmg, file, indent=4)


if __name__ == '__main__':
    generate_FabUlt_dice_odds(DICE_SIZES)

    generate_FabUlt_dice_hr(DICE_SIZES)

    with open('../JSON/FabUlt_dice_avg_hr_passing_dc.json') as file:
        cumulative_avg_hr = json.load(file)
    with open('../JSON/FabUlt_dice_cumulative.json') as file:
        cumulative_dice_odds = json.load(file)
    generate_FabUlt_dice_avg_hr(DICE_SIZES_STR, cumulative_avg_hr, cumulative_dice_odds)
