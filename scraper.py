from bs4 import BeautifulSoup as bs
import requests
import urllib.request
import shutil
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import argparse

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

parser = argparse.ArgumentParser(description = "get the hostel")
parser.add_argument('YEAR', help = "Enter Hostel")
args = parser.parse_args()
YEAR = args.YEAR

def main():
	url = "https://swd.bits-goa.ac.in/search1.php"
	r = requests.get(url, verify=False)
	soup = bs(r.text, "html.parser")
	ids = [tag.td.text.strip() for tag in soup.find_all('tr')]
	printer(ids)
	download(ids)
	
def printer(data):
	with open("ID.txt", 'w') as f:
		for row in data:
			for column in row:
				f.write(column)
			f.write('\n')
			
def download(data):
	with open("ID.txt") as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	content = [x.replace("G","") for x in content]
	for column in content:
			if YEAR in column:
				response = requests.get("https://swd.bits-goa.ac.in/css/studentImg/" + column + ".jpg", verify=False, stream = True)
				with open(column + '.jpg', 'wb') as out_file:
					shutil.copyfileobj(response.raw, out_file)
				del response
		
if __name__ == "__main__":
	main()