import os
import subprocess
import pycurl
from bs4 import BeautifulSoup
from googlesearch import search
import xml.etree.cElementTree as ET
import ipaddress
from pathlib import Path
import re
import argparse

#todo
#1: make it so SAMBA scan will run based on port numbers open, 139, 445
#2: Fix nikto scan output

#notes:
#1: user input
#2: create md file for report
#3: scan subnet / ip
#4: add active ones to section of report
#5: nmap scan all active IPs
#6: add nmap scans in md format to md report, create a section for each IP
#7: do exploit db search for all services and version numbers running on machines
#8: add exploit-db results to report for each device
#9: attempt inital access with stuff like anonymous login to ftp or samba

def main():
    #get user input
    #get ip or subnet to scan
    print('''                    (                   (                  (     
                 )  )\ )             )  )\ )  *   )     )  )\ )  
 (    (   (   ( /( (()/(     (    ( /( (()/(` )  /(  ( /( (()/(  
 )\   )\  )\  )\()) /(_))    )\   )\()) /(_))( )(_)) )\()) /(_)) 
((_) ((_)((_)((_)\ (_))     ((_) ((_)\ (_)) (_(_()) ((_)\ (_))   
| __|\ \ / /  / (_)| |     _ | ||__ (_)/ __||_   _||__ (_)| _ \  
| _|  \ V /   | |  | |__  | || | |_ \  \__ \  | |   |_ \  |   /  
|___|  \_/    |_|  |____|  \__/ |___/  |___/  |_|  |___/  |_|_\  
                                                                 

''')
    print("Created by: S1n1st3r")

    activeIPs = []                                                   
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type",
                    dest="type",
                    help="The type of scan to run, 1 for subnet, 2 for single IP",
                    action='store',
                    required=True)
    parser.add_argument("-i", "--ip",
                    dest="ip",
                    help="ip address/subnet (without the /24) to scan",
                    action='store',
                    required=True)
    parser.add_argument("-o", "--output",
                    dest="output",
                    help="output file name",
                    action='store')
    parser.add_argument("-s", "--stealth",
                    dest="stealth",
                    help="enable stealth mode, requires root",
                    action='store_true')
    parser.add_argument("-a", "--arp",
                    dest="arp",
                    help="enable arp scan instead of ping sweep",
                    action='store_true')
    
    args = parser.parse_args()
    stealth = args.stealth

    if args.type == "1":
        userInput = args.ip
        if ip_is_valid(userInput):
            print("IP is valid")
            if args.arp:
                print("ARP scan enabled")
                activeIPs = scanARP()
            else:
                activeIPs = scanSubnet(userInput)
        else:
            print("Invalid IP address!")
            quit()
    elif args.type == "2":
        userInput = args.ip
        if ip_is_valid(userInput):
            if ping_ip(userInput):
                print("IP is active")
                activeIPs = [userInput]
            else:
                print("IP is not active")
                quit()
        else:
            print("Invalid IP address!")
            quit()
    else:
        print("Invalid input")
        return

    #create md file for report
    #if output is not specified, use default name
    if args.output is None:
        outputFile = "notes.md"
    else:
        outputFile = args.output
    notesFile = open(outputFile, "w")
    notesFile.write("<h1>Notes for " + userInput + " scan </h1>\n<br>")
    notesFile.close()
    #add active ones to section of report
    notesFile = open(outputFile, "a")
    notesFile.write("\n<h2>Active IPs</h2>\n<br>")
    for ip in activeIPs:
        notesFile.write(ip + "\n<br>")
    notesFile.close()
    #nmap scan all active IPs
    #add nmap scans in md format to md report, create a section for each IP
    listOfServices = nmapScan(activeIPs, outputFile, stealth)
    listOfPorts = getPorts()
    os.remove("temp.xml")
    #attempt inital access with stuff like anonymous login to ftp or samba
    print("Running service enumeration on active IPs")
    for service in listOfServices:
        #if listOfServices contains smb, try smb login
        if "smb" in service or "SMB" in service or '139' in listOfPorts or '445' in listOfPorts:
            for ip in activeIPs:
                SAMBAcheck(ip, outputFile)
        #if listOfServices contains ftp, try ftp login
        if "ftp" in service or "FTP" in service:
            for ip in activeIPs:
                ftpCheck(ip, outputFile)
        #if listOfServices contains http, try http check
        if "http" in service or "HTTP" in service or '80' in listOfPorts or '443' in listOfPorts or '8080' in listOfPorts:
            for ip in activeIPs:
                httpCheck(ip, listOfPorts, outputFile)
        #if listOfServices contains ssh, try ssh check
        if "ssh" in service or "SSH" in service:
            for ip in activeIPs:
                sshCheck(ip, outputFile)
        #if listOfServices contains telnet, try telnet check
        if "telnet" in service or "TELNET" in service:
            for ip in activeIPs:
                telnetCheck(ip, outputFile)
        #if listOfServices contains snmp, try snmp check
        if "snmp" in service or "SNMP" in service:
            for ip in activeIPs:
                snmpCheck(ip, outputFile)
        #if mysql is in listOfServices, try mysql check
        if "mysql" in service or "MYSQL" in service:
            for ip in activeIPs:
                mysqlCheck(ip, outputFile)
        #if listOfServices contains icmp, try icmp check
        if "icmp" in service or "ICMP" in service:
            for ip in activeIPs:
                icmpCheck(ip, outputFile)
        #if listOfServices contains dns, try dns check
        if "dns" in service or "DNS" in service:
            for ip in activeIPs:
                dnsCheck(ip, outputFile)
        #if listOfServices contains smtp, try smtp check
        if "smtp" in service or "SMTP" in service:
            for ip in activeIPs:
                smtpCheck(ip, outputFile)
        #if listOfServices contains pop3, try pop3 check
        if "pop3" in service or "POP3" in service:
            for ip in activeIPs:
                pop3Check(ip, outputFile)
    #do exploit db search for all services and version numbers running on machines
    #add exploit-db results to report for each device
    print("Running exploit-db search on active IPs")
    searchExploitDB(listOfServices, outputFile)
    print("Completed successfully")

# this function will validate a given IP address
# and return True or False based on the validation result
def ip_is_valid(ip):
    try:
        ipaddress.IPv4Network(ip)
        return True
    except Exception as e:
        return False

def ping_ip(ip):
    #ping IP
    DEVNULL = open(os.devnull, 'w')
    try:
        response = os.popen(f"ping -c 2 {ip}").read()
        if "Received = 4" in response:
            return False
        else:
            return True
    except Exception:
            return False

def scanSubnet(subnet):
    DEVNULL = open(os.devnull,'w')
    list = []
    for ping in range(1,255):
        address = subnet[:-1] + str(ping)
        res = subprocess.call(['ping', '-c', '1', address], stdout=DEVNULL)
        if res == 0:
            print("ping to", address, "OK")
            list.append(address)
        elif res == 2:
            print("no response from", address)
        else:
            print("ping to", address, "failed!")
    return list

def scanARP():
    results = []
    output = os.popen('arp -a > temp').read()
    #get just the ip address from the arp scan output
    for line in output:
        if "incomplete" in line:
            output.remove(line)
        results += re.match("(?:[0-9]{1,3}\.){3}[0-9]{1,3}", line)
    print(results) #remove this
    return results

def getServiceListOutput():
    servicesList = []
    tree = ET.parse('temp.xml')
    root = tree.getroot()
    for item in list(root):
        if item.tag == 'host':
            for child in list(item):
                if child.tag == 'ports':
                    for port in list(child):
                        if port.tag == 'port':
                            for service in list(port):
                                if service.tag == 'service':
                                    try:
                                        servicesList.append(service.attrib['product'] + ' ' + service.attrib['version'])
                                    except KeyError:
                                        pass
    return servicesList

def getPorts():
    portsList = []
    tree = ET.parse('temp.xml')
    root = tree.getroot()
    for item in list(root):
        if item.tag == 'host':
            for child in list(item):
                if child.tag == 'ports':
                    for port in list(child):
                        if port.tag == 'port':
                                try:
                                    portsList.append(port.attrib['portid'])
                                except KeyError:
                                    pass
    return portsList

def cleanMDfile():
    datafile = []
    # if the temp.md file doesn't exist, create an empty file to avoid errors
    tmp_file = Path('temp.md')
    tmp_file.touch(exist_ok=True)
    file = open('temp.md', 'r')
    # delete matching content and 326 lines after
    currentLine = 0
    content = "<head>"
    datafile = file.readlines()
    for line in datafile:
        if content in line:
            lines = currentLine
            while currentLine < (lines + 327):
                datafile[currentLine] = ""
                currentLine += 1
        else:
            currentLine += 1
    file.close()
    file2 = open('temp.md', 'w')
    file2.writelines(datafile)
    file2.close()
        

def nmapScan(ipList, outputFile, stealth):
    #nmap scan all active IPs
    #add nmap scans in md format to md report, create a section for each IP
    print("Nmap scan started")
    
    for ip in ipList:
        if stealth:
            cmd = "nmap -sS -P0 -T2 -oX temp.xml " + ip + " -Pn > /dev/null"
        else:
            cmd = "nmap -sV -sC -T4 -oX temp.xml " + ip + " -Pn > /dev/null"
        os.system(cmd)
        print("Nmap scan for " + ip + " complete")    
        #convert to markdown and add to notes file
        cmd = "xsltproc temp.xml -o temp.md"
        os.system(cmd)
        cleanMDfile()
        notesFile = open(outputFile, "a")
        notesFile.write("\n<h2>" + ip + "</h2>\n")
        with open("temp.md") as f:
            for line in f:
                notesFile.write(line)
        listOfServices = getServiceListOutput()
        #remove temp file
        os.remove("temp.md")
    print("Nmap scan complete")
    return listOfServices

class ContentCallback:
    def __init__(self):
        self.contents = ''

    def content_callback(self, buf):
        self.contents = self.contents + str(buf)

def searchExploitDB(services, outputFile):
    #do exploit db search for all services and version numbers running on machines
    notesFile = open(outputFile, "a")
    notesFile.write("<br>\n<h2>Exploits found: </h2>")
    notesFile.close()
    for service in services:
        try:
            query = service + ' ' + 'site:https://www.exploit-db.com'
            for data in search(query, tld='com', num=10, start=0, stop=25, pause=2):
                if "https://www.exploit-db.com/exploits" in data:
                    t = ContentCallback()
                    curlObj = pycurl.Curl()
                    curlObj.setopt(curlObj.URL, '{}'.format(data))
                    curlObj.setopt(curlObj.WRITEFUNCTION, t.content_callback)
                    curlObj.perform()
                    curlObj.close()
                    #url = data 
                    soup = BeautifulSoup(t.contents,'lxml')
                    desc = soup.find("meta", property="og:title")
                    publish = soup.find("meta", property="article:published_time")
                    #write results to md file
                    notesFile = open(outputFile, "a")
                    notesFile.write("<br>\n<h3>" + desc.get('content') + "</h3><br>\n")
                    notesFile.write("\n" + publish.get('content') + "<br>\n")
                    notesFile.write("\n" + data + "<br>\n")
                    notesFile.close()

        except Exception as e:
            print("Error connecting to ExploitDB")
            # print(e)
    
def SAMBAcheck(ip, outputFile):
    #check if samba is running on machine
    if ping_ip(ip):
        cmd = "nmap --script smb-enum-shares.nse,smb-os-discovery.nse,smb-vuln-conficker.nse,smb-vuln-cve2009-3103.nse,smb-vuln-cve-2017-7494.nse,smb-vuln-ms06-025.nse,smb-vuln-ms07-029.nse,smb-vuln-ms08-067.nse,smb-vuln-ms10-054.nse,smb-vuln-ms10-061.nse,smb-vuln-ms17-010.nse,smb-vuln-regsvc-dos.nse,smb-vuln-webexec.nse -p445 -oX temp.xml " + ip + " -Pn > /dev/null"
        os.system(cmd)
        #convert to markdown and add to notes file
        cmd = "xsltproc temp.xml -o temp.md"
        os.system(cmd)
        cleanMDfile()
        notesFile = open(outputFile, "a")
        with open("temp.md") as f:
            notesFile.write("\n<h2>Samba enumeration: </h2><br>\n")
            for line in f:
                notesFile.write(line)
        notesFile.close()
        #remove temp files
        os.remove("temp.xml")
        os.remove("temp.md")

def ftpCheck(ip, outputFile):
    #check if ftp is running on machine
    if ping_ip(ip):
        cmd = "nmap --script ftp-anon.nse,ftp-banner.nse,ftp-proftpd-backdoor.nse,ftp-vsftpd-backdoor.nse -p21 -oX temp.xml " + ip + " -Pn > /dev/null"
        os.system(cmd)
        #convert to markdown and add to notes file
        cmd = "xsltproc temp.xml -o temp.md"
        os.system(cmd)
        cleanMDfile()
        notesFile = open(outputFile, "a")
        with open("temp.md") as f:
            notesFile.write("\n<h2>FTP enumeration: </h2><br>\n")
            for line in f:
                notesFile.write(line)
        notesFile.close()
        #remove temp files
        os.remove("temp.xml")
        os.remove("temp.md")

def httpCheck(ip, ports, outputFile):
    #check if http is running on machine
    if ping_ip(ip):
        for port in ports:
            if port == "80" or port == "443" or port == "8080":
                cmd = "nikto -o temp.xml -Format xml --host http://" + ip + " -p " + port + " > /dev/null"
                os.system(cmd)
                #convert to markdown and add to notes file
                notesFile = open("temp.md", "w")
                notesFile.write("\n<h2>HTTP enumeration: </h2><br>\n")
                with open("temp.xml") as f:
                    for line in f:
                        notesFile.write(line)
                notesFile.close()
                cleanMDfile()
                notesFile = open(outputFile, "a")
                with open("temp.md") as f:
                    notesFile.write("\n")
                    for line in f:
                        notesFile.write(line)
                notesFile.close()
                #remove temp files
                os.remove("temp.xml")
                os.remove("temp.md")

def sshCheck(ip, outputFile):
    #check if ssh is running on machine
    if ping_ip(ip):
        cmd = "nmap --script ssh2-enum-algos.nse,ssh-hostkey.nse -p22 -oX temp.xml " + ip + " -Pn > /dev/null"
        os.system(cmd)
        #convert to markdown and add to notes file
        cmd = "xsltproc temp.xml -o temp.md"
        os.system(cmd)
        cleanMDfile()
        notesFile = open(outputFile, "a")
        with open("temp.md") as f:
            notesFile.write("\n<h2>SSH enumeration: </h2><br>\n")
            for line in f:
                notesFile.write(line)
        notesFile.close()
        #remove temp files
        os.remove("temp.xml")
        os.remove("temp.md")

def telnetCheck(ip, outputFile):
    #check if telnet is running on machine
    if ping_ip(ip):
        cmd = "nmap --script telnet-encryption.nse -p23 -oX temp.xml " + ip + " -Pn > /dev/null"
        os.system(cmd)
        #convert to markdown and add to notes file
        cmd = "xsltproc temp.xml -o temp.md"
        os.system(cmd)
        cleanMDfile()
        notesFile = open(outputFile, "a")
        with open("temp.md") as f:
            notesFile.write("\n<h2>Telnet enumeration: </h2><br>\n")
            for line in f:
                notesFile.write(line)
        notesFile.close()
        #remove temp files
        os.remove("temp.xml")
        os.remove("temp.md")

def snmpCheck(ip, outputFile):
    #check if snmp is running on machine
    if ping_ip(ip):
        cmd = "nmap --script snmp-netstat.nse,snmp-processes.nse,snmp-sysdescr.nse,snmp-win32-services.nse -p161 -oX temp.xml " + ip + " -Pn > /dev/null"
        os.system(cmd)
        #convert to markdown and add to notes file
        cmd = "xsltproc temp.xml -o temp.md"
        os.system(cmd)
        cleanMDfile()
        notesFile = open(outputFile, "a")
        with open("temp.md") as f:
            notesFile.write("\n<h2>SNMP enumeration: </h2><br>\n")
            for line in f:
                notesFile.write(line)
        notesFile.close()
        #remove temp files
        os.remove("temp.xml")
        os.remove("temp.md")

def mysqlCheck(ip, outputFile):
    #check if mysql is running on machine
    if ping_ip(ip):
        cmd = "nmap --script mysql-enum.nse -p3306 -oX temp.xml " + ip + " -Pn > /dev/null"
        os.system(cmd)
        #convert to markdown and add to notes file
        cmd = "xsltproc temp.xml -o temp.md"
        os.system(cmd)
        cleanMDfile()
        notesFile = open(outputFile, "a")
        with open("temp.md") as f:
            notesFile.write("\n<h2>MySQL enumeration: </h2><br>\n")
            for line in f:
                notesFile.write(line)
        notesFile.close()
        #remove temp files
        os.remove("temp.xml")
        os.remove("temp.md")

def icmpCheck(ip, outputFile):
    #check if icmp is running on machine
    if ping_ip(ip):
        cmd = "nmap --script icmp-echo.nse -p icmp -oX temp.xml " + ip + " -Pn > /dev/null"
        os.system(cmd)
        #convert to markdown and add to notes file
        cmd = "xsltproc temp.xml -o temp.md"
        os.system(cmd)
        cleanMDfile()
        notesFile = open(outputFile, "a")
        with open("temp.md") as f:
            notesFile.write("\n<h2>ICMP enumeration: </h2><br>\n")
            for line in f:
                notesFile.write(line)
        notesFile.close()
        #remove temp files
        os.remove("temp.xml")
        os.remove("temp.md")

def smtpCheck(ip, outputFile):
    #check if smtp is running on machine
    if ping_ip(ip):
        cmd = "nmap --script smtp-commands.nse,smtp-enum-users.nse,smtp-open-relay.nse -p25 -oX temp.xml " + ip + " -Pn > /dev/null"
        os.system(cmd)
        #convert to markdown and add to notes file
        cmd = "xsltproc temp.xml -o temp.md"
        os.system(cmd)
        cleanMDfile()
        notesFile = open(outputFile, "a")
        with open("temp.md") as f:
            notesFile.write("\n<h2>SMTP enumeration: </h2><br>\n")
            for line in f:
                notesFile.write(line)
        notesFile.close()
        #remove temp files
        os.remove("temp.xml")
        os.remove("temp.md")

def dnsCheck(ip, outputFile):
    #check if dns is running on machine
    if ping_ip(ip):
        cmd = "nmap --script dns-recursion.nse,dns-zone-transfer.nse -p53 -oX temp.xml " + ip + " -Pn > /dev/null"
        os.system(cmd)
        #convert to markdown and add to notes file
        cmd = "xsltproc temp.xml -o temp.md"
        os.system(cmd)
        cleanMDfile()
        notesFile = open(outputFile, "a")
        with open("temp.md") as f:
            notesFile.write("\n<h2>DNS enumeration: </h2><br>\n")
            for line in f:
                notesFile.write(line)
        notesFile.close()
        #remove temp files
        os.remove("temp.xml")
        os.remove("temp.md")

def pop3Check(ip, outputFile):
    #check if pop3 is running on machine
    if ping_ip(ip):
        cmd = "nmap --script pop3-capabilities.nse,pop3-enum-users.nse -p110 -oX temp.xml " + ip + " -Pn > /dev/null"
        os.system(cmd)
        #convert to markdown and add to notes file
        cmd = "xsltproc temp.xml -o temp.md"
        os.system(cmd)
        cleanMDfile()
        notesFile = open(outputFile, "a")
        with open("temp.md") as f:
            notesFile.write("\n<h2>POP3 enumeration: </h2><br>\n")
            for line in f:
                notesFile.write(line)
        notesFile.close()
        #remove temp files
        os.remove("temp.xml")
        os.remove("temp.md")


    
main()