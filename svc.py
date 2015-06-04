import sys

class SVC:
	def __init__(self):
		if(len(sys.argv)==1):
			print "svc is Simple Version Control System. which keep track on single file ."
			print "Options Available : "
			print "1) svc FILENAME commit file"
			print "2) svc N display version number"
			exit(0)
		elif(len(sys.argv)==2):
				if(sys.argv[1].isdigit()):
					self.display()
				else:
					self.commit()
	def commit(self):
			print "comminting"
			file1=open(sys.argv[1],"r+")	
			fileTemp=""			
			try:
				fileTemp=open("temp","r")
			except:
				fileTemp=open("temp","w")	
				fileTemp.close()
				fileTemp=open("temp","r")
			oldData=fileTemp.readlines()
			newData=file1.readlines()
			fileTemp.close()
			fileTemp=open("temp","a")
			count=0
			if len(oldData)>0:
				for i in oldData[-2]:
					if(i==" "):
						count+=1
				if(len(newData)==count-1):
						print "already commited!!!"		
						exit()
			else:
				fileTemp.write(" ")		
			for i in range(len(newData)):
					newData[i]=newData[i][0:-1]
			newData.append("\n")
			totLines=20
			if(len(newData)<20):
					totLines=len(newData)
			for i in range(totLines):
					if(len(newData[i])>9):
						newData[i]=newData[i][0:9]
					fileTemp.write(newData[i]+" ")	
			file1.close()		
			fileTemp.close()
				
			
	def display(self):
				temp=open("temp","r")	
				totVersion=0
				for version,data in enumerate(temp):
					if(version==i):
						print data
					totVersion+=1	
				else:
					print "available versions :"+str(totVersion)
				temp.close()	
				
				
trackFile=SVC()				
