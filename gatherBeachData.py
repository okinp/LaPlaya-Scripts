#!python3
from xml.etree import ElementTree as et
from xml.dom import minidom as md
# tree = ET.parse('../greece-latest-beaches.osm.pbf.xml')

def createBeachNode(name, wayId):
	beach = et.Element('beach')
	nameNode = et.Element('name')
	nameNode.text = name
	idNode = et.Element('id')
	idNode.text = wayId
	beach.append(idNode)
	beach.append(nameNode)
	return beach

def prettify(elem):
	rough_string = et.tostring(elem, 'utf-8')
	reparsed = md.parseString(rough_string)
	return reparsed.toprettyxml(indent="\t")

def parseXMl(fileIn, fileOut):
	tree = et.parse(fileIn)
	root = tree.getroot()
	xmlRoot = et.Element('beaches')
	xmlTree = et.ElementTree(xmlRoot)
	for way in root.findall('way'):
		if way.find('.//tag[@k="natural"][@v="beach"]') is not None:
			wayId = way.get('id')
			nameElem = way.find('.//tag[@k="name"]')
			if nameElem is not None:
				name = nameElem.get('v')
			else:
				name = ''
			utfName = str(name)
			currentBeach = createBeachNode(utfName, wayId)
			xmlRoot.append(currentBeach)
			# out.write(wayId + utfName.encode() + '\n')
	newXmlRoot = prettify(xmlRoot)
	with open(fileOut, 'wb') as file:
		file.write(newXmlRoot.encode("UTF-8"))
		# newXmlRoot.write(file, encoding='unicode')

parseXMl('../greece-latest-beaches.osm.pbf.xml','parsedBeaches.xml')
#Look at http://gis.stackexchange.com/questions/108533/postgis-insert-a-point-using-python for using python with postgis