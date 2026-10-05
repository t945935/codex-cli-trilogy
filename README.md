# Codex CLI Trilogy｜讀者範例

這是《Codex CLI 入門／實例演習／聰明用》的公開讀者服務倉庫，提供可下載的練習素材、範例專案、提示模板與自我檢核表；不提供完整章節、未公開稿件或電子書檔。

倉庫：https://github.com/t945935/codex-cli-trilogy

## 取得方式

有 Git：

```bash
git clone https://github.com/t945935/codex-cli-trilogy.git
cd codex-cli-trilogy
```

不使用 Git：開啟 GitHub 頁面，選 Code → Download ZIP，解壓後進入 `examples/`。

## 從哪裡開始

- 第一本《Codex CLI 入門》：`examples/book-1/`，從 `starter/` 開始；`chapter-examples.md` 有全章練習卡，`solution/` 是完成後再對照的參考實作。
- 第二本《Codex CLI 實例演習》：`examples/book-2/`，`chapter-examples.md` 覆蓋各章演習；以刻意保留缺陷的搜尋範例練習重現、修正，並可用獨立參考解答核對。`todo-project/` 提供延續第一冊的功能案例起始版和參考實作。
- 第三本《Codex CLI 聰明用》：`examples/book-3/`，`chapter-examples.md` 提供各章情境卡，並有任務提示模板、專案指引範本及安全檢核表。

各資料夾的 README 說明練習目標及執行方式。範例是教學素材，不代表適用於所有正式專案；執行前請先閱讀檔案與指令，並在自己的練習副本操作。

## 注意

Codex CLI 的安裝、登入、指令、旗標及功能會更新。請以 OpenAI 官方文件為準：
- https://developers.openai.com/codex/cli
- https://developers.openai.com/codex/cli/reference

本倉庫不要求讀者提交憑證、API 金鑰或私人專案內容。練習中若 Codex 建議執行會刪除資料、連線外部服務或改動練習目錄以外檔案的命令，先停下來確認影響。
