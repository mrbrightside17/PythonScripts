listofelements = [1,2,4,5,1,2,4,5,6,74,1]
newlist = []
# for i in listofelements:
# 	if i not in newlist:
# 		newlist.append(i)

# print listofelements
# print newlist

for i in range(0,len(listofelements)):
	if listofelements[i] not in newlist:
		newlist.append(listofelements[i])

print listofelements
print newlist