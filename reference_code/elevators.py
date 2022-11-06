from random import randint
elevators = [randint(-3, 30) for i in range(5)]
# print(elevators)
# elevators.sort ()
# print('Largest number is:', elevators[-1])
# bob = elevators[0]
# burger = elevators[1]
position = int(input("What floor are you on?"))
# print("Elevator 0 " + str(bob))
# print(abs(position - bob))
# print("Elevator 1 " + str(burger))
# print(abs(position - burger))
# if abs(position - bob) <= abs(position - burger):
#     print("Take elevator 0")
# else:
#     print("Take elevator 1")
low_distance = 33
elevator_index = 5
index_counter = 0
for elevator in elevators:
    distance = abs(position - elevator)
    if distance < low_distance:
        low_distance = distance
        elevator_index = index_counter
    print(distance)
    index_counter += 1
print(low_distance)
print("Take elevator " + str(elevator_index))
