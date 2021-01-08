# Git報告

## Git版本控制系統
#### 優點：

1.更新歷史會保存在Git，因此可以把檔案復原到以前的狀態。

<img src='https://github.com/syuan0327/se109a/blob/master/git/1.JPG'>

2.可以顯示編輯過內容的差異。

3.可以避免其他人覆蓋最新檔案，因為系統會發出警告。

#### 實做：

1.建立一個資料夾(versionControl)，並在裡面放一個txt檔(version1.txt)

<img src='https://github.com/syuan0327/se109a/blob/master/git/2.JPG'>

建立好後進行以下3步，就可以成功上傳github
```
1.git add -A
2.git commit 
3.git push (origin main)
```
`git add`:追蹤完所有你想要追蹤的檔案

`git commit`: 提交

`git commit -m "提交訊息"`: 提交並寫下提交訊息

`git push`: 將檔案上傳

如果期間想查看狀態可以使用`git status`：
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
移除資料的方法是用`git rm 要移除的檔案`，下一次提交時，該檔案將會消失而且不再被追蹤。
```
PS C:\Users\Owner\Desktop\110710520-3\hw\se109a\git\versionControl>git rm rm.txt        
rm 'git/versionControl/rm.txt'
PS C:\Users\Owner\Desktop\110710520-3\hw\se109a\git\versionControl> git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    rm.txt
```
如果你想複製github的專案到自己的電腦上，可以用`git clone`：

`註`：在clone前請先在電腦建立一個資料夾，才能把資料clone進去。

<img src='https://github.com/syuan0327/se109a/blob/master/git/4.JPG'>
圖中我建立了叫git的資料夾

`註`：這裡示範的是clone自己的網址，網址處請放自己要clone的網址。
```
git clone https://github.com/syuan0327/se109a.git
```
網址位置圖：

<img src='https://github.com/syuan0327/se109a/blob/master/git/3.JPG'>

clone完後，可用`git log`來查看歷史
```
git log
commit 3ddbd685b31e5e64459d0961f8755a48421a09ce (HEAD -> master, origin/master, origin/HEAD)
Author: syuan <syuan.jhong1989@gmail.com>
Date:   Fri Jan 8 11:05:24 2021 +0800

    samba

commit 59d5df24d2b1d794090af8b8ce8e60ea9102fe52
Author: syuan <syuan.jhong1989@gmail.com>
Date:   Fri Jan 8 11:02:18 2021 +0800

    samba

commit 2b45a27b73f41effe82cab40a8e34fb4fbaea434
Author: syuan <syuan.jhong1989@gmail.com>
Date:   Fri Jan 8 11:01:17 2021 +0800

    samba

```
最後想要分享一個我學到的好東西也就是`Git Aliases`，他可以把比較長的指令，運用別名的方式來讓我們快速打出來，
```
git config --global alias.cm commit
```
格式：
```
git config --global alias.別名 原指令名稱
```
實作：
```
PS C:\Users\Owner\Desktop\110710520-3\hw\se109a\git\versionControl> git add -A
PS C:\Users\Owner\Desktop\110710520-3\hw\se109a\git\versionControl> git cm  -m "hi"
[master a4dbbf9] hi
 1 file changed, 1 insertion(+)
```
以上就是關於Git版本控制系統的實作和筆記，還有一些實用的指令沒有一一實作，如果想要知道更多指令可以參考：[點我](https://git-scm.com/book/zh-tw/v2)