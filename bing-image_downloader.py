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
















query = ['deprem',
         'deprem fotolari',
         'ev yıkıldı',
         'deprem hasar',
         'deprem hatay',
         'deprem bina',
         'deprem yapı'
         'deprem oldu',
         'bina yangın',
         'yıkılan bina deprem',
         'alevler sardı',
         'earthquake',
         'earthquake in city',
         'earthquake buildings',
         'earthquake disaster',
         'earthquake column',
         'earthquake beam',
         'earthquake damage',
         'earthquake damage to buildings',
         'earthquake structural damage'
           ]


for query_string in query:
    try:
        downloader.download(query_string, limit=300, page_limit=3000, output_dir='deprem fotolari', adult_filter_off=True, force_replace=False, timeout=1000, verbose=True)
    except:
        continue



















query = ['sel oldu',
         'sel kahramanmaraş',
         'sel bina',
         'sel karadeniz',
         'sel hasar',
         'sel ev hasar',
         'evleri su bastı'
         'su baskını',
         'su baskını afet',
         'sel afet',
         'sel bina zarar',
         'flood',
         'flooding',
         'flood structure damage',
         'flood disaster',
         'flood in florida',
         'flood occurred',
         'flash flood ',
         'flash flood building',
         'flash flood damage'
           ]


for query_string in query:
    try:
        downloader.download(query_string, limit=300, page_limit=3000, output_dir='sel fotolari', adult_filter_off=True, force_replace=False, timeout=1000, verbose=True)
    except:
        continue






















    query = ['binalar',
         'orman türkiye',
         'havuz deniz',
         'rastgele fotolar',
         'rastgele mekanlar',
         'su şehir',
         'bina fotoğrafları'
         'fotoğraflar',
         'manzara',
         '2023 dünya',
         'şehir',
         'people',
         'get',
         'yapılar',
         'mimari',
         'geleneksel mimari',
         'rastgele resimler',
         'fotoğraflar',
         'inşaat işçi',
         'nesneler'
           ]


for query_string in query:
    try:
        downloader.download(query_string, limit=400, page_limit=3000, output_dir='alakasiz fotolar', adult_filter_off=True, force_replace=False, timeout=1000, verbose=True)
    except:
        continue
