---

# 🖼️ Pixiv Automatic Downloader  

🚀 **Pixiv Automatic Downloader** 是一款 Windows 桌面應用程式，可自動下載 Pixiv 用戶的所有作品！  
透過簡單的 GUI 介面，只需提供 **Pixiv 用戶 ID** 和 **PHPSESSID**，即可開始下載，不需要手動操作。 
---

## 📥 下載與安裝  

### **🔗 下載連結**
👉 **[點此下載最新版本](https://github.com/wayne1000901103/Pixiv-Automatic-download/releases)**  

💻 **支援系統**：Windows 10 / 11（無需額外安裝 Python）

---

## 🎯 功能特色  

✔ **全自動下載**：只需輸入 Pixiv 用戶 ID，立即下載該用戶的所有作品  
✔ **簡單 GUI 介面**：無需命令行，適合所有用戶  
✔ **PHPSESSID 登入**：模擬 Pixiv 帳號登入，獲取所有公開作品
✔ **下載記錄保存**：避免重複下載，節省流量  
✔ **暫停 / 恢復下載**：可隨時暫停或繼續，不怕中斷  
✔ **批量下載**：支援一次下載多個 Pixiv 用戶的作品  

---

## 🔧 使用方法  

### **1️⃣ 準備必要檔案**  

🔹 **Pixiv 用戶 ID 檔案**（`pixiv_user_ids.txt`）  
用記事本建立一個 `.txt` 檔案，每行填入一個用戶 ID，例如：  
```
12345678
87654321
13579246
```

🔹 **PHPSESSID 檔案**（`phpseSSID.txt`）  
用戶需提供有效的 Pixiv **PHPSESSID**，以便程式登入下載圖片。  
```
100087303_546463247147216946574
```
**如何獲取 PHPSESSID？**  
1. 登入 [Pixiv](https://www.pixiv.net/)  
2. 按 **F12** 開啟「開發者工具」→ 選擇「Application」→ Cookies  
3. 找到 `PHPSESSID`，複製其值，並存入 `phpseSSID.txt`  

---

### **2️⃣ 開始下載**  

1. **打開 `pixiv_downloader.exe`**  
2. **選擇 `pixiv_user_ids.txt`** 和 `phpseSSID.txt`  
3. 點擊 **「開始下載」**  
4. 圖片將會自動儲存至：  
   ```
   C:\Users\你的使用者名稱\Pictures\Pixiv_Downloads\用戶ID\作品ID.jpg
   ```

---

## ❓ 常見問題  

### **Q1. 為什麼下載失敗？**
- 確保 `phpseSSID.txt` 內容正確，且沒有過期  
- 檢查網路連線是否正常  
- 確保目標用戶的作品是公開的  

### **Q2. 如何避免重複下載？**
- 下載記錄儲存在 `downloaded.json`，程式會自動跳過已下載的圖片  

### **Q3. 我可以下載 R-18 作品嗎？**
- 可以，但你的 Pixiv 帳號需要開啟 **R-18 顯示選項**，否則 API 可能無法獲取  

---

## ⚠️ 注意事項  

⚠️ **本工具僅供學習與個人使用，請勿用於商業或非法用途！**  
⚠️ **請尊重 Pixiv 及創作者的版權，下載作品後請勿二次發布或商業使用！**  

---

## ❤️ 支持與貢獻  

如果你覺得這個工具有幫助，請幫忙 **Star ⭐** 此專案！  
有任何建議或問題，歡迎提交 **Issues** 或發送 **Pull Requests**！  

📌 **GitHub 專案**：👉 [Pixiv-Automatic-download](https://github.com/wayne1000901103/Pixiv-Automatic-download)  

---
