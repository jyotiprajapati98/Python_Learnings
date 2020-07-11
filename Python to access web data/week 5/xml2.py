import xml.etree.ElementTree as ET
input = '''<stuff>
	<users>
		<user x="2">
			<id>001</id>
			<name>Jyoti Prajapati</name>
		</user>
		<user x="3">
			<id>003</id>
			<name>Jiya Khan</name>
		</user>
	</users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')

print('user count',len(lst))

for item in lst:
	print('name',item.find('name').text)
	print('id',item.find('id').text)
	print('attribute',item.get("x"))

