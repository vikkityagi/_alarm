'''v=input()

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
while l<len(list1):
    i=list1[l]
    m=0
    temp=0
    count=0
    while m<len(i):
        j=i[m]
        if j in v:
            #while count<k:
            prev_index=temp
            for key,value in d1.items():
                if value==j:
                    get_index=key
                    break


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
            print('POSOTIVE')
            count=0
        m+=1

    l+=1


'''



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

'''from collections import Counter
v=input()
v1=v
d1=Counter(v)

list1=[]
for i in range(int(input())):
    name=input()
    list1.append(name)

j1=0
ans='t'
while j1<len(list1):
    pat=list1[j1]
    d2=Counter(pat)
    for key1,value1 in d2.items():
        for key2,value2 in d1.items():
            if key1==key2:
                if value1>value2:
                    ans='f'

    if ans=='t':
        j=0
        prev_index=0
        temp=0
        get_index=0
        count=0
        while j<len(pat):
            char=pat[j]
            prev_index=temp
            get_index=v.index(char)
            v=v.replace(char,'.')
            temp=get_index
            if prev_index<=get_index:
                count+=1

            else:
                print('NEGATIVE')
                count=0
                break
            if count==len(pat):
                print('POSITIVE')
                count=0
                break

            j+=1
            v=v1
    else:
        print('NEGATIVE')
    j1+=1'''






