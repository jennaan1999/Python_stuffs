import matplotlib.pyplot as plt


def deniro_average():
    file = open("deniro.csv", "r")
    contents = file.read()
    entries = contents.split("\n")
    score_sum = 0
    total_movies = 0
    for e in entries:
        if "Score" in e:
            continue
        if len(e) == 0:
            continue
        info = e.split(",")
        print(info[1])
        score = int(info[1])
        score_sum += score
        total_movies += 1
    average = score_sum/total_movies
    return average

def read_deniro_csv():
    file = open("deniro.csv", "r")
    contents = file.read()
    score_list = []
    year_list = []
    entries = contents.split("\n")
    for e in entries:
        if "Score" in e:
            continue
        if len(e) == 0:
            continue
        info = e.split(",")
        score = int(info[1])
        score_list.append(score)
        year = info[0]
        year_list.append(year)
    return score_list , year_list
scores , years = read_deniro_csv()
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(years, scores);  # Plot some data on the axes.
plt.xticks(rotation=90)
plt.show()
