# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/cube.svg" card_color="#222222" width="50" height="50" style="vertical-align:bottom"/> Google Aiy Voicehat
Enables the button and led on the Google AIY voicehat.

## About
This skill follows the code outline of the excellent
picroft-google-aiy-voicekit skill by andlo, but uses 
the gpiozero library (instead of RPi.GPIO) to operate
the button-led combo connected to the voicehat.

The idea is to test gpiozero's ability to handle switch
bounce when polling for a button press. RPi.GPIO does
not fare too in these matters. 

If all goes well, I'd like an extended button press 
(> 7 seconds) to  initiate a system shutdown.

## Credits
kalyaninagaraj

## Category
**IoT**

## Tags
#Mycroft AI
#Google
#AIY
#voicehat

