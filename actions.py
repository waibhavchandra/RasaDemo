# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
from duckling import Duckling, Dim, Language

#
#
duck = Duckling()
duck.load()


class WeatherAction(Action):
     def name(self) -> Text:
         return "weather_action"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         print('running weather_action')
         dispatcher.utter_message(template="utter_fetching_data")
         print(tracker.latest_message.get('entities'))
         elements = [{"type":"weather_action","entities":tracker.latest_message.get('entities'), "intent" : "weather_action"}]
         dispatcher.utter_message(json_message=elements)
         #dispatcher.utter_custom_message(*elements)
         #dispatcher.utter_custom_json(elements)
         return []




class FallbackAction(Action):
   def name(self):
      return "fallback_action"

   def run(self, dispatcher, tracker, domain):
      print('inside "fallback_action"')
      intent_ranking = tracker.latest_message.get('intent_ranking', [])
      print(intent_ranking)
      if len(intent_ranking) > 0 :
         dispatcher.utter_message(template='utter_low_confidence')
         #dispatcher.utter_template('utter_'+str(intent_ranking[0].get("name")), tracker)
         print("confidence below threashold")
      else :
         dispatcher.utter_message(template='utter_out_of_scope')
         print("no intent detected")
