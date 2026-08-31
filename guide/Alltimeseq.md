<p align="left">
      <a href="https://mtgpublic.github.io/infinitode-dqseq/">Return to the main page</a>
</p>

<h1 align="center" style="font-weight: bold;">infinitode-dqseq 💻</h1>
<p align="center" style="font-weight: bold;">A Library/Database of Infinitode Top Dailyquest Bonus Sequence</p>

# All-Time Sequence Guide

All-time sequences are high-scoring Bonus sequences found by SeqUniverse by searching all submittable date seeds within one minimum positive period of the date-seed cycle.

These data are intended to identify strong sequences for each DQ level across the entire range of submittable dates. They are not records of current Daily Quests, nor do they imply that the official servers have been running for ninety thousand years. To look up the current DQ or the DQ for a historical date, use the regular daily sequence data instead.

You can view the submittable-date sequences in the `/data/Alltime` directory.

## Special Data Columns

This section covers only the columns specific to all-time data. For complete rules on the standard data columns, see the [Raw Data Specification](https://mtgpublic.github.io/infinitode-dqseq/guide/Rawdata). For Bonus abbreviations, see [Abbreviation](https://mtgpublic.github.io/infinitode-dqseq/guide/Abbreviation).

### Code

The base-32 date seed code associated with the sequence. It provides a quick way to set dates far into the future. The code is exactly 5 characters long and matches `[0-9a-vA-VzZ]{5}`: digits `0`–`9`, letters `a`–`v` (case-insensitive), and `z` or `Z`. Both `z` and `Z` represent `0`, preventing confusion between the digit `0` and the letter `O`.

For example, `RA59I` in the data is the seed code corresponding to the date `80396_05_30`. `Code` and `Date` are two representations of the same date, so either method can be used to set it.

### Date

The full date associated with the sequence. It can be set by changing the date directly. When entering the date, use the `YYYYY-MM-DD` format: the year must contain 5 digits, while the month and day must each contain 2 digits, padded with a leading `0` when necessary.

For easier column alignment, dates in the data files use underscores as separators. For example, `80396_05_30` in the data should be entered as `80396-05-30` when setting the date.

## Compliance

**You should use these sequences in dev mode only.**

Therainycat has explicitly stated that this is not a bug but a feature. However, because it can undermine the leaderboards, you should not submit scores using these date seeds. If submission is absolutely necessary, **you must not affect today's leaderboard; doing so will be considered cheating**.

You can view the issue report on the [Infinitode 2 Tracker](https://tracker.prineside.com/view.php?id=2637).

The explicit statement comes from [Therainycat's message on Discord](https://discord.com/channels/610566909590765608/939316510365724712/1333387320333963306). This is a Discord post; to read it, you must first join the [Infinitode Modding Server](https://discord.gg/KPE7a9B).
