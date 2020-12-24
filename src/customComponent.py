from rasa.nlu.components import Component
from typing import Any, Optional, Text, Dict


class MyComponent(Component):

    def __init__(self, component_config=None):
        super().__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        print('custom train component called')
        print(dir(training_data))
        for data in training_data.training_examples:
            print(dir(data))
        pass

    def process(self, message, **kwargs):
        print('custom process component called-------------------------------------------------')
        print(message.data)
        print(message.text)
        message.text = (message.text).replace('+', ' plus ')
        message.text = (message.text).replace('-', ' minus ')
        message.text = (message.text).lower()
        print(message.text)


        pass

    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        print('custom persist component called')
        pass

