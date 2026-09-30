# F3 固定评价审计

- 任务：`F3-AUDIT-20260929-v1`
- 状态：`F3_AUDIT_PASS_PENDING_MAIN_AGENT_DECISION`
- 范围：只读复算既有 F2 盲预测、评分审计和固定指标；未打开 Gold 文件，未运行模型、增加样本/标签、改阈值、重新评分或重跑 F2。
- 证据等级：D2 是受控校准的 challenge/confirmation set；不是概率样本、独立第三方 Gold 或完整三动作链接测试。

## 完整性与分母

`predictions.jsonl` 为 102 行、102 个唯一 `item_id`，与 F2 `scoring_audit.json` 的标签及簇键集合一致；标签为 57 ADMISSIBLE、45 REJECT。预测文件 SHA-256 与预测 manifest、评分审计和指标 manifest 相互一致；评分审计、指标文件哈希与指标 manifest 一致。所有方法的 Admission Retention 和 REJECT FAR 均以 57/45 为固定分母，缺分数和失败项未被剔除。

候选覆盖 79/102，无候选 23/102；解析失败 9/102（6 `INVALID_SPANS`、3 `INVALID_JSON`），generation/retrieval/rerank failure 均为 0。Primary 有 79 `OK`、16 `NO_CANDIDATE`、4 `INVALID_SPANS`、3 `INVALID_JSON`。覆盖率与失败类别并非互斥分组，不能相加为 102。

## 独立复算

从既有盲预测与 `scoring_audit.json` 的评分标签重新计算八个方法的覆盖、决策计数、ROC-AUC、AUPRC 和全部 Retention--FAR 曲线；数值最大绝对误差为 0。按冻结的 Gold 分层、内容簇、seed `20260928`、2,000 次抽样和冻结的顺序统计量规则重建成对 bootstrap；八个方法全部四项 95% 区间与 F2 文件逐项一致。以下 AUC/AUPRC 只在 102/102 分数覆盖时报告全量值。

| 冻结方法 | 分数覆盖 | 保留 / 57 | 误收 / 45 | 全量 ROC-AUC | 全量 AUPRC |
|---|---:|---:|---:|---:|---:|
| Admit all | 102/102 | 57 | 45 | .5000 | .5588 |
| BM25 top-1 | 101/102 | 53 | 27 | NA | NA |
| BGE top-1 | 101/102 | 55 | 40 | NA | NA |
| Validity | 79/102 | 44 | 13 | NA | NA |
| Direct admission | 102/102 | 46 | 10 | .8680 | .9024 |
| Clean linear | 102/102 | 39 | 24 | .5263 | .5460 |
| Clean RBF | 102/102 | 35 | 9 | .7930 | .8308 |
| Primary joint linear | 79/102 | 40 | 10 | NA | NA |

Primary 的条件分数仅覆盖 79 行（其中 50 ADMISSIBLE、29 REJECT），条件 ROC-AUC=.7697、AUPRC=.8222。它们不能写成 102 行全量 AUC/AUPRC；全量均为 `NA_NOT_FULL_COVERAGE`。

冻结决策点的 95% 成对簇 bootstrap：Primary 保留率 [.5789,.8246]、FAR [.1111,.3556]；Direct 保留率 [.7018,.9123]、FAR [.1111,.3333]；Clean RBF 保留率 [.4912,.7368]、FAR [.0889,.3111]。独立重算的 Direct-Primary 保留差为 +6/57，95% CI [-2/57,14/57]；FAR 差为 0/45，CI [-7/45,7/45]。Clean RBF-Primary 保留差为 -5/57，CI [-14/57,3/57]；FAR 差为 -1/45，CI [-7/45,5/45]。这些方法间区间均跨 0；它们是对既有 F2 预测的审计性成对差异复算，不是新评价批次。

## 裁决边界

本次执行可接受为“完成、带已披露协议偏离”：F2 的盲预测先于评分和 Gold 读取；评分完成后，哈希登记额外只读重算了 Gold SHA-256，越过严格的 score-only Gold 访问边界。记录显示没有解析标签、修改预测/配置或重跑；该偏离必须在方法或限制中披露，不构成因结果不佳重跑的理由。

科学结论限于：在这批冻结 D2 item 上，Primary 未显示相对 Direct admission 的优势；Direct 在相同 10/45 FAR 下多保留 6/57 且覆盖更完整，但成对差异区间跨 0，不能宣称总体上已确认 Direct 优于 Primary。Clean RBF 的低误收伴随更低保留。历史 DEV/EVAL 不能替代本次相对比较。不得由此推断 Web prevalence、真实部署损害、NEW/EXISTING/REJECT 三动作链接性能，或独立 admission 模型的必要性。

输入、输出及 SHA-256 见 `F3_input_output_hashes_20260929.txt`。Claim--number--source 已追加至 Stage3 的 `claim-evidence-matrix.md`，原 C0--C5 保留为历史时点。F3 到此停止，等待主代理决定收缩主张写作或关闭本稿；不放行任何新实验。
