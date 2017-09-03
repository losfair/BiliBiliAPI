from ._Imports import requests, re

header = {}


def getVideoStat(aid: int) -> dict:
    """
    data={
        'aid': int, 
        'view': int, 
        'danmaku': int, 
        'reply': int, 
        'favorite': int, 
        'coin': int, 
        'share': int, 
        'now_rank': int, 
        'his_rank': int, 
        'no_reprint': int, 
        'copyright': int
    }
    """
    api_pattern = 'https://api.bilibili.com/x/web-interface/archive/stat?aid={}'
    url = api_pattern.format(aid)
    stat = requests.get(url, headers=header)
    if stat.status_code != 200: return {}
    stat = stat.content.decode('utf8')
    data = re.compile('"data":{.+?}').findall(stat)
    if data == []: return {}
    data = data[0][7:]
    data = eval(data)
    return data
