import requests
r = requests.get('http://www.mocky.io/v2/5b026eb43000007a00cee110')
print (r.headers)
print ('Flag is: ' + r.headers['Flag'])
