class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.arr=[]
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node is not None:
            yield node
            node=node.next

    def length(self):
        node=self.head
        i=0
        while node is not None:
            i+=1
            node=node.next
        return i

    def printll(self):
        # arr=[]
        self.arr=[]
        node=self.head
        while node is not None:
            self.arr.append(node.value)
            # print(node.value,end=" ")
            node=node.next
        # print(self.arr)

    def add(self,item):
        if self.head is None:
            newNode=Node(item)
            self.head=newNode
            self.tail=newNode
            self.head.next=self.tail
            self.tail.next=None
            print('node',newNode)
        else:
            newNode=Node(item)
            node=self.head
            while node is not None:
                temp=node
                node=node.next
            self.tail=newNode
            temp.next=self.tail
            self.tail.next=None
            print('node',newNode)

    def partition(self,lb,ub):
        print(lb,ub)
        pivot_index=lb
        pivot=self.arr[pivot_index]
        start=lb
        end=ub

        while start<end:
            while self.arr[start]<=pivot:
                start+=1
                if start>end:
                    break
            while self.arr[end]>pivot:
                end-=1
                if start>end:
                    break

            if start<end:
                temp=self.arr[end]
                self.arr[end]=self.arr[start]
                self.arr[start]=temp

        if pivot>self.arr[end]:
            temp1=self.arr[end]
            self.arr[end]=pivot
            self.arr[pivot_index]=temp1
        print(self.arr)
        print(end)
        return end

    def heapsort(self,lb,ub):
        if lb<ub:
            loc=self.partition(lb,ub)
            self.heapsort(lb,loc-1)
            self.heapsort(loc+1,ub)

    def linearSearch(self,item):
        n=len(self.arr)
        for i in range(0,n):
            if item==self.arr[i]:
                return i
        return 'item does not find'

    def binarySearch(self,item,l,r):
        if l<=r:
            mid=(l+r)//2
            if self.arr[mid]==item:
                return mid
            elif self.arr[mid]>item:
                return self.binarySearch(item,l,mid-1)
            elif self.arr[mid]<item:
                return self.binarySearch(item,mid+1,r)
            return 'item does not find'

        
    def check(self):
        print('head node',self.head)
        print('head next',self.head.next)
        print('tail',self.tail)
        print('tail next',self.tail.next)

sllwqs=LinkedList()
sllwqs.add(3)
sllwqs.add(1)
sllwqs.printll()
sllwqs.add(5)
sllwqs.add(2)
sllwqs.add(78)
sllwqs.add(6)
# print('length',sllwqs.length())
sllwqs.printll()
print(sllwqs.arr)
sllwqs.heapsort(0,sllwqs.length()-1)
print('after',sllwqs.arr)
print('item is located at ',sllwqs.linearSearch(78),' place')
# print([sllwqs.arr[i] for i in range(len(sllwqs.arr))])
# print()
# sllwqs.check()
