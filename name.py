import re
def main(s1, s2):
    string1=''
    string2=''
    count=0
    if s1[0] == 'mr.':
        s1.pop(0)
    elif s1[0] == 'mrs':
        s1.pop(0)
    elif s1[0] == 'ms':
        s1.pop(0)
    elif s1[0] == 'shri':
        s1.pop(0)
    if s2[0] == 'mr.':
        s2.pop(0)
    elif s2[0] == 'mrs':
        s2.pop(0)
    elif s2[0] == 'ms':
        s2.pop(0)
    elif s2[0] == 'shri':
        s2.pop(0)
    for i in s1:
        string1+=i+' '
    for i in s2:
        string2+=i+' '
    string1=re.findall('[a-z]',string1)
    string2=re.findall('[a-z]',string2)
    for j in string2:
        if j in string1:
            count+=1
    if count>len(string2)-2:
        print('Match')
    else:
        print('No Match')


# Write code here
name1 = input().lower()
name2 = input().lower()
name1_list=name1.split( )
name2_list=name2.split( )

main(name1_list, name2_list)