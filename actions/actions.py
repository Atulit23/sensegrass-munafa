# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import requests

# class ActionGetPrice(Action):
#     def name(self) -> Text:
#         return "action_get_price"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         product = tracker.latest_message.get('entities')[0]['value']
#         product = product.lower()

#         api_endpoints = {
#             "wheat": "https://api.data.gov.in/catalog/859fe05b-eba0-402d-b777-eccd064734fd?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json",
#             "cotton seed": "https://api.data.gov.in/resource/4af6f1a8-8d1f-46bb-aa99-f884e081df96?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json",
#             "cotton seeds": "https://api.data.gov.in/resource/4af6f1a8-8d1f-46bb-aa99-f884e081df96?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json",
#             "almond": "https://api.data.gov.in/resource/f97b1996-0c47-454f-859b-609dc2c7aac6?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json",
#             "almonds": "https://api.data.gov.in/resource/f97b1996-0c47-454f-859b-609dc2c7aac6?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json",
#             "litchi": "https://api.data.gov.in/resource/2760d764-e884-4c44-9068-322b9351bc33?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json",
#             "lime": "https://api.data.gov.in/resource/679465d9-f20d-44d9-8133-f85ee664e93a?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json",
#             "mango": "https://api.data.gov.in/resource/c7c0c766-bad9-4b31-98ba-98f7c5703830?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json",
#             "masur dal": "https://api.data.gov.in/resource/9b4c48d3-f92e-4bdd-bc80-c2f1531451a2?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json",
#             "mushroom": "https://api.data.gov.in/resource/8955cc44-621e-4c92-b439-4cb2ec28e72c?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json",
#             "maida": "https://api.data.gov.in/resource/407d8885-0d68-4df6-bccb-60cd9d741092?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json",
#         }

#         if product.lower() in api_endpoints:
#             product_api_url = api_endpoints[product.lower()]
#             try:
#                 response = requests.get(product_api_url)
#                 data = response.json()
#                 str_ = ''
#                 for i in data['records']:
#                     str_ = str_ + 'Commodity: ' + i['commodity'] + ' Variety: ' + i['variety'] + ' Max Price: ' + str(i['max_price'])  + ' Min Price: ' + str(i['min_price']) + '\n'
#                 print(str_)

#                 dispatcher.utter_message(text=str_)
#             except Exception as e:
#                 dispatcher.utter_message(text="Sorry, I couldn't retrieve the price information at the moment.")
#                 print(e)
#         else:
#             dispatcher.utter_message(text="Sorry, I don't have information about the price of that product.")

#         return []


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionGetPrice(Action):
    def name(self) -> Text:
        return "action_get_price"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_input = tracker.latest_message.get('text')

        crop_names = ["wheat", "paddy", "cotton seed", "almond", "litchi", "lime", "mango", "masur daal", "mushrooms",
            "raw ripe mango", "maida", "castor seed", "castor seeds", "cotton", "dry chillies", "onion", "maize"]

        crop_type = next(
            (crop for crop in crop_names if crop in user_input.lower()), None)

        url = 'https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit=60&filters%5Bcommodity%5D='

        if crop_type:
            response = requests.get(url + crop_type)
            data = response.json()
            str_ = ''
            for i in data['records']:
                str_ = str_ + 'Commodity: ' + i['commodity'] + '; Variety: ' + i['variety'] + '; Max Price: ' + str(
                    i['max_price']) + '; Min Price: ' + str(i['min_price']) + '; State: ' + i['state'] + '; Market: ' + i['market'] + '\n'
            print(str_)

            dispatcher.utter_message(text=str_)
        else:
            dispatcher.utter_message(text="Sorry, I couldn't determine the crop type from your message.")

        return []
