# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/brands/google.svg" card_color="#222222" width="50" height="50" style="vertical-align:bottom"/> Google AIY Voicehat
Enables the button and LED on the Google AIY voicehat.

## About
This Mycroft skill roughly follows @andlo's code outline for the 
excellent [picroft-google-aiy-voicekit](https://github.com/andlo/picroft-google-aiy-voicekit-skill) skill. It provides
the same functionality but uses the gpiozero library 
instead of RPi.GPIO to operate the button-LED combo 
connected to the voicehat.

Additionally, an extended button press 
(> 7 seconds) forces a Linux shutdown.

The idea is to test gpiozero's ability to handle switch 
bounce when polling for a button press; in my experience, RPi.GPIO 
doesn't register hold times too well. 

## Credit
[@kalyaninagaraj](https://github.com/kalyaninagaraj)

## Category
**IoT**

## Tags
#Mycroft AI
#Google
#AIY
#voicehat

