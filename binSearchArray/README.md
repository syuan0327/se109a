#### 程式
```
function bsearch(a, o, from, to) {
    while(from<=to)
    {
        var mid = Math.floor((from + to)/2)
        if (a[mid] === o)
           return mid
        else
        {
           if(o<a[mid])
              to=mid-1;
              //return bsearch(a, o, 0, mid-1)
           else//o > a[mid]
              from=mid+1;
              //return bsearch(a, o, mid+1, to)
        }
    }
  }
function search(a, o) {
    var n = a.length
    return bsearch(a, o, 0, n)
}
```
#### 測試資料
```
var t = search([1, 3, 4, 6, 7, 8], 4)
console.log('t=', t)
var t = search([1, 3, 4, 6, 7, 8], 5)
console.log('t=', t)
var t = search([1, 3, 4, 6, 7, 8], 8)
console.log('t=', t)
var t = search([1, 3, 4, 6, 7, 8], 9)
console.log('t=', t)
```
  
#### 執行結果
<img src="https://github.com/syuan0327/se109a/blob/master/binSearchArray/loop.JPG?raw=true">
