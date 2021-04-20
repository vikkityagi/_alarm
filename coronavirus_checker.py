


from collections import Counter
v=input()




d1=dict(enumerate(v))


list1=[]
for i in range(0,int(input())):
    person=input()
    list1.append(person.lower())

value=d1.values()
count=0
k=1
temp=0
l=0
m=0
get_index=0
prev_index=0
v1=v

while l<len(list1):
    v=v1
    i=list1[l]
    s1=Counter(i)
    m=0
    temp=0
    count=0
    while m<len(i):
        j=i[m]
        #new
       

        #here
        if j in v:
            #while count<k:
            prev_index=temp
            get_index=v.index(j)
            v=v.replace(j,'.',1)

            if get_index >= prev_index:
                count+=1
                temp=get_index
            else:
                print('NEGATIVE')
                count=0
                break
        else:
            print('NEGATIVE')
            break


        if count==len(i):
            print('POSITIVE')
            count=0
        m+=1

    l+=1




