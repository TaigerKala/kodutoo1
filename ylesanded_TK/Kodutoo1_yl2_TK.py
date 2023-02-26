#ülesande püstitus
#https://projecteuler.net/problem=822

MOD = 1234567891

#algne list mida hakkame astendama
list = []
listi_kogusumma = 0


n = 10
max_aste = 100

#lisame niipalju elemente listi kui vaja
for i in range(n + 1):
    if i <= 1:
        continue
    else:
        list.append(i)
    i += 1


for i in range(max_aste):
    astendatav_element = min(list)
    elemendi_index = list.index(astendatav_element)
    element = pow(astendatav_element, 2)

    list[elemendi_index] = element

listi_kogusumma = sum(list)
#print(list)
print(listi_kogusumma % MOD)