from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

balance_db = {
    "Joe": "4000",
    "John": "1000",
    "Adam": "5000",
    "Jack": "2000",
    "Alex": "6000",
    "Jill": "3000",
}

class ActionRememberName(Action):
    def name(self) -> Text:
        return "action_remember_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, 
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_name = next(tracker.get_latest_entity_values("account_name"), None)

        return [SlotSet("account_name", current_name)]


class ActionReturnBalance(Action):
    def name(self) -> Text:
        return "action_return_balance"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_name = tracker.get_slot("account_name")
        current_number = next(tracker.get_latest_entity_values("account_number"), None)


        balance_amt = balance_db.get(current_name, None)
        msg = f"Dear {current_name}, your account number: {current_number} has a balance of Rs. {balance_amt}."
        dispatcher.utter_message(text=msg)

        return []
