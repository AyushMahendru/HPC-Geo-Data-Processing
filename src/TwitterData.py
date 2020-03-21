"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-3-11 11:51:27
Description: class for twitter data
"""

import json
from string import punctuation, whitespace


STOP_SIGN = punctuation + whitespace


class TwitterData:
    """ required Dada model for Twitter data to be processed """

    def __init__(self, data: str):
        """
        :param data: twitter string
        """
        json_data = json.loads(data)
        self.language_code = json_data["doc"]["metadata"]["iso_language_code"]
        # method a)
        #   1. search hashtag starts with '#' followed by alphabet or numbers and end with a white space or a punctuation
        #   2. turn it to lower case
        # method b)
        #   use provided entities -> hashtags
        #
        # either method is accepted by:
        #   https://canvas.lms.unimelb.edu.au/courses/17514/discussion_topics/160043 -> suggests hashtag should contain foreign characters
        #       -> https://canvas.lms.unimelb.edu.au/courses/17514/discussion_topics/154594
        # method b is used at here

        self.hash_tags = tuple(map(lambda x: '#' + x["text"].lower(), json_data["doc"]["entities"]["hashtags"]))
