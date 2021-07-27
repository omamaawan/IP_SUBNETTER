# -*- coding: utf-8 -*-

from socket import *
import ipaddress
from ipaddress import IPv4Address, IPv4Network, IPv4Interface
import ServerUI as gui
import PyQt5
import time
from PyQt5 import QtWidgets
import sys


status = False

def makeGui():
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = gui.Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui.resetbttn.clicked.connect(lambda:works(ui,app))
	MainWindow.show()
	sys.exit(app.exec_())


def works(ui,app):
	global status
	ui.infoEdit.setText("")
	if status == False:
		serverPort = 12000
		serverPort1 = 12001
		ip = '192.168.0.106'
		ui.iplbl.setText(ip)
		serverSocket = socket(AF_INET,SOCK_STREAM)
		serverSocket.bind((ip ,serverPort))
		serverSocket1 = socket(AF_INET,SOCK_STREAM)
		serverSocket1.bind((ip ,serverPort1))
		serverSocket.listen(1)
		serverSocket1.listen(1)
		status = True
		ui.statuslbl.setText("Ready")
		app.processEvents()
		while True:
			
			connectionSocket , addr = serverSocket.accept()
			connectionSocket1 , addr = serverSocket1.accept()
			ipadd = connectionSocket.recv(1024).decode()
			noOfhosts = connectionSocket.recv(1024).decode()
			noOfSubnet = connectionSocket.recv(1024).decode()
			ui.infoEdit.append(ipadd)
			ui.infoEdit.append("\n")
			x=ipaddress.ip_network(ipadd)
			noOfhosts = int(noOfhosts)
			noOfSubnet = int(noOfSubnet)
			currentprefix = x.prefixlen 
			count = 0
			count1 = 0
			a = 1
			b=1
			newprefix = 0
			while a < noOfSubnet:
				a = a*2
				count+=1
			newprefix = currentprefix + count 
			ui.infoEdit.append("Count " + str(count)+'\n')
			ui.infoEdit.append("Current Prefix " + str(currentprefix)+'\n')
			ui.infoEdit.append("New Prefix " + str(newprefix)+'\n')
			if newprefix <= 32:
				while b < noOfhosts:
					b = b*2
					count1 += 1
			newprefix1  = newprefix + count1
			if newprefix1 > 32:
				ui.infoEdit.append('Prefix with Hosts: ' + str(newprefix1)+'\n')
				ui.infoEdit.append('Cannot be subnetted'+'\n')
				connectionSocket1.send(("Cannot be subnetted").encode())
				connectionSocket.close()
				connectionSocket1.close()
				ui.statuslbl.setText("Not Ready")
				status = False
				return
			s1=list(x.subnets(new_prefix=newprefix))
			s12=str(len(s1))
			ui.infoEdit.append('Hosts: {}'.format(noOfhosts)+'\n')
			ui.infoEdit.append('Subnets: {}'.format(noOfSubnet)+'\n')
			ui.infoEdit.append("No of Networks: " + str(len(s1))+'\n')
			connectionSocket1.send(("No of Networks: " + s12 + "\n").encode('utf-8'))
			for s in s1:
				connectionSocket1.send((str(s.with_netmask)+ '\n').encode('utf-8'))
			for s in s1:
				connectionSocket1.send("\n\n".encode('ascii'))
				x=ipaddress.ip_network(s.with_netmask)
				connectionSocket1.send(("No of possible Hosts per subnet: " + str(len(list(x.hosts()))) + "\n").encode('utf-8'))
				for x1 in x.hosts():
					a=str(x1)
					connectionSocket1.send((a + "\n").encode('utf-8'))
			ui.infoEdit.append("The total number of addresses in the network: "+str(x.num_addresses)+'\n')
			# ui.infoEdit.append("Network address: "+str(x.network_address)+'\n')
			connectionSocket.close()
			connectionSocket1.close()
			ui.statuslbl.setText("Not Ready")
			status = False
			app.processEvents()
			return
	else:
		return

if __name__ == "__main__":
	makeGui()