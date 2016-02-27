#! /usr/bin/env python je suis landelin
# -*- coding: Latin-1 -*-

# Définition d'un client réseau rudimentaire
# Ce client dialogue avec un serveur ad hoc

import socket
import datetime

# Exemple d'adresse IP / PORT
# HOST = '1.1.1.1'
# HOST = 'localhost'
# PORT = 60002

HOST = 'ee.lbl.gov'
PORT = 80

# création du socket :
TCP_ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_ClientSocket.connect((HOST, PORT))

# data= raw_input('Enter sentence: ')

# ecriture/lecture au niveau du socket


TCP_ClientSocket.send('HEAD /floyd/index.html HTTP/1.1\r\nHost: ee.lbl.gov\r\n\r\n ')

dataServeur = TCP_ClientSocket.recv(1024)

now = datetime.datetime.now()
print dataServeur, now

TCP_ClientSocket.close()

        
        

