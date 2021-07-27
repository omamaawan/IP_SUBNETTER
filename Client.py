
from socket import *
import ClientUI as gui
import PyQt5 
from PyQt5 import QtWidgets
import sys

status = False


def makeGui():
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = gui.Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui.sendBttn.clicked.connect(lambda:sWorks(ui,app))

	MainWindow.show()
	sys.exit(app.exec_())

def sWorks(ui,app,tex = ''):
	ui.browser.setText(tex)
	bass = []
	bass = works(ui,app)
	str1 = "[ "
	for i in bass:
    		str1 += str(i)+' '
	str1 += ']'	
	ui.browser.append(str1)

	


def works(ui,app):
	global status
	ip = '192.168.0.106'
	serverPort = (ip,12000)
	serverPort1 = (ip,12001)
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect(serverPort)
	clientSocket1 = socket(AF_INET, SOCK_STREAM)
	clientSocket1.connect(serverPort1)
	status = True
	bass = []
	ipadd = ui.ipedit.text()
	requiredClients = ui.hostedit.text()
	requiredNetworks = ui.netedit.text()
	bass.append(ipadd)
	clientSocket.send(ipadd.encode())
	bass.append(requiredClients)
	clientSocket.send(requiredClients.encode())
	bass.append(requiredNetworks)
	clientSocket.send(requiredNetworks.encode())
	while(True): 
		data = clientSocket1.recv(4096)
		ui.browser.append(data.decode())
		if data.decode() == "Cannot be subnetted":
			clientSocket.close()
			clientSocket1.close()
			status = False
			return bass
		if not data: 
			break
	clientSocket.close()
	clientSocket1.close()
	status = False
	return bass
makeGui()