'''
Created on Dec 22, 2013

@author: Justin
'''

import Tkinter as tk
import threading
from src import server, world


class Application(tk.Frame):

  def __init__(self, bg_color, master = None):
    tk.Frame.__init__(self, master,
                      bg = bg_color)
    self.bg = bg_color
    # Allow for window resizing
    top = self.winfo_toplevel()
    top.rowconfigure(0, weight = 1)
    top.columnconfigure(0, weight = 1)
    self.rowconfigure(0, weight = 1)
    self.columnconfigure(0, weight = 1)
    self.grid(sticky = tk.N + tk.S + tk.E + tk.W)
    self._run()

  def _startServer(self):

    self.server_thread = threading.Thread(target = self.server.run)
    # self.server_thread = multiproc.Process(target = self.server.run)
    self.server_thread.start()

  def _stopServer(self):

    self.server.forceFakeConnection()

  def _gridWidgets(self):
    
    self.onoff_button_area.grid(row=0,
                                column = 0,
                                sticky=tk.NW)
    self.start_server_button.grid(row = 0,
                                  column = 0,
                                  sticky = tk.NW)
    self.stop_server_button.grid(row = 0,
                                 column = 1,
                                 sticky = tk.NW)

  def _createWidgets(self):

    self.onoff_button_area = tk.Frame(self, bg = self.bg)
    self.log_output = tk.Text(self)
    self.start_server_button = tk.Button(self.onoff_button_area,
                                         text = "Start Server",
                                         bg = self.bg,
                                         command = self._startServer,
                                         width = 12)
    self.stop_server_button = tk.Button(self.onoff_button_area,
                                         text = "Stop Server",
                                         bg = self.bg,
                                         command = self._stopServer,
                                         width = 12)

  def _run(self):

    self.server = server.Server()
    self.server.world = world.World()
    self.server.world.build()

    self._createWidgets()
    self._gridWidgets()
    self._startServer()

if __name__ == "__main__":
  app = Application("#999")
  app.master.title("PyMUD Server Control")
  # app.master.geometry("800x600+200+200")
  app.mainloop()
  # server = src.server.Server()
  # server.run()
