# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    EventType,
    ActionExecuted,
    SessionStarted,
    Restarted,
    FollowupAction,
    UserUtteranceReverted,
)

#
#
class ActionChange(Action):

    def name(self) -> Text:
        return "action_change"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    	slots = {"pizza_type": None,"pizza_size": None,"pizza_quantity": None}
    	dispatcher.utter_message(text="Your cart has been refreshed.Please! enter the asked item,size and quantity again")
    	return [SlotSet(slot, value) for slot, value in slots.items()]
