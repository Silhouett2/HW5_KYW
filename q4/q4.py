import csv
f = open('q4.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
header = next(data)


print("*** Subway Report for Seoul on March 2023 ***")

ghtjsaud = header[1]
pnumber = int(header[-2]) + int(header[-3])
n = 0
dictghtjs = {}
station1 = header[3]
station2 = station1
least = pnumber

# print(header[2])
# print(ghtjsaud)
# print(ghtjsaud == header[1]) or'2호선'or'1호선'or'1호선':
for row in data:
    if not(ghtjsaud == '1호선'or ghtjsaud == '2호선'or ghtjsaud == '3호선'or ghtjsaud == '4호선'):
        continue
    if row[1] != ghtjsaud:
        #print(ghtjsaud,pnumber)
        # dictghtjs[pnumber] = ghtjsaud 
        # print(dictghtjs)
        strings = list(ghtjsaud)
        print("Line",strings[0],":")
        ghtjsaud = row[1]
        # sorteddict = sorted(dictghtjs)
        print("buisiest staion :",station1,"(",pnumber,")")
        print("least used staion :",station2,"(",least,")")
        pnumber = 0
        pnumber = int(row[-2]) + int(row[-3])
        least = pnumber
    else :
        if pnumber < int(row[-2]) + int(row[-3]):
            pnumber = int(row[-2]) + int(row[-3])
            station1 = row[3]
        if least > int(row[-2]) + int(row[-3]):
            least = int(row[-2]) + int(row[-3])
            station2 = row[3]


# print(dictghtjs[sorteddict[-1]])
# # print(dictghtjs[sorteddict[0]])

# print("1st busiest Line: Line" ,dictghtjs[sorteddict[-1]],"(", sorteddict[-1],")")
# print("2st busiest Line: Line" ,dictghtjs[sorteddict[-2]],"(", sorteddict[-2],")")

# print("1st Least used Line: Line" ,dictghtjs[sorteddict[0]],"(", sorteddict[0],")")
# print("2st Least used Line: Line" ,dictghtjs[sorteddict[1]],"(", sorteddict[1],")")

# ghtjsfltmxm = []
# ghtjsfltmxm =  list(dictghtjs.values())
# print(ghtjsfltmxm)
        
    # if row[1] == ghtjsaud:
    #     sum = int(row[-2]) + int(row[-3])
    #     pnumber += sum
    #     #print(pnumber)
    # else :
    #     print(ghtjsaud,pnumber)
    #     ghtjsaud = row[1]
    #     pnumber = 0
    #     pnumber = pnumber + int(row[-2]) + int(row[-3])


f.close()


def main():

    print(" ")

 

if __name__ == '__main__':

 

    main()
