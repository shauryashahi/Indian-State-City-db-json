from lxml.html import parse
import demjson

def main():
	url = 'http://en.wikipedia.org/wiki/List_of_cities_and_towns_in_India_by_population'
	page = parse(url).getroot()
	db = {}
	for i in xrange(1,26):
		table = page.cssselect('table.wikitable')[i]
		flag = 0
		for r in table:
			if(flag == 0):
				flag = 1
			else:
				city = r[0].text_content().strip()
				state = r[1].text_content().strip()
				db.setdefault(state, [])
				db[state].append(city)
	json = demjson.encode(db)
	t = open("state_city.js", "w")
	t.write(json)
if __name__ == '__main__':
	main()
