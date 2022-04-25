# EV1L J3ST3R
<div id="header" align="center">
  <img src=https://github.com/gsmith257-cyber/EV1L-J3ST3R/blob/main/skullJester.png />
 </div>
<h2>An automated scanning, enumeration, and note taking tool</h2>
<h2>Created by S1n1st3r</h2>

Meant to help easily go through Hack The Box machine and TryHackMe rooms and take good notes throughout the process.

This tool will run through a subdomain or single IP and scan it with nmap, search for exploits of the services it finds, and print out all the results in a markdown file so you can easily read through.
<div>
Check notes.md for an example output

## Quick start
```bash
# From github
git clone https://github.com/gsmith257-cyber/EV1L-J3ST3R.git
cd EV1L-J3ST3R
sudo apt-get install nikto
sudo apt-get install xsltproc
pip install -r requirements.txt
python3 EV1L_J3ST3R.py
```
<div>

I am working on adding more features and simplifying some of the code so create a pull request if you have any ideas.
