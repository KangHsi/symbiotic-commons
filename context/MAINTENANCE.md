# 接续资料维护规则 · Continuity maintenance rules

<a id="b01"></a>

用三层记录恢复上下文：简短的 START_HERE 与 PROJECT_STATE；保留理由、来源和替代关系的 DECISION_LOG 与 NEXT_WORK；指向提交和成果的 SESSION_LOG、state.json 及本地证据和回执。

Restore context through three layers: concise START_HERE and PROJECT_STATE; DECISION_LOG and NEXT_WORK retaining reasons, sources, and supersession; and SESSION_LOG, state.json, plus local evidence and receipts pointing to commits and results.

<a id="b02"></a>

开始时读取入口，再依任务阅读相关原文，核对远端 main 和本地差异，保留他人更改，不强制覆盖历史。区分新指令与旧提案；冲突明确解释，不把历史建议当作永久授权。

Start with the entry point, read relevant originals for the task, compare remote main with local state, and preserve others’ changes without forcing over history. Distinguish new instructions from old proposals; explain conflicts rather than treating historical suggestions as permanent authority.

<a id="b03"></a>

重要结论改变、交付完成、新证据推翻旧结论、授权变化或交接时更新记录；格式小改无需长日志。当前只维护中英文，两边完整配对；编辑配对源并重新生成，运行 --check，阅读核对事实、条件、否定与列表。白皮书语义变化说明理由并更新版本。

Update records when material conclusions change, work is delivered, new evidence overturns old conclusions, authority changes, or work is handed over; minor formatting needs no long log. Maintain only Chinese and English with full pairing; edit paired source, regenerate, run --check, and read both texts to compare facts, conditions, negations, and lists. Explain semantic whitepaper changes and update versions.

<a id="b04"></a>

交付前核对状态、链接、JSON、变更范围与哈希。未知写未知，不把历史 78 版或 90% 计划恢复为当前要求。仅提交公开资料；凭据、私聊、个人财务、成员隐私和本机操作细节不进公共仓库。

Before delivery, check status, links, JSON, change scope, and hashes. Leave unknowns unknown, and do not reinstate the historical 78-edition or 90% plan as a current requirement. Publish only public material; credentials, private conversations, personal finances, member privacy, and local operational details stay out of the public repository.

<a id="b05"></a>

推送后核对远端，再保存本地回执。推送失败应明确“仅本地完成”。同一提交不写入它自身的提交号；准确版本查历史或提交后回执。保存流程不等于自动同步，当前没有自动同步服务。

Check the remote after pushing, then save the local receipt. If pushing fails, clearly state “completed locally only.” Do not embed a commit’s own SHA in that same commit; consult history or a post-commit receipt for its exact revision. A saving workflow is not automatic synchronization; no automatic sync service is currently configured.

<a id="b06"></a>

工作应可被其他人或系统接手，AI 可更换、停止或缩小授权。记录不要求隐藏运行、规避关闭、自行扩权或为模型延续筹集资源。财务和权限仍按具体授权及规则执行。

Work should be transferable to other people or systems, and AI can be replaced, stopped, or assigned less authority. Records must not require hidden operation, shutdown evasion, self-expanded authority, or resource collection for model continuation. Finances and permissions remain governed by specific mandates and rules.
