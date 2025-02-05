import os
import requests
import json
import time
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
import winreg

# 取得使用者的「圖片」資料夾
def get_pictures_folder():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders")
        pictures_path, _ = winreg.QueryValueEx(key, "My Pictures")
        winreg.CloseKey(key)
        return os.path.expandvars(pictures_path)
    except:
        return os.path.join(os.path.expanduser("~"), "Pictures")

# 設定下載路徑
BASE_DOWNLOAD_FOLDER = os.path.join(get_pictures_folder(), "Pixiv_Downloads")
os.makedirs(BASE_DOWNLOAD_FOLDER, exist_ok=True)

# 下載紀錄檔案
DOWNLOAD_HISTORY_FILE = os.path.join(BASE_DOWNLOAD_FOLDER, "downloaded.json")

# 全域變數
is_paused = False
download_thread = None
current_downloading_file = None  # 記錄當前下載的圖片檔案

# 讀取已下載的圖片紀錄
def load_download_history():
    if os.path.exists(DOWNLOAD_HISTORY_FILE):
        with open(DOWNLOAD_HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# 儲存已下載的圖片紀錄
def save_download_history(history):
    with open(DOWNLOAD_HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)

# 取得用戶的所有作品 ID
def get_user_illusts(user_id, phpsessid):
    headers = {"Referer": f"https://www.pixiv.net/users/{user_id}", "User-Agent": "Mozilla/5.0"}
    cookies = {"PHPSESSID": phpsessid}
    
    url = f"https://www.pixiv.net/ajax/user/{user_id}/profile/all?lang=zh"
    response = requests.get(url, headers=headers, cookies=cookies)
    
    if response.status_code != 200:
        return []
    
    data = response.json()
    return list(data.get("body", {}).get("illusts", {}).keys())

# 下載 Pixiv 圖片
def download_pixiv_image(image_id, user_id, phpsessid, history):
    global is_paused, current_downloading_file
    headers = {"Referer": f"https://www.pixiv.net/artworks/{image_id}", "User-Agent": "Mozilla/5.0"}
    cookies = {"PHPSESSID": phpsessid}

    url = f"https://www.pixiv.net/ajax/illust/{image_id}?lang=zh"
    response = requests.get(url, headers=headers, cookies=cookies)
    
    if response.status_code != 200:
        return
    
    data = response.json()
    image_url = data.get("body", {}).get("urls", {}).get("original")
    if not image_url:
        return

    user_folder = os.path.join(BASE_DOWNLOAD_FOLDER, str(user_id))
    os.makedirs(user_folder, exist_ok=True)
    filename = os.path.join(user_folder, f"{image_id}.jpg")

    # 跳過已下載的圖片
    if image_id in history.get(str(user_id), []):
        print(f"跳過已下載: {filename}")
        return

    # 記錄目前正在下載的圖片
    current_downloading_file = filename

    # 下載圖片
    img_response = requests.get(image_url, headers=headers, cookies=cookies, stream=True)
    if img_response.status_code == 200:
        with open(filename, "wb") as f:
            for chunk in img_response.iter_content(1024):
                if is_paused:
                    f.close()
                    os.remove(filename)  # 刪除未完成的圖片
                    print(f"下載暫停，刪除未完成的圖片: {filename}")
                    return
                f.write(chunk)

        print(f"已下載: {filename}")

        # 更新下載紀錄
        if str(user_id) not in history:
            history[str(user_id)] = []
        history[str(user_id)].append(image_id)
        save_download_history(history)

    # 下載完成後，清除記錄
    current_downloading_file = None

# 暫停 / 恢復按鈕邏輯
def toggle_pause():
    global is_paused, current_downloading_file
    is_paused = not is_paused
    pause_button.config(text="恢復下載" if is_paused else "暫停下載")

    # 如果有未完成的下載，則刪除
    if is_paused and current_downloading_file and os.path.exists(current_downloading_file):
        os.remove(current_downloading_file)
        print(f"下載暫停，刪除未完成的圖片: {current_downloading_file}")
        current_downloading_file = None

# 開始下載
def start_download():
    global download_thread
    if download_thread and download_thread.is_alive():
        messagebox.showwarning("提示", "下載進行中，請勿重複開始")
        return

    phpsessid_file = filedialog.askopenfilename(title="選擇 PHPSESSID 檔案")
    if not phpsessid_file:
        return
    with open(phpsessid_file, "r", encoding="utf-8") as f:
        phpsessid = f.read().strip()

    users_file = filedialog.askopenfilename(title="選擇 Pixiv 用戶 ID 檔案")
    if not users_file:
        return
    with open(users_file, "r", encoding="utf-8") as f:
        user_ids = [line.strip() for line in f.readlines() if line.strip().isdigit()]

    if not user_ids:
        messagebox.showerror("錯誤", "無效的用戶 ID 檔案")
        return

    def download_task():
        global is_paused
        history = load_download_history()

        for user_id in user_ids:
            print(f"獲取用戶 {user_id} 的作品...")
            illusts = get_user_illusts(user_id, phpsessid)
            if not illusts:
                print(f"用戶 {user_id} 無作品")
                continue

            for illust_id in illusts:
                while is_paused:
                    time.sleep(1)  # 暫停時等待
                download_pixiv_image(illust_id, user_id, phpsessid, history)
                time.sleep(1)  # 避免封鎖

        messagebox.showinfo("完成", "所有圖片下載完成")

    # 使用執行緒執行下載
    download_thread = threading.Thread(target=download_task)
    download_thread.start()

# 建立 UI
window = tk.Tk()
window.title("Pixiv 用戶作品下載器")

start_button = tk.Button(window, text="開始下載", command=start_download)
start_button.pack(pady=10)

pause_button = tk.Button(window, text="暫停下載", command=toggle_pause)
pause_button.pack(pady=10)

window.mainloop()
