from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler
from mycroft.skills.context import adds_context, removes_context


class DdpTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    #@intent_file_handler('test.ddp.intent')
    @intent_handler(IntentBuilder('WhatsupIntent').require('como').require('encuentras').build())
    @adds_context('WhatsupContext')
    def handle_test_ddp(self, message):
        self.log.info('Respuesta')
        self.speak_dialog('test.ddp', expect_response=True)
    '''
    def converse(self, utterances, lang):
        self.log.info('Utterance received')
        if utternaces:
            self.log.info(utterances[0])

        if utterances and self.voc_match(utterances[0], 'bien'):
            self.speak_dialog('respuesta.positiva')
            return True
        elif utterances and self.voc_match(utterances[0], 'mal'):
            self.speak_dialog('respuesta.negativa')
            return True
        else:
            return False
'''

    @intent_handler(IntentBuilder('BienIntent').require('bien').require('WhatsupContext').build())
    @removes_context('WhatsupContext')
    def handle_whatsup_pos(self, message):
        self.log.info('Answer received')
        self.log.info(message)
        self.speak_dialog('respuesta.positiva')

    @intent_handler(IntentBuilder('MalIntent').require('mal').require('WhatsupContext').build())
    @removes_context('WhatsupContext')
    def handle_whatsup_neg(self, message):
        self.log.info('Answer received')
        self.log.info(message)
        self.speak_dialog('respuesta.negativa')

    def shutdown(self):
        self.speak_dialog('adios')
        self.log.info('Shutdown')

def create_skill():
    return DdpTest()

