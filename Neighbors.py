import urllib2
import json

command = {'command': 'getNeighborsActivity'}

stringified = json.dumps(command)

headers = {'content-type': 'application/json'}

request = urllib2.Request(url="http://localhost:14265", data=stringified, headers=headers)
returnData = urllib2.urlopen(request).read()

neighbors = json.loads(returnData)
length=len(neighbors['neighbors'])
for i in range (0,length):
	print("IP:"+str(neighbors['neighbors'][i]['node'])+"LatestPacketReceived:"+str(neighbors['neighbors'][i]['latestPacketReceived']))

respond=raw_input("Should I delete not responding Neighbors? [y/n]")
while True:
	if respond=="y":
		#filepath=raw_input("Where is the file locatet? ")
		filepath='IRI.cfg'
		f = open(filepath, 'r+')
		#print(f.read())
		lines=f.readlines()
		#print(lines)
		for i in range (0,length):
			if str(neighbors['neighbors'][i]['latestPacketReceived'])=='None':
				ip=str(neighbors['neighbors'][i]['node'])
				ip.replace(ip[:4], '+udp://')
				print(ip)
				for x in range(0,len(lines)):
					if ip in lines[x-1]:
						del lines[x-1]
						print("deletet line:"+str(x-1))
				print("Succesfully delet bad Neighbors!")
		f.close()
		f=open(filepath, 'w')
		f.write("".join(lines))
		f.close()
		break
	elif respond=="n":
		exit()
		break
	else:
		print("No correct Input.")
		respond=raw_input("Should I delete not responding Neighbors? [y/n]")
