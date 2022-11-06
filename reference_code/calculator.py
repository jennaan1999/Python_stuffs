# number1 = 3
# number2 = 7
# print (number1 + number2)
# print (number2 - number2)
# print (number1 * number2)
# print (number2 / number1)
# print (number2 // number1)
# print (number2 ** number1)
# word = input()
# print(word.split("o"))
# 3 * 4
# 5 / 2
variable = input("what do you want to calculate?")
lists = (variable.split())
no1 = int(lists[0])
no2 = int(lists[2])
operation = lists[1]
if operation == "+":
    result = no1 + no2
if operation == "-":
    result = no1 - no2
if operation == "*":
    result = no1 * no2
if operation == "/":
    result = no1 / no2
print(result)
