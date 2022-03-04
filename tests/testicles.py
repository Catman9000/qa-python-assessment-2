# input1="three"
# input2="hello"
# x = len(input1)
# y = len(input2)
# if x > y:
#     print (input1)
# elif x < y:
#     print (input2)
# else:
#     print (input1 + " " + input2)

# arg1=15
# if arg1 %5 ==0 and arg1 %3 == 0:
#     print ("fizzbuzz")
# elif arg1 %5 ==0:
#     print ("buzz")
# elif arg1 %3 == 0:
#     print("fizz")
# else:
#     print ("null")

# input="hEelLoooO"
# vowels = set('aeiou')
# counter = 0
# for x in input.lower():
#     if x in vowels:
#         counter += 1
# print (counter)

# input1="Hi-There"
# my_list=[]
# for x in input1:
#     my_list.append(x*3)
# my_list2 = ''.join(my_list)
# print(my_list2)

arg1=3
x=arg1
for i in range(2,x):
    if (x % i) == 0:
        print("false")
        break
    else:
        print ("true")
        break