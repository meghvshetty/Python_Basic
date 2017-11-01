import	json
from urllib.request import urlopen
url = "https://www.googleapis.com/youtube/v3/videos?id=<video_id>&key=<YOUR_API_KEY>&part=snippet"
response = urlopen(url)
contexts = response.read()
text = contexts.decode('utf8')
data = json.loads(text)
for video in data['feed']['entry'][0:6]:
	print(video['title']['$t'])