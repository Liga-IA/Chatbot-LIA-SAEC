
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from pprint import pprint

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_register_ong"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pprint(tracker)
        dispatcher.utter_message(text="Registrando...")

        return []
