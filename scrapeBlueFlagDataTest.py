#!python3
import csv
import urllib.request as req
import codecs
from io import StringIO
import json
class BlueflagBeach(object):
	def __init__(self, scrapedData):
		self.data = {}
		self.data['address'] = scrapedData[1]
		self.data['blueFlagSince'] = scrapedData[2]
		self.data['blueflag'] = scrapedData[3]
		self.data['comments'] = scrapedData[4]
		self.data['contact'] = scrapedData[5]
		self.data['country'] = scrapedData[6]
		self.data['blindAccess'] = scrapedData[0]
		self.data['disabledAccessBeach']  = scrapedData[7]
		self.data['disabledAccessWater'] = scrapedData[8]
		self.data['avgVisitors'] = scrapedData[10]
		self.data['maxVisitors'] = scrapedData[11]
		self.data['length'] = scrapedData[13]
		self.data['price'] = scrapedData[14]
		self.data['coastal'] = scrapedData[22]
		self.data['nudist'] = scrapedData[24]
		self.data['rocky'] = scrapedData[25]
		self.data['sandy'] = scrapedData[26]
		self.data['free'] = scrapedData[27]
		self.data['kioskNear'] = scrapedData[28]
		self.data['lat1'] = scrapedData[29]
		self.data['lat2'] = scrapedData[30]
		self.data['lon1'] = scrapedData[33]
		self.data['lon2'] = scrapedData[35]
		self.data['lifeguard'] = scrapedData[31]
		self.data['url'] = scrapedData[32]
		self.data['location'] = scrapedData[34]
		self.data['municipality'] = scrapedData[36]
		self.data['seasonStart'] = scrapedData[42]
		self.data['seasonEnd'] = scrapedData[9]
		self.data['locationType'] = scrapedData[43]
		self.scrapedData = scrapedData
	def print(self):
		print(json.dumps(self.data,sort_keys=True, indent=4))
def downloadData():
	beaches = {}
	errorIds = [];
	with open('./blueFlagIDs.txt') as f:
		beachIds = f.read().splitlines()
		beachIds.sort()
	f.close()
	for beachId in beachIds:
		try:
			reqUrl = 'https://cartocdn-ashbu.global.ssl.fastly.net/fee/api/v1/map/675d9b36608b454b708ae08d5f368344:1468852143726/0/attributes/'
			with req.urlopen(reqUrl+str(beachId)) as response:
				html = response.read()
				html = str(html,'utf-8')
				html = html[1:-1]
			csvfile = csv.reader(StringIO(html), delimiter=',')
			data = list(csvfile)
			data = data[0]
			current = []
			for datum in data:
				#print(datum)
				cc = datum.split(':')
				if cc[0] == "link" and len(cc) == 3:
					cc = cc[1] + ':' + cc[2]
				elif len(cc)>1:
					cc = cc[1]
				current.append(cc)
			currentBeach = BlueflagBeach(current)
			beaches[str(beachId)] = currentBeach.data
		except:
			errorIds.append(beachId)
	with open('./blueFlagErrorIds.txt', 'w') as errorIdsFile:
		for item in errorIds:
			errorIdsFile.write("%s\n" % item)
	errorIdsFile.close()
	with open('./blueFlagData.json', 'w') as blueFlagData:
		json.dump(beaches, blueFlagData, sort_keys=True, indent=4)
	blueFlagData.close()
downloadData()