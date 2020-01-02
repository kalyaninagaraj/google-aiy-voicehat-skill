""" This skill follows the code outline of the excellent
picroft-google-aiy-voicekit skill by @andlo, but uses
the gpiozero library (instead of RPi.GPIO) to operate
the button-led combo connected to the voicehat.

The idea is to test gpiozero's ability to handle switch
bounce when polling for a button press. RPi.GPIO does
not fare too in these matters.

If all goes well, I'd like an extended button press
(> 7 seconds) to  initiate a system shutdown.
"""

#from mycroft.messagebus.message import Message
from mycroft import MycroftSkill
from gpiozero import Button, LED
from signal import pause
import time

#button = Button(23)
led = LED(25)

class GoogleAIYVoicehat(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        led.off()
        self.schedule_repeating_event(self.handle_voicehat_button, None, 0.01, 'buttonpress')
        #self.add_event('recognizer_loop:record_begin', self.handle_listener_started)
        #self.add_event('recognizer_loop:record_end', self.handle_listener_ended)

    def handle_voicehat_button(self, message):
        if button.when_pressed
            self.say_hello()
        pause()

    def say_hello(self):
        led.on()
        self.speak("Hello!")
        led.off()

def create_skill():
    return GoogleAIYVoicehat()
