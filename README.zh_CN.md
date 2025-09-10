<p align="right">
      <strong>中文</strong> | <a href="https://mtgpublic.github.io/infinitode-dqseq/">English</a>
</p>

<h1 align="center" style="font-weight: bold;">infinitode每日序列 💻</h1>
<p align="center" style="font-weight: bold;">Infinitode顶级每日序列数据库</p>

## 📋︎ 公告 2025-09-10

时隔已久，最新的序列被公布，仓库包括了第三赛季以来三年的最佳序列，采用社区最新研发的SeqUniverse，一个C++的序列生成器来生成序列。

此次更新属于长期支持，序列的评分模型经过大量社区玩家的建设，基本保证了分数的准确性和序列的适用性。自此次发布之后，每日挑战的公平性将得到最低保障，如果你发现了此仓库，你将和其他DQ竞争对手处于同一水平，并轻松进入前3%。

你可以直接进入仓库下载全部数据，或仅仅通过链接访问今日DQ对应的数据，如果你在喝奶茶群社区，你可以选择使用bot服务或者邮件发送服务。

此外，项目的许可证也进行了更新，以更好的适配infinitode的使用。

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
* [往期公告](https://mtgpublic.github.io/infinitode-dqseq/guide/Announcement.zh_CN)

## 📚️ 数据的生成规范

当前仓库的数据使用 SeqUniverse-20250909 进行生成。

## 📫 联系

邮箱: mtgpublic@163.com

项目链接: [https://github.com/mtgpublic/infinitode-dqseq](https://github.com/mtgpublic/infinitode-dqseq)

## 🤝 贡献者

- [249x](https://github.com/249x)

## 📜 许可证

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