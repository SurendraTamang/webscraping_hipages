def get_proxy_list():
    f = open("proxies.txt", "r")
    proxies = f.read().splitlines()
    f.close()
    return proxies

if __name__ == '__main__':
    proxies = get_proxy_list()
    for proxy in proxies:
        proxy_len = proxy.split(':')
        proxy_format = f'{proxy_len[2]}:{proxy_len[3]}@{proxy_len[0]}:{proxy_len[1]}\n'
        with open('st_proxies.txt','a') as fp:
            fp.write(proxy_format)