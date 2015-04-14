# -*- coding: utf-8 -*-
import platform
import widgetUtils
import os
import paths
import logging
import reverse_sort
log = logging.getLogger("extra.SoundsTutorial.soundsTutorial")
import soundsTutorial_constants
if platform.system() == "Windows":
 import wx_ui as UI
elif platform.system() == "Linux":
 import gtk_ui as UI

class soundsTutorial(object):
 def __init__(self, sessionObject):
  log.debug("Creating sounds tutorial object...")
  super(soundsTutorial, self).__init__()
  self.session = sessionObject
  self.actions = []
  log.debug("Loading actions for sounds tutorial...")
  [self.actions.append(i[1]) for i in soundsTutorial_constants.actions]
  self.files = []
  log.debug("Searching sound files...")
  [self.files.append(i[0]) for i in soundsTutorial_constants.actions]
  log.debug("Alphabetizing actions...")
  actions=reverse_sort.reverse_sort(self.actions)
  log.debug("Creating dialog...")
  self.dialog = UI.soundsTutorialDialog(self.actions)
  widgetUtils.connect_event(self.dialog.play, widgetUtils.BUTTON_PRESSED, self.on_play)
  self.dialog.get_response()

 def on_play(self, *args, **kwargs):
  try:
   self.session.sound.play(self.files[self.dialog.get_selection()]+".ogg")
  except:
   log.exception("Error playing the %s sound" % (self.files[self.dialog.items.GetSelection()],))