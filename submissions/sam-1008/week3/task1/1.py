import requests

headers = requests.get("http://www.mocky.io/v2/5b026eb43000007a00cee110").headers
print "Flag is : " , headers["flag"]

