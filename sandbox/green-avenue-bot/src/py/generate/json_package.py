import json

def make_post_message(text=''):
    json_data = json.dumps({
        'text': u'%s'%(__replace_line_feed_code(text)),
        'link_names': 1,
    })
    return json_data

def __replace_line_feed_code(text):
    return text.replace('<br>', '\n')
