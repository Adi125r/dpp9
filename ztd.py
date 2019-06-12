import csv
import  math
import matplotlib.pyplot as plt



dane1 = []
dane1t = []
dane1p = []
dane2 = []
dane2t = []
dane2p = []
dane3 = []
dane3t = []
dane3p = []
dane4 = []
dane4t = []
dane4p = []
dane5 = []
dane5t = []
dane5p = []
dane6 = []
dane6t = []
dane6p = []
dane7 = []
dane7t = []
dane7p = []
dane8 = []
dane8t = []
dane8p = []

with open('surface_20150912_00.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
       if  row[2] == "BIAL":
          dane1.append(row[3])
          dane1t.append(row[10])
          p= float(row[12])*pow(((float(row[10])- 0.0065*(float(row[8])-float(row[9])))/float(row[10])),5.25)
          dane1p.append(p)

with open('surface_20150912_06.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
       if  row[2] == "BIAL":
          dane2.append(row[3])
          dane2t.append(row[10])
          p= float(row[12])*pow(((float(row[10])- 0.0065*(float(row[8])-float(row[9])))/float(row[10])),5.25)
          dane2p.append(p)
with open('surface_20150912_12.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
       if  row[2] == "BIAL":
          dane3.append(row[3])
          dane3t.append(row[10])
          p= float(row[12])*pow(((float(row[10])- 0.0065*(float(row[8])-float(row[9])))/float(row[10])),5.25)
          dane3p.append(p)
with open('surface_20150912_18.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
       if  row[2] == "BIAL":
          dane4.append(row[3])
          dane4t.append(row[10])
          p= float(row[12])*pow(((float(row[10])- 0.0065*(float(row[8])-float(row[9])))/float(row[10])),5.25)
          dane4p.append(p)
with open('surface_20150913_00.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
       if  row[2] == "BIAL":
          dane5.append(row[3])
          dane5t.append(row[10])
          p= float(row[12])*pow(((float(row[10])- 0.0065*(float(row[8])-float(row[9])))/float(row[10])),5.25)
          dane5p.append(p)
with open('surface_20150913_06.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
       if  row[2] == "BIAL":
          dane6.append(row[3])
          dane6t.append(row[10])
          p= float(row[12])*pow(((float(row[10])- 0.0065*(float(row[8])-float(row[9])))/float(row[10])),5.25)
          dane6p.append(p)
with open('surface_20150913_12.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
       if  row[2] == "BIAL":
          dane7.append(row[3])
          dane7t.append(row[10])
          p= float(row[12])*pow(((float(row[10])- 0.0065*(float(row[8])-float(row[9])))/float(row[10])),5.25)
          dane7p.append(p)
with open('surface_20150913_18.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
       if  row[2] == "BIAL":
          dane8.append(row[3])
          dane8t.append(row[10])
          p= float(row[12])*pow(((float(row[10])- 0.0065*(float(row[8])-float(row[9])))/float(row[10])),5.25)
          dane8p.append(p)

def oblicz(danet,dane,danep):
    zdt = []
    for i in range(0,len(danet)):
        tc = float(dane7t[i]) - 273.15
        liczba =6.112 * math.exp((17.67 *tc)/(tc + 243.5))

        z= 0.002277*(danep[i]+((1255/float(dane1t[i]))+0.05)*liczba)
        zdt.append(z)

    return zdt



jup=[]
z1= []
z1 = oblicz(dane1t,dane1,dane1p)
#print(z1)
z2 = oblicz(dane2t,dane2,dane2p)
#print(z2)
z3 = oblicz(dane3t,dane3,dane3p)
#print(z3)
z4 = oblicz(dane4t,dane4,dane4p)
#print(z4)
z5 = oblicz(dane5t,dane5,dane5p)
#print(z5)
z6 = oblicz(dane6t,dane6,dane6p)
#print(z6)
z7 = oblicz(dane7t,dane7,dane7p)
#print(z7)
z8 = oblicz(dane8t,dane8,dane8p)
#print(z8)
for i in range(0,5):
    jup.append(z1[i])
for i in range(6,11):
    jup.append((z1[i]*(1/(i+2))+z2[i-6]*(1/(i-4)))/ ((1/(i+2))+ (1/(i-4))))

for i in range(12,17):
    jup.append((z1[i]*(1/(i+2))+z2[i-6]*(1/(i-4))+z3[i-12]*(1/(i-10)))/ ((1/(i+2))+ (1/(i-4)+(1/(i-10) ))))

for i in range(18,23):
    jup.append((z1[i]*(1/(i+2))+z2[i-6]*(1/(i-4))+z3[i-12]* (1/(i-10)) +z4[i-18] *(1/(i-16)))/ ((1/(i+2))+ (1/(i-4))+(1/(i-10) )+(1/(i-16))))

for i in range(24,29):
    jup.append((z5[i-24]*(1/(i-22))+z2[i-6]*(1/(i-4))+z3[i-12]* (1/(i-10)) +z4[i-18] *(1/(i-16)))/ ((1/(i-22))+ (1/(i-4))+(1/(i-10) )+(1/(i-16))))

for i in range(30,35):
    jup.append((z5[i-24]*(1/(i-22))+z6[i-30]*(1/(i-28))+z3[i-12]* (1/(i-10)) +z4[i-18] *(1/(i-16)))/ ((1/(i-22))+ (1/(i-28))+(1/(i-10) )+(1/(i-16))))

for i in range(36,41):
    jup.append((z5[i-24]*(1/(i-22))+z6[i-30]*(1/(i-28))+z7[i-36]* (1/(i-34)) +z4[i-18] *(1/(i-16)))/ ((1/(i-22))+ (1/(i-28))+(1/(i-34) )+(1/(i-16))))

for i in range(42,47):
    jup.append((z5[i-24]*(1/(i-22))+z6[i-30]*(1/(i-28))+z7[i-36]* (1/(i-34)) +z8[i-42] *(1/(i-40)))/ ((1/(i-22))+ (1/(i-28))+(1/(i-34) )+(1/(i-40))))

for i in range(48,53):
    jup.append((z6[i-30]*(1/(i-28))+z7[i-36]* (1/(i-34)) +z8[i-42] *(1/(i-40)))/ ((1/(i-28))+(1/(i-34) )+(1/(i-40))))

for i in range(54,59):
    jup.append((z7[i-36]* (1/(i-34)) +z8[i-42] *(1/(i-40)))/ ((1/(i-34) )+(1/(i-40))))

for i in range(60,66):
    jup.append((z8[i-42] *(1/(i-40)))/ ((1/(i-40))))


print(jup)

plik = open('szdt', 'w')
plik.writelines(str(jup))
plik.close()


plt.plot(jup)
plt.ylabel('Srednie ZDT')
plt.show()
