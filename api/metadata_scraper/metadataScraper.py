import metadata_parser
import requests
import feedparser

class rssMetadata:

    def __init__(self,string):
        self.metadata = feedparser.parse(string).feed

"get metadata of given url"
def metadataparse(url: str):
    rss_headers = {
        'text/xml; charset=utf-8',
        'application/rss+xml; charset=utf-8',
        'application/atom+xml; charset=utf-8',
        'application/rss+xml',
        'application/atom+xml',
        'text/xml;'
    }
    
    r = requests.get(url, timeout=5)

    if r.headers["Content-Type"].lower() in rss_headers:
        return rssMetadata(r.text)

    return metadata_parser.MetadataParser(
        html = r.text,
        search_head_only = False
    )
