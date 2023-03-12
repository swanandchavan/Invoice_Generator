shoppingList = []

print('Welcome to Venus Store')
ch = str(input("Enter Object name, quantity and price. To continue press 'y', to exit press 'n': "))
while(ch == 'y') :
    ob = {}
    name = str(input('Enter object name: '))
    qty = int(input('Enter quantity: '))
    price = int(input('Enter price: '))
    ob['name'] = name
    ob['qty'] = qty
    ob['price'] = price
    ob['totalPrice'] = qty * price
    shoppingList.append(ob)
    ch = input("To continue press 'y', to exit press 'n': ")
    if(ch != 'y'):
        break

# print(shoppingList)

# create a company name and information
shop_name = 'Venus Store\n'
shop_address = 'Balewadi Phata, Baner\n'
shop_city = 'Pune\n'

# declare ending message
message = 'Thanks for shopping with us today!\n'


with open('invoice.txt', 'w') as file:
    file.write('*****************************************************\n')
    file.write(shop_name)
    file.write(shop_address)
    file.write(shop_city)
    file.write('=====================================================\n')
    file.write('Name\t\tQty\t\tPrice\t\tTotal\n')
    for val in shoppingList:
        file.writelines(f"{val['name']}\t\t{val['qty']}\t\t{val['price']}\t\t{val['totalPrice']}\n")
    file.write('=====================================================\n')
    total = []
    for v in shoppingList:
        temp = v['totalPrice']
        total.append(temp)
    file.write(f"Total amount is: {sum(total)}\n")
    file.write('=====================================================\n')
    file.write(message)
    file.write('*****************************************************')






# declare ending message
# message = 'Thanks for shopping with us today!'

# create a top border
# print('*' * 50)
#
# # print company information first using format
# print('\t\t{}'.format(company_name.title()))
# print('\t\t{}'.format(company_address.title()))
# print('\t\t{}'.format(company_city.title()))
#
# # print a line between sections
# print('=' * 50)
#
# # print out header for section of items
# print('\tProduct Name\tProduct Price')
#
# # create a print statement for each item
# print('\t{}\t\t${}'.format(product1_name.title(), product1_price))
# print('\t{}\t${}'.format(product2_name.title(), product2_price))
# print('\t{}\t\t${}'.format(product3_name.title(), product3_price))
#
# # print a line between sections
# print('=' * 50)
#
# # print out header for section of total
# print('\t\t\tTotal')
#
# # calculate total price and print out
# total = product1_price + product2_price + product3_price
# print('\t\t\t${}'.format(total))
#
# # print a line between sections
# print('=' * 50)
#
# # output thank you message
# print('\n\t{}\n'.format(message))
#
# # create a bottom border
# print('*' * 50)