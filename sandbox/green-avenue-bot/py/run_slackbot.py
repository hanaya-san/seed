import requests, json


WEB_HOOK_URL = 'https://hooks.slack.com/services/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'

requests.post(WEB_HOOK_URL, data = json.dumps({
    'text': u'Hello everyone!!',
    'username': u'Genie',
    'link_names': 1,
}))