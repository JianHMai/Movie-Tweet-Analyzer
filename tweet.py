from twitterscraper import query_tweets
import datetime as dt

begin_date = dt.date(2020,2,23)
end_date = dt.date(2020,3,1)
limit = 100
lang = 'english'

tweets = query_tweets('#test', begindate = begin_date, enddate = end_date, limit = limit, lang = lang)
for t in tweets:
    print(t.text)