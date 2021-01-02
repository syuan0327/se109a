# add BDD(口語化的測試語法)

## 參考鏈接
https://zhuanlan.zhihu.com/p/42987110

https://www.itread01.com/p/500891.html

## 實作

#### 一、安裝behave
```
pip install behave
```
#### 二、在features資料夾下寫場景測試文件
Gherkin语言規範
```
Feature:功能名稱；
Description（可選）：描述測試中的功能。
Scenario:測試場景名稱；
Given：給出測試前提條件；
when：相當我們的測試步驟；
Then：給出期望結果。
```
add.feature
```
Feature: add two number

  Scenario: add two numbers
    Given I have two integers "first" and "second"
    When  I add the two numbers
    Then  I get the sum
```
#### 三、在steps資料夾下寫add.py
add.py
```
from behave import given, when, then
use_step_matcher('re')

@given('I have two integers "first" and "second"')
def step_impl(context):
    context.first = 5
    context.second = 10
@when('I add the two numbers')
def step_impl(context):
    context.sum = context.first + context.second
@then('I get the sum')
def step_impl(context):
    print(context.sum)
```
#### 四、測試結果
```
PS C:\Users\Owner\Desktop\110710520-3\hw\se109a\Test\BDD\features> behave add.feature
Feature: add two number # add.feature:1

  Scenario: add two numbers                        # add.feature:3  
    Given I have two integers "first" and "second" # steps/add.py:4 
    When I add the two numbers                     # steps/add.py:8 
    Then I get the sum                             # steps/add.py:11

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.000s
```
#### 五、檔案存放規則
<img src=''>
