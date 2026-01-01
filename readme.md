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

TODO

---

## Alchemist

TODO

