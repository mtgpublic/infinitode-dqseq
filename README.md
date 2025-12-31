<p align="right">
      <a href="https://mtgpublic.github.io/infinitode-dqseq/README.zh_CN">中文</a> | <strong>English</strong>
</p>

<h1 align="center" style="font-weight: bold;">infinitode-dqseq 💻</h1>
<p align="center" style="font-weight: bold;">A Library/Database of Infinitode Top Dailyquest Bonus Sequence</p>

## 📌 Description

Infinitode is a tower defense game developed by The Rainy Cat.

Daily quest is a gameplay feature within the game where players need to complete tasks in designated daily levels to earn rewards or achieve high scores to compete on leaderboards. In Daily quest, players can select Bonuses to enhance the strength of their defense towers. By choosing the appropriate path, the best Bonus sequence can be found.

**This repository stores a large number of Top Dailyquest Bonus Sequences to help players complete tasks more easily or consistently secure top positions on the daily quest leaderboard**.

## 📋︎ Announcement 2025-12-31

**This is a major update to welcome the arrival of 2026. Wishing everyone a smooth and successful new year**!

* Data content and specification updates

One highlight of this update is the addition of an English-formatted sequence, allowing more players in the international community to read the sequence content directly. In addition, the translation guidelines for Chinese sequences have been updated in line with Sequinverse.

Thanks to Infinitode Discord user Sela (ERKA) for contributing to this update.

In addition, this update adds Venom FS data for DQ3, making it easier for players who enjoy the Venom FS strategy to choose it. The designated code is `DQ3L`, where `L` is an abbreviation of the Chinese term for “chain reaction”.

* DQ8 score adjustment

For DQ8, the score for the second level of `GV_TowersMaxExpLevel` has been adjusted from +17% to +7%. This is a temporary change to prevent the score from being too high and affecting sequence searches.

Thanks to MTG user WeakCat for contributing to this update.

* Documentation updates

This update also revises the documentation format and some descriptions to make it easier for players to understand and read, helping them get started with the project more quickly.

One notable documentation update is the addition of historical corresponding DQ records, making it easier for players to find past sequences and replay them in developer mode.

[Announcement Archive](https://mtgpublic.github.io/infinitode-dqseq/guide/Announcement)

## 🚩 Quick Start

If you are already familiar with the project, please go directly to the `data` directory and search according to the language you use, the DQ level number, and the DQ date.  

For example, if I want to search for the English version of DQ8 on December 31, 2025, the file path would be `/data/en_US/DQ8/2025/12/DQ8_2025_12_31.txt`.

Project Link: [https://github.com/mtgpublic/infinitode-dqseq](https://github.com/mtgpublic/infinitode-dqseq)

## 🔗 Project Releases and Other Services  

This repository is only published on GitHub and the Infinitode Chinese Community.  

In the Infinitode Chinese Community, additional services such as Bot sequence query and email sequence delivery are provided.  

Infinitode2 Milk Tea Group(Infinitode Chinese Community) QQ number: 1020322961  

## 🚀 Understanding and Reading of Sequences

Using the sequence is very simple. Before that, however, make sure you have a good understanding of infinitode daily quests and are clear on the following points.

[Infinitode 2 Wiki - Bonus](https://infinitode-2.fandom.com/wiki/Bonuses) provides a brief introduction to the mechanics of Bonus in Infinitode Dailyquest. Here, the focus will primarily be on the description method of the data.

If you want to fully understand the sequence, you can read [Rawdata](https://mtgpublic.github.io/infinitode-dqseq/guide/Rawdata).

If you want to learn the commonly used community terms/descriptions for the sequence, you can read [Abbreviation](https://mtgpublic.github.io/infinitode-dqseq/guide/Abbreviation).

### Dense Marker Sequence Standard

Use Arabic numerals to describe the sequence, with a space between every five selections. Dense Marker first created this description method, which was then used for community communication sequences.

Encode using a selection record method, describing selection serial numbers from left to right, with the final record index determined by the number of selectable items and whether a reset occurs, with the index starting from 1.

In the current version of Infinitode, without selecting MoreBonusVariantsNextTime, the first item from left to right is 1, the second is 2, the third is 3. In the case of a reroll, the first item is 4, the second is 5, the third is 6.

When selecting MoreBonusVariantsNextTime, the first item from left to right is 1, the second is 2, the third is 3, the fourth is 4. In the case of a reroll, the first item is 5, the second is 6, the third is 7, the fourth is 8.

Example:
```
33513 23432
```

In the provided sequence, assuming there is no MoreBonusVariantsNextTime, there are 3 choices per stage and the selections are:
- First Group (3, 3, 5, 1, 3):
  - The first selection are 3 (third bonus).
  - The second selection are 3 (third bonus).
  - The third selection is 5 (second bonus after a reroll).
  - The fourth selection is 1 (first bonus).
  - The fifth selection is 3 (third bonus).
- Second Group (2, 3, 4, 3, 2):
  - The sixth selection is 2 (second bonus).
  - The seventh selection is 3 (third bonus).
  - The eighth selection is 4 (first bonus after a reroll).
  - The ninth selection is 3 (third bonus).
  - The tenth selection is 2 (second bonus).

Assuming you select MoreBonusVariantsNextTime on stage 2, after this stage there are 4 choices per stage and the selections are:
- First Group (3, 3, 5, 1, 3):
  - The first selection are 3 (third bonus). There are 3 choices in this stage.
  - The second selection are 3 (third bonus). There are 3 choices in this stage and you select MoreBonusVariantsNextTime.
  - The third selection is 5 (first bonus after a reroll). Now there are 4 choices in the rest stages.
  - The fourth selection is 1 (first bonus).
  - The fifth selection is 3 (third bonus).
- Second Group (2, 3, 4, 3, 2):
  - The sixth selection is 2 (second bonus).
  - The seventh selection is 3 (third bonus).
  - The eighth selection is 4 (fourth bonus).
  - The ninth selection is 3 (third bonus).
  - The tenth selection is 2 (second bonus).

### 249 Bonus Model

A score model for evaluating the merits of bonuses, invented by 249.

The score model assumes that every 100 score points double the damage output. In other words, the final damage multiplier x and the score y satisfy the relationship y = 100log2(x) . For example, a score of 230 corresponds to a damage multiplier of approximately 4.925.   

For a sequence of bonuses, the total score is the sum of all selected bonuses’ scores.

### DQ8 Bounty

Bounty upgrades in the core of DQ8 will affect your Bonus. The data will indicate the previous stage of the bounty to assist you in upgrading the core at the right time.

This implies:
- Must complete the previous stage's selection (including rerolls) before upgrading bounty
- Do NOT trigger the next stage's selection conditions (i.e., avoid meeting enemy kill requirements for subsequent stages)

Mechanically speaking, bounty affect all "already generated" sequences. This means if reward selection occurs after bounty upgrade (typically from meeting kill requirements or rerolls), those rewards will be bounty-affected.

## 🎮 Usage  

If you've gone through the "Quick Start" section, you'll find it easy to grasp how to use the sequences.  

All released data is stored in the `data` directory in txt format, where you can locate sequence data for all stages of the day by date.  

The sequences are already sorted, and generally, the earlier sequences are the stronger ones.  

### Pages

* [Abbreviation](https://mtgpublic.github.io/infinitode-dqseq/guide/Abbreviation)
* [Rawdata](https://mtgpublic.github.io/infinitode-dqseq/guide/Rawdata)
* [Compliance Troubleshooting](https://mtgpublic.github.io/infinitode-dqseq/guide/Compliance)
* [Announcement Archive](https://mtgpublic.github.io/infinitode-dqseq/guide/Announcement)
* [Dailyquest Date Reference Table](https://mtgpublic.github.io/infinitode-dqseq/guide/Dailyquestsheet)

## 📚️ Data Generation Specifications  

The data in this repository is generated using SeqUniverse-dqseq-20251231.  

## 📫 Contact

Email: mtgpublic@163.com

Project link: [https://github.com/mtgpublic/infinitode-dqseq](https://github.com/mtgpublic/infinitode-dqseq)

## 🤝 Contirbution

- [249x](https://github.com/249x)

## 📜 Lisense

Milk Tea Group Infinitode Modding Open Source License

This project is licensed under a modified version of the Apache License 2.0, with the following additional conditions:

Usage for Infinitode Modding & Game Support
You may use this project for modding the official Infinitode game or providing related technical support, provided that:
1. Competitive Online Play: If used in competitive online play of Infinitode, you must explicitly disclose that this project was utilized for such purposes.
2. No Cheating: This project shall not be used to create cheats for Infinitode or to facilitate any form of gameplay manipulation.

Contributor Terms
By contributing, you agree that:
1.The project maintainers may modify this license to be more permissive or restrictive as deemed necessary.

Apart from the specific conditions mentioned above, all other rights and restrictions follow the Apache License 2.0. Detailed information about the Apache License 2.0 can be found at http://www.apache.org/licenses/LICENSE-2.0.

2025 Milk Tea Group Community(mtgpublic@163.com)
