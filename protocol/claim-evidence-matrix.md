# Claim--Evidence Matrix

日期：2026-09-28。文档任务 ID：`D0-20260928-v1`；不是实验运行 ID。唯一 active route：`B-journal Open-Web Event Admission / Calibration`。本表仅登记已有证据，不生成结果；C0--C5 为 Stage3 的稳定编号，不沿用历史 Stage2 表中同名编号的含义。

| Claim ID | Exact claim | Scope | Evidence artifact | Unit / denominator | Evidence level | Current result | Allowed wording | Forbidden wording | Missing evidence | Gate |
|---|---|---|---|---|---|---|---|---|---|---|
| C0 | 在 P0 校准材料中，mention 事件性、item 准入和 target 对齐标签不能直接互相传播。 | EventLink-NYT 匹配诊断包；P0 最终校准口径；2026-09-21；纯文本，三轴分别评估。 | [P0报告][p0-report]、[三轴表][p0-gold]、[item表][p0-items]、[原始IAA][p0-iaa] | 80 item，39 YES /39 NO /2 UNCERTAIN；124 mention；前两轴均 YES 的对齐分母为43 mention。 | development | **P0**：19个 mention YES /item NO；28个 mention NO /item YES；18/43不对齐。39个YES item中22个无已审计三轴全YES legacy NIL target。 | “本校准包内不可互相传播”；item 获准不等于正确 target 被保留。 | “REJECT 都没有事件”；“发现全新本体”；“P0 是独立第三人验证”；将25个对齐目标称为 qualified NEW。 | 未见材料的三轴确认；目标覆盖不是全文所有目标 Gold；C及最终确认含AI辅助。 | 正文：受限的任务单位证据；原始IAA与裁决来源保留。 |
| C1 | 在固定纯文本组织政策下，抽取到事件候选并不充分决定该 item 是否准入。 | 2026-09 Latest限额Web池；`WEB-TEXT-ADMISSION-v2`；仅展示正文与元数据；离线候选链，item级。 | [Web60可靠性][web-iaa]、[原始漏斗][funnel]、[系统协议][protocol] | Web60即EVAL60：33 ADMISSIBLE /27 REJECT；DEV30为12/18，另用于开发；不能合并估计比例。 | controlled diagnostic | **EVAL60原始漏斗**：候选存在29/33和22/27；validity-YES阶段留下25/33和11/27。**Web60**首次一致51/60、κ=.6932。 | “本离线链中候选存在与准入不同”；候选命中数不是 eligible-target 覆盖率。 | “有候选就应接收”；“已证明真实部署损害”；“27/60是Web prevalence”。 | 独立确认；目标级Gold；实际部署后果。Web60有2条接触声明、9条AI辅助裁决。 | 正文：受控链诊断；总体入口/部署外推暂缓。 |
| C2 | 在受控文本准入诊断中，部分检索和语义信号及其组合具有预测性，但并非所有实现都有效。 | 同一DEV30/EVAL60、v2政策、Qwen2.5-7B与BM25/BGE；2020 KB相关性信号用于2026 Web；非LINK/NIL正确性。 | [原始指标][metrics]、[系统报告][system-report]、[恢复指标][recovered-metrics] | EVAL固定60 item；保留分母33，误收分母27；AUC正负为33/27；DEV拟合分母30。 | controlled diagnostic | **原始EVAL60 AUC**：BM25 .7632、BGE .5466、validity .7357、direct admission .7469、联合线性 .7969、RBF .8058；salience .4871且119候选中118答YES。**恢复诊断**：联合线性 .8361。 | “部分信号在本受控集有预测性”；恢复结果说明测量敏感性；validity是实现名称，不是已验证构念。 | “所有EL分数无用”；“direct稳定优于已有组合”；“salience已可靠测量”；把恢复增益称为新语义能力。 | 真正独立确认；D1去解析产物浅层对照；独立validity/salience构念Gold未取得。 | 正文：原始与恢复分账；退化salience放诊断/限制，不作等强主方法。 |
| C3 | 在本受控诊断中，低REJECT误收伴随准入保留损失，DEV选择的高保留阈值不能稳定迁移到EVAL。 | v2文本政策；阈值仅用DEV选，目标≥90%准入保留；同一EVAL固定；事后DEV重抽样，不是新test。 | [原始指标][metrics]、[恢复指标][recovered-metrics]、[稳定性报告][robust-report]、[恢复稳定性][stability] | DEV30：12/18；EVAL60：33/27；2,000次固定分数阈值重抽样和200次分层重拟合是重复分析，不是新增item。 | controlled diagnostic | **原始EVAL**：BM25保留26/33、误收14/27；联合线性19/33、3/27；RBF12/33、2/27。**恢复EVAL**：线性23/33、2/27；RBF10/33、0/27。恢复线性2,000次重抽样中达到90% EVAL保留的比例为0。 | “本DEV→EVAL迁移存在保留损失与阈值敏感性”；同时报告Retention--FAR。 | “零FAR即可安全部署”；“AUC足以证明系统收益”；“已证明所有来源阈值都不稳定”；把Admission Retention改称NEW Retention。 | 冻结系统在独立集的一次确认；按内容簇区间；现有重抽样不涵盖所有选择、标注及抽样不确定性。 | 正文：条件化取舍与迁移；重抽样细节可进附录。 |
| C4 | 候选片段格式和解析规则是本准入测量链的误差源，严格恢复会改变部分系统结果。 | 原始/严格恢复共享90 item、policy、模型与既有标签；2026-09-28事后稳健性诊断；只允许唯一绑定正文的受限格式等价。 | [原始漏斗][funnel]、[恢复计划][recovery-plan]、[恢复报告][robust-report]、[恢复完成清单][robust-completion] | 90 item=DEV30+EVAL60；原始119候选→恢复136；EVAL仍60，33/27不变。 | controlled diagnostic | **原始EVAL**：9/60无候选，含4个可准入。**恢复诊断**：13/90 item发生恢复变化，补17候选，2/90仍UNRESOLVED_SPANS；EVAL中4个可准入及2个拒绝从无候选变有候选，剩3个无候选均拒绝。 | “本实现的部分错误来自测量链”；恢复与语义能力分开归因；缺候选不出分母。 | “所有错误都是解析错误”；“恢复结果是独立确认”；“候选数等于合格目标数”；用含解析产物的浅层对照否定语义信号。 | D1冻结primary链、missing-score与无候选处理；clean shallow-control须排除candidate_count/generator_error；独立确认。 | 正文：误差源与敏感性；事后含解析产物浅层结果仅附录/限制。 |
| C5 | 现有受控准入证据尚不足以支持完整三动作链接性能、Web总体比例或独立新模型必要性。 | 截至2026-09-28的P0、Web60、DEV30/EVAL60及恢复诊断；仅文本准入政策，不扩展至完整链接或整个Web。 | [P0报告][p0-report]、[Web60可靠性][web-iaa]、[系统报告][system-report]、[恢复报告][robust-report]、[Stage3冻结][freeze] | 已有分母沿用上述各包；未取得的独立确认/qualified NEW/EXISTING/概率样本无可报告性能分母。 | unsupported | **证据缺口，不是负实验结果**：P0不填动作Gold；Web60有接触与AI辅助裁决；系统/恢复复用DEV/EVAL；300条是限额检索池。未取得独立三动作Gold、概率prevalence及实际部署成本。 | “这些目标尚未验证”；REJECT为当前证据下NO-ADMISSION；不等于现实事件不存在。 | “完成三状态链接”；“NEW=legacy NIL或item YES”；“全部linker需要新模块”；“真实事件库污染已证明”；“完整链接已被否定”。 | 独立准入确认是本稿待补；B2最多20--30条仅可行性试点，plausible NEW不自动成Gold；完整链接/B1 prevalence/多模态为后置。 | 限制：明确披露；完整三动作/总体比例/新模型必要性主张暂缓。 |

证据读法：`development`为定义/开发材料；`controlled diagnostic`为有开发或裁决接触的受控结果；`independent confirmation`须有冻结系统和独立新材料，本轮没有；`unsupported`标记C5列出的未获支持外推，不表示这些目标已被证伪。Web60与EVAL60是同一批，不算两份确认。P0原始item一致率67.50%、κ=.335，mention一致率83.87%、κ=.673，共同可评alignment子集37/38、κ=.944；裁决后标签不替换原始IAA。以上均保留AI辅助、条件筛选与证据接触限制。

执行门：D0只完成本矩阵和入口同步，停止等待验收；下一步为D1测量链冻结。不启动模型、采样、标注或新实验。

## F3 证据更新（2026-09-29）

上表 C0--C5 保留为 D0 时点的历史登记；其中“独立确认待补”和“下一步 D1”不再表示当前执行状态。F2 已在冻结的 D2 challenge/confirmation set 上完成一次固定评价，F3 只复算和审计既有产物。D2 有 102 个 item（57 ADMISSIBLE、45 REJECT），不是概率样本，也没有 EXISTING/NEW/REJECT 三动作 Gold。融合标签由 A/B 人工盲标和 C 人工裁决构成；有道仅作翻译辅助。评分后额外重算 Gold SHA-256 是已披露的 score-only 边界偏离；盲预测先于 Gold 读取，未改预测或重跑。

| Claim ID | 当前可用 claim | 数字与分母 | 来源 | 证据边界 |
|---|---|---|---|---|
| C2-F2 | 在 D2 固定评价中，Primary 未显示相对 direct admission 的准入优势。 | Primary 覆盖79/102、保留40/57、误收10/45；direct 覆盖102/102、保留46/57、误收10/45。Direct 的全量 ROC-AUC=.8680、AUPRC=.9024；Primary 全量二者均为 NA，条件 ROC-AUC=.7697 不能替代全量值。 | [F2指标][f2-metrics]、[F3审计][f3-audit] | 成对 bootstrap 的 Direct-Primary 保留差为+6/57，95% CI [-2/57,14/57]，跨0；不能声称统计确认的普遍优势或联合信号稳定增益。 |
| C3-F2 | D2 上的固定决策点仍有保留率--误收折衷，但不是新方法胜出证据。 | Clean RBF 覆盖102/102、保留35/57、误收9/45；Primary 为40/57、10/45。 | [F2指标][f2-metrics]、[F3审计][f3-audit] | RBF-Primary 保留差-5/57，95% CI [-14/57,3/57]；误收差-1/45，95% CI [-7/45,5/45]，均跨0。 |
| C4-F2 | 候选与解析覆盖仍是本次评价的重要测量限制。 | 候选覆盖79/102；无候选23/102；解析失败9/102；Primary 全量 AUC/AUPRC 为 NA。 | [F2指标][f2-metrics]、[F3审计][f3-audit] | 失败项留在 Retention/FAR 分母；条件分数只作诊断，不代表完整系统评价。 |
| C5-F2 | 本次确认了准入评价链可执行，但未验证完整开放世界事件链接、Web prevalence、部署后果或专门模型必要性。 | 102 item 的二元准入 Gold；无三动作 target Gold、概率抽样分母或部署成本分母。 | [F2运行记录][f2-receipt]、[F3审计][f3-audit] | 不能将 D2 称为概率样本、独立第三方 Gold 或完整链接 benchmark；不得以历史 DEV/EVAL 替代本次相对比较。 |

F3 后的当前执行门：停止新实验、补标、调阈值和重跑；等待主代理决定收缩主张写作，或关闭本稿。上表早期结果继续作为开发/受控诊断，不提升证据等级。

[p0-report]: ../Stage2_实验验证/experiments/task_alignment/results/P0结项报告.md
[p0-gold]: ../Stage2_实验验证/experiments/task_alignment/results/P0_final_gold.csv
[p0-items]: ../Stage2_实验验证/experiments/task_alignment/results/P0_final_items.csv
[p0-iaa]: ../Stage2_实验验证/experiments/task_alignment/results/P0_AB原始统计报告.md
[web-iaa]: ../Stage2_实验验证/experiments/open_web_prevalence/automation_20260927/results/reliability_report.md
[funnel]: ../Stage2_实验验证/experiments/open_web_prevalence/system_diagnostic/candidate_funnel.csv
[protocol]: ../Stage2_实验验证/experiments/open_web_prevalence/system_diagnostic/protocol.json
[metrics]: ../Stage2_实验验证/experiments/open_web_prevalence/system_diagnostic/metrics.csv
[system-report]: ../Stage2_实验验证/experiments/open_web_prevalence/system_diagnostic/report.md
[recovered-metrics]: ../Stage2_实验验证/experiments/open_web_prevalence/robustness_diagnostic/recovered/metrics.csv
[robust-report]: ../Stage2_实验验证/experiments/open_web_prevalence/robustness_diagnostic/report.md
[stability]: ../Stage2_实验验证/experiments/open_web_prevalence/robustness_diagnostic/recovered/stability_summary.json
[recovery-plan]: ../Stage2_实验验证/experiments/open_web_prevalence/robustness_diagnostic/recovery_plan_summary.json
[robust-completion]: ../Stage2_实验验证/experiments/open_web_prevalence/robustness_diagnostic/completion.json
[freeze]: 投稿冻结与一周执行安排.md
[f2-metrics]: d2_independent_confirmation_v1/fixed_evaluation_v1/runtime/fixed_metrics.json
[f2-receipt]: d2_independent_confirmation_v1/fixed_evaluation_v1/F2_run_receipt_20260929.md
[f3-audit]: d2_independent_confirmation_v1/fixed_evaluation_v1/F3_audit_report_20260929.md
