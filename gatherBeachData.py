#!python3
from xml.etree import ElementTree as et
from xml.dom import minidom as md

def parseRelations(fileIn, fileOut):
	#Parses the file
	tree = et.parse(fileIn)
	root = tree.getroot()
	#Start creating the output xml file
	xmlRoot = et.Element('relations')
	xmlTree = et.ElementTree(xmlRoot)
	for relation in root.findall('relation'):
		if isBeach(relation):
			relationElement = et.Element('relation')
			relationId = et.Element('id')
			relationId.text = relation.get('id')
			relationElement.append(relationId)
			xmlRoot.append(relation)
	nodesRoot = et.Element('nodes')
	xmlRoot.append( nodesRoot)
	for node in root.findall('node'):
		if len(list(node)) == 0:
			nodesRoot.append(node)
	beachesRoot = et.Element('beaches')
	xmlRoot.append(beachesRoot)
	for way in root.findall('way'):
		if isBeach(way):
			beachesRoot.append(way)
	newXmlRoot = prettify(xmlRoot)
	writeXmlToDisk(fileOut, newXmlRoot)	

def parseXMl(fileIn, fileOut):
	#Parses the file
	tree = et.parse(fileIn)
	root = tree.getroot()
	#Start creating the output xml file
	xmlRoot = et.Element('beaches')
	xmlTree = et.ElementTree(xmlRoot)
	#Look for beaches on input
	count = 0
	for way in root.findall('way'):
		if isBeach(way):
			print(count)
			count+=1
			if count == 30:
				break
			wayId = way.get('id')
			nameElem = way.find('.//tag[@k="name"]')
			name = ''
			if nameElem is not None:
				name = nameElem.get('v')
			utfName = str(name)
			polyData = getPolygonData(way, root)
			currentBeach = createBeachNode(utfName, wayId, polyData )
			xmlRoot.append(currentBeach)
			# out.write(wayId + utfName.encode() + '\n')
	newXmlRoot = prettify(xmlRoot)
	writeXmlToDisk(fileOut, newXmlRoot)

def prettify(elem):
	#Pretty prints the XML
	rough_string = et.tostring(elem, 'utf-8')
	reparsed = md.parseString(rough_string)
	return reparsed.toprettyxml(indent="\t") 

def writeXmlToDisk(fileOut, data):
	with open(fileOut, 'wb') as file:
		file.write(data.encode("UTF-8"))
 
def createBeachNode(name, wayId, polyData):
	#Gathers data for a single beach
	beach = et.Element('beach')
	nameNode = et.Element('name')
	nameNode.text = name
	idNode = et.Element('id')
	idNode.text = wayId
	polygon = et.Element('polygon')
	beach.append(idNode)
	beach.append(nameNode)
	for coord in polyData:
		nd = et.Element('coord')
		lat = et.Element('lat')
		lon = et.Element('lon')
		lat.text = coord['lat']
		lon.text = coord['lon']
		nd.append(lat)
		nd.append(lon)
		beach.append(nd)
	return beach

def isBeach(way):
	retVal = True
	if way.find('.//tag[@k="natural"][@v="beach"]') == None:
		retVal = False 
	return retVal

def getPolygonData(elem, root):
	polygon = list(elem.iter('nd'))
	refList = []
	for nd in polygon:
		coordDict = getCoords(nd.get("ref"), elem, root)
		refList.append(coordDict)
	return refList

def getCoords(nodeId, elem, root):
	#root = elem.getroot()
	nodeElem = root.find('.//node[@id=' + '"' + str(nodeId) + '"' +']')
	coords = {'lat': None, 'long': None }
	try:
		coords['lat'] = nodeElem.get('lat');
		coords['lon'] = nodeElem.get('lon');
	except:
		 sys.exit("No node with specified Id was found")
	return coords

parseRelations('../greece-latest-beaches.osm.pbf.xml','beachData-new.xml')
#Look at http://gis.stackexchange.com/questions/108533/postgis-insert-a-point-using-python for using python with postgis