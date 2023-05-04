import csv
f = open('q1.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
header = next(data)
# print(header)
# header = next(data)
# print(header)
#헤더가 한줄만 읽는건가? 그니깐 next(data) 이게 한줄만 읽는건가 그런가보네
print("*** Annual Tempurature Report for Seoul in 2022 ***")

n = 0.0
totaldhseh = 0
for row in data:
    if row[-3] == ' ':
        continue
    else : 
        row[-3] = float(row[-3])# 평균기온
        totaldhseh += row[-3]
        n+=1
print("Average Temperature:",round((totaldhseh/n),2), "Celsius")
f.close()

f = open('q1.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
header = next(data)

    
n2 = 0.0
totaldhseh2 = 0
for row in data:
    if row[-2] == ' ':
        continue
    else : 
        try:
            row[-2] = float(row[-2])# 평균기온
            totaldhseh2 += row[-2]
            n2 = n2 + 1
        except ValueError:
            continue
print("Average Minimun Temperature:",round((totaldhseh2/n2),2), "Celsius")
    
f.close()
        

f = open('q1.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
header = next(data)

    
n3 = 0.0
totaldhseh3 = 0
for row in data:
    if row[-1] == ' ':
        continue
    else : 
        try:
            row[-1] = float(row[-1])# 평균기온
            totaldhseh3 += row[-1]
            n3 = n3 + 1
        except ValueError:
            continue
print("Average Maximum Temperature:",round((totaldhseh3/n3),2), "Celsius")
    
f.close()


def main():

    print(" ")

 

if __name__ == '__main__':

 

    main()