
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

API_PATH = "https://3333-tan-goose-kjycxojb.ws-us17.gitpod.io"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests
import json
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
        pprint("registrando em "+ API_PATH+ '/ongs')
        pload = {
            'name':str(tracker.get_slot('ong_name')), 
            'email':str(tracker.get_slot('ong_email')), 
            'whatsapp':str(tracker.get_slot('ong_whatsapp')), 
            'city':str(tracker.get_slot('ong_city')), 
            'uf':str(tracker.get_slot('ong_uf'))}
        headers = {'Content-Type': "application/json", 'Accept': "application/json"}
        r = requests.post(API_PATH+ '/ongs', data = json.dumps(pload),headers=headers)  
        
        if(int(r.status_code) != 200):
            dispatcher.utter_message(text="Erro ao criar a ong.. tente novamente mais tarde")
        else:
            dispatcher.utter_message(text ='registrando a ONG ' + str(nome) + '\n da ' + local + "\n contatos: " + contatos +"\n\n" + "O código da sua ong é: " + r.json()['id'])
