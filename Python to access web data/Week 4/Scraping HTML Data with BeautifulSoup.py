
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('enter -')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
count = 0
for tag in tags:
	
	#We need to cast them to int, as they're parsed as text strings
	count += int(tag.contents[0])

print(count)

"""for tag in tags:
    # Look at the parts of a tag
    print('hello')
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
"""


