import bs4
import requests

def get_recent_movies():
    url = "https://www.imdb.com/chart/boxoffice/?ref_=hm_cht_sm"
    response = requests.get(url)
    content = bs4.BeautifulSoup(response.content, "html.parser")
    movie = content.findAll('td',{'class','titleColumn'})
    for movie_name in movie:
      print(movie_name.find("a").text)

if __name__ == '__main__':
    get_recent_movies()