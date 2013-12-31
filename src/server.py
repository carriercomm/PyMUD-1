#!/usr/bin/env python
# vim: tabstop=4 : expandtab : shiftwidth=4

from __future__ import division
import socket, threading, re, urllib

import player
import color


class Server:
    """ Sets up connection and listening for player login """

    port = 1030
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__ (self, logcallback = None):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.log = logcallback
        self.locIP = None
        self.extIP = None
        
        self.world = None

    def localIP (self, ifname = 'lo'):
        """ Return: local IP """

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 0))
            sname = s.getsockname()[0]
            s.shutdown(socket.SHUT_RDWR)
            s.close()
            return sname
        except socket.gaierror, msg:
            print msg
            print (
                color.red + "No router connection. "
                "Server running on localhost only." + color.reset)
        except:
          print "Unable to connect to 8.8.8.8 -- Hope it all works out. :/ "

    def externalIP (self):
        """ Return: External IP """

        try:
            group = re.compile(u'(?P<ip>\d+\.\d+\.\d+\.\d+)').search(
                urllib.URLopener().open(
                'http://jsonip.com/').read()).groupdict()
            return group['ip']
        except IOError:
            if self.locIP:
                print (color.red + "No internet connection, server now running "
                       "on LAN only." + color.reset)

    def openPort (self):

        try:
            self.socket.bind(("", self.port))
            self.running = True
        except socket.error, message:
            print "Port", self.port, "was unable to be opened!"
            print message
            return False

        print "Opened port", self.port
        self.locIP = self.localIP()
        self.extIP = self.externalIP()
        if self.locIP:
            print "Server is running locally     @ " + self.locIP, (self.port)
        if self.extIP:
            print "External connections accepted @ " + self.extIP, (self.port)
        return True

    def listenForConnections (self):

        while self.running:
          self.socket.listen(1)
          conn, addr = self.socket.accept()
          if self.running:
            print "Player is connecting from " + list(addr)[0] + " ..."
            new_player = player.Player(self, conn = conn, addr = addr)
            self.world.moveObj(new_player.location, new_player)
            threading.Thread(target = new_player.handleLogin).start()
          else:
            print "Fake connection force closing socket"
            return

    def closeAllConnections (self):

        # Then shut down the server socket
        try:
            self.socket.shutdown(socket.SHUT_RDWR)
            self.socket.close()
        except socket.error, msg:
            print color.red + "Warning, problem shutting down socket." + color.reset
            print msg
        print "Port", self.port, "closed.\n\n"

    def forceFakeConnection(self):

      self.running = False
      socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((self.locIP, self.port))

    def run (self):

        if self.openPort():
          self.listenForConnections()  # Server loops here until shutdown
          self.closeAllConnections()


"""
def assignEmail (player):

    if player.name.lower() == "admin":
        return
    email = player.input("\nPlease enter you email meow.\n"
                         "If you'd rather not, just press enter",
                         color.gray)
    if email == None: return
    if email == "":22
        player.error("No email address recorded. You will not receive "
                     "emails at all. Ever. \nFor anything.")
    else:
        verify = player.input("Please verify your email by typing "
                              "it again.", color.gray)
        if verify == None: return
        if verify == email:
            player.email = email
            e = emailer.EmailSetup(player.email)
            threading.Thread(None, e.loginAndSendMail).start()
        else:
            player.error("Email verification failed. Please try again.")
            assignEmail(player)

    print color.yellow + player.name + "'s account has been created!", (
                                                                color.reset)

def progressBar (progress, total):

    try:
        bar = "#"*int((progress / total) * 50)
        space = " "*(50 - int((progress / total) * 50))
        percent = len(bar) * 2
        sys.stdout.write("\r [%s%s] %d%%" % (bar, space, percent))
        sys.stdout.flush()
    except ZeroDivisionError:
        pass
"""
