import socks

def get_proxy(proxy):
    return (socks.SOCKS5, proxy['addr'], proxy['port'], True, proxy['username'],
        proxy['password'])
