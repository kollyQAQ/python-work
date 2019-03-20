import os

CMD_PREFIX = 'prefix'
CMD_CHAT = 'chat'
CMD_SHUTUP = 'shutup'
CMD_SHOW = 'show'

FILE_PATH = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir)) + '\static\ice\\'
FILE_PATH_OTHER = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir)) + '\static\other\\'

ICE_NAME = ''
FRIENDS_NAME = ''
CHATROOM_NAME = ''
CHATROOM_USER_LIST = []
CHATROOM_USER_ALL = False
CHAT_PREFIX = ''

SZ_WEATHER = ''