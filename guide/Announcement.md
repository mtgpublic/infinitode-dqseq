<p align="left">
      <a href="https://mtgpublic.github.io/infinitode-dqseq/">Return to the main page</a>
</p>

<h1 align="center" style="font-weight: bold;">infinitode-dqseq 💻</h1>
<p align="center" style="font-weight: bold;">A Library/Database of Infinitode Top Dailyquest Bonus Sequence</p>

# Announcement Archive  

Contains historical announcement records.  

## 2025-11-02

With Sequniverse receiving an update, dqseq has been synchronized to better provide optimal sequences.

Specific adjustments in the scoring model for v20251025 compared to v20250909 include:

1. DQ3 Modifications:
   - Increased weight for DebuffsLastLonger
   - Decreased weight for TowersAttackSpeed
   - Significantly reduced weight for LightningStrikeOnTowerLevelUp

2. DQ9 Optimizations:
   - Improved weight calculation logic for AddAllAbilityCharges and IncreasedTowerToEnemyEfficiency_SPLASH_ARMORED
   - When other bonus score totals are low, AddAllAbilityChargess and IncreasedTowerToEnemyEfficiency_SPLASH_ARMORED will receive proportionally lower weights

3. Global Adjustment:
   - NukeOnBonusStage weight calculations are no longer restricted to Stage 10 in most levels

Additionally, we've implemented bug fixes and enhanced example sets for the Dense Marker Sequence Standard to improve player comprehension.

## 2025-09-10

After a long wait, the latest sequences have been released. The repository includes the best sequences from the past three years since Season 3, generated using the community's newly developed SeqUniverse, a C++ sequence generator.  

This update is part of long-term support. The scoring model for the sequences has been refined through extensive contributions from community players, ensuring the accuracy of the scores and the practicality of the sequences. Starting from this release, the fairness of the daily challenges will be guaranteed at a minimum level. If you discover this repository, you’ll be on the same playing field as other DQ competitors, easily placing in the top 3%.  

You can directly access the repository to download all the data or simply use the link to retrieve the data corresponding to today’s DQ challenge. If you're part of the MilkTea Group community, you can opt for the bot service or the email delivery service.  

Additionally, the project's license has been updated to better align with Infinitode's usage.

## 2025-08-02

Modifitode 1.6.2 has updated its data specifications. From this version onward, the data will be fully compliant with dqseq's standards. The MTG community is currently developing a C++-based sequence traversal project. If progress goes smoothly, dqseq's data source will primarily be provided by this new project.

The MTG community has recently observed frequent occurrences of scores using the Venom FS strategy. dqseq currently has no plans to modify sequence weighting, which means if you wish to employ Venom FS strategies, you'll need to locate sequences yourself.

**Since the game's developer Therainycat has no intention of fixing either the Venom FS strategy exploit or the DQ leaderboard submission exploit, this means the fairness of the DQ leaderboard will be significantly compromised. Please view DQ leaderboard competition with discretion and be prepared for others possessing unfair advantages that cannot be matched through normal gameplay.** While dqseq strives to uphold DQ fairness, MTG has stated it can do nothing about this situation.

## 2025-07-20

**Due to the emergence of more efficient technologies and implementation scripts, as well as the progressive refinement of fairness and anti-cheat declarations, the infinitode-dqseq project has resumed updates. The data is now powered by Modifitode version >=1.6.1.**

**Currently, the data on GitHub has been updated up to August 20, 2025.**

The sequence will currently only be provided in Chinese, and internationalization is not being considered for a considerable period. Internationalization requires a substantial base of in-depth users of infinitode-dqseq, and currently, the project lacks a foundation of non-native Chinese-speaking users. If you are willing to contribute in this regard, feel free to submit suggestions via issues or discuss it in international communities such as the Infinitode Discord.  