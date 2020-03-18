"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-3-11 11:51:27
Description: class for twitter data
"""

import json


class TwitterData:
    def __init__(self, data: str):
        json_data = json.loads(data)
        self.language_code = json_data["doc"]["metadata"]["iso_language_code"]
