from copy import deepcopy
import json

# effects
DM_BUFF = {1}
IW_BUFF = {2}
STAT_BUFFS = DM_BUFF.union(IW_BUFF)
ELEM_ATTACK = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20}
ELEM_RES_BUFF = {9, 10, 11}
INFLICT_STATUS = {12, 13, 14}
SPECIFIC_STATUS = {12, 13}
STATUS_RECOVERY = {15}
MP_HEAL = {16, 17, 19, 20}
BIG_HP_HEAL = {16, 17, 18, 20}
HP_HEAL = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20}

# targets
ALLY = {1, 2, 3, 4, 5, 6}
ENEMY = {7, 8, 9, 10, 11}
ALL_ALLY = {12, 13, 14, 15, 16}
ALL_ENEMY = {17, 18, 19, 20}
ANY_ALLY = ALLY.union(ALL_ALLY)
ANY_ENEMY = ENEMY.union(ALL_ENEMY)

FRIENDLY_EFFECT_KEYS = ['warrior_buff', 'mage_buff', 'stat_buff',
                        'elem_resist',
                        'status_heal', 'hp', 'mp', 'big_hp']

ENEMY_EFFECT_KEYS = ['elem_attack', 'any_status', 'specific_status']

ALLY_KEYS = ['any_ally', 'all_allies']
ENEMY_KEYS = ['any_enemy', 'all_enemies']

BENEFICIAL_EFFECT_D20_VALS = {}
BENEFICIAL_EFFECT_D20_VALS['warrior_buff'] = DM_BUFF
BENEFICIAL_EFFECT_D20_VALS['mage_buff']    = IW_BUFF
BENEFICIAL_EFFECT_D20_VALS['stat_buff']    = STAT_BUFFS
BENEFICIAL_EFFECT_D20_VALS['elem_resist']  = ELEM_RES_BUFF
BENEFICIAL_EFFECT_D20_VALS['status_heal']  = STATUS_RECOVERY
BENEFICIAL_EFFECT_D20_VALS['hp']           = HP_HEAL
BENEFICIAL_EFFECT_D20_VALS['big_hp']       = BIG_HP_HEAL
BENEFICIAL_EFFECT_D20_VALS['mp']           = MP_HEAL

ALLY_D20_ROLLS = {}
ALLY_D20_ROLLS['any_ally'] = ANY_ALLY
ALLY_D20_ROLLS['all_allies'] = ALL_ALLY

ATTACK_D20_VALS = {}
ATTACK_D20_VALS['elem_attack'] = ELEM_ATTACK
ATTACK_D20_VALS['any_status'] = INFLICT_STATUS
ATTACK_D20_VALS['specific_status'] = SPECIFIC_STATUS

ENEMY_D20_ROLLS = {}
ENEMY_D20_ROLLS['any_enemy'] = ANY_ENEMY
ENEMY_D20_ROLLS['all_enemies'] = ALL_ENEMY


def has_exclusive_value_in_both(test, set1, set2):
    test_set = deepcopy(test)
    intersection = list(test_set & set1)
    if len(intersection) > 0:
        if len(intersection) == 1:
            test_set.remove(intersection[0])
        if test_set & set2:
            return True
    return False

def initialise_outcomes(outcomes):
    for value in outcomes.values():
        for effect in BENEFICIAL_EFFECT_D20_VALS:
            for group in ALLY_D20_ROLLS:
                value[effect + '_' + group] = 0

        for effect in ATTACK_D20_VALS:
            for group in ENEMY_D20_ROLLS:
                value[effect + '_' + group] = 0


def update_positive_outcomes(rolls, outcomes):
    for effect in BENEFICIAL_EFFECT_D20_VALS:
        for group in ALLY_D20_ROLLS:
            if has_exclusive_value_in_both(rolls, BENEFICIAL_EFFECT_D20_VALS[effect], ALLY_D20_ROLLS[group]):
                outcomes[effect + '_' + group] += 1

def update_negative_outcomes(rolls, outcomes):
    for effect in ATTACK_D20_VALS:
        for group in ENEMY_D20_ROLLS:
            if has_exclusive_value_in_both(rolls, ATTACK_D20_VALS[effect], ENEMY_D20_ROLLS[group]):
                outcomes[effect + '_' + group] += 1

def outcomes_count_to_probability(outcomes, combinations):
    for effect in BENEFICIAL_EFFECT_D20_VALS:
        for group in ALLY_D20_ROLLS:
            outcomes[effect + '_' + group] /= combinations

    for effect in ATTACK_D20_VALS:
        for group in ENEMY_D20_ROLLS:
            outcomes[effect + '_' + group] /= combinations


if __name__ == '__main__':

    outcomes = {2: {}, 3: {}, 4: {}}
    initialise_outcomes(outcomes)

    combinations = 0
    for i in range(1, 21):
        for j in range(1, 21):
            rolls = {i, j}

            update_positive_outcomes(rolls, outcomes[2])
            update_negative_outcomes(rolls, outcomes[2])

            combinations += 1
    outcomes_count_to_probability(outcomes[2], combinations)

    combinations = 0
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                rolls = {i, j, k}
                update_positive_outcomes(rolls, outcomes[3])
                update_negative_outcomes(rolls, outcomes[3])
                combinations += 1
    outcomes_count_to_probability(outcomes[3], combinations)

    combinations = 0
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                for l in range(1, 21):
                    rolls = {i, j, k, l}
                    update_positive_outcomes(rolls, outcomes[4])
                    update_negative_outcomes(rolls, outcomes[4])
                    combinations += 1
    outcomes_count_to_probability(outcomes[4], combinations)

    with open('../JSON/alchemist_odds.json', 'w') as file:
        json.dump(outcomes, file, indent=4)

    print(outcomes)