from mycroft import MycroftSkill, intent_file_handler


class GoogleAiyVoicehat(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('voicehat.aiy.google.intent')
    def handle_voicehat_aiy_google(self, message):
        self.speak_dialog('voicehat.aiy.google')


def create_skill():
    return GoogleAiyVoicehat()

