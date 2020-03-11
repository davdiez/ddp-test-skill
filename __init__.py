from mycroft import MycroftSkill, intent_file_handler


class DdpTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.ddp.intent')
    def handle_test_ddp(self, message):
        self.speak_dialog('test.ddp')


def create_skill():
    return DdpTest()

