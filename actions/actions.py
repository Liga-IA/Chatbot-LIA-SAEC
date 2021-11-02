
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from pprint import pprint

class registraong(Action):

    def name(self) -> Text:
        return "action_register_ong"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nome = tracker.get_slot('ong_name')
        contatos = ' Whatsapp: ' + str(tracker.get_slot('ong_whatsapp')) + ' Email: ' + str(tracker.get_slot('ong_email'))
        local = 'cidade de ' + str(tracker.get_slot('ong_city')) + ', ' + str(tracker.get_slot('ong_uf'))
        dispatcher.utter_message(text ='registrando a ONG ' + str(nome) + '\n da ' + local + "\n contatos: " + contatos)
