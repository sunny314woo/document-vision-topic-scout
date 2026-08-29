# Document Vision Topic Scout — ChatGPT 网页版提示词库

## 0 初始化
初始化 Topic Scout 项目，建立空白状态，不虚构论文或 gap。项目短名 OCRScout，sequence 从 01 开始。

## 1 领域地图
我目前没有系统读过这个领域。先做 Beginner Orientation 和 Field Map，不要直接给最终选题。

## 2 Venue Map
目标期刊：[填写]。按 target +1 默认建立 Venue Map；+2 只按条件触发。

## 3 Anchor Papers
选择 8–12 篇最小学习集并分配明确 role，不扩大成无边界综述。

## 4 Problem Map
整理反复问题、失败模式、矛盾、benchmark 弱点和限制。只生成 candidate gaps，不宣布创新。

## 5 Kill Search
候选：[Qxx]。主动寻找最可能证明“这个题已经被做掉”的工作，记录 search envelope、closest prior、最强竞争者和 gap status。

## 6 Top 3
只保留最多 3 个。先过硬 Gate，再排序；不用假精确分数。

## 7 冻结
冻结：[Qxx]。冻结准确 RQ、范围、closest prior、search envelope、约束、fatal risk。

## 8 阶段复盘 / 自然迁移点
报告当前 phase、MP、sequence、active Q、context risk、唯一下一任务。LOW 可继续；MEDIUM/HIGH 按协议决定迁移。

## 9 创建 handoff
先真实生成并核验 ZIP、START_HERE、MANIFEST、PROMPT、CHECKSUMS，再给下一 sequence 和建议短标题。

## 10 新对话接收
先核验 handoff ID、sequence、title、实际 inventory 与 manifest；通过后报告 `CONTINUATION ACCEPTED`。
