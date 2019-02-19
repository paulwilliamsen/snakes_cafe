customer_name = input('Please enter who this order is for: ')

appetizers = ['BBQ Wings', 'Cheese plate', 'Spring Rolls', 'Sampler Platter']
entrees = ['Chicken Marsala', 'Steak Tartar', 'Tofu',
           'Chicken Strips', 'Mac and Cheese', 'Vegetarian Tacos']
desserts = ['Oreo pudding', 'Ice Cream Cake', 'Pumpkin Pie', 'Churros']
beverages = ['Coffee', 'Light Beer', 'Water', 'Mountain Dew', 'Berry Smoothie']


menu = f"""
**************************************
Welcome, {customer_name}, to  the Snakes Cafe!              
                                  
   Order by Phone (206) 818-9504  
                                  
    Please see our menu below.    
                                  
  If you need to leave a review,  
     visit www.snakescafe.com     
                                  
   To exit at any time, type "exit" 
**************************************

Appetizers
----------
{appetizers[0]}
{appetizers[1]}
{appetizers[2]}
{appetizers[3]}


Entrees
-------
{entrees[0]}
{entrees[1]}
{entrees[2]}
{entrees[3]}
{entrees[4]}
{entrees[5]}


Desserts
--------
{desserts[0]}
{desserts[1]}
{desserts[2]}
{desserts[3]}


Beverages
------
{beverages[0]}
{beverages[1]}
{beverages[2]}
{beverages[3]}
{beverages[4]}


***********************************
** What would you like to order? **
***********************************
"""
print(menu)

customer_item_total = {}
for i in appetizers:
  customer_item_total[i.upper()] = 0
for i in entrees:
  customer_item_total[i.upper()] = 0
for i in desserts:
  customer_item_total[i.upper()] = 0
for i in beverages:
  customer_item_total[i.upper()] = 0

full_order = []
customer_order = ''
customer_order_message = ''

import pdb; pdb.set_trace()


while customer_order != 'exit':
  customer_order = input('Add item to order: ').upper()
  quantity = customer_item_total[customer_order]
  quantity += 1
  customer_item_total[customer_order] = quantity
  if (customer_item_total[customer_order] == 1):
    print(f'** You have 1 order of {customer_order}.')
  else:
    print(f'** You currently have {quantity} orders of {customer_order}.')
  if customer_order != 'exit':
    full_order.append(customer_order)
  elif customer_order == 'exit':
    break
  print(full_order)
