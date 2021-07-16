'''import time
class Resturant_management:

    def __init__(self,count,dictionary,_list):
        self.count=count
        self.dictionary=dictionary
        self._list=_list
    def available_food(self):
        print('which item did you Puchase  in resturant')
        time.sleep(2)
        print('first name of the item iind is quantity of item iiird individual price')
        time.sleep(2)
        print('for example...name=thumbs up,quantity=5,price=10')
        time.sleep(2)


        ans='+'

        while ans=='+':
            name, quantity = input(), int(input())
            price=list(map(int,input().split()))
            self.dictionary[self.count]=[str(quantity)+name,price]
            self.count+=1
            print('press +/-')
            ans=input()
            if ans=='-':
                return self.dictionary
    def total_food(self):
        for i,j in self.dictionary.items():
            for k in range(len(j)-1):
                print(i,'item is '+j[k]+' :',end='')
                print(sum(j[k+1]))

    def total_bill(self):
        for key,value in self.dictionary.items():
            for i in value[1]:
                self._list.append(i)
        return sum(self._list)


cus1=Resturant_management(1,{},[])
cus1.available_food()
cus1.total_food()
time.sleep(1)
print('your bills : '+ str(cus1.total_bill()))'''
import time
class Resturant_management:
    #price=[0]
    def __init__(self,item_dictionary,count=0):
        self.item_dictionary=item_dictionary
        self.count=count
    def available_item(self):

        print('Available item in the ')
        if bool(self.item_dictionary):
            print('item name', '  Quantity', '   price')
            for key,value in self.item_dictionary.items():

                for i in range(len(value)-2):
                    print(key,'     ',value[0],',',value[1],',',value[2])

        else:
            print('no item')

    def add_item(self):
        temp='yes'
        while temp=='yes':
            print('which item do you want to add')
            print('Item Name')
            name=input()
            print('Quantity')
            quantity=int(input())
            print('price')
            price1=list(map(int, input().split()))
            data=[name,quantity,price1]


            self.item_dictionary[self.count]=data
            self.count += 1
            temp=input('do you want to add more item?')




    def delete_item(self):
        print('which item you want to delete?')
        time.sleep(1)

        temp1=0
        temp2='yes'
        while temp2=='yes':
            quantity = int(input('quantity?'))
            name = input('name of the item?')
            price2 = list(map(int, input('price?').split()))
            for key,value in self.item_dictionary.items():

                if name in value:
                    check=all(item in value[2] for item in price2)
                    if check is True:

                        if quantity>value[1]:
                            print(f'Sorry! we have only {value[1]} item, you can delete only {value[1]} item.')
                        elif quantity<=value[1]:
                            for i in price2:
                                value[2].remove(i)
                            new_value=value[2]
                            remain_itemquantity=value[1]-quantity
                            if remain_itemquantity>0:

                                self.item_dictionary[key]=[name,remain_itemquantity,new_value]
                            else:
                                self.item_dictionary[key] = [0, remain_itemquantity, 0]
                            temp=1
                    else:
                        print('you have not this items.')

                if temp1==1:
                    break
            temp2=input('do you want to delete more item?')
            
    def replace_item(self):
        print('which item do you want to replace?')
        name1=input('old name?')
        quantity1=int(input('old quantity?'))
        price3=list(map(int,input('old price?').split()))
        ans='yes'
        while ans=='yes':
            temp1=0
            # first of all delete old item
            for key, value in self.item_dictionary.items():

                if name1 in value:
                    check = all(item in value[2] for item in price3)
                    if check is True:

                        if quantity1 > value[1]:
                            print(f'Sorry! we have only {value[1]} item, you can delete only {value[1]} item.')
                        elif quantity1 <= value[1]:
                            for i in price3:
                                value[2].remove(i)
                            new_value1 = value[2]
                            remain_itemquantity1 = value[1] -quantity1
                            if remain_itemquantity1 > 0:

                                self.item_dictionary[key] = [name1, remain_itemquantity1, new_value1]
                            else:
                                self.item_dictionary[key] = [0, remain_itemquantity1, 0]
                            temp1 = 1
                    else:
                        print('you have not this items.')

                if temp1 == 1:
                    break
            print(f'which item you want to replace with {quantity1} {name1}')
            temp = 'yes'
            while temp == 'yes':
                print('which item do you want to add')
                print('Item Name')
                name = input()
                print('Quantity')
                quantity = int(input())
                print('price')
                price1 = list(map(int, input().split()))
                data = [name, quantity, price1]

                for key, value in self.item_dictionary.items():
                    if name in value:
                        quantity = value[1] + quantity
                        for i in price1:
                            value[2].append(i)
                        self.item_dictionary[key] = [name, quantity, value[2]]
                        break


                temp = 'no'
            ans=input('do you want to replace more item?')

    def get_item(self,get_item_dictionary,count2):
        temp='yes'
        while temp=='yes':
            if bool(self.item_dictionary):
                print('item name', '  Quantity', '   price')
                for key,value in self.item_dictionary.items():

                    for i in range(len(value)-2):
                        print(key,'     ',value[0],',',value[1],',',value[2])

            else:
                print('no item')
                break

            print('which item do you want to buy:')

            item_name = input('item name?')
            for key,value in self.item_dictionary.items():

                if item_name in value:
                    quantity = int(input('quantity?'))
                    if quantity<=value[1]:
                        remain_quantity=value[1]-quantity
                        price = list(map(int, input('price? ').split()))

                        check = all(item in value[2] for item in price)
                        if check is True:
                            get_item_dictionary[count2] = [item_name, quantity, price]
                            for i in price:
                                value[2].remove(i)
                            self.item_dictionary[key]=[item_name,remain_quantity,value[2]]
                            count2+=1
                            break
                        else:
                            print(f'something has wrong')
                    else:
                        print(f'we have only {value[1]} items.')
                        break


            temp=input('do you purchase more item?')
    def check_item(self):
        print('which item you want to check?')
        item_name=input()
        for key,value in self.item_dictionary.items():
            if item_name in value:
                quantity=value[1]
                print(f'yes we have {quantity} {item_name}')
                break
    def total_item(self):
        print('which item you did purchase.')
        for key,value in get_item_dictionary.items():
            print(key,'   ',value)
    def total_payment(self):
        sum1=0
        print('your total bill:')
        time.sleep(1)
        for key,value in get_item_dictionary.items():
            sum1+=sum(value[2])
        print(sum1)








'''name1,quantity1,price1='Thumbs up',5,20
        name2,quantity2,price2='Red up',5,20
        name3,quantity3,price3='7 up',5,20
        name4,quantity4,price4='corona',5,20
        name5,quantity5,price5='Budweiser',5,20
        name6,quantity6,price6='Heogaarader',5,20
        name7,quantity7,price7='Heineken',5,20

        name8,quantity8,price8='Chicken rogan josh Biryani',5,20
        name9,quantity9,price9='Butter chicken Biryani',5,20
        name10,quantity10,price10='Chicken Tikka Masala Biryani',5,20
        name11,quantity11,price11='Chicken Bhuna Biryani',5,20
        name12,quantity12,price12='Chicken Hyderabadi Biryani',5,20
        name13,quantity13,price13='Chicken Dum Biryani',5,20
        name14,quantity14,price14='Chicken kadhai Biryani',5,20
        name15, quantity15,price15= 'Bira', 5, 20'''
item_dictionary={0:[0]}

cus1=Resturant_management(item_dictionary)
cus1.add_item()
#cus1.available_item()
#cus1.delete_item()
#cus1.available_item()
#cus1.replace_item()
get_item_dictionary={0:[0]}
cus1.get_item(get_item_dictionary,0)
#cus1.check_item()

cus1.total_item()
cus1.total_payment()


'''d={0:[1]}
name=input()
for key,value in d.items():
    if name in value:
        print('yes')
    else:
        print('no')'''