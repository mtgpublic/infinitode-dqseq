<p align="left">
      <a href="https://mtgpublic.github.io/infinitode-dqseq/">Return to the main page</a>
</p>

<h1 align="center" style="font-weight: bold;">infinitode-dqseq 💻</h1>
<p align="center" style="font-weight: bold;">A Library/Database of Infinitode Top Dailyquest Bonus Sequence</p>

# Raw Data Specification

Refers to the specification for describing raw data.

## Sequence

**Applies to the first column of data.**

Use Arabic numerals to describe the sequence, with a space between every five selections. Dense Marker first created this description method, which was then used for community communication sequences.

Encode using a selection record method, describing selection serial numbers from left to right, with the final record index determined by the number of selectable items and whether a reset occurs, with the index starting from 1.

In the current version of Infinitode, without selecting MoreBonusVariantsNextTime, the first item from left to right is 1, the second is 2, the third is 3. In the case of a reroll, the first item is 4, the second is 5, the third is 6.

When selecting MoreBonusVariantsNextTime, the first item from left to right is 1, the second is 2, the third is 3, the fourth is 4. In the case of a reroll, the first item is 5, the second is 6, the third is 7, the fourth is 8.

Example:

```
33513 23432
```

In the provided sequence, assuming there is no MoreBonusVariantsNextTime, the selections are:

- First Group (3, 3, 5, 1, 3):
  - The first two selections are 3 (third bonus).
  - The third selection is 5 (first bonus after a reroll).
  - The fourth selection is 1 (first bonus).
  - The fifth selection is 3 (third bonus).
- Second Group (2, 3, 4, 3, 2):
  - The sixth selection is 2 (second bonus).
  - The seventh selection is 3 (third bonus).
  - The eighth selection is 4 (first bonus after a reroll).
  - The ninth selection is 3 (third bonus).
  - The tenth selection is 2 (second bonus).

## Sequence Score

**Applies to the second column of data.**

Uses the sequence scoring model invented by player 249.

The score model assumes that every 100 score points double the damage output. In other words, the final damage multiplier x and the score y satisfy the relationship y = 100log2(x) . For example, a score of 230 corresponds to a damage multiplier of approximately 4.925.  

For a sequence of bonuses, the total score is the sum of all selected bonuses’ scores.

## Summary

**Applies to the third column of data.**

Follows the abbreviation specification.

The summary describes the general bonuses and cores of a given sequence.

Typically, it consists of cores information and main bonus information:

* Core information records the obtained core type. If a core is obtained on stage 1–5, it is noted as *ALPHA(Core)*; for stage 6–10, it is noted as *DELTA(Core)*.

* Main bonus information includes the bonus types and their levels, with levels represented using Arabic numerals.

**Example:**

```
ALPHADELTA3DMG4VULN2ASPD2LVL
```

This sequence indicates:

- Has ALPHA Core  
- Has DELTA Core  
- Has power 3 TowersDamage
- Has power 4 ExtraDamagePerBuff
- Has power 2 TowersAttackSpeed
- Has power 2 GV_TowersMaxExpLevel
- *May contain additional bonuses*

The summary is not a complete record. It does **not** include bonuses with low or zero scores, nor the stages of when the bonuses were acquired.

**Note:** Due to the nature of raw data generation, the summary of the same sequence may vary slightly depending on the generation environment. Typically, only bonuses scoring at or above **3% of the highest sequence score** will be included as main bonuses.

## Detailed Description

**Applies to the fourth column of data.**

Follows the abbreviation specification.

The detailed description outlines the bonuses obtained on each individual stage. All bonuses are recorded.

In the Daily Challenge, there are a total of ten stages, represented using hexadecimal notation from 1 to *a* (with *a* being lowercase) to indicate the stage number.

Notably, when obtaining the IncreaseSelectedBonusesPower (POWER+, sometimes referred to by the community as "All"), multiple bonuses are granted simultaneously.

**Example:**

```
1ALL_ABI24aLIT3DUST58aLVL6aVULN7RND_CORE9RND_PLTaPOWER+
```

This sequence indicates:

- AllAbilitiesForRandomTower obtained on stage 1  
- LightningStrikeOnTowerLevelUp on stages 2, 4, and 10  
- MinedItemsTurnIntoDust obtained on stage 3  
- GV_TowersMaxExpLevel obtained on stages 5, 8, and 10  
- ExtraDamagePerBuff obtained on stages 6 and 10  
- DELTA Core obtained on stage 7  
- AddRandomPlatform obtained on stage 9  
- IncreaseSelectedBonusesPower obtained on stage 10

## Tags

**Applies to the fifth column of data.**

**Deprecated.** This field is retained only for compatibility with legacy data and has now been replaced by the Detailed Description.

## Bounty Identifier

**Applies to the sixth column of data.**

**Appears only in DQ8.**

Bounty upgrades in the core of DQ8 will affect your Bonus. The data will indicate the previous stage of the bounty to assist you in upgrading the core at the right time.

This means you need to complete the previous stage's selection before choosing bounty, and dont't trigger the next stage's selection (fulfilling the enemy kill conditions for the next stage's selection). 