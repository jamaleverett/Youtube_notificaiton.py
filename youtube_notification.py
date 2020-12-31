import urllib, json
from selenium import webdriver 
import time 

def look_for_new_video:()
  api_key = "#grab your API key from https://developers.google.com/ 
  channel_id " #grabs the intended channel ID from the browser"
  
  base_video_url = " #base video url " 
  base_search_url = " #search url "
  
  url = base_search_url + 'key #'
  inp = urllib.urlopen (url)
  resp =json.load(inp)
  
  vidID = resp['items'][0]['id']['videoID']
  
  video_exists = False
  with open('videoid.json', 'r) as json_file:
        data =json.load(json_file)
        if data['variable'] != vidID
            browser = webdriver.Chrome()
            browser.get(base_video_url +vidID)
            video_exists =True
    
    if video_exists:
        with open('videoid.json', 'w') as json_file:
            data = {"videoID: vidID"}
            jsondump(data. json_file)
  
