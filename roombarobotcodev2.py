from pyrobot import *
import sys
import logging
import time
import SocketServer
import Queue
#=============================================================
# put defines here e.x.
# define_name = define value
#=============================================================
# define the Rtbot class to init and start itself
queue = Queue.Queue()

class Rtbot(Create):
  def __init__(self, tty='/dev/ttyUSB0'):
    super(Create, self).__init__(tty)
    self.sci.AddOpcodes(CREATE_OPCODES)
    self.sensors = CreateSensors(self)
    self.safe = False  # Use full mode for control.

  def start(self):
    logging.debug('Starting up the Rtbot.')
    self.SoftReset()
    self.Control()

  def testdrive(self):
    logging.debug('driving  the Rtbot.')

    self.Drive(300, 300)
    time.sleep(5)
    self.Drive(-300,300)
    time.sleep(5)
    self.SlowStop(25)
#=============================================================
#place further functions in the Rtbot class e.x.
# def somefunction(some_argvs):
#   some code
class Robot_Controller(threading.Thread):
  def __init__(self, robot):
     threading.Thread.__init__(self)
     self.rtbot = robot
     self.queue    = queue
  def dowork(self,item):
      if(item == "left"):
         rtbot.Drive(300, 300)

      if(item == "right"):
         rtbot.Drive(300, 300)

      if(item == "forward"):
         rtbot.Drive(300, 300)

      if(item == "reverse"):
         rtbot.Drive(300, 300)

  def run(self):
      print "rtbot control called"
      while True:
        item = queue.get
        self.dowork(item)



class TCPHandler(SocketServer.BaseRequestHandler):
  def handle(self):
       self.queue = queue
       # self.request is the TCP socket connected to the client
       print "handler called"
       self.data = self.request.recv(1024).strip()
       print "{} wrote:".format(self.client_address[0])
       print self.data
       queue.put(self.data)

