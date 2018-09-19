import random
import urllib.request

def download_image(url):
    name = random.randrange(1,10000)
    fullname = str(name)+".jpg"
    urllib.request.urlretrieve(url,fullname)     

image_urls = [

'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'
]

for image_url in image_urls:
	try:
		download_image(image_url)
	except Exception as e:
		print(f"something wrong with{image_url} ")
	
