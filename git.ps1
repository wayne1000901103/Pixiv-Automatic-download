# 显示当前 Git 状态
git status

# 添加所有更改到暂存区
git add .

# 获取当前日期和时间，用于提交信息
$date = Get-Date -Format "yyyy-MM-dd HH:mm"
$commitMessage = "自動提交 $date"

# 提交更改
git commit -m $commitMessage

# 检查提交是否成功
if ($?) {
    Write-Host "提交成功！"
} else {
    Write-Host "提交失败！"
    exit
}

# 推送更改到远程仓库的 main 分支
git push origin main

# 检查推送是否成功
if ($?) {
    Write-Host "推送成功！"
} else {
    Write-Host "推送失败！"
    exit
}

Write-Host "操作完成，脚本已结束。"
