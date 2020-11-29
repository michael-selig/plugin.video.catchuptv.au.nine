import sys
import xbmcaddon
from urlparse import parse_qsl

from aussieaddonscommon import utils

import resources.lib.menu as menu
import resources.lib.play as play


def main():
    """
    Router function that calls other functions depending on the
    provided paramstring
    """
    params = dict(parse_qsl(sys.argv[2][1:]))
    if (len(params) == 0):
        menu.list_categories()
    else:

        if params['action'] == 'listcategories':
            if params['category'] == 'Live TV':
                menu.make_live_list(params)
            else:
                menu.make_series_list(params)
        elif params['action'] == 'listseries':
            menu.make_episodes_list(params)
        elif params['action'] in ['listepisodes', 'listchannels']:
            play.play_video(params)
        elif params['action'] == 'settings':
            xbmcaddon.Addon().openSettings()
        elif params['action'] == 'sendreport':
            utils.user_report()


if __name__ == '__main__':
    main()
