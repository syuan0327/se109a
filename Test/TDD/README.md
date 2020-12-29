# lte TDD測試(測試 → 程式)

## 實作

#### 一、測試
lte函式的功能是：
```
Checks if value is less than or equal to other.
```
lt 和 lte 比較：
```
lt是less than,
lte是 less than or equal.
```
lodash官網提供：
```
_.lte(1, 3);
// => true
 
_.lte(3, 3);
// => true
 
_.lte(3, 1);
// => false
```
測試：
```
from lte import lte

print(lte(1,3))
print(lte(3,3))
print(lte(3,1))

```
#### 二、程式
程式：
```
def lte(left,right):
    if left < right or left == right:
        return True
     
    else:
        return False
```
#### 三、測試結果
測試結果：
```
PS C:\Users\Owner\Desktop\110710520-3\hw\se109a\Test\TDD> python ./lteTest.py
True
True
False
```
