import metadata_parser

"get metadata of given url"
def metadataparse(url: str):

    metadata = metadata_parser.MetadataParser(url=url,search_head_only=False)
    return metadata


