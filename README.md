Pixiv 用戶作品下載器

這是一個 Python 應用程式，能夠自動下載 Pixiv 用戶的所有公開作品。

特色功能

✅ 自動下載 Pixiv 用戶的所有作品
✅ 支援 PHPSESSID 登入（無需 API）
✅ 下載到 Windows 的圖片資料夾
✅ 支援暫停 / 恢復下載
✅ 避免重複下載
✅ 下載未完成時暫停，會自動刪除該圖片

📥 安裝與運行

1. 安裝 Python（若尚未安裝）

請前往 Python 官網 下載並安裝 Python。

2. 安裝必要的函式庫

在命令提示字元（CMD）或 PowerShell 中執行：

pip install requests tkinter

3. 準備 PHPSESSID 與用戶 ID 檔案

取得 PHPSESSID

登入 Pixiv 網站。

在瀏覽器開發者工具 (F12) > 應用程式 (Application) > 儲存的 Cookie (Cookies) > pixiv.net，找到 PHPSESSID。

將 PHPSESSID 複製到一個文字檔案（例如 phpsessid.txt）。

建立用戶 ID 檔案

在 Pixiv 找到你想下載的用戶。

用戶 ID 在網址中，例如 https://www.pixiv.net/users/12345678，則 用戶 ID 為 12345678。

將所有用戶 ID 存入 user_ids.txt，每行一個 ID。

🚀 使用方法

運行程式

python pixiv_downloader.py

選擇 phpsessid.txt 檔案。

選擇 user_ids.txt 檔案。

下載將自動開始！

📌 可隨時按「暫停下載」，未完成的圖片會自動刪除。

📂 下載位置

所有圖片將會下載到 Windows 圖片 資料夾內，

範例：

C:\Users\你的名稱\Pictures\Pixiv_Downloads\用戶ID\

⚠ 注意事項

本工具僅用於個人備份 Pixiv 作品，請勿用於非法用途。

若 PHPSESSID 失效，請重新取得新的 PHPSESSID。

建議不要頻繁下載，以免被 Pixiv 暫時封鎖。
