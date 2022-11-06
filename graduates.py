import matplotlib.pyplot as plt


file = open("./data/graduates.csv", "r")
contents = file.read()
file.close()
lines = contents.split("\n")
list_of_majors = []
mean_salaries = []
# 0,3,5
for line in lines:
    entries = line.split(",")
    year = entries[0]
    if year == '"2015"':
        salary = float(entries[5].replace('"',''))
        major = entries[2].replace('"','')
        mean_salaries.append(salary)
        list_of_majors.append(major)
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(list_of_majors, mean_salaries);  # Plot some data on the axes.
plt.xticks(rotation = 90)
plt.grid()
plt.show()
