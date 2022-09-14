import requests

a = input("proxy list path >> ")
b = input("url >> ")

url = b

with open(a,"r") as f:
	a = f.read().split("\n")
	c = 0
	for i in a:
		c += 1
		print("Done Viewed By" + str(c))
	proxies = {
	   'http': 'http://'+a,
	}

	try:
		response = requests.post(url, proxies=proxies)
	except:
		pass
