# 演算法(Algorithm)
首先先來寫一個簡單的演算法，這個演算法是和操作都是在[leetcode](https://leetcode.com/explore/)上操作的，他寫完後會顯示計算時間及內存，還蠻有趣的，有興趣的可以去試看看。
## Two Sum
#### 題目
```
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
```
#### 解題思路
題目中有提到，如果兩數加起來等於target就return兩個數。

所以，首先先使用第一個迴圈尋找陣列的n1，後再使用第二個迴圈找n2，如果n1+n2=target的話，就return值，沒的話就繼續尋找。
#### 程式
```
class Solution(object):
    def twoSum(self, nums, target):
       for i in range (len(nums)):
           for j in range (i+1,len(nums)):
               if nums[i]+nums[j]==target:
                   return [i,j]
```
#### 提交結果
運行時間
<img src="https://github.com/syuan0327/se109a/blob/master/algorithm/1.JPG">

內存消耗
<img src="https://github.com/syuan0327/se109a/blob/master/algorithm/2.JPG">

#### 時間複雜度和空間複雜度分析
設有 n 個數，任取兩數為 C(n取2)=n(n-1)/2， 所以時間複雜度為 O(n²) 。而此方法所需記憶體與 n 無關， 空間複雜度為 O(1)。


接下來正式進入較難的演算法
## 煎餅排序（Pancake sorting）

指的是將大小不同的一疊煎餅按大小排序的數學問題，其中煎餅鏟子每次只能從任意位置鏟起上方全部煎餅並翻面。「煎餅數」是指給定煎餅的張數時，最壞情況下需要的最少翻面次數。煎餅排序的目標和傳統排序演算法最小化比較次數不同，因為它每次操作只允許反轉序列的字首，所以需要最小化反轉字首次數。

參考：[維基百科](https://zh.wikipedia.org/wiki/%E7%85%8E%E9%A4%85%E6%8E%92%E5%BA%8F)

## 解題思路
先找出陣列中的最大值，然後再進行翻轉，把最大值翻到最前面後，再進行反轉動作。最後結果就會完整排序。
```
以[3,2,4,1]為例，最大值為4(陣列位置2)
=>[4,2,3,1]進行翻轉 =>[1,2,3,4]
                    =>[1,3,2,4]
=>[1,3,2,4]，最大值為3(陣列位置1，最大值4以放到對的位置所以不看)
=>[3,1,2,4]進行翻轉 =>[2,1,3,4]
=>[2,1,3,4]，最大值為2，因為最大值2已在前不用翻，直接換1,2位置即可。
最後=>[1,2,3,4]
```
## 程式
```
#找出陣列中的最大值
def Max(arr,n):
    a=0
    for i in range (0,n):
        if arr[i]>arr[a]:
            a=i
    return a
#進行翻轉
def Reverse(arr,i):
    num=0
    while num < i:
        pos = arr[num]
        arr[num]=arr[i]
        arr[i]=pos
        num += 1
        i -= 1

def pancakeSort(arr,i):
    Size=i
    while Size > 1:
        maxId = Max(arr,Size)
        #print("maxid=",maxId)
        if maxId != Size-1 :
            Reverse(arr,maxId)
            #print("arr=",arr)
            Reverse(arr,Size-1)
            #print("arr2=",arr)
        Size -= 1
    print("ans=",arr)
    
arr = [3,2,4,1]
n = len(arr)
#n=4
pancakeSort(arr,n)

```
#### 提交結果
```
PS C:\Users\Owner\Desktop\110710520-3\hw\se109a\algorithm> python ./pancake_sorting.py
arr= [4, 2, 3, 1]
arr2= [1, 3, 2, 4]
arr= [3, 1, 2, 4]
arr2= [2, 1, 3, 4]
arr= [2, 1, 3, 4]
arr2= [1, 2, 3, 4]
ans= [1, 2, 3, 4]
```
#### 撰寫測試(test.py)
```
from pancake_sorting import pancakeSort
arr = [3,2,4,1]
n = len(arr)
pancakeSort(arr,n)
```
#### 時間複雜度分析
由於對時間複雜度的分析，還沒有說非常了解，所以以下的分析，是嘗試寫寫看的，如果有錯，非常歡迎指正，謝謝！

最大值：
```
def Max(arr,n):
    a=0
    for i in range (0,n):
        if arr[i]>arr[a]:
            a=i
    return a
```
for迴圈裡面的程式碼會執行n遍，因此它消耗的時間是隨著n的變化而變化的，因此表示O(n)。

翻轉：
```
def Reverse(arr,i):
    num=0
    while num < i:
        pos = arr[num]
        arr[num]=arr[i]
        arr[i]=pos
        num += 1
        i -= 1
```
這裡因為有while，省去改變位置的部分，也算一個O(n)。

也就是說在pancakeSort裡，會變成(省略較小計算)
```
def pancakeSort(arr,i):
    while Size > 1:#O(n)
        O(n)#maxId
        O(n)#reverse1
        O(n)#reverse2
```
這樣每一次迴圈做了三次O(n)，因為計算複雜度時不考慮係數，所以複雜度也是O(n)。因此再加上外迴圈的O(n)，總時間複雜度為O(n^2)。

## 參考資料
pancake sort 講解：

https://maxming0.github.io/2020/08/29/Pancake-Sorting/

https://www.geeksforgeeks.org/pancake-sorting/

時間複雜度講解：

https://ithelp.ithome.com.tw/articles/10203082

https://www.itread01.com/content/1542770709.html
