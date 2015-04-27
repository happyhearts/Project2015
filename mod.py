import math
f=open("result.txt","w")
for m in range(3,21,1):
	for x in range(2,m*3+1 ):
		f.write("x= "+str(x)+" m = "+str(m)+"\t\t\t")
		for y in range(1,16):
			f.write(str(pow(x,y)%m)+"\t")
		f.write("\n")	
	f.write("\n\n")	
			
		
