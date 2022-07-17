def get_webhook_url(room='_random'):
    '''
    Args:
        room: The room you want to notify
        (Default) _random
    '''
    post_url = '{0}{1}'.format(webhook_url.head_common,
                               webhook_url.room_dict[room])
    return post_url

def main():
    get_webhook_url()


'''
Unit test code
'''
if __name__ == '__main__':
    from config import webhook_url
    main()

else:
    from setting.config import webhook_url
