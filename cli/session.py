###########################################################
#   File Details
###########################################################
#   Contains the definition and implementation of the Session object.
#   Created by Jason van Hattum - 23/07/2017

from Variable_Handler.variableHandler import *
import socket
from printColors import *
import signal
import sys
from functools import partial

quit_message = "QUIT"


def handle_sigint(session,signal, frame):
        print("Closing CLI..")
        if (session.connected):
            session.close()
        sys.exit(0)

class Session:
    """
    A Session object will contain the variables and operations of the current session,
    as well as the components that can be used.
    """

    def __init__(self, _connectionDetails):
        self.connectionDetails = _connectionDetails
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
        # Handle Ctrl-C
        signal.signal(signal.SIGINT, partial(handle_sigint, self))

    def connectToDaemon(self):
        print("> Attemping to connect to Odin Daemon on {}:{} .. ".format(self.connectionDetails['hostname'], self.connectionDetails['port']),end='')
        try:
            self.socket.connect((self.connectionDetails['hostname'], self.connectionDetails['port']))
        except ConnectionRefusedError:
            return False
        return True

    def sendToDaemon(self, data):
        # print(data)
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

        if len(self.operations) <= 0:
            print("{}There is no point in executing the session - it contains zero operations.{}".format(PrintColors.FAIL, PrintColors.ENDC))
            return

        # Rename output variablee to result
        self.variables.getVariable(self.operations[-1].outputvar).name = 'result'

        toSend = bytearray()
        toSend.extend(map(ord, self.toJson()))
        # Do the sending
        self.sendToDaemon(toSend)
        self.waitForResponse()

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
        json += ';'.join(map(str,self.operations))
        if len(self.operations) > 0:
            json += ';'
        return json

    def close(self):
        if self.connected:
            toSend = bytearray()
            toSend.extend(map(ord, quit_message))
            self.socket.send(toSend)
        self.socket.close()

    def waitForResponse(self):
        print("{}Waiting for response from Daemon...{}".format(PrintColors.OKBLUE, PrintColors.ENDC))
        recvd = ""
        while len(recvd) == 0:
            recvd = self.socket.recv(4096)
        result = json.loads(recvd.decode("utf-8"))
        # print(result)
        if 'errors' in result:
            print("{}Error: {}, {}{}".format(PrintColors.FAIL, result['errors'][0]['status'], result['errors'][0]['details'], PrintColors.ENDC))
        else:
            print("{}Received response: {}{}".format(PrintColors.OKBLUE, result['values'], PrintColors.ENDC))
        self.resetSession()

    def resetSession(self):
        self.operations = []
        self.variables.deleteAll()
