<p align="left">
      <a href="https://mtgpublic.github.io/infinitode-dqseq/README.zh_CN">返回主页</a>
</p>

<h1 align="center" style="font-weight: bold;">infinitode每日序列 💻</h1>
<p align="center" style="font-weight: bold;">Infinitode顶级每日序列数据库</p>

# 可提交日期序列指南

可提交日期序列是使用 SeqUniverse 在全部可提交日期种子中搜索得到的高分奖励序列，由于这段时间的最小正周期循环。

这些数据用于寻找各个 DQ 关卡在整个可提交日期范围内的强力序列。它们不是当前每日挑战的日期记录，也不表示官方服务器已经运行了九万年。若要查询当前或某个历史日期的 DQ，请使用普通的每日序列数据。

你可以查看 `/data/Alltime` 目录来阅读可提交日期序列。

## 特殊的数据列含义

此处仅讲述特殊的数据列，对于常规的数据列的完整规则请阅读[原始数据规范](https://mtgpublic.github.io/infinitode-dqseq/guide/Rawdata.zh_CN)，奖励简称请查阅[缩写规范](https://mtgpublic.github.io/infinitode-dqseq/guide/Abbreviation.zh_CN)。

### Code

表示该序列对应日期的 32 进制种子代码，可用于快速设置较为遥远的日期。代码固定为 5 位，格式为 `[0-9a-vA-VzZ]{5}`，可使用数字 `0`～`9`、字母 `a`～`v`（不区分大小写）以及 `z` 或 `Z`。其中 `z` 和 `Z` 代表 `0`，用于避免数字 `0` 与字母 `O` 混淆。

例如，数据中的 `RA59I` 是日期 `80396_05_30` 对应的种子代码。`Code` 和 `Date` 表示的是同一个日期，使用任意一种方式设置即可。

### Date

表示该序列对应的完整日期，可通过直接修改日期的方式进行设置。设置时应使用 `YYYYY-MM-DD` 格式：年份为 5 位，月份和日期各为 2 位，不足位数时在左侧补 `0`。

为了方便数据按列展示，文件中的日期使用下划线分隔。例如，数据中的 `80396_05_30` 在设置时应输入为 `80396-05-30`。

## 合规性

**你应该在仅开发者模式下使用这些序列**。

Therainycat 明确说明这不是一个 Bug 而是一个 Feature，但由于其对排行榜的破坏性，你不应该提交这些时间的种子。如有必须，**你不应影响今日排行榜，影响今日排行榜的行为将会视为作弊**。

你可以在[Infinitode 2 Tracker](https://tracker.prineside.com/view.php?id=2637)上查阅漏洞报告。

明确声明的消息来源于[Therainycat's message on Discord](https://discord.com/channels/610566909590765608/939316510365724712/1333387320333963306)，这是一个Discord上的帖子，为了阅读它，你需要先加入[Infinitode Modding Server](https://discord.gg/KPE7a9B)。

