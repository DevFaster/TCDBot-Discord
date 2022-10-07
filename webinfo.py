from socket import gethostbyname

def toIp(domain):
    return gethostbyname(domain)

def ipInfo(addr=''):
    from urllib.request import urlopen
    from json import load
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    data = load(res)
    print(len(data))
    for attr in data.keys():
        print(attr,' '*13+'\t->\t',data[attr])
    
    return data

