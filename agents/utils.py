import json
import re

def extract_json(text):

    start_index = text.find('{')
    end_index = text.rfind('}')

    if start_index != -1 and end_index != -1 and start_index < end_index:
        try:
            return json.loads(text[start_index:end_index + 1])
        except:
            return None
    else:
        return None