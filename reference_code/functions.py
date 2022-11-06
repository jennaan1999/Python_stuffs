# print("What numbers do you want to add?")
# def add(a, b):
#     return a + b
#
# print(add(2,3))
def summation(num):
    results = 0
    for x in range (1, num + 1):
        results = x + results
    return results
print(summation(3))
