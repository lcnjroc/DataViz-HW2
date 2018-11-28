import csv
import numpy as np
import matplotlib.pyplot as plt


categories = []
men = []
women = []
goldbefore2014 = []
goldafter2014 = []
silverbefore2014 = []
silverafter2014 = []
bronzebefore2014 = []
bronzeafter2014 = []
australiaGold = []
canGold = []
australiaSilver = []
canSilver = []
australiaBronze = []
canBronze = []


with open('data/medal_data.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            print('pushing categories into seperate array')
            categories.append(row)
            line_count += 1
        else:
            yearData = row[0]
            countryData = row[4]
            genderData = row[5]
            medalData = row[7]

        	if countryData == "AUS":
        		if genderData == "Men":
                    men.append(genderData)
                else:
                    women.append(genderData)

                if medalData == "Gold":
                    if int(yearData) < 2014:
                        goldbefore2014.append(medalData)
                    else:
                        goldafter2014.append(medalData)

                if medalData == "Silver":
                    if int(yearData) < 2014:
                        silverbefore2014.append(medalData)
                    else:
                        silverafter2014.append(medalData)

                if medalData == "Bronze":
                    if int(yearData) < 2014:
                        bronzebefore2014.append(medalData)
                    else:
                        bronzeafter2014.append(medalData)

            if medalData == "Gold":
                if countryData == "AUS":
                    australiaGold.append(medalData)
                if countryData == "CAN":
                    canadaGold.append(medalData)

            if medalData == "Silver":
                if countryData == "AUS":
                    australiaSilver.append(medalData)
                if countryData == "CAN":
                    canadaSilver.append(medalData)

            if medalData == "Bronze":
                if countryData == "AUS":
                    australiaBronze.append(medalData)
                if countryData == "CAN":
                    canadaBronze.append(medalData)

            line_count += 1

print('processed', line_count, 'lines of data')
# print(categories)
print("AUS Gold before and after")
goldbefore = goldbefore2014.count("Gold")
print(goldbefore)
goldafter = goldafter2014.count("Gold")
print(goldafter)

print("AUS Silver before and after")
silverbefore = silverbefore2014.count("Silver")
print(silverbefore)
silverafter = silverafter2014.count("Silver")
print(silverafter)

print("AUS Bronze before and after")
bronzebefore = bronzebefore2014.count("Bronze")
print(bronzebefore)
bronzeafter = bronzeafter2014.count("Bronze")
print(bronzeafter)

print("Men vs Women")
print(men.count("Men"))
print(women.count("Women"))

print("AUS vs CAN Gold")
print(australiaGold.count("Gold"))
print(canadaGold.count("Gold"))

print("AUS vs CAN Silver")
print(australiaSilver.count("Silver"))
print(canadaSilver.count("Silver"))

print("AUS vs CAN Bronze")
print(australiaBronze.count("Bronze"))
print(canadaBronze.count("Bronze"))

#print("AUS before and after Gold %")
totalGold = goldafter2014.count("Gold") + goldbefore2014.count("Gold")
#goldBefore_percent = goldbefore2014.count("Gold") / totalGold * 100
# print(goldBefore_percent)
#goldAfter_percent = 100 - goldBefore_percent
# print(goldAfter_percent)

#print("AUS before and After Silver %")
totalSilver = silverafter2014.count("Silver") + silverbefore2014.count("Silver")
#silverBefore_percent = silverbefore2014.count("Silver") / totalSilver * 100
# print(silverBefore_percent)
#silverAfter_percent = 100 - silverBefore_percent
# print(silverAfter_percent)

#print("AUS before and after Bronze %")
totalBronze = bronzeafter2014.count("Bronze") + bronzebefore2014.count("Bronze")
#bronzeBefore_percent = bronzebefore2014.count("Bronze") / totalBronze * 100
# print(bronzeBefore_percent)
#bronzeAfter_percent = 100 - bronzeBefore_percent
# print(bronzeAfter_percent)

print("AUS Men vs Women %")
totalGender = men.count("Men") + women.count("Women")
men_percent = men.count("Men") / totalGender * 100
print(men_percent)
women_percent = 100 - men_percent
print(women_percent)

print("AUS vs CAN Gold %")
totalG = australiaGold.count("Gold") + canadaGold.count("Gold")
australiaGold_percent = australiaGold.count("Gold") / totalG * 100
print(australiaGold_percent)
canadaGold_percent = 100 - australiaGold_percent
print(canadaGold_percent)

print("AUS vs CAN Silver %")
totalS = australiaSilver.count("Silver") + canadaSilver.count("Silver")
australiaSilver_percent = australiaSilver.count("Silver") / totalS * 100
print(australiaSilver_percent)
canadaSilver_percent = 100 - australiaSilver_percent
print(canadaSilver_percent)

print("AUS vs CAN Bronze %")
totalB = australiaBronze.count("Bronze") + canadaBronze.count("Bronze")
australiaBronze_percent = australiaBronze.count("Bronze") / totalB * 100
print(australiaBronze_percent)
canadaBronze_percent = 100 - australiaBronze_percent
print(canadaBronze_percent)

# AUS medals bar graph before and after 2014
np_medal = 3
before = (bronzebefore, silverbefore, goldbefore)
after = (bronzeafter, silverafter, goldafter)
fig, ax = plt.subplots()
index = np.arange(np_medal)
bar_width = 0.35
opacity = 0.4
error_config = {"ecolor": "0.3"}
rects1 = ax.bar(index, before, bar_width,
                alpha=opacity, color="k",
                error_kw=error_config,
                label="Before")

rects2 = ax.bar(index + bar_width, after, bar_width,
                alpha=opacity, color="g",
                error_kw=error_config,
                label="After")

ax.set_xlabel("Medals")
ax.set_ylabel("# of Medals")
ax.set_title("Australian Medals Before and After 2014")
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(("Bronze", "Silver", "Gold"))
ax.legend()

fig.tight_layout()
plt.show()

# pie chart for AUS  men vs women
labels = "Men", "Women"
sizes = [men_percent, women_percent]
colors = ["blue", "pink"]

plt.pie(sizes, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Australian Men vs Women in Olympics")
plt.xlabel("Total Men: 7 Total Women: 7")
plt.show()

# pie chart for AUS vs CAN gold medals
labels = "Australia", "CAN"
sizes = [australiaGold_percent, canadaGold_percent]
colors = ["crimson", "cyan"]

plt.pie(sizes, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Australia vs CAN Gold Medals")
plt.xlabel("Total Australia: 5 Total CAN: 315")
plt.show()

# pie chart for AUS vs CAN silver medals
labels = "Australia", "CAN"
sizes = [australiaSilver_percent, canadaSilver_percent]
colors = ["crimson", "cyan"]

plt.pie(sizes, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Australia vs CAN Silver Medals")
plt.xlabel("Total Australia: 3 Total CAN: 203")
plt.show()

# pie chart for AUS vs CAN bronze medals
labels = "Australia", "CAN"
sizes = [australiaBronze_percent, canadaBronze_percent]
colors = ["crimson", "cyan"]

plt.pie(sizes, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Australia vs CAN Bronze Medals")
plt.xlabel("Total Australia: 6 Total CAN: 107")
plt.show()
