import urllib2
import simplejson as json

def make_params(params_dict):
    params = ''
    for key in params_dict:
        params += str(key) + '=' + str(params_dict[key]) + '&'
    return params

def fetch_JSON(params):
    domain = 'http://api.geonames.org/searchJSON?'
    uri = domain + params + 'username=######' 
    resource = urllib2.urlopen(uri).readlines()
    js = json.loads(resource[0])
    return js

if __name__ == '__main__':
    params = make_params({'q' : 'Karachi'})
    results = fetch_JSON(params)
    lat = results['geonames'][0]['lat']
    lng = results['geonames'][0]['lng']
    print 'The latitude is: %s' % (str(lat))
    print 'The longitude is: %s' % (str(lng))
