<p align="right">
      <strong>中文</strong> | <a href="https://mtgpublic.github.io/infinitode-dqseq/">English</a>
</p>

<h1 align="center" style="font-weight: bold;">infinitode每日序列 💻</h1>
<p align="center" style="font-weight: bold;">Infinitode顶级每日序列数据库</p>

## 📋︎ 公告 2025-08-02

Modifitode 1.6.2更新了数据规范，在此之后，数据将与dqseq的规范完全一致。目前MTG社区正在开发基于C++的序列遍历项目，若项目进展顺利，dqseq的数据源将主要由新项目提供。

MTG社区最近发现使用连锁策略的成绩频繁出现，dqseq目前不会更改序列权重，这意味着如果你需要进行连锁策略，你需要自行寻找序列。

**由于游戏作者Therainycat无意修复连锁策略漏洞和DQ排行榜分数提交漏洞，这意味着目前DQ排行榜的公平性将受到极大影响。请合理看待DQ排行榜竞争，做好他人拥有无法通过正常游戏弥补的不公平优势的准备。**虽然dqseq尽力在DQ公平性上做出贡献，但对此MTG表示无能为力。

## 📌 这是什么？

《无限塔防》是由The Rainy Cat开发的一款塔防游戏。  

每日挑战是游戏中的一项玩法，玩家需要在特定的每日关卡中完成任务以获得奖励，或通过高分竞争排行榜名次。在该模式中，玩家可通过选择奖励(Bonuses)来增强防御塔实力。通过合适的路线选择，就能找到最优的奖励序列。  

本仓库存储了大量每日挑战顶尖奖励序列，帮助玩家更轻松完成任务或持续占据排行榜前列。

## 🔗 链接

项目链接: [https://github.com/mtgpublic/infinitode-dqseq](https://github.com/mtgpublic/infinitode-dqseq)

本仓库仅发布于GitHub及《无限塔防》中文社区。

Infinitode2喝奶茶群QQ群号：1020322961  

## 🚀 快速开始

使用这些序列非常简单。但在开始前，请确保您已充分理解无限塔防每日挑战机制，并明确以下要点：

[Infinitode 2 Wiki - 奖励系统](https://infinitode-2.fandom.com/wiki/Bonuses)简要介绍了《Infinitode》每日挑战中奖励的运作机制，本文将主要说明数据的描述方式。

### ob序列描述标准

采用阿拉伯数字描述序列，每五个选择用空格隔开。该方法最初由ob(Dense Marker)创建，后成为社区交流序列的通用描述方式。

在当前版本的Infinitode中，若没有选择[额外获得选择选项]，则我们用 1 代表选择从左往右数第一项奖励，2 代表选择第二项奖励，3 代表选择第三项奖励。如果本轮进行了重新选择，我们用 4 代表重新选择后的第一项，5 代表选择第二项，6 代表选择第三项。

如果在某一轮次选择了[额外获得选择选项]，在下一轮次，我们用 4 代表选择第四项；若该回合出现重新选择，我们用 5 代表重新选择后的第一项，6 代表重新选择后的第二项，以此类推。

示例：
```
33513 23432
```

假设未选择[额外获得选择选项]，该序列表示：
- 前五层(3,3,5,1,3)：
  - 前两次选择3（第三个奖励）
  - 第三次选择5（重置后的第一个奖励）
  - 第四次选择1（第一个奖励）
  - 第五次选择3（第三个奖励）
- 后五层(2,3,4,3,2)：
  - 第六次选择2（第二个奖励）
  - 第七次选择3（第三个奖励）
  - 第八次选择4（重置后的第一个奖励）
  - 第九次选择3（第三个奖励）
  - 第十次选择2（第二个奖励）

### 249奖励序列模型  

由玩家249发明的序列评分模型。

该模型的核心计算方法是：每100分对应伤害输出翻倍。即最终伤害倍率x与分数y满足 y = 100log2(x) 的关系式。例如230分对应的伤害倍率约为4.925倍。

对于奖励序列而言，总得分为所选所有奖励项的分值之和。

### DQ8赏金机制

DQ8核心中的赏金升级会影响可选择奖励。数据中将标注赏金的前一阶段，以便玩家把握核心升级时机。

这意味着：  
- 需完成前一阶段的选择后再进行赏金升级  
- 不要触发下一阶段的选择条件（即不要达成下一阶段所需的敌人击杀条件）  

## 🎮 使用

如果你已经阅读了"快速开始"的内容，你可以很容易的掌握序列的使用方法。

所有的发布数据都会在`data`目录下，以txt文件格式存储，你可以通过日期找到当天所有关卡的序列数据。

序列已经经过排序，通常来说越前面的序列越强。

### 进阶使用

序列同时包含了摘要，详细描述，分数等信息帮助你进行序列的选择，如有需要，请阅读下面的扩展页面。

* [缩写规范](https://mtgpublic.github.io/infinitode-dqseq/guide/Abbreviation.zh_CN)
* [原始数据规范](https://mtgpublic.github.io/infinitode-dqseq/guide/Rawdata.zh_CN)
* [合规性疑难解答](https://mtgpublic.github.io/infinitode-dqseq/guide/Compliance.zh_CN)

## 📚️ 数据的生成规范

当前仓库的数据使用 Modifitode >=1.6.1 进行生成。

参数列表：
* scoreRecord = 200
* scoreThreshhold = 30

## 📫 联系

邮箱: mtgpublic@163.com

项目链接: [https://github.com/mtgpublic/infinitode-dqseq](https://github.com/mtgpublic/infinitode-dqseq)

## 🤝 贡献者

- [249x](https://github.com/249x)

## 📜 许可证

<a href="https://github.com/mtgpublic/infinitode-dqseq">infinitode-dqseq</a> © 2025 by <a href="https://github.com/mtgpublic">mtgpublic</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" style="max-width: 1em;max-height:1em;margin-left: .2em;">