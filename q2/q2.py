import csv
print("*** Annual Tempurature Report for Seoul in 2022 ***")
f = open('2022_Seoul_Temp.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
header = next(data)
# print(header)
# header = next(data)
# print(header)
#헤더가 한줄만 읽는건가? 그니깐 next(data) 이게 한줄만 읽는건가 그런가보네


date = ''
max = 0.0
for row in data:
    if row[-2] == ' ':
        continue
    elif row[-1] == ' ':
        continue
    else : 
        try:
            row[-1] = float(row[-1])
            row[-2] = float(row[-2])
            if max < row[-1] - row[-2]:
                max = row[-1] - row[-2]
                date = row[0]
        except ValueError:
            continue
print("Day with the largest temperature variation:", date)
print("maximum temperature difference :", round(max,2),"Celsius")
f.close()

f = open('2022_Seoul_Temp.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
header = next(data)
# print(header)
# header = next(data)
# print(header)
#헤더가 한줄만 읽는건가? 그니깐 next(data) 이게 한줄만 읽는건가 그런가보네


date2 = ''
min = 1000.0
for row in data:
    if row[-2] == ' ':
        continue
    elif row[-1] == ' ':
        continue
    else : 
        try:
            row[-1] = float(row[-1])
            row[-2] = float(row[-2])
            if min > row[-1] - row[-2]:
                min = row[-1] - row[-2]
                date2 = row[0]
        except ValueError:
            continue
print("Day with the smallest temperature variation:", date2)
print("minimum temperature difference :", round(min,2),"Celsius")
f.close()


def main():

    print(" ")

 

if __name__ == '__main__':

 

    main()