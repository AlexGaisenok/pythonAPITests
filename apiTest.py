import requests
namesFile = input('Enter the name of a file with names: ')
if len(namesFile)<1: namesFile='names.txt'
f = open(namesFile,'r')
resFileName=input('Enter the file name for results: ')
if len(resFileName)<1: resFileName='results.txt'
resFile = open(resFileName,'w+')
numOfLines = input('Enter number of records you want to retrieve: ')
print('Information is loading... Please, wait')
for i in range(int(numOfLines)):
    userName = f.readline().strip()
    params = {'name':userName}
    response = requests.get('https://api.agify.io/', params)
    resFile.write(response.text + "\n")
f.close()
resFile.close()
