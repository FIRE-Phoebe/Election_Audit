#create an empty list.
fruits=[]
#add fruits: apple, banana, grape to it.
fruits.append('apple')
print(fruits)
fruits.append('banana')
fruits.append('grape')
print(fruits)
#insert index 2, with pear
fruits.insert(2,'pear')
print(fruits)
#remove item pear use remove function.
fruits.remove('pear')
print(fruits)
#remove banana using pop function.
fruits.pop(1)
print(fruits)

#change element in the list: replace grape to banana
fruits[1]='banana'
print(fruits)
#insert grape in the list
fruits.append('grape')
print(fruits)

#make up a dictionary with fruits.
fruits_dict={'apple':38,'banana':20,'grape':43}
#get key form dictionary
fruits_dict.keys()
print(fruits)
#get key-value pairs:
for fruit, num in fruits_dict.items():
    print(fruit,num)
for num in fruits_dict.values():
    print(num)
#create a list of dictionary:
fruits_data=[{'fruit':'watermelon', 'num_fruits':38},{'fruit':'orange', 'num_fruits':20},{'fruit':'peach', 'num_fruits':43}]
#get the list of dictionary:
for fruits_dict in fruits_data:
    print(fruits_dict)
    #use varible to get list data
for i in range(len(fruits_data)):
    print(fruits_data[i])
#use nested loop to get each value from key
for fruits_dict in fruits_data:
    for num in fruits_dict.values():
        print(num)
#get value from data:
for fruits_dict in fruits_data:
    print(fruits_dict['num_fruits'])
#get key from data:
for fruits_dict in fruits_data:
    print (fruits_dict['fruit'])


fruits_dict={'apple':343768,'banana':238790,'grape':4983753}
#using f-string literal
for fruits, num_fruits in fruits_dict.items():
    print(f'we have {num_fruits:,} {fruits} in stock.')
