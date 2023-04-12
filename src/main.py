from datetime import datetime
import requests
import env


class Headline:
    def __init__(self, text:str, thumbnail_url:str, url:str):
        self.text = text
        self.thumbnail_url = thumbnail_url
        self.url = url
    def __repr__(self):
        return f"{self.text}\nStory: {self.url}\nThumbnail: {self.thumbnail_url}\n---"


today = datetime.now()
month,day = today.strftime('%B'), today.day

search_url = f"https://customsearch.googleapis.com/customsearch/v1?key={env.GOOGLE_SEARCH_API_KEY}&cx={env.GOOGLE_SEARCH_ENGINE_ID}&exactTerms=florida man&q={month} {day}&num=5"
j = requests.get(search_url).json()

stories = []
for item in j['items']:
    stories.append(Headline(item['title'], item['pagemap']['cse_thumbnail'][0]['src'], item['link']))
for story in stories:
    print(story)
