import socks,socket
import random,time,sys,csv

sys.setrecursionlimit(1000)
#socket.setdefaulttimeout(5)
PROXY_PORT = 9050
PORT = 80
BUFFSIZE = 1024
LOCAL_ADDR = "127.0.0.1"
sock = socks.socksocket()
sock.setproxy(socks.PROXY_TYPE_SOCKS5, LOCAL_ADDR, PROXY_PORT)

def connection(value2):
	URL = value2
	try:
		sock = socks.socksocket()
		sock.setproxy(socks.PROXY_TYPE_SOCKS5, LOCAL_ADDR, PROXY_PORT)
		sock.connect((URL, PORT))
		print '[+] ' + URL + ' is Tor Web Site !!!!'		
	except:
		print   '[+] ' + URL + ' is Socket error...'
	finally:
		time.sleep(0.1)
		print 
		return 

def main():
		filename = "url.csv"
		csvfile = open(filename)
		reader = csv.reader(csvfile)
		for row in csv.reader(csvfile):
			#print row
			for elem in row:
				value = elem
				#print "URL of was passed by .. " + value
			connection(value)

if __name__ == '__main__':
	print "_____________________________________________"
	main()	
	print "_____________________________________________"
