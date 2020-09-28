#!/usr/bin/python

import os
import sys
import time
import socket


def banner():
  a = '''
\033[1;34m***********************************************
*                                              *
*  .d8888b   .d8888b  8888b.  88888b.          *
* .88K      d88P"        "88b 888 "88b         *
* ."Y8888b. 888      .d888888 888  888         *
*       X88 Y88b.    888  888 888  888         *
*   88888P'  "Y8888P "Y888888 888  888         *
*                                              *           
*  Criador: Vitor                              *      
************************************************                  
'''
  return a

def usage():
  us = '''
Usage[+]:
------------------------------------------------
    -all  ==> Tests all ports TCP (0 a 65536)
    -tp ==> Test Top 20 Port(ssh, telnet, ftp...)

Examples:
------------------------------------------------

  ./scan 127.0.0.1 -tp
  ./scan 127.0.0.1 -all

------------------------------------------------
'''
  return us

def start(argv):
  if len(argv) == 2:
    pass
  elif len(argv) <= 1 :
    print banner()
    print usage()
    print "\nERRO: Por favor digite '-all' ou '-tp' para executar os testes\n"
    sys.exit()
  else:
    sys.exit()

  top_ports = False
  all_ports = False

  wordlist = [
      (20,"TCP","FTP"),
      (21,"TCP","FTP"),
      (22,"TCP/UDP","SSH"),
      (23,"TCP/UDP","TELNET"),
      (25,"TCP/UDP","SMTP"),
      (53,"TCP/UDP","DNS"),
      (67,"UDP","DHCP"),
      (68,"UDP","DHCP"),
      (80,"TCP","HTTP"),
      (110,"TCP", "POP3"),
      (123,"UDP","NTP"),
      (156,"TCP/UDP","SQL"),
      (143,"IMAP4"),
      (161,"TCP/UDP","SNMP"),
      (179,"TCP","BGP"),
      (443,"TCP","HTTPS"),
      (1723,"TCP/UDP","TUNEL PPTP"),
      (1863,"TCP","SQUID"),
      (3389,"TCP","TERMINAL SERVER"),
      (3389,"TCP","TERMINAL SERVER")
      ]

  print banner()
 
  if sys.argv[2] == "-all":
    all_ports = True

  elif sys.argv[2] == "-tp":
    top_ports = True
  
  else:
    os.system('clear')
    print banner()
    print usage()
    print "\nERRO: Por favor digite '-d' ou '-tp' para executar os testes\n"
    sys.exit()

  open_ports = []
  if all_ports == True:
    print "scaning ports......\n\n"
    for port in range(1,65536):
      my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      if my_socket.connect_ex((sys.argv[1],port)) == 0:
        my_socket.settimeout(0.1)
        open_ports.append('%s'%(port))
        my_socket.close()     

    if len(open_ports) == 0:
        os.system('clear')
        print banner()
        print "\n Mode: Test All Ports"
        print "================================================="
        print "|| ****** [-] No open door was found [-] ******||"
        print "=================================================\n\n"
    
    else: 
      print "[+] Result of scan: [+]"
      print "------------------------------------------------\n"
      for x in open_ports:  
        print "==============================="
        print "|| PORT: %s -- STATUS[OPEN]  ||"%(x)
        print "==============================="
  
  if top_ports == True:
    for x in wordlist:
      my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      if my_socket.connect_ex((sys.argv[1],x[0])) == 0:
        my_socket.settimeout(0.1)
        open_ports.append(x)
        my_socket.close()
    
    if len(open_ports) == 0:
       os.system('clear')
       print banner()
       print "\n Mode: Test Top 20 ports active......\n"  
       print "================================================="
       print "|| ****** [-] No open door was found [-] ******||"
       print "=================================================\n\n"

    else:
      os.system('clear')
      print banner()
      print "[+] Result of scan: [+]"
      print "-------------------------------------------------------------\n"
      for x in open_ports:
        print "==========================================================="
        print "|| PORT: %s -- STATUS[OPEN] protocol:[%s] service:[%s] ||"%(x[0], x[1], x[2])
        print "==========================================================="

if __name__ == '__main__':
  start(sys.argv[1:])
