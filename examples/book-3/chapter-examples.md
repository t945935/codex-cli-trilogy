# 第三本範例索引（配套素材，不是章節稿）

每章情境卡連到一份可複製的工作表或範本。素材都在 `examples/book-3/`；大多數工作表是空白待填，不代表已發生的執行紀錄或帳號量測結果。所有 CLI 指令、設定格式、方案／用量與功能成熟度都要依當期官方文件核對。

| 章 | 跟做情境 | 可觀察成果／過關條件 | 配套素材 |
|---|---|---|---|
| 1 效率不是少打字 | 固定同一類小任務，記錄起始狀態、計時邊界、測試與返工 | 建立可重跑的基準；不以少打一段提示作唯一效率指標 | `workflow-kit/task-metrics.csv` |
| 2 高品質任務提示 | 把「修一下搜尋」改成有背景、範圍、驗收和停手條件的任務簡報 | 隊友不需猜資料格式或是否可加依賴 | `task-brief.md`、`workflow-kit/handoff-template.md` |
| 3 專案指引 | 為練習專案挑短小且可測的常駐規則，檢查載入來源 | 規則沒有互相矛盾；不把 `AGENTS.md` 誤當 sandbox | `AGENTS.example.md` |
| 4 上下文管理 | 將一項功能拆成盤點、實作、驗收三段並交接 | 摘要區分已證實事實、決策、未驗證項 | `workflow-kit/handoff-template.md` |
| 5 權限與沙箱 | 把任務分成唯讀、工作區修改和外部副作用 | 能指出技術 sandbox 與 approval policy 差異 | `workflow-kit/risk-decision-matrix.md` |
| 6 執行命令與自動化 | 對公用練習 clone 做一次唯讀 `codex exec` 檢查 | 明確 model、目錄、唯讀 sandbox；失敗 exit status 會停止 | `workflow-kit/workflow-checklist.md` |
| 7 MCP 與外部工具 | 評估一個假想文件 server，先畫資料流、不安裝 | 說清 server 來源、讀寫工具、認證、批准和撤銷 | `workflow-kit/mcp-server-review.md` |
| 8 Skills／Plugins | 評估一個候選擴充的指令、腳本、來源和移除方式 | 採用／隔離試用／不採用均有依據 | `workflow-kit/extension-review.md` |
| 9 團隊品質閘門 | 為一個小 PR 指派需求、實作、review、發布責任 | 每個 gate 有負責人和可檢查證據 | `workflow-kit/team-gates.md` |
| 10 成本與模型選擇 | 用相同任務與驗收條件比較設定，保留未取得欄位為空 | 不以一次或小樣本聲稱普遍最佳模型 | `workflow-kit/usage-study.csv` |
| 11 失敗復盤 | 分析一個錯誤 exit status 的測試變異，追到可重現根因 | 預防改善能由測試或 gate 驗證 | `workflow-kit/failure-review.md` |
| 12 建立工作系統 | 組合任務卡、AGENTS、風險、handoff、測試和 review | 同伴能在練習 clone 依流程重跑並識別人工核可點 | `workflow-kit/workflow-checklist.md` |

資料列與模板是學習輔具；不要把未實際量測的時間、成本、模型表現或 review findings 填成觀察結果。工作表不是 Codex 權限設定，也不會自動批准操作。
