import sys, requests
from bs4 import *

arguments = sys.argv
id_contest = arguments[1]
pb = arguments[2]

url = "https://codeforces.com/contest/"+str(id_contest)+"/problem/"+str(pb)
cf_request = requests.get(url)
source_code = cf_request.text
soup = BeautifulSoup(source_code, "lxml")
test = soup.find_all("pre")
for i in range(0, len(test), 2):
	input_test = test[i].get_text().split("\n")
	file = open("input" + str(i//2) + ".txt", "w")
	for i2 in range(1, len(input_test)-1):
		file.write(input_test[i2]+"\n")
	file.close()
	print("Input of problem", str(pb), " in", " input" + str(i//2) + ".txt")
