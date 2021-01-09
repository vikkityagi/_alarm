# shoe stores
no_of_shoe=int(input("No of shoe into the list:"))

shoe_list = list(map(int, input('shoe sizes: ').split()))
orginal_length=len(shoe_list)
if no_of_shoe!=len(shoe_list):
    print("Shoes entry wrong")
    while orginal_length<no_of_shoe:
        length_of_shoe=len(shoe_list)
        size=int(input('Enter the shoe size: '))
        shoe_list.append(size)
        orginal_length+=1
        if orginal_length==no_of_shoe:
            break
    else:
        while orginal_length > no_of_shoe:
            length_of_shoe = len(shoe_list)
            size = int(input('Enter the shoe size you want to remove: '))
            shoe_list.remove(size)
            orginal_length -= 1
            if orginal_length == no_of_shoe:
                break

no_of_cus=int(input('No of customer: '))
total_customer=no_of_cus
while total_customer>len(shoe_list):
    print(f'I have only {len(shoe_list)} pair of shoes and you are {total_customer} person')
    add_customer=total_customer-len(shoe_list)
    total_customer-=add_customer
    break
no_of_cus=total_customer
i,total,count=0,0,0
while i<no_of_cus:
    size,price=input('Enter the shoe size with price: ').split( )
    size=int(size)
    price=int(price)
    if size in shoe_list:
        shoe_list.remove(size)
        total+=price
        i += 1
        count += 1
    else:
        print('this shoe is not availale')
        choice=input('are you purchased another shoes: ')
        if choice=='yes':
            pass
        elif choice=='no':
            i += 1
            count += 1

    if count==no_of_cus:
        break


print(total)