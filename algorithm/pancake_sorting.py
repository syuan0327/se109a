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
        print("maxid=",maxId)
        if maxId != Size-1 :
            Reverse(arr,maxId)
            print("arr=",arr)
            Reverse(arr,Size-1)
            print("arr2=",arr)
        Size -= 1
    print("ans=",arr)
    
arr = [3,2,4,1]
n = len(arr)
#n=4
pancakeSort(arr,n)


