# Fabla Ultima dice probability calculator

This repo contains python tools to analyse and visualise the odds of the various dice rolls in the [Fabula Ultima](https://need.games/fabula-ultima/) JTTRPG

## Rolling a success

Checks in Fabula Ultima use a combination of two of you characters' attributes. These attributes are in turn represented by a dice ranging from a six-sided D6 to a twelve sided D12. The score is simply the sum of the numbers rolled on those dice. In addition to this, double ones are considered an automatic failure (a fumble) and any double over a 6 is considered an automatic success (a critical).

This plot shows the odds of achieving a certain target based on the dice used in the attempt:
![Likelihood vs Target](/IMG/dice_odds.png)

It can be seen that when it comes to rolling higher results, as long as the sum of the dice values are the same, then the odds are also roughly equivalent, i.e.: Rolling D8 + D8 is roughly equivalent to D6 + D10.

## High roll

Many checks also make use of the highest result on either of the dice rolled, most commonly for calculating damage done when attacking in combat. Notably as the difficulty of the roll increases, so too does the average high roll of a success, due to needing to first pass the success threshold.

Below is a plot of the average high roll when achieving a certain success threshold, for each combination of two dice:
![High roll vs Target](/IMG/dice_dmg.png)

This shows that although dice pairs with the same total are equivalent for ***success***, dice pairs with the highest value dice will perform better when it comes to their ***high roll***.

---

## Two weapon fighting

Fabula Ultima allows you to play fight with the same type of one-handed weapon in each hand. In this case a separate attack is made for each weapon, but the highroll for each is always condidered 0 (simply dealing the weapons' base damage on a hit).

The damage done by a conventional attack is:
**chance to hit** * (**high roll** + **base weapon damage**)

The damage done by Two weapon fighting is:
**chance to hit** * **base weapon damage** * **2**

There are now many factors:
- Chance to hit, which depends on:
  - Dice pair
- High roll, which depends on:
  - Dice pair
  - Success threshold
- Weapon base damage

This creates a more complex plot where each dice combination has been separated out and the difference between using a single weapon and adding the high roll or making multiple attacks with two of said weapon are better. The Y axis represents:

**single weapon average damage** - **two weapon fighting average damage**

i.e. positive numbers indicate how much more damage attacking twice with a weapon  does when compared to attacking with a single weapon

![Two weapon advantage](/IMG/two_weapon_fighting.png)

n.b. a limited number or weapon bonuses have been plotted, covering only those listed in the basic equipment list.

As you can see from the plots, Two weapon fighting is seldom worth it in Fabula Ultima, as the Two weapon fighting advantage is only positive for incredibly low difficulties. You are better served by equipping a higher damage two-handed weapon or gaining the defence boost from a shield.

---

## Alchemist

The Tinkerer class offers the *Gadgets* skill. One of the options within this skill is to specialise in Alchemy. This is represented by two tables that detail:
1) The **target** of your potion
2) The **effect** of your potion

When making a potion, you roll a number of D20s based on your Alchemy skill and how many Inventory points you are willing to spend (2, 3 or 4 D20s). You then assign one of the D20s to each table to create the potion, then apply those effects. You always have the option to apply a healing effect or some poison damage.

The chart below shows the odds of achieving the various outcomes based on the number of D20s rolled (2, 3 or 4):

PLOT GOES HERE
