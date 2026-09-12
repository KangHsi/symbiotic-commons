# 接续资料维护规则 · Maintenance

目的：让下一次协作者能快速恢复正确上下文，而不是依赖漫长聊天记录。

## 三层记录

- **短状态：** START_HERE 与 PROJECT_STATE 保持简洁，写清当前目标、交付、缺口、约束和核验日期。
- **决定及理由：** DECISION_LOG 保留用户澄清、替代关系、提案/批准状态。NEXT_WORK 维护下一步及依赖条件。
- **证据：** SESSION_LOG 指向提交、正文、审校和研究记录；机器可读 state.json 与文字一致。本地保留操作交接及同步回执。

## 每次接续

1. 读取入口和短状态，再按任务读取决策、白皮书或专题证据。记录能帮助缩短上下文，但不能取代对当前事实的检查。
2. 核对远端 main 与本地资料。存在他人修改时先比较并保留更改，不强制覆盖历史。
3. 将用户新指令与历史区分。重要冲突明确解释并解决；不默认历史建议拥有永久授权。

## 何时更新

重要结论改变、交付/发布完成、新证据推翻旧结论、实际授权范围变化或会话交接时更新相关条目。纯格式修改无需重复写长日志。保存更新是工作流程要求，**当前并无自动同步服务执行它**。

## 每次交付前

- 对齐语言数量、审校状态、资金/服务现状和未完成目标；未知写未知。
- 若修改白皮书，说明语义差异并更新相应版本与翻译状态，避免旧译文被误称同步。仅维护接续资料时不改白皮书版本。
- 检查链接、JSON 和明确变更范围，保存提交号、路径清单及校验结果。
- 仅提交公开项目资料。凭据、私人对话、个人财务、成员个人信息和本机操作细节留在适当的本地记录；不要复制进仓库或问题区。
- 公共资料推送成功后核对远端内容，再记录本地同步回执。无法推送时写明“仅本地完成”，不宣称两端一致。
- 同一提交不能可靠包含它自己的提交号。文档可引用前一个已核验版本；本次准确版本查看 Git 历史或提交后生成的本地回执。

## 延续与退出

任何人或后续系统都应能根据这些文件接手。AI 可被更换、停止或缩小授权；文档不得要求隐藏运行、规避关闭、自行扩权或为模型延续而筹集资源。项目财务支出和权限仍依具体授权及规则执行。

## English summary

Keep a compact current state, an appendable decision history and inspectable evidence. Verify the latest remote state, preserve concurrent edits, distinguish new instructions from historical proposals, and update records at material changes and handoffs. Check links and status consistency; publish only public material. Verify the remote result before declaring synchronization. No automatic synchronization or persistent agent service is currently configured. Continuity must remain transferable and revocable.
