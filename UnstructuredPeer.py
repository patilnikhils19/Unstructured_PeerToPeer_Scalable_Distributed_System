import os
import argparse
import sys
import socket
import socket
import subprocess
import time
import thread
from thread import *
import datetime
import logging


if __name__ == '__main__':

          parser = argparse.ArgumentParser()#Define argument parser
          parser.add_argument("-p","--port",help="Port Number",type=int)
          parser.add_argument("-b","--bootstrapip",help="Bootstrap Server IP address",type=str)
          parser.add_argument("-n","--bootstrapport",help="Bootstrap Server Port Number",type=int)
          parser.add_argument("-u","--username",help = "Username for registering with the bootstrap Server",type=str)
          args = parser.parse_args()

          if not args.bootstrapip or  not args.port or not args.bootstrapport :
                 print("Need Bootstrap ServerIP")

          elif not args.port :
                 print("Need Port Number")

          elif  not args.bootstrapport :
                 print("Need Bootstrap Server Port Number")

          else :

