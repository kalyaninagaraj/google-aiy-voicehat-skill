"""
About
-----
This skill roughly follows @andlo's code outline for the
excellent picroft-google-aiy-voicekit skill, but uses
the gpiozero library (instead of RPi.GPIO) to operate
the button-led combo connected to the voicehat.

Also, an extended button press (> 7 seconds) initiates a
Linux shutdown.

The idea is to test gpiozero's ability to handle switch
bounce when polling for a button press; RPi.GPIO does
not do it very well.

Author
------
Kalyani Nagaraj
Dec 2019
"""

from mycroft import MycroftSkill
from mycroft.messagebus.message import Message
from gpiozero import Button, LED
import time
import subprocess

class GoogleAIYVoicehat(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.time_held = 100
        self.short_press = 2
        self.button = Button(23, hold_time = 7)
        self.led = LED(25)
        self.schedule_repeating_event(self.handle_button, None, 0.01, 'buttonpress')

    def handle_button(self):
        self.button.when_pressed = self.start_timer
        self.button.when_held = self.graceful_exit
        self.button.when_released = self.stop_timer
        self.add_event('recognizer_loop:record_begin', self.handle_listener_started)
        self.add_event('recognizer_loop:record_end', self.handle_listener_ended)

    def start_timer(self):
        self.time_held = time.time()

    def stop_timer(self):
        self.time_held = time.time() - self.time_held
        if self.time_held < self.short_press:
            self.bus.emit(Message('mycroft.mic.listen'))
        elif self.time_held < self.button.hold_time:
            self.bus.emit(Message('mycroft.stop'))

    def handle_listener_started(self):
        self.led.on()

    def handle_listener_ended(self):
        self.led.off()

    # In truth, this is a not-so-graceful power down.
    # Emitting message 'system.shutdown' doesn't work on Picroft.
    def graceful_exit(self):
        self.blink()
        self.log.info('Forcing a linux shutdown ...')
        subprocess.call(['sudo', 'shutdown', '-h', 'now'])

    def blink(self):
        for i in range(6):
            self.led.toggle()
            time.sleep(0.5)

    def shutdown(self):
        self.cancel_scheduled_event('buttonpress')
        self.button.close()
        self.led.close()

def create_skill():
    return GoogleAIYVoicehat()
