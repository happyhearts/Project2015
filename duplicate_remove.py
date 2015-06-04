import os
import sys
dir1=sys.argv[1]
os.chdir(dir1)
os.system("find -not -empty -type f -printf \"%s\n\" | sort -rn | uniq -d | xargs -I{} -n1 find -type f -size {}c -print0 | xargs -0 md5sum |  uniq -w32 --all-repeated=separate>files.txt")


f=open("files.txt","r")
dup=open("dup","w")
cwd=os.getcwd()
while(True):
	data=f.readline()
	index=data.find("/")
	if(index!=-1):
		dup.write(cwd+data[index:-1]+" ")
	else:
		dup.write(data)
	if(data.find("\n")==-1):
		break
dup.close()				

def remove():
	dup=open("dup","r")
	i=0
	while True:
		data=dup.readline()
		if(data==""):
			break
		i+=1
		temp=data.split(" ")
		sys.stdout.write(str(i))
		for j in temp:
			print "\t"+j
		
	ch=raw_input("choose option to delete (press n to stop)")		
	if(ch=="n"):
		exit()
	dup.seek(0)	

	for i,line in enumerate(dup):
		if(i==int(ch)-1):
			temp=line.split(" ")	
			for i in range(len(temp)-1):
				print str(i+1)+"\t"+temp[i]
			c=input()
			os.remove(temp[c-1])			
			remove()
			dup.close()
			break
			
remove()			
