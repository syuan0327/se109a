# lt傳統測試(程式 → 測試)

## 實作

#### 一、程式
lt函式的功能是：
```
Checks if value is less than other
```
第一版程式：
```
def lt(left,right):
    if left < right:
        return true
    else:
        return false
```
#### 二、測試
lodash官網提供：
```
_.lt(1, 3);
// => true
 
_.lt(3, 3);
// => false
 
_.lt(3, 1);
// => false
```
測試程式：
```
from lt import lt

print(lt(1,3))
print(lt(3,3))
print(lt(3,1))
```
#### 三、測試結果
第一版測試結果：
```
 python ltTest.py
Traceback (most recent call last):
  File "ltTest.py", line 3, in <module>
    print(lt(1,3))
  File "C:\Users\Owner\Desktop\110710520-3\hw\se109a\Test\traditional\lt.py", line 3, in lt
    return true
NameError: name 'true' is not defined
```
第二版程式(修改第一版的程式)：
```
def lt(left,right):
    if left < right:
        return True
    else:
        return False
```
第二版測試結果：
```
PS C:\Users\Owner\Desktop\110710520-3\hw\se109a\Test\traditional> python ltTest.py
True
False
False
```

