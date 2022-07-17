import sys, requests
from setting import load_setting
from generate import json_package

def main(room='_random', text=''):
    if text == '':
        print('[WRN] Not found post message.')
    requests.post(load_setting.get_webhook_url(room),
                  data=json_package.make_post_message(text))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('[ERR] Invalid Argument.')
    main(room=sys.argv[1], text=sys.argv[2])
