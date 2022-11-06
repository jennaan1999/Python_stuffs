import matplotlib.pyplot as plt


file = open("crash_catalonia.csv", "r")
contents = file.read()
entries = contents.split("\n")
dictionary_data = {}
for e in entries:
    if e == "":
        continue
    if e == '"Day of Week", "Number of Crashes"':
        continue
    entry_contents = e.split(",")
    print(entry_contents)
    Day_of_week = entry_contents[0].replace('"',"")
    Number_of_crashes = int(entry_contents[1])
    dictionary_data[Day_of_week] = Number_of_crashes
# print(dictionary_data["Tuesday"])
# crash_sum = dictionary_data["Monday"] + dictionary_data["Tuesday"] + dictionary_data["Wednesday"] + dictionary_data["Thursday"] + dictionary_data["Friday"] + dictionary_data["Saturday"] + dictionary_data["Sunday"]
# average = crash_sum/7
# print(average)
crash_sum = 0
for day in dictionary_data:
    crash_sum = crash_sum + dictionary_data[day]
average = crash_sum/len(dictionary_data)
print(average)
# number_sum = 0
# for number in range(10):
#     number_sum = number_sum + number
#     print(number_sum , number)

def read_crash_catalonia_csv():
    file = open("crash_catalonia.csv", "r")
    contents = file.read()
    crash_list = []
    day_list = []
    entries = contents.split("\n")
    for e in entries:
        if "Number of Crashes" in e:
            continue
        if len(e) == 0:
            continue
        info = e.split(",")
        crash = int(info[1])
        crash_list.append(crash)
        day = info[0]
        day_list.append(day)
    return crash_list , day_list
day , crash = read_crash_catalonia_csv()
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(crash, day);  # Plot some data on the axes.
plt.xticks()
plt.show()
