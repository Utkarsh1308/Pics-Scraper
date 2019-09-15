from bs4 import BeautifulSoup as bs
import requests
import urllib.request
import shutil
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import argparse

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def make_parser():
	parser = argparse.ArgumentParser(
		formatter_class=argparse.RawTextHelpFormatter)
	
	parser.add_argument('year',
		type=str,
		default='',
		help='Starting year of the Student')
	
	parser.add_argument('--hostel',
		type=str,
		default=None,
		help='Hostel which the students reside in')
		
	parser.add_argument('-i', '--intern',
		type=str,
		default=None,
		help='Student currently doing PS2 or thesis')
	
	return parser


def main():
	args = make_parser().parse_args()
	year = args.year
	hostel = args.hostel 
	
	url = "https://swd.bits-goa.ac.in/search1.php"
	r = requests.get(url, verify=False)
	soup = bs(r.text, "html.parser")
	
	if args.intern == 'PS2' or args.intern == 'Thesis':
		hostel = args.intern
	
	if hostel:
		ids = [tag.td.text.strip() for tag in soup.find_all('tr') if hostel in str(tag)]
	else:
		ids = [tag.td.text.strip() for tag in soup.find_all('tr')]
		
	printer(ids)
	download(ids, year)
	
def printer(data):
	with open("ID.txt", 'w') as f:
		for row in data:
			for column in row:
				f.write(column)
			f.write('\n')
			
def download(data, year):
	with open("ID.txt") as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	content = [x.replace("G","") for x in content]
	for column in content:
		if year in column:
			response = requests.get("https://swd.bits-goa.ac.in/css/studentImg/" + column + ".jpg", verify=False, stream = True)
			with open(column + '.jpg', 'wb') as out_file:
				shutil.copyfileobj(response.raw, out_file)
			del response
		
if __name__ == "__main__":
	main()