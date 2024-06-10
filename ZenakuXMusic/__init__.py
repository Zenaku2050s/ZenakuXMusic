from ZenakuXMusic.core.bot import Anony
from ZenakuXMusic.core.dir import dirr
from ZenakuXMusic.core.git import git
from ZenakuXMusic.core.userbot import Userbot
from ZenakuXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
