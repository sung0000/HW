# Part 1
import csv

# Part 2
cwb_filename = '107061214.csv'
data = []
header = []
test = []
i = 0
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
        data.append(row)
        i += 1

# Part 3 
for n in range(i):
    if data[n]["HUMD"] == "-99" or data[n]["HUMD"] == "-999":
        data[n]["HUMD"] = "None"
    n += 1

C0A880 = []
C0F9A0 = []
C0G640 = []
C0R190 = []
C0X260 = []
r_1 = 0
r_2 = 0
r_3 = 0
r_4 = 0
r_5 = 0
for n in range(i):
    if data[n]["station_id"] == "C0A880":
        if (data[n]["HUMD"] != 'None'):
            C0A880.append(float(data[n]["HUMD"]))
            r_1 += 1
    if data[n]["station_id"] == "C0F9A0":
        if (data[n]["HUMD"] != 'None'):
            C0F9A0.append(float(data[n]["HUMD"]))
            r_2 += 1
    if data[n]["station_id"] == "C0G640":
        if (data[n]["HUMD"] != 'None'):
            C0G640.append(float(data[n]["HUMD"]))
            r_3 += 1
    if data[n]["station_id"] == "C0R190":
        if (data[n]["HUMD"] != 'None'):
            C0R190.append(float(data[n]["HUMD"]))
            r_4 += 1
    if data[n]["station_id"] == "C0X260":
        if (data[n]["HUMD"] != 'None'):
            C0X260.append(float(data[n]["HUMD"]))
            r_5 += 1

target_data = []

if (r_1 == 0):
    ans_1 = 'None'
else:
    ans_1 = sum(C0A880)
    target_data.append(['C0A880', ans_1])

if (r_2 == 0):
    ans_2 = 'None'
else:
    ans_2 = sum(C0F9A0)
    target_data.append(['C0F9A0', ans_2])

if (r_3 == 0):
    ans_3 = 'None'
else:
    ans_3 = sum(C0G640)
    target_data.append(['C0G640', ans_3])

if (r_4 == 0):
    ans_4 = 'None'
else:
    ans_4 = sum(C0R190)
    target_data.append(['C0R190', ans_4])

if (r_5 == 0):
    ans_5 = 'None'
else:
    ans_5 = sum(C0X260)
    target_data.append(['C0X260', ans_5])

# Part. 4 print answer
print(target_data)
