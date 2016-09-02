items = [5.94, 4.23, 12.99, 1.29, 7.49]
def register(cost, payment):
	item = 0;
	if(cost == 1):
		item = items[0]
	elif(cost == 2):
		item = items[1]
	elif(cost == 3):
		item = items[2]
	elif(cost == 4):
		item = items[3]
	elif(cost == 5):
		item = items[4]
	return float("{0:.2f}".format(payment - item))

def change_machine(change):
	change = float("{0:.2f}".format(change))
	if(change <= 0.0):
		return
	elif(change >= 20):
		bills = 0
		while(change >= 20):
			bills+=1
			change-=20
		print(str(bills), '$20 dollar bills')
		return change_machine(change)
	elif(change >= 10):
		bills = 0
		while(change >= 10):
			bills+=1
			change-=10
		print(str(bills), '$10 dollar bills')
		return change_machine(change)
	elif(change >= 5):
		bills = 0
		while(change >= 5):
			bills+=1
			change-=5
		print(str(bills), '$5 dollar bills')
		return change_machine(change)
	elif(change >= 1):
		bills = 0
		while(change >= 1):
			bills+=1
			change-=1
		print(str(bills), '$1 dollar bills')
		return change_machine(change)
	elif(change >= 0.25):
		coins = 0
		while(change >= .25):
			coins+=1
			change-=0.25
		print(str(coins), 'quarters')
		return change_machine(change)
	elif(change >= 0.10):
		coins = 0
		while(change >= .10):
			coins+=1
			change-=0.10
		print(str(coins), 'dimes')
		return change_machine(change)
	elif(change >= 0.05):
		coins = 0
		while(change >= .05):
			coins+=1
			change-=0.05
		print(str(coins), 'nickels')
		return change_machine(change)
	elif(change >= 0.01):
		coins = 0
		while(change >= .01):
			coins+=1
			change-=0.01
		print(str(coins), 'pennies')
		return change_machine(change)
print('Choose an item to buy')
counter = 1
for num in items:
	print(str(counter) + ')', '$' + str(num)) 
	counter+=1
item_to_buy = int(input())
print('You are choosing to buy an item worth $' + str(items[item_to_buy - 1]), 'how much are you going to pay?')
payment = float(input())
change = register(item_to_buy, payment)
print('Your change is: $' + str(change))
change_machine(change)