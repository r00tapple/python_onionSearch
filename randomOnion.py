import socks,socket
import random,time,sys

sys.setrecursionlimit(1000)
sock = socks.socksocket()
PROXY_PORT = 9050 
PORT = 80
BUFFSIZE = 1024
LOCAL_ADDR = "127.0.0.1"

def makingurl():
    source_str = 'abcdefghijklmnopqrstuvwxyz234567'
    name = "".join([random.choice(source_str) for x in xrange(16)])
    url = name + ".onion"
    return  url
    
def connection():
    URL = makingurl()
    try:
        sock = socks.socksocket()
        sock.setproxy(socks.PROXY_TYPE_SOCKS5, LOCAL_ADDR, PROXY_PORT)
        sock.connect((URL, PORT))
        print
        print
        print "Connection Tor Web Site !!"
        print "[+]" + URL
        print
        print
        sock.close()
    except:
        print "Address-related error connecting to server:" + URL
    finally:
		time.sleep(0.1)
		return 

def main():
    while 1:
        connection()

if __name__ == '__main__':
	print "_____________________________________________"
	main()
	print "_____________________________________________"
