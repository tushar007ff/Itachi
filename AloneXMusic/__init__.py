from Itachi.core.bot import Itachi
from Itachi.core.dir import dirr
from Itachi.core.git import git
from Itachi.core.userbot import Userbot
from Itachi.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Itachi()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
