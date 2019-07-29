import os

head_common = 'https://hooks.slack.com/services/'

room_dict = {
    '_random': os.environ['SLACK_R_RANDOM'],
    'rykura': os.environ['SLACK_RRYKURA'],
}
