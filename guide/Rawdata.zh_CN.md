<p align="left">
      <a href="https://mtgpublic.github.io/infinitode-dqseq/README.zh_CN">返回主页</a>
</p>

<h1 align="center" style="font-weight: bold;">infinitode每日序列 💻</h1>
<p align="center" style="font-weight: bold;">Infinitode顶级每日序列数据库</p>

# 原始数据规范

指原始数据的描述规范。

## 行号(0)

**适用第一列数据。**

为了方便序列的分发与展示，额外给定一列作为行号。

## 序列(Index)

**适用第二列数据。**

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

## 类别最优标识符(\*)

**适用第三列数据。**

如果存在一个序列的主要奖励差于另一个序列的主要奖励，那么这个序列就不算类别最优。

通过星号进行标识。某种意义上，类别最优标识符可以以较好的方式表示出某一类序列的最优序列。

## 序列得分(Score)

**适用第四列数据。**

采用由玩家249发明的序列评分模型。

该模型的核心计算方法是：每100分对应伤害输出翻倍。即最终伤害倍率x与分数y满足 y = 100log2(x) 的关系式。例如230分对应的伤害倍率约为4.925倍。

对于奖励序列而言，总得分为所选所有奖励项的分值之和。

## 摘要(Code)

**适用第五列数据。**

适用缩写规范。

摘要描述了一组序列大概的奖励和等级是什么。

通常来说，摘要由核心信息和主要奖励信息组成：

* 核心信息记录了获取的核心，如果在 1-5 层获取核心，记录为紫（核），如果在 6-10 层获得核心，记录为橙 （核）。
* 主要奖励信息包括奖励内容和登记，采用阿拉伯数字记录奖励等级。

示例：

```
紫橙3伤害4易伤2攻速2等级
```

该序列表示：

- 拥有紫核
- 拥有橙核
- 拥有等级为3的伤害
- 拥有等级为4的易伤
- 拥有等级为2的攻速
- 拥有等级为2的（塔的）等级
- *可能拥有其他奖励*

摘要记录的信息是不完整的，它不会记录分数较低或为0的奖励，也不会记录获得奖励的时间。

**请注意，由于原始数据生成的特性，同一条序列记录的摘要在不同的生成环境下可能不同。**一般来说，只会输出大于等于最高序列得分的3%对应的奖励作为主要奖励。

## 详细描述(Var)

**适用第六列数据。**

适用缩写规范。

详细描述介绍了你在每一层获得的奖励，所有的奖励都会被记录。

在每日挑战中，一共有十层，分别被记录为 1 到 a（采用十六进制，a为小写）来表示层数。

特别的，当获得序列之力（社区有时也会称之为All）时，此时你会同时获得多个奖励。

示例：

```
1全技能24a雷电3尘58a等级6a易伤7核9平台a序列之力
```

该序列表示：

- 在第一层获得了全技能
- 在第二层，第四层，第十层获得了雷电
- 在第三层获得了尘掉落
- 在第五层，第八层，第十层获得了等级
- 在第六层，第十层获得了易伤
- 在第七层获得了（橙）核
- 在第九层获得了平台
- 在第十层获得了序列之力

## 赏金标识符(Bounty)

**适用第七列数据。**

**仅在DQ8中出现。**

DQ8核心中的赏金升级会影响可选择奖励。数据中将标注赏金的前一阶段，以便玩家把握核心升级时机。

这意味着：  

- 需完成前一阶段的选择后再进行赏金升级  

- 不要触发下一阶段的选择条件（即不要达成下一阶段所需的敌人击杀条件）  