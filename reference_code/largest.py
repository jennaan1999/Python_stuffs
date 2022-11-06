from random import randint
elevators = [randint(-3, 30) for i in range(2)]
# print(elevators)
# elevators.sort ()
# print('Largest number is:', elevators[-1])
bob = elevators[0]
burger = elevators[1]
position = int(input("What floor are you on?"))
print("Elevator 0 " + str(bob))
print(abs(position - bob))
print("Elevator 1 " + str(burger))
print(abs(position - burger))
if abs(position - bob) <= abs(position - burger):
    print("Take elevator 0")
else:
    print("Take elevator 1")
