# Git報告

## Git版本控制系統
#### 優點：

1.更新歷史會保存在Git，因此可以把檔案復原到以前的狀態。

<img src=''>

2.可以顯示編輯過內容的差異。

3.可以避免其他人覆蓋最新檔案，因為系統會發出警告。

#### 實做：

1.建立一個資料夾(versionControl)，並在裡面放一個txt檔(version1.txt)

<img src=''>

建立好後進行以下3步，就可以成功上傳github`
```
1.git add -A
2.git commit 
3.git push (origin main)
```
*`git add`:追蹤完所有你想要追蹤的檔案
*`git commit`: 提交
*`git commit -m "提交訊息"`: 提交並寫下提交訊息
*`git push`: 將檔案上傳

如果期間想查看狀態可以使用*`git status`
```
PS C:\Users\Owner\Desktop\110710520-3\hw\se109a\git\versionControl>git add -A
PS C:\Users\Owner\Desktop\110710520-3\hw\se109a\git\versionControl>git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   ../2.JPG
        modified:   ../READEME.md
```
