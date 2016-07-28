#!python3
import urllib.request as req
reqUrl = 'https://cartocdn-ashbu.global.ssl.fastly.net/fee/api/v1/map/675d9b36608b454b708ae08d5f368344:1468852143726/0/attributes/325657574'
class BlueflagBeach(object):
	def __init__(self):
		self.accessForBlind = None
		self.address = None
		self.blueFlagSince = None
		self.blueflag = None
		self.comments = None
		self.contact = None
		self.country = None
		self.disabledAccessBeach  = None
		self.disabledAccessWater = None
		self.avgVisitors = None
		self.maxVisitors = None
		self.beachLength = None
		self.entryPrice = None
		self.isCoastal = None
		self.isInland = None
		self.isNudist = None
		self.isRocky = None
		self.isSandy = None
		self.freeEntry = None
		self.kioskNear = None
		self.lat1 = None
		self.lat2 = None
		self.lon1 = None
		self.lon2 = None
		self.lifeguard = None
		self.url = None
		self.locationName = None
		self.municipality = None
		self.seasonStart = None
		self.seasonEnd = None
		self.wayType = None
	@property
	def accessForBlind(self):
		return self.__accessForBlind
	@accessForBlind.setter
	def accessForBlind(self, val):
		self.__accessForBlind = val;

	@property
	def address(self):
		return self.__address
	@address.setter
	def address(self, val):
		self.__address = val;

	@property
	def blueFlagSince(self):
		return self.__blueFlagSince
	@blueFlagSince.setter
	def blueFlagSince(self, val):
		self.__blueFlagSince = val

	@property
	def blueFlag(self):
		return self.__blueFlag
	@blueFlag.setter
	def blueFlag(self, val):
		self.__blueFlag = val

	@property
	def comments(self):
		return self.__comments
	@comments.setter
	def comments(self, val):
		self.__comments = val

	@property
	def contact(self):
		return self.__contact
	@contact.setter
	def contact(self, val):
		self.__contact = val

	@property
	def country(self):
		return self.__country
	@country.setter
	def country(self, val):
		self.__country = val

	@property
	def disabledAccessBeach(self):
		return self.__disabledAccessBeach
	@disabledAccessBeach.setter
	def disabledAccessBeach(self, val):
		self.__disabledAccessBeach = val
	@property
	def disabledAccessWater(self):
		return self.__disabledAccessWater
	@disabledAccessWater.setter
	def disabledAccessWater(self, val):
		self.__disabledAccessWater = val
	@property
	def avgVisitors(self):
		return self.__avgVisitors
	@avgVisitors.setter
	def avgVisitors(self, val):
		self.__avgVisitors = val
	@property
	def maxVisitors(self):
		return self.__maxVisitors
	@maxVisitors.setter
	def maxVisitors(self, val):
		self.__maxVisitors = val
	@property
	def beachLength(self):
		return self.__beachLength
	@beachLength.setter
	def beachLength(self, val):
		self.__beachLength = val
	@property
	def entryPrice(self):
		return self.__entryPrice
	@entryPrice.setter
	def entryPrice(self, val):
		self.__entryPrice = val
	@property
	def isCoastal(self):
		return self.__isCoastal
	@isCoastal.setter
	def isCoastal(self, val):
		self.__isCoastal = val
	@property
	def isInland(self):
		return self.__isInland
	@isInland.setter
	def isInland(self, val):
		self.__isInland = val
	@property
	def isNudist(self):
		return self.__isNudist
	@isNudist.setter
	def isNudist(self, val):
		self.__isNudist = val
	@property
	def isRocky(self):
		return self.__isRocky
	@isRocky.setter
	def isRocky(self, val):
		self.__isRocky = val
	@property
	def isSandy(self):
		return self.__isSandy
	@isSandy.setter
	def isSandy(self, val):
		self.__isSandy = val
	@property
	def freeEntry(self):
		return self.__freeEntry
	@freeEntry.setter
	def freeEntry(self, val):
		self.__freeEntry = val
	@property
	def kioskNear(self):
		return self.__kioskNear
	@kioskNear.setter
	def kioskNear(self, val):
		self.__kioskNear = val
	@property
	def lat1(self):
		return self.__lat1
	@lat1.setter
	def lat1(self, val):
		self.__lat1 = val
	@property
	def lat2(self):
		return self.__lat2
	@lat2.setter
	def lat2(self, val):
		self.__lat2 = val
	@property
	def lon1(self):
		return self.__lon1
	@lon1.setter
	def lon1(self, val):
		self.__lon1 = val
	@property
	def lon2(self):
		return self.__lon2
	@lon2.setter
	def lon2(self, val):
		self.__lon2 = val
	@property
	def lifeguard(self):
		return self.__lifeguard
	@lifeguard.setter
	def lifeguard(self, val):
		self.__lifeguard = val
	@property
	def url(self):
		return self.__url
	@url.setter
	def url(self, val):
		self.__url = val
	@property
	def locationName(self):
		return self.__locationName
	@locationName.setter
	def locationName(self, val):
		self.__locationName = val
	@property
	def municipality(self):
		return self.__municipality
	@municipality.setter
	def municipality(self, val):
		self.__municipality = val
	@property
	def seasonStart(self):
		return self.__seasonStart
	@seasonStart.setter
	def seasonStart(self, val):
		self.__seasonStart = val
	@property
	def seasonEnd(self):
		return self.__seasonEnd
	@seasonEnd.setter
	def seasonEnd(self, val):
		self.__seasonEnd = val
	@property
	def wayType(self):
		return self.__wayType
	@wayType.setter
	def wayType(self, val):
		self.__wayType = val

	def setContent(html):
		return
def downloadData(fileOut):
	html = req.urlopen(reqUrl).read()
	f = open(fileOut, 'wb')
	f.write(html)
	f.close()
downloadData('testBlueFlag.txt')