# 第三本：工作流模板

## 本冊相容版本

本次繁體中文版相容 tag：`book3-compatible-v1`（第三冊資深編輯修訂版）。
公開配套僅包含練習素材，不包含書稿或電子書。請在新的練習目錄執行：

```bash
git clone --branch book3-compatible-v1 https://github.com/t945935/codex-cli-trilogy.git "$HOME/codex-cli-trilogy-book3"
cd "$HOME/codex-cli-trilogy-book3"
git rev-parse HEAD
```

將輸出與本書列出的完整 commit 核對，相符後再執行 `git switch -c book3-practice`。
不得以 `main` 最新版或同名分支取代本書固定的 commit。
本版保留其餘冊別既有共享程式；搜尋起始版的刻意缺陷仍應呈現 RED，參考解答與待辦參考實作則應通過其測試。

本資料夾提供可自行複製修改的空白模板、`chapter-examples.md` 全章演練卡，以及 `workflow-kit/` 衡量表、交接卡、風險評估和團隊品質閘門範本；不會自動設定 Codex 權限，也不會替使用者核准命令。

- `task-brief.md`：任務範圍、背景、驗收、限制與驗證記錄。
- `AGENTS.example.md`：示範如何描述專案慣例；不是任何專案的通用規則，使用前需依實際專案審核。
- `risk-checklist.md`：變更前、中、後檢核點。

演練方式：先依本書版別指定的 companion tag／完整 commit 核對 `git rev-parse HEAD`；未列版本或不相符時，只做書面演練，不執行程式、mutation 或 capstone。版本相符後，挑一個可丟棄的練習分支，填好任務卡，再請 Codex 先回述需求與風險，確認後才開始修改。外部服務、刪除操作、機密存取與部署等高影響動作，應採用明確人工審查流程，不以模板取代批准。
