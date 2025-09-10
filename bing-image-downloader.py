from bing_image_downloader import downloader

query = ['keyword 1',
         'keyword 2',
         'keyword 3'
           ]


for query_string in query:
    try:
        downloader.download(query_string, limit=300, page_limit=3000, output_dir='photos', adult_filter_off=True, force_replace=False, timeout=1000, verbose=True)
    except:
        continue
