# 第二冊待辦專案素材

本目錄提供第二冊功能演習的起始版與參考實作；逐章情境卡在 `../chapter-examples.md`。它們是練習素材，不是章節正文或正式產品。

## 起始版

`starter/` 是第一冊簡單待辦程式的起始版；`reference/` 是完成示例。`task-brief.template.md` 是任務卡空白範本，複製後依你的實際規則填寫。執行前確認已在獨立 Git clone 的 `book2-practice` 分支，避免改動公開來源或第一冊練習。

Linux／macOS／WSL shell，從倉庫根目錄執行：

```bash
python3 -m unittest discover -s examples/book-2/todo-project/starter -p 'test_*.py'
python3 examples/book-2/todo-project/starter/todo.py list
```

接著進入 `examples/book-2/todo-project/starter/`，先跑基線，再單獨執行功能合約測試：

```bash
python3 -m unittest discover -s . -p 'test_*.py'
python3 -m unittest -v feature_contract
```

基線應通過；第二個命令預期因 `done ID` 尚未實作而出現行為斷言失敗。若看到匯入或語法錯誤，先修測試環境，不算預期 RED。修改完成後在同一目錄重跑這兩個命令；完成練習後可在 `reference/` 目錄執行相同的 `feature_contract` 模組，核對 GREEN。

初始資料是兩筆字串。第二冊功能案例逐步把它轉為 schema version 2：

```json
{
  "schema_version": 2,
  "tasks": [
    {"id": 1, "text": "Review API design", "completed": false}
  ]
}
```

新格式必須是 version 2 且每筆只含 `id`、`text`、`completed`；未知欄位會被拒絕，避免遷移時無聲丟失資料。練習要求：穩定 ID、`done ID` 狀態更新、未知／無效 ID 不改資料、重複完成可安全重跑、`list --open` 只列未完成項目。`starter/feature_contract.py` 包含功能合約測試，不符合 `test_*.py` 的基線發現模式；在 `starter/` 目錄可單獨跑它來看新需求 RED。參考實作中有相同合約測試，可驗證 GREEN。舊字串陣列需遷移時，保留項目文字和順序；損壞或不支援的資料格式必須報錯且不可覆寫原始檔。先看懂合約測試，再改程式。

## 參考實作

`reference/` 展示一種可能的完成方式，包含舊格式遷移、輸入檢查和測試。完成練習後，從倉庫根目錄執行：

```bash
cd examples/book-2/todo-project/reference
python3 -m unittest discover -s . -p 'test_*.py'
python3 -m unittest -v feature_contract
python3 todo.py list --open
```

參考實作不代表唯一解法；你應比較資料契約、錯誤行為與測試，不需逐行複製。程式以本機 JSON 教學，未處理多程序同時寫入、崩潰安全的原子更新或正式備份，不能用於重要資料。

## 除錯案例

`../search_tasks.py` 刻意保留大小寫搜尋缺陷；依 `../README.md` 先看 RED 測試，再修正自己的副本，最後和 `../solution_search_tasks.py` 對照。除錯案例和待辦功能專案分開執行，避免一項練習污染另一項資料。
