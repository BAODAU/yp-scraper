
import urllib.parse

keyword = "de"
place = "new york city, ny"
url = "https://www.yellowpages.com/search?search_terms={0}&geo_location_terms={1}".format(keyword, place)
print(urllib.parse.urlencode(url))