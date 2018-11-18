import sys
print(sys.path)

from itchatTest.utils import weather_util
weather_util.get_weather_today()

from itchatTest.utils import nba_util
nba_util.get_game_today()