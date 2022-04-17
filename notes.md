#Notes for 127.0.0.1 scan
<br>
##Active IPs
<br>127.0.0.1
<br>
##127.0.0.1
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html xmlns:fo="http://www.w3.org/1999/XSL/Format">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<!--generated with nmap.xsl - version 0.9c by Benjamin Erb - http://www.benjamin-erb.de/nmap_xsl.php --><style type="text/css">
/* stylesheet print */
@media print
{
  #menu {
    display:none;
  }

  body {
    font-family: Verdana, Helvetica, sans-serif;
  }
  
  h1 {
    font-size: 13pt;
    font-weight:bold;
    margin:4pt 0pt 0pt 0pt;
    padding:0;
  }

  h2 {
    font-size: 12pt;
    font-weight:bold;
    margin:3pt 0pt 0pt 0pt;
    padding:0;
  }

  h3, a:link, a:visited {
    font-size: 9pt;
    font-weight:bold;
    margin:1pt 0pt 0pt 20pt;
    padding:0;
    text-decoration: none;
    color: #000000;
  }

  p,ul {
    font-size: 9pt;
    margin:1pt 0pt 8pt 40pt;
    padding:0;
    text-align:left;
  }

  li {
    font-size: 9pt;
    margin:0;
    padding:0;
    text-align:left;
  }

  table {
    margin:1pt 0pt 8pt 40pt;
    border:0px;
    width:90%
  }

  td {
    border:0px;
    border-top:1px solid black;
    font-size: 9pt;
  }

  .head td {
    border:0px;
    font-weight:bold;
    font-size: 9pt;
  }
  .noprint { display: none; }
}

/* stylesheet screen */
@media screen
{
  body {
    font-family: Verdana, Helvetica, sans-serif;
    margin: 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: center;
  }

  #container {
    text-align:left;
    margin: 10px auto;
    width: 90%;
  }

  h1 {
    font-family: Verdana, Helvetica, sans-serif;
    font-weight:bold;
    font-size: 14pt;
    color: #FFFFFF;
    background-color:#2A0D45;
    margin:10px 0px 0px 0px;
    padding:5px 4px 5px 4px;
    width: 100%;
    border:1px solid black;
    text-align: left;
  }

  h2 {
    font-family: Verdana, Helvetica, sans-serif;
    font-weight:bold;
    font-size: 11pt;
    color: #000000;
    margin:30px 0px 0px 0px;
    padding:4px;
    width: 100%;
    background-color:#F0F8FF;
    text-align: left;
  }

  h2.green {
    color: #000000;
    background-color:#CCFFCC;
    border-color:#006400;
  }

  h2.red {
    color: #000000;
    background-color:#FFCCCC;
    border-color:#8B0000;
  }
   
  h3 {
    font-family: Verdana, Helvetica, sans-serif;
    font-weight:bold;
    font-size: 10pt;
    color:#000000;
    background-color: #FFFFFF;
    width: 75%;
    text-align: left;
  }

  p {
    font-family: Verdana, Helvetica, sans-serif;
    font-size: 8pt;
    color:#000000;
    background-color: #FFFFFF;
    width: 75%;
    text-align: left;
  }

  p i {
    font-family: Verdana, Helvetica, sans-serif;
    font-size: 8pt;
    color:#000000;
    background-color: #CCCCCC;
  }

  ul {
    font-family: Verdana, Helvetica, sans-serif;
    font-size: 8pt;
    color:#000000;
    background-color: #FFFFFF;
    width: 75%;
    text-align: left;
  }

  a {
    font-family: Verdana, Helvetica, sans-serif;
    text-decoration: none;
    font-size: 8pt;
    color:#000000;
    font-weight:bold;
    background-color: #FFFFFF;
    color: #000000;
  }

  li a {
    font-family: Verdana, Helvetica, sans-serif;
    text-decoration: none;
    font-size: 10pt;
    color:#000000;
    font-weight:bold;
    background-color: #FFFFFF;
    color: #000000;
  }

  a:hover {
    text-decoration: underline;
  }

  a.up {
      color:#006400;
  }

  table {
    width: 80%;
    border:0px;
    color: #000000;
    background-color: #000000;
    margin:10px;
  }

  tr {
    vertical-align:top;
    font-family: Verdana, Helvetica, sans-serif;
    font-size: 8pt;
    color:#000000;
    background-color: #FFFFFF;
  }

  tr.head {
    background-color: #E1E1E1;
    color: #000000;
    font-weight:bold;
  }

  tr.open {
    background-color: #CCFFCC;
    color: #000000;
  }
	
  tr.script {
    background-color: #EFFFF7;
    color: #000000;
  }

  tr.filtered {
    background-color: #F2F2F2;
    color: #000000;
  }

  tr.closed {
    background-color: #F2F2F2;
    color: #000000;
  }
    
  td {
    padding:2px;
  }
        
  #menu li {
    display         : inline;
    margin          : 0;
    /*margin-right    : 10px;*/
    padding         : 0;
    list-style-type : none;
  }    
 
  #menubox {
    position: fixed;
    bottom: 0px;
    right: 0px;
    width: 120px;
  }
  
  
  
  /* This section handle's IE's refusal to honor the fixed CSS attribute */
  
  * html div#menubox {
    position: absolute;
    top:expression(eval(
      document.compatMode && document.compatMode=='CSS1Compat') ?
      documentElement.scrollTop+(documentElement.clientHeight-this.clientHeight) 
      : document.body.scrollTop +(document.body.clientHeight-this.clientHeight));
  }
  /* This fixes the jerky effect when scrolling in IE*/
  * html,* html body {
    background: #fff url(nosuchfile) fixed;
  }

  
 
  .up {
    color: #000000;
    background-color:#CCFFCC;
  }
  
  .down {
    color:#626262;
    background-color: #F2F2F2;
  }

  .print_only { display: none; }
  .hidden { display: none; }
  .unhidden { display: block; }
  
}
</style>
<title>Nmap Scan Report - Scanned at Sun Apr 17 20:52:27 2022</title>
<script type="text/javascript">
     
      
                
      function toggle(divID) {
        var item = document.getElementById(divID);
        if (item) {
          item.className=(item.className=='hidden')?'unhidden':'hidden';
        }
      }
           
      function togglePorts(tableID,portState) {
        var table = document.getElementById(tableID);    
        var tbody = table.getElementsByTagName("tbody")[0];
        var rows = tbody.getElementsByTagName("tr");
        for (var i=0; i < rows.length; i++) {
          var value = rows[i].getElementsByTagName("td")[2].firstChild.nodeValue;
          if (value == portState) {
            rows[i].style.display = (rows[i].style.display == 'none')?'':'none';
          }
        }
      }
      
      function toggleAll(portState) {
        var allTables = document.getElementsByTagName("table");
        for (var c=0; c < allTables.length; c++) {
          if (allTables[c].id != "") {
            togglePorts(allTables[c].id, portState)
          }
        }
      }
      
      function init (){
        toggleAll('closed');
        toggleAll('filtered');     
      }     
            
      window.onload = init; 
      
      
    
    </script>
</head>
<body>
<a name="top"></a><div id="container">
<h1>Nmap Scan Report - Scanned at Sun Apr 17 20:52:27 2022</h1>
<ul id="menu">
<li><a href="#scansummary">Scan Summary</a></li>
<li> | <a href="#host_127_0_0_1" class="up">localhost (127.0.0.1)
                  </a>
</li>
</ul>
<a name="scansummary"></a><hr class="print_only">
<h2>Scan Summary</h2>
<p>
      Nmap 7.91 was initiated at Sun Apr 17 20:52:27 2022 with these arguments:<br><i>nmap -sV -sC -T4 -oX temp.xml 127.0.0.1</i><br></p>
<p>
    Verbosity: 0; Debug level 0</p>
<p>Nmap done at Sun Apr 17 20:52:35 2022; 1 IP address (1 host up) scanned in 7.45 seconds</p>
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

##SSH enumeration: <br>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html xmlns:fo="http://www.w3.org/1999/XSL/Format">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<!--generated with nmap.xsl - version 0.9c by Benjamin Erb - http://www.benjamin-erb.de/nmap_xsl.php --><style type="text/css">
/* stylesheet print */
@media print
{
  #menu {
    display:none;
  }

  body {
    font-family: Verdana, Helvetica, sans-serif;
  }
  
  h1 {
    font-size: 13pt;
    font-weight:bold;
    margin:4pt 0pt 0pt 0pt;
    padding:0;
  }

  h2 {
    font-size: 12pt;
    font-weight:bold;
    margin:3pt 0pt 0pt 0pt;
    padding:0;
  }

  h3, a:link, a:visited {
    font-size: 9pt;
    font-weight:bold;
    margin:1pt 0pt 0pt 20pt;
    padding:0;
    text-decoration: none;
    color: #000000;
  }

  p,ul {
    font-size: 9pt;
    margin:1pt 0pt 8pt 40pt;
    padding:0;
    text-align:left;
  }

  li {
    font-size: 9pt;
    margin:0;
    padding:0;
    text-align:left;
  }

  table {
    margin:1pt 0pt 8pt 40pt;
    border:0px;
    width:90%
  }

  td {
    border:0px;
    border-top:1px solid black;
    font-size: 9pt;
  }

  .head td {
    border:0px;
    font-weight:bold;
    font-size: 9pt;
  }
  .noprint { display: none; }
}

/* stylesheet screen */
@media screen
{
  body {
    font-family: Verdana, Helvetica, sans-serif;
    margin: 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: center;
  }

  #container {
    text-align:left;
    margin: 10px auto;
    width: 90%;
  }

  h1 {
    font-family: Verdana, Helvetica, sans-serif;
    font-weight:bold;
    font-size: 14pt;
    color: #FFFFFF;
    background-color:#2A0D45;
    margin:10px 0px 0px 0px;
    padding:5px 4px 5px 4px;
    width: 100%;
    border:1px solid black;
    text-align: left;
  }

  h2 {
    font-family: Verdana, Helvetica, sans-serif;
    font-weight:bold;
    font-size: 11pt;
    color: #000000;
    margin:30px 0px 0px 0px;
    padding:4px;
    width: 100%;
    background-color:#F0F8FF;
    text-align: left;
  }

  h2.green {
    color: #000000;
    background-color:#CCFFCC;
    border-color:#006400;
  }

  h2.red {
    color: #000000;
    background-color:#FFCCCC;
    border-color:#8B0000;
  }
   
  h3 {
    font-family: Verdana, Helvetica, sans-serif;
    font-weight:bold;
    font-size: 10pt;
    color:#000000;
    background-color: #FFFFFF;
    width: 75%;
    text-align: left;
  }

  p {
    font-family: Verdana, Helvetica, sans-serif;
    font-size: 8pt;
    color:#000000;
    background-color: #FFFFFF;
    width: 75%;
    text-align: left;
  }

  p i {
    font-family: Verdana, Helvetica, sans-serif;
    font-size: 8pt;
    color:#000000;
    background-color: #CCCCCC;
  }

  ul {
    font-family: Verdana, Helvetica, sans-serif;
    font-size: 8pt;
    color:#000000;
    background-color: #FFFFFF;
    width: 75%;
    text-align: left;
  }

  a {
    font-family: Verdana, Helvetica, sans-serif;
    text-decoration: none;
    font-size: 8pt;
    color:#000000;
    font-weight:bold;
    background-color: #FFFFFF;
    color: #000000;
  }

  li a {
    font-family: Verdana, Helvetica, sans-serif;
    text-decoration: none;
    font-size: 10pt;
    color:#000000;
    font-weight:bold;
    background-color: #FFFFFF;
    color: #000000;
  }

  a:hover {
    text-decoration: underline;
  }

  a.up {
      color:#006400;
  }

  table {
    width: 80%;
    border:0px;
    color: #000000;
    background-color: #000000;
    margin:10px;
  }

  tr {
    vertical-align:top;
    font-family: Verdana, Helvetica, sans-serif;
    font-size: 8pt;
    color:#000000;
    background-color: #FFFFFF;
  }

  tr.head {
    background-color: #E1E1E1;
    color: #000000;
    font-weight:bold;
  }

  tr.open {
    background-color: #CCFFCC;
    color: #000000;
  }
	
  tr.script {
    background-color: #EFFFF7;
    color: #000000;
  }

  tr.filtered {
    background-color: #F2F2F2;
    color: #000000;
  }

  tr.closed {
    background-color: #F2F2F2;
    color: #000000;
  }
    
  td {
    padding:2px;
  }
        
  #menu li {
    display         : inline;
    margin          : 0;
    /*margin-right    : 10px;*/
    padding         : 0;
    list-style-type : none;
  }    
 
  #menubox {
    position: fixed;
    bottom: 0px;
    right: 0px;
    width: 120px;
  }
  
  
  
  /* This section handle's IE's refusal to honor the fixed CSS attribute */
  
  * html div#menubox {
    position: absolute;
    top:expression(eval(
      document.compatMode && document.compatMode=='CSS1Compat') ?
      documentElement.scrollTop+(documentElement.clientHeight-this.clientHeight) 
      : document.body.scrollTop +(document.body.clientHeight-this.clientHeight));
  }
  /* This fixes the jerky effect when scrolling in IE*/
  * html,* html body {
    background: #fff url(nosuchfile) fixed;
  }

  
 
  .up {
    color: #000000;
    background-color:#CCFFCC;
  }
  
  .down {
    color:#626262;
    background-color: #F2F2F2;
  }

  .print_only { display: none; }
  .hidden { display: none; }
  .unhidden { display: block; }
  
}
</style>
<title>Nmap Scan Report - Scanned at Sun Apr 17 20:52:47 2022</title>
<script type="text/javascript">
     
      
                
      function toggle(divID) {
        var item = document.getElementById(divID);
        if (item) {
          item.className=(item.className=='hidden')?'unhidden':'hidden';
        }
      }
           
      function togglePorts(tableID,portState) {
        var table = document.getElementById(tableID);    
        var tbody = table.getElementsByTagName("tbody")[0];
        var rows = tbody.getElementsByTagName("tr");
        for (var i=0; i < rows.length; i++) {
          var value = rows[i].getElementsByTagName("td")[2].firstChild.nodeValue;
          if (value == portState) {
            rows[i].style.display = (rows[i].style.display == 'none')?'':'none';
          }
        }
      }
      
      function toggleAll(portState) {
        var allTables = document.getElementsByTagName("table");
        for (var c=0; c < allTables.length; c++) {
          if (allTables[c].id != "") {
            togglePorts(allTables[c].id, portState)
          }
        }
      }
      
      function init (){
        toggleAll('closed');
        toggleAll('filtered');     
      }     
            
      window.onload = init; 
      
      
    
    </script>
</head>
<body>
<a name="top"></a><div id="container">
<h1>Nmap Scan Report - Scanned at Sun Apr 17 20:52:47 2022</h1>
<ul id="menu">
<li><a href="#scansummary">Scan Summary</a></li>
<li> | <a href="#host_127_0_0_1" class="up">localhost (127.0.0.1)
                  </a>
</li>
</ul>
<a name="scansummary"></a><hr class="print_only">
<h2>Scan Summary</h2>
<p>
      Nmap 7.91 was initiated at Sun Apr 17 20:52:47 2022 with these arguments:<br><i>nmap --script ssh2-enum-algos.nse,ssh-hostkey.nse -p22 -oX temp.xml 127.0.0.1</i><br></p>
<p>
    Verbosity: 0; Debug level 0</p>
<p>Nmap done at Sun Apr 17 20:52:48 2022; 1 IP address (1 host up) scanned in 0.90 seconds</p>
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
###OpenSSH 2.3 < 7.7 - Username Enumeration<br>

2018-08-21<br>

https://www.exploit-db.com/exploits/45233<br>
