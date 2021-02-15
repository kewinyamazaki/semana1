N = int(input())

diamonds = [input().strip() for x in range(0,N)]
counterList1 = []
counterList2 = []
for x in diamonds:
 counter = 0
 for y in range(len(x)):
  if x[y] == '<' and x[y+1] != '<':
   for z in range(y+1,len(x)):
    if x[z] == '<':
     break
    elif x[z] == '>':
     counter+=1
     counterList1.append(counter)
     break
    else:
     continue
  else:
    continue
 counterList2.append(counterList1)
 counterList1 = []

for x in counterList2:
	print(sum(x))