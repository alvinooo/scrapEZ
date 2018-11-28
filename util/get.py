from urllib.request import urlopen
from bs4 import BeautifulSoup

# TODO add cached option
def get_html(url, output_file=None):
	with urlopen(url=url) as response:
		html = response.read()
		if output_file:
			with open(f'tmp/{output_file}', 'wb') as output:
				output.write(html)
		return html

def get_parsed(url, output_file=None):
	html = get_html(url=url, output_file=output_file)
	parsed = BeautifulSoup(html, 'html.parser')
	return parsed

parsed = get_parsed(url='https://www.webscraper.io/test-sites/e-commerce/allinone', output_file='test.html')