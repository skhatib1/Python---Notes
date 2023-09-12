import requests

url = 'google.com'
url_request = requests.get(url)
query_output = url_requst.json() if url_request.status_code == 200 else None
