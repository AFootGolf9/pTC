import configparser
from twitchAPI.twitch import Twitch
from twitchAPI.chat import Chat
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope

USER_SCOPE = [AuthScope.CHAT_READ]

def get_config():
    config = configparser.ConfigParser()
    config.read('./Bot/res/config.ini')
    id = config['OAuth']['app_id']
    secret = config['OAuth']['app_secret']
    return id, secret

async def get_twitch():
    id, secret = get_config()
    twitch = await Twitch(id, secret)
    auth = UserAuthenticator(twitch, USER_SCOPE)
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)
    return twitch

async def get_chat(twitch):
    chat = await Chat(twitch)
    return chat