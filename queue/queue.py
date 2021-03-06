class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

# 印出list中的所有資料
    def PrintList(self): 
        arr = self.head
        while arr != None:
            print(arr.value, end=' ')
            arr = arr.next
        print()

# dequeue：取出佇列前端之資料
    def dequeue(self): 
        pop = self.head
        if pop == None:
            print("List is empty.")
        else:
            self.head = pop.next
            pop = None
        self.size -= 1
# enqueue：將資料放入佇列尾端
    def enqueue(self, data): 
        NewNode = ListNode(data)
        if self.head == None:
            self.head = NewNode
        else:
            push = self.head
            while(push.next != None):
                push = push.next
            push.next = ListNode(data)
            self.size += 1

if __name__ == '__main__': # 檔案被import時，不執行main()函式

    list = LinkedList()
    list.enqueue(2)
    list.enqueue(4)
    list.enqueue(6)
    list.PrintList()
    list.dequeue()
    list.PrintList()
    list.enqueue(19)
    list.PrintList()
    list.dequeue()
    list.PrintList()