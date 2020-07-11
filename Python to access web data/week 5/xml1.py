import xml.etree.ElementTree as ET
data = '''<person>
	<name>jyoti</name>
	<phone type="intl">
		887187234
	</phone>
	<email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('name',tree.find('name').text)
print('attr',tree.find('email').get('hide'))



