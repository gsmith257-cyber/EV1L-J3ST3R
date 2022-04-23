<h1>Notes for 10.10.11.152 scan </h1>
<br>
<h2>Active IPs</h2>
<br>10.10.11.152
<br>
<h2>10.10.11.152</h2>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html xmlns:fo="http://www.w3.org/1999/XSL/Format">
<body>
<a name="top"></a><div id="container">
<h1>Nmap Scan Report - Scanned at Sat Apr 23 18:40:06 2022</h1>
<ul id="menu">
<li><a href="#scansummary">Scan Summary</a></li>
<li> | <a href="#host_10_10_11_152" class="up">timelapse.htb (10.10.11.152)
                  </a>
</li>
</ul>
<a name="scansummary"></a><hr class="print_only">
<h2>Scan Summary</h2>
<p>
      Nmap 7.91 was initiated at Sat Apr 23 18:40:06 2022 with these arguments:<br><i>nmap -sV -sC -T4 -oX temp.xml -Pn 10.10.11.152</i><br></p>
<p>
    Verbosity: 0; Debug level 0</p>
<p>Nmap done at Sat Apr 23 18:41:12 2022; 1 IP address (1 host up) scanned in 65.63 seconds</p>
<hr class="print_only">
<a name="host_10_10_11_152"></a><h2 class="up">10.10.11.152 / timelapse.htb<span class="print_only">(online)</span>
</h2>
<div id="hostblock_10.10.11.152" class="unhidden">
<h3>Address</h3>
<ul><li>10.10.11.152
            (ipv4)
          </li></ul>

<h3>Hostnames</h3>
<ul>
<li>timelapse.htb (PTR)</li>
</ul>
<h3>Ports</h3>
<p>The 989 ports scanned but not shown below are in state: <b>filtered</b></p>
<ul><li><p>989 ports replied with: <b>no-responses</b></p></li></ul>
<table id="porttable_10.10.11.152" cellspacing="1">
<tr class="head">
<td colspan="2">Port</td>
<td>State 
          <a href="javascript:togglePorts('porttable_10.10.11.152','closed');"><span class="noprint"><small> (toggle closed [0] </small></span></a><a href="javascript:togglePorts('porttable_10.10.11.152','filtered');"><span class="noprint"><small> | filtered [0])</small></span></a>
</td>
<td>Service</td>
<td>Reason</td>
<td>Product</td>
<td>Version</td>
<td>Extra info</td>
</tr>


<tr class="open">
<td>53</td>
<td>tcp</td>
<td>open</td>
<td>domain </td>
<td>syn-ack</td>
<td>Simple DNS Plus </td>
<td> </td>
<td> </td>
</tr>
<tr class="open">
<td>88</td>
<td>tcp</td>
<td>open</td>
<td>kerberos-sec </td>
<td>syn-ack</td>
<td>Microsoft Windows Kerberos </td>
<td> </td>
<td>server time: 2022-04-24 01:40:18Z </td>
</tr>
<tr class="open">
<td>135</td>
<td>tcp</td>
<td>open</td>
<td>msrpc </td>
<td>syn-ack</td>
<td>Microsoft Windows RPC </td>
<td> </td>
<td> </td>
</tr>
<tr class="open">
<td>139</td>
<td>tcp</td>
<td>open</td>
<td>netbios-ssn </td>
<td>syn-ack</td>
<td>Microsoft Windows netbios-ssn </td>
<td> </td>
<td> </td>
</tr>
<tr class="open">
<td>389</td>
<td>tcp</td>
<td>open</td>
<td>ldap </td>
<td>syn-ack</td>
<td>Microsoft Windows Active Directory LDAP </td>
<td> </td>
<td>Domain: timelapse.htb0., Site: Default-First-Site-Name </td>
</tr>
<tr class="open">
<td>445</td>
<td>tcp</td>
<td>open</td>
<td>microsoft-ds </td>
<td>syn-ack</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr class="open">
<td>464</td>
<td>tcp</td>
<td>open</td>
<td>kpasswd5 </td>
<td>syn-ack</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr class="open">
<td>593</td>
<td>tcp</td>
<td>open</td>
<td>ncacn_http </td>
<td>syn-ack</td>
<td>Microsoft Windows RPC over HTTP </td>
<td>1.0 </td>
<td> </td>
</tr>
<tr class="open">
<td>636</td>
<td>tcp</td>
<td>open</td>
<td>tcpwrapped </td>
<td>syn-ack</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr class="open">
<td>3268</td>
<td>tcp</td>
<td>open</td>
<td>ldap </td>
<td>syn-ack</td>
<td>Microsoft Windows Active Directory LDAP </td>
<td> </td>
<td>Domain: timelapse.htb0., Site: Default-First-Site-Name </td>
</tr>
<tr class="open">
<td>3269</td>
<td>tcp</td>
<td>open</td>
<td>tcpwrapped </td>
<td>syn-ack</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
</table>
<h3>Host Script Output</h3>
<table>
<tr class="head">
<td>Script Name</td>
<td>Output</td>
</tr>
<tr class="script">
<td>clock-skew </td>
<td><pre>7h59m51s </pre></td>
</tr>
<tr class="script">
<td>smb2-security-mode </td>
<td><pre>
  2.02: 
    Message signing enabled and required </pre></td>
</tr>
<tr class="script">
<td>smb2-time </td>
<td><pre>
  date: 2022-04-24T01:40:23
  start_date: N/A </pre></td>
</tr>
</table>
<br><a href="javascript:toggle('metrics_10.10.11.152');">
    Misc Metrics <span class="noprint"><small> (click to expand)</small></span></a><div id="metrics_10.10.11.152" class="hidden"><table cellspacing="1">
<tr class="head">
<td>Metric</td>
<td>Value</td>
</tr>
<tr>
<td>Ping Results</td>
<td>user-set</td>
</tr>
</table></div>
</div>
</div>
<div id="menubox" class="noprint">
<a href="#top"><small>Go to top</small></a><br><a href="javascript:toggleAll('closed');"><small>Toggle Closed Ports</small></a><br><a href="javascript:toggleAll('filtered');"><small>Toggle Filtered Ports</small></a>
</div>
</body>
</html>

<h2>Samba enumeration: </h2><br>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html xmlns:fo="http://www.w3.org/1999/XSL/Format">
<body>
<a name="top"></a><div id="container">
<h1>Nmap Scan Report - Scanned at Sat Apr 23 18:41:13 2022</h1>
<ul id="menu">
<li><a href="#scansummary">Scan Summary</a></li>
<li> | <a href="#host_10_10_11_152" class="up">timelapse.htb (10.10.11.152)
                  </a>
</li>
</ul>
<a name="scansummary"></a><hr class="print_only">
<h2>Scan Summary</h2>
<p>
      Nmap 7.91 was initiated at Sat Apr 23 18:41:13 2022 with these arguments:<br><i>nmap --script smb-enum-shares.nse,smb-os-discovery.nse,smb-vuln-conficker.nse,smb-vuln-cve2009-3103.nse,smb-vuln-cve-2017-7494.nse,smb-vuln-ms06-025.nse,smb-vuln-ms07-029.nse,smb-vuln-ms08-067.nse,smb-vuln-ms10-054.nse,smb-vuln-ms10-061.nse,smb-vuln-ms17-010.nse,smb-vuln-regsvc-dos.nse,smb-vuln-webexec.nse -p445 -oX temp.xml -Pn 10.10.11.152</i><br></p>
<p>
    Verbosity: 0; Debug level 0</p>
<p>Nmap done at Sat Apr 23 18:41:29 2022; 1 IP address (1 host up) scanned in 16.19 seconds</p>
<hr class="print_only">
<a name="host_10_10_11_152"></a><h2 class="up">10.10.11.152 / timelapse.htb<span class="print_only">(online)</span>
</h2>
<div id="hostblock_10.10.11.152" class="unhidden">
<h3>Address</h3>
<ul><li>10.10.11.152
            (ipv4)
          </li></ul>

<h3>Hostnames</h3>
<ul>
<li>timelapse.htb (PTR)</li>
</ul>
<h3>Ports</h3>
<table id="porttable_10.10.11.152" cellspacing="1">
<tr class="head">
<td colspan="2">Port</td>
<td>State 
          <a href="javascript:togglePorts('porttable_10.10.11.152','closed');"><span class="noprint"><small> (toggle closed [0] </small></span></a><a href="javascript:togglePorts('porttable_10.10.11.152','filtered');"><span class="noprint"><small> | filtered [0])</small></span></a>
</td>
<td>Service</td>
<td>Reason</td>
<td>Product</td>
<td>Version</td>
<td>Extra info</td>
</tr>
<tr class="open">
<td>445</td>
<td>tcp</td>
<td>open</td>
<td>microsoft-ds </td>
<td>syn-ack</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
</table>
<h3>Host Script Output</h3>
<table>
<tr class="head">
<td>Script Name</td>
<td>Output</td>
</tr>
<tr class="script">
<td>smb-vuln-ms10-054 </td>
<td><pre>false </pre></td>
</tr>
<tr class="script">
<td>smb-vuln-ms10-061 </td>
<td><pre>Could not negotiate a connection:SMB: Failed to receive bytes: ERROR </pre></td>
</tr>
</table>
<br><a href="javascript:toggle('metrics_10.10.11.152');">
    Misc Metrics <span class="noprint"><small> (click to expand)</small></span></a><div id="metrics_10.10.11.152" class="hidden"><table cellspacing="1">
<tr class="head">
<td>Metric</td>
<td>Value</td>
</tr>
<tr>
<td>Ping Results</td>
<td>user-set</td>
</tr>
</table></div>
</div>
</div>
<div id="menubox" class="noprint">
<a href="#top"><small>Go to top</small></a><br><a href="javascript:toggleAll('closed');"><small>Toggle Closed Ports</small></a><br><a href="javascript:toggleAll('filtered');"><small>Toggle Filtered Ports</small></a>
</div>
</body>
</html>
<br>
<h2>Exploits found: </h2><br>
<h3>Microsoft Windows - 'RPC DCOM' Remote (Universal)</h3><br>

2003-08-07<br>

https://www.exploit-db.com/exploits/76<br>
<br>
<h3>Microsoft Windows 7/8.1/2008 R2/2012 R2/2016 R2 - 'EternalBlue' SMB Remote Code Execution (MS17-010)</h3><br>

2017-07-11<br>

https://www.exploit-db.com/exploits/42315<br>
<br>
<h3>Microsoft DNS RPC Service - 'extractQuotedChar()' TCP Overflow (MS07-029) (Metasploit)</h3><br>

2010-07-25<br>

https://www.exploit-db.com/exploits/16748<br>
<br>
<h3>Microsoft Windows Server 2008 R2 (x64) - 'SrvOs2FeaToNt' SMB Remote Code Execution (MS17-010)</h3><br>

2017-05-10<br>

https://www.exploit-db.com/exploits/41987<br>
<br>
<h3>Microsoft Windows - Print Spooler Service Impersonation (MS10-061) (Metasploit)</h3><br>

2011-02-17<br>

https://www.exploit-db.com/exploits/16361<br>
<br>
<h3>Microsoft Windows - COM Aggregate Marshaler/IRemUnknown2 Type Confusion Privilege Escalation</h3><br>

2017-05-17<br>

https://www.exploit-db.com/exploits/42020<br>
<br>
<h3>Microsoft Exchange - IIS HTTP Internal IP Address Disclosure (Metasploit)</h3><br>

2014-09-29<br>

https://www.exploit-db.com/exploits/34817<br>
<br>
<h3>Microsoft Windows - NTLM Weak Nonce (MS10-012)</h3><br>

2010-10-17<br>

https://www.exploit-db.com/exploits/15266<br>
<br>
<h3>Microsoft IIS 4.0/5.0 and PWS - Extended Unicode Directory Traversal (4)</h3><br>

2000-10-17<br>

https://www.exploit-db.com/exploits/20301<br>
<br>
<h3>SolarWinds MSP PME Cache Service 1.1.14 - Insecure File Permissions</h3><br>

2020-05-11<br>

https://www.exploit-db.com/exploits/48448<br>
<br>
<h3>Microsoft Message Queueing Service - Path Overflow (MS05-017) (Metasploit)</h3><br>

2010-05-09<br>

https://www.exploit-db.com/exploits/16747<br>
<br>
<h3>Trend Micro Email Encryption Gateway 5.5 (Build 1111.00) - Multiple Vulnerabilities</h3><br>

2018-02-22<br>

https://www.exploit-db.com/exploits/44166<br>
<br>
<h3>Phrack #62</h3><br>

2004-07-13<br>

https://www.exploit-db.com/exploits/42873<br>
<br>
<h3>[eZine] h0no 1</h3><br>

2006-10-02<br>

https://www.exploit-db.com/exploits/13154<br>
<br>
<h3>Phrack #59</h3><br>

2002-07-28<br>

https://www.exploit-db.com/exploits/42870<br>
<br>
<h3>[eZine] Zero For 0wned (ZFO) 5</h3><br>

2009-07-30<br>

https://www.exploit-db.com/exploits/12892<br>
