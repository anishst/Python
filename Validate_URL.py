import requests,csv

def WritetoTextFile(filename, value):
	f = open(filename,"a") #opens file with name of "test.txt"
	f.write(value)
	f.close()

# urlList = ['http://www.google.com']
urlList = []
with open('TestCase_URLs.txt', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
    	urlList.append(line[0].strip())

for i, url in enumerate(urlList):
	try:
		r = requests.get(url)
		print("{} out of {}: {} {} ".format(i,len(urlList), url, r.status_code))
		output = "{},{}\n ".format(url, r.status_code)
		WritetoTextFile("TestCase_URL_Validation_Results.csv", output)
	except Exception as e:
		output = "There was an issue with {}\n ".format(url)
		WritetoTextFile("TestCase_URL_Validation_Results.csv", output)
