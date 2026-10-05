# 第一本：入門練習素材

本資料夾配合入門書，提供一個刻意保持簡單的 Python 待辦 CLI。逐章素材索引見 `chapter-examples.md`。先讓 Codex 說明程式做什麼，再要求只新增一項小功能；每次都檢查 diff。

## 執行起始版本測試

需要 Python 3。於此資料夾執行：

```bash
python3 starter/todo.py list
python3 -m unittest discover -s starter -p 'test_*.py'
```

程式資料存在 `starter/todos.json`，初始為空。`todos.json` 僅為練習資料；請勿放入私人資訊。

## 練習任務

1. 讀取 `starter/todo.py`，用自己的話描述目前支援的命令與資料格式，不先改檔。
2. 請 Codex 新增 `add` 命令：接受一段待辦文字、存入 JSON，且不覆蓋既有待辦。
3. 檢查改動是否只涉及必要檔案，新增成功與空白文字兩種測試。
4. 執行測試；若失敗，將完整錯誤訊息交給 Codex，請它先解釋再修正。

成功條件：待辦可新增並列出；空白輸入不建立資料；既有資料不被清除；所有測試通過。不同實作可以接受，只要符合條件。

## 參考解答（完成練習後再看）

`solution/` 提供一種可能的實作及測試。先嘗試自行完成，再執行：

```bash
python3 -m unittest discover -s solution -p 'test_*.py'
python3 solution/todo.py add "Example task"
python3 solution/todo.py list
```

參考解答包含空白輸入及損壞 JSON 的保護；它只是教學範例，不是完整正式產品。

提示詞起點：

> 先閱讀 `starter/todo.py` 和測試，先不要修改。請指出資料流、目前行為及你需要確認的假設。等我確認後，只實作「新增待辦」功能，保留現有資料格式，補上成功與空白輸入測試。完成後說明改了哪些檔案、如何驗證，以及尚未處理的限制。

此提示詞是教材起點，請依自己的需求調整；並非 Codex 的固定語法。
