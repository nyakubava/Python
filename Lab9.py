from urllib.request import urlopen
from datetime import date
import re
from urllib import error
import sys


def validationData(url):  #Validate if there is an error
    try:
        content = urlopen(url).read().decode("utf-8")
    except error.URLError as url_error:      #Validate URL
        print("Please, check URL:   ", url_error)
        sys.exit(1)
    except UnicodeDecodeError as decode_err:  #Validate decoding
        print("Error with decoding data:    ", decode_err)
    except error.HTTPError as http_error:  #Validate HTTP
        print("HTTP Error", http_error)
    else:
        return content

def topics(url, topics): #print date and count finded topics
    content = validationData(url)
    today = date.today()   # get date
    print("Today's date:", today)  # date
    for x in topics:
         topic = re.findall(x, content, re.I | re.M)
         count = len(topic)
         print('{} appears {} times.'.format(x, count))

#data
topics('http://www.nasonline.org',['research', 'climate',
'evolution', 'cultural', 'leadership', 'discovery', 'national'])
