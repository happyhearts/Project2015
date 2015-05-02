a=raw_input()				#input
numbers=a.split(" ")

for i in range(len(numbers)):
	numbers[i]=int(numbers[i])		
count=len(numbers)	
repeat=0
new_addition=0
array=[0 for i in range(count+1)]
addition=(count*(count+1))/2
for i in range(count):
	new_addition+=numbers[i]
	array[numbers[i]]+=1
	if(array[numbers[i]]==2):
		repeat=numbers[i]
print "repeat  = "+str(repeat)
print "missing = "+str(addition-(new_addition-repeat))	
