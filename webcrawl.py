import requests
import bs4
# cls to clear console 
res = requests.get("https://leagueoflegends.fandom.com/wiki/List_of_champions")

soup = bs4.BeautifulSoup(res.text, 'lxml')

raw_html_champion = soup.select('table')[1].find_all('span',{'class' : 'champion-icon'})

champion_list=[]
###From LOLWIKI it pulls the img location and champion name from the html below
for champion_html in raw_html_champion:
	res2 = requests.get('https://leagueoflegends.fandom.com/'+champion_html.a['href'])
	soup2 = bs4.BeautifulSoup(res2.text, 'lxml')
	### think you could just use find here it would be much more clean
	raw_html_categories = soup2.select('.categories')[0].find_all('li',{'class' : 'category'})

	categories_list=[]
	for category in raw_html_categories:
		categories_list.append(category['data-name'])
	champion = {
		'link':'https://leagueoflegends.fandom.com/'+champion_html.a['href'],
		'name':champion_html['data-champion'],
		'image':champion_html.img['data-src'],
		'categories':categories_list
	}
	print('----',champion,'----')
	champion_list.append(champion)

import pickle

f = open("file.pkl","wb")
pickle.dump(champion_list,f)
f.close()

objects = []
with (open("file.pkl", "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break
			
print(objects)
	 
	
	
# <span class="inline-image label-after champion-icon" data-champion="Aatrox" data-param="" data-skin="Original" style="display:inline;white-space:pre;">
 # <span class="border icon-30" data-width="30" style="display:inline-block;position:relative;">
  # <a class="image image-thumbnail link-internal" href="/wiki/Aatrox" title="Aatrox the Darkin Blade">
   # <img alt="Aatrox OriginalSquare" class="thumbborder lzy lzyPlcHld" data-image-key="Aatrox_OriginalSquare.png" data-image-name="Aatrox OriginalSquare.png" data-src="https://vignette.wikia.nocookie.net/leagueoflegends/images/1/15/Aatrox_OriginalSquare.png/revision/latest/scale-to-width-down/30?cb=20180612203801" height="30" onload="if(typeof ImgLzy==='object'){ImgLzy.load(this)}" src="data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D" width="30"/>
   # <noscript>
    # <img alt="Aatrox OriginalSquare" class="thumbborder" data-image-key="Aatrox_OriginalSquare.png" data-image-name="Aatrox OriginalSquare.png" height="30" src="https://vignette.wikia.nocookie.net/leagueoflegends/images/1/15/Aatrox_OriginalSquare.png/revision/latest/scale-to-width-down/30?cb=20180612203801" width="30"/>
   # </noscript>
  # </a>
 # </span>
 # <span style="white-space:normal;">
  # <a href="/wiki/Aatrox" title="Aatrox">
   # Aatrox the Darkin Blade
  # </a>
 # </span>
# </span>