import feedparser

def parse(rssUrl:str):

    return feedparser.parse(f'{rssUrl}')
