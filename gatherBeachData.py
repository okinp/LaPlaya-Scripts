import xml.etree.ElementTree as ET
tree = ET.parse('../greece-latest-beaches.osm.pbf.xml')
root = tree.getroot()
# with open('../pythonWays.txt', 'a') as out:
for way in root.findall('way'):
	if way.find('.//tag[@k="natural"][@v="beach"]') is not None:
		wayId = way.get('id')
		nameElem = way.find('.//tag[@k="name"]')
		if nameElem is not None:
			name = nameElem.get('v')
		else:
			name = 'No Name'
		utfName = str(name)
		print(utfName + '-' + wayId + '\n' )
		# out.write(wayId + utfName.encode() + '\n')