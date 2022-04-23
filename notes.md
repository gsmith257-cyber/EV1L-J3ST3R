<h1>Notes for 127.0.0.1 scan </h1>
<br>
<h2>Active IPs</h2>
<br>127.0.0.1
<br>
<h2>127.0.0.1</h2>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html xmlns:fo="http://www.w3.org/1999/XSL/Format">
<body>
<a name="top"></a><div id="container">
<h1>Nmap Scan Report - Scanned at Sat Apr 23 03:39:11 2022</h1>
<ul id="menu">
<li><a href="#scansummary">Scan Summary</a></li>
<li> | <a href="#host_127_0_0_1" class="up">localhost (127.0.0.1)
                  </a>
</li>
</ul>
<a name="scansummary"></a><hr class="print_only">
<h2>Scan Summary</h2>
<p>
      Nmap 7.91 was initiated at Sat Apr 23 03:39:11 2022 with these arguments:<br><i>nmap -sV -sC -T4 -oX temp.xml 127.0.0.1</i><br></p>
<p>
    Verbosity: 0; Debug level 0</p>
<p>Nmap done at Sat Apr 23 03:39:19 2022; 1 IP address (1 host up) scanned in 7.42 seconds</p>
<hr class="print_only">
<a name="host_127_0_0_1"></a><h2 class="up">127.0.0.1 / localhost<span class="print_only">(online)</span>
</h2>
<div id="hostblock_127.0.0.1" class="unhidden">
<h3>Address</h3>
<ul><li>127.0.0.1
            (ipv4)
          </li></ul>

<h3>Hostnames</h3>
<ul>
<li>localhost (PTR)</li>
</ul>
<h3>Ports</h3>
<p>The 998 ports scanned but not shown below are in state: <b>closed</b></p>
<ul><li><p>998 ports replied with: <b>conn-refused</b></p></li></ul>
<table id="porttable_127.0.0.1" cellspacing="1">
<tr class="head">
<td colspan="2">Port</td>
<td>State 
          <a href="javascript:togglePorts('porttable_127.0.0.1','closed');"><span class="noprint"><small> (toggle closed [0] </small></span></a><a href="javascript:togglePorts('porttable_127.0.0.1','filtered');"><span class="noprint"><small> | filtered [0])</small></span></a>
</td>
<td>Service</td>
<td>Reason</td>
<td>Product</td>
<td>Version</td>
<td>Extra info</td>
</tr>


<tr class="open">
<td>22</td>
<td>tcp</td>
<td>open</td>
<td>ssh </td>
<td>syn-ack</td>
<td>OpenSSH </td>
<td>8.4p1 Debian 5 </td>
<td>protocol 2.0 </td>
</tr>
<tr class="script">
<td></td>
<td>ssh-hostkey </td>
<td colspan="6"><pre>
  3072 14:23:6f:2d:ab:fc:e7:b9:a4:f4:8b:c2:4e:15:9b:07 (RSA)
  256 bd:81:7a:9d:6e:f2:2d:e0:50:03:01:04:01:2f:a1:97 (ECDSA)
  256 9f:cf:53:e1:41:b1:29:c4:40:c4:db:a5:1a:7b:40:73 (ED25519) </pre></td>
</tr>
<tr class="open">
<td>111</td>
<td>tcp</td>
<td>open</td>
<td>rpcbind </td>
<td>syn-ack</td>
<td> </td>
<td>2-4 </td>
<td>RPC #100000 </td>
</tr>
<tr class="script">
<td></td>
<td>rpcinfo </td>
<td colspan="6"><pre>
  program version    port/proto  service
  100000  2,3,4        111/tcp   rpcbind
  100000  2,3,4        111/udp   rpcbind
  100000  3,4          111/tcp6  rpcbind
  100000  3,4          111/udp6  rpcbind
 </pre></td>
</tr>
</table>

<br><a href="javascript:toggle('metrics_127.0.0.1');">
    Misc Metrics <span class="noprint"><small> (click to expand)</small></span></a><div id="metrics_127.0.0.1" class="hidden"><table cellspacing="1">
<tr class="head">
<td>Metric</td>
<td>Value</td>
</tr>
<tr>
<td>Ping Results</td>
<td>conn-refused</td>
</tr>
</table></div>
</div>
</div>
<div id="menubox" class="noprint">
<a href="#top"><small>Go to top</small></a><br><a href="javascript:toggleAll('closed');"><small>Toggle Closed Ports</small></a><br><a href="javascript:toggleAll('filtered');"><small>Toggle Filtered Ports</small></a>
</div>
</body>
</html>

<h2>SSH enumeration: </h2><br>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html xmlns:fo="http://www.w3.org/1999/XSL/Format">
<body>
<a name="top"></a><div id="container">
<h1>Nmap Scan Report - Scanned at Sat Apr 23 03:39:20 2022</h1>
<ul id="menu">
<li><a href="#scansummary">Scan Summary</a></li>
<li> | <a href="#host_127_0_0_1" class="up">localhost (127.0.0.1)
                  </a>
</li>
</ul>
<a name="scansummary"></a><hr class="print_only">
<h2>Scan Summary</h2>
<p>
      Nmap 7.91 was initiated at Sat Apr 23 03:39:20 2022 with these arguments:<br><i>nmap --script ssh2-enum-algos.nse,ssh-hostkey.nse -p22 -oX temp.xml 127.0.0.1</i><br></p>
<p>
    Verbosity: 0; Debug level 0</p>
<p>Nmap done at Sat Apr 23 03:39:21 2022; 1 IP address (1 host up) scanned in 1.11 seconds</p>
<hr class="print_only">
<a name="host_127_0_0_1"></a><h2 class="up">127.0.0.1 / localhost<span class="print_only">(online)</span>
</h2>
<div id="hostblock_127.0.0.1" class="unhidden">
<h3>Address</h3>
<ul><li>127.0.0.1
            (ipv4)
          </li></ul>

<h3>Hostnames</h3>
<ul>
<li>localhost (PTR)</li>
</ul>
<h3>Ports</h3>
<table id="porttable_127.0.0.1" cellspacing="1">
<tr class="head">
<td colspan="2">Port</td>
<td>State 
          <a href="javascript:togglePorts('porttable_127.0.0.1','closed');"><span class="noprint"><small> (toggle closed [0] </small></span></a><a href="javascript:togglePorts('porttable_127.0.0.1','filtered');"><span class="noprint"><small> | filtered [0])</small></span></a>
</td>
<td>Service</td>
<td>Reason</td>
<td>Product</td>
<td>Version</td>
<td>Extra info</td>
</tr>
<tr class="open">
<td>22</td>
<td>tcp</td>
<td>open</td>
<td>ssh </td>
<td>syn-ack</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr class="script">
<td></td>
<td>ssh-hostkey </td>
<td colspan="6"><pre>
  3072 14:23:6f:2d:ab:fc:e7:b9:a4:f4:8b:c2:4e:15:9b:07 (RSA)
  256 bd:81:7a:9d:6e:f2:2d:e0:50:03:01:04:01:2f:a1:97 (ECDSA)
  256 9f:cf:53:e1:41:b1:29:c4:40:c4:db:a5:1a:7b:40:73 (ED25519) </pre></td>
</tr>
<tr class="script">
<td></td>
<td>ssh2-enum-algos </td>
<td colspan="6"><pre>
  kex_algorithms: (9)
      curve25519-sha256
      curve25519-sha256@libssh.org
      ecdh-sha2-nistp256
      ecdh-sha2-nistp384
      ecdh-sha2-nistp521
      diffie-hellman-group-exchange-sha256
      diffie-hellman-group16-sha512
      diffie-hellman-group18-sha512
      diffie-hellman-group14-sha256
  server_host_key_algorithms: (5)
      rsa-sha2-512
      rsa-sha2-256
      ssh-rsa
      ecdsa-sha2-nistp256
      ssh-ed25519
  encryption_algorithms: (6)
      chacha20-poly1305@openssh.com
      aes128-ctr
      aes192-ctr
      aes256-ctr
      aes128-gcm@openssh.com
      aes256-gcm@openssh.com
  mac_algorithms: (10)
      umac-64-etm@openssh.com
      umac-128-etm@openssh.com
      hmac-sha2-256-etm@openssh.com
      hmac-sha2-512-etm@openssh.com
      hmac-sha1-etm@openssh.com
      umac-64@openssh.com
      umac-128@openssh.com
      hmac-sha2-256
      hmac-sha2-512
      hmac-sha1
  compression_algorithms: (2)
      none
      zlib@openssh.com </pre></td>
</tr>
</table>

<br><a href="javascript:toggle('metrics_127.0.0.1');">
    Misc Metrics <span class="noprint"><small> (click to expand)</small></span></a><div id="metrics_127.0.0.1" class="hidden"><table cellspacing="1">
<tr class="head">
<td>Metric</td>
<td>Value</td>
</tr>
<tr>
<td>Ping Results</td>
<td>conn-refused</td>
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
##Exploits found: <br>
<h3>OpenSSH 2.3 < 7.7 - Username Enumeration</h3><br>

2018-08-21<br>

https://www.exploit-db.com/exploits/45233<br>
