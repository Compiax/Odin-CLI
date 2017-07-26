###########################################################
#   File Details
###########################################################
#   Contains the definition and implementation of the Session object.
#   Created by Jason van Hattum - 23/07/2017

from Variable_Handler.variableHandler import *
import socket
from printColors import *

class Session:
    """
    A Session object will contain the variables and operations of the current session,
    as well as the components that can be used.
    """

    def __init__(self):
        self.variables = VariableHandler()
        self.operations = []
        self.components = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.connectToDaemon():
            print("{}connected{}".format(PrintColors.OKBLUE, PrintColors.ENDC))
            self.connected = True
        else:
            print("{}unable to connect - running in offline mode{}".format(PrintColors.FAIL, PrintColors.ENDC))
            self.connected = False
    
    def connectToDaemon(self):
        connectionDetails = {'hostname': 'localhost', 'port':8000}
        print("> Attemping to connect to Odin Daemon on {}:{} .. ".format(connectionDetails['hostname'], connectionDetails['port']),end='')
        try:
            self.socket.connect((connectionDetails['hostname'], connectionDetails['port']))
        except ConnectionRefusedError:            
            return False
        return True

    def sendToDaemon(self, data):
        amountToSend = len(data)
        if (amountToSend == 0):
            print("> {}Nothing to send to the Daemon - session is empty{}".format(PrintColors.FAIL, PrintColors.ENDC))
            return
        print("> Sending {} bytes to the Daemon.. ".format(amountToSend), end='')

        totalsent = 0
        while totalsent < amountToSend:
            sent = self.socket.send(data[totalsent:])
            if sent == 0:
                print("{}Failed - Deamon connection broken{}".format(PrintColors.FAIL, PrintColors.ENDC))
                self.connected = false
                return
            totalsent = totalsent + sent
        print("{}{} variable(s) and {} operation(s) sent to Daemon.{}".format(
            PrintColors.OKBLUE,
            len(self.variables.list),
            len(self.operations),
            PrintColors.ENDC
        ))

    def execute(self):
        """
        Executes the session, sending all variables and operations to the Daemon
        """
        if (not self.connected):
            if (self.connectToDaemon()):
                print("{}connected{}".format(PrintColors.OKBLUE, PrintColors.ENDC))
                self.connected = True
            else:
                print("{}unable to connect - cannot execute the session{}".format(PrintColors.FAIL, PrintColors.ENDC))
                self.connected = False
                return

        toSend = bytearray()
        toSend.extend(map(ord, self.toJson()))
        # Do the sending
        # self.connectToDaemon()
        self.sendToDaemon(toSend)

    def print(self):
        print("Variables:")
        for var in self.variables.list:
            print("- {}".format(var.convertToJson()))
        print("Operations:")
        for op in self.operations:
            print("- {}".format(op))
    
    def toJson(self):
        json = '\n'.join(map(lambda x: x.convertToJson(),self.variables.list))
        if len(json) > 0:
            json += '\n'  # Could also add some other separater between the variables and the commands
        json += '\n'.join(map(str,self.operations))
        return json


    