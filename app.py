import requests
import _constants
import datetime

def send_report(note="ERROR", exception_content=None):
    method = 'sendMessage'
    url = 'https://api.telegram.org/bot%s/%s' % (_constants.TOKEN, method)

    text = "%s: \n%s\ntime: %s" % (note, str(exception_content), datetime.datetime.now())

    data = {
        'chat_id': _constants.CHAT_ID,
        'text': text
    }

    response = requests.post(url=url, json=data)

    return response