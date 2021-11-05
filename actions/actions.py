
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

API_PATH = "https://3333-aquamarine-warbler-xbftz3tt.ws-us18.gitpod.io"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests
import json
from pprint import pprint

class ActionRegistraOng(Action):

    def name(self) -> Text:
        return "action_register_ong"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        

        
        nome = tracker.get_slot('ong_name')
        zap = str(tracker.get_slot('ong_whatsapp'))
        email = str(tracker.get_slot('ong_email'))
        contatos = ' Whatsapp: ' + zap + ' Email: ' + email
        city = str(tracker.get_slot('ong_city'))
        uf = str(tracker.get_slot('ong_uf'))
        local = 'cidade de ' + city + ', ' + uf


        pprint("registrando em "+ API_PATH+ '/ongs')
        pload = {
            'name':str(tracker.get_slot('ong_name')), 
            'email':email, 
            'whatsapp':zap, 
            'city':city, 
            'uf':uf}
        headers = {'Content-Type': "application/json", 'Accept': "application/json"}
        r = requests.post(API_PATH+ '/ongs', data = json.dumps(pload),headers=headers)  
        

        print(r.text)
        if(int(r.status_code) != 200):
            dispatcher.utter_message(text="Erro ao criar a ong.. tente novamente mais tarde")
        else:
            dispatcher.utter_message(text ='registrando a ONG ' + str(nome) + '\n da ' + local + "\n contatos: " + contatos +"\n\n" + "O código da sua ong é: " + r.json()['id'])
        return []


class ActionExclusionSelect(Action):

    def name(self) -> Text:
        return "action_delete_case_selection"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        

        id = str(tracker.get_slot('ong_id'))
        print("Deletando.." + id)
        
        if(id and id != "" and id != "None"):
            
            r = requests.get(API_PATH+ '/ongs/'+str(id))  
            if(int(r.status_code)==404):
                dispatcher.utter_message(text ="Não há casos para serem excluidos ou id incorreto")
                return
            if(int(r.status_code)==500 or int(r.status_code)==401 ):
                dispatcher.utter_message(text ="Pera que eu fiquei confuso.... deu um errinho aqui kk vamos de novo!")
                return
            print(r.json())
            cases = r.json()

            btns = []
            for i in range(len(cases)):
                btns.append({"payload":'/delete_specific_case{"case_id":"'+str(cases[i]["id"])+'"}',"title":cases[i]["title"]})
            btns.append({"payload":"/cancel_operation","title":"Nenhum"})
            dispatcher.utter_message(text="Escolha qual caso quer excluir", buttons=btns)
        else:
            dispatcher.utter_message(text ="Id não informado, ou está incorreto")
        return []


class ActionDeleteCaseById(Action):

    def name(self) -> Text:
        return "action_delete_case_by_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        

        id = str(tracker.get_slot('case_id'))
        ong_id = str(tracker.get_slot('ong_id'))
        print("Deletando caso..." + id)
        
        if(id and id != "" and id != "None"):
            print("chamando a api em: ",API_PATH+ '/incidents/'+str(id),{"authorization":str(ong_id)})
            r = requests.delete(API_PATH+ '/incidents/'+str(id),headers= {"authorization":str(ong_id)}) 
            if(int(r.status_code)==404):
                dispatcher.utter_message(text ="Caso não encontrado")
                return
            if(int(r.status_code)==500 or int(r.status_code)==401 ):
                dispatcher.utter_message(text ="Pera que eu fiquei confuso.... deu um errinho aqui kk vamos de novo!")
                return
            
            
            dispatcher.utter_message(text ="Deletado!")
        else:
            dispatcher.utter_message(text ="Id não informado, ou está incorreto")

        return []
