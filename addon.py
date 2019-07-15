from xbmcswift2 import Plugin, xbmcgui
from resources.lib import joeroganexperiencepodcast

plugin = Plugin()

URL = "http://joeroganexp.joerogan.libsynpro.com/rss"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "http://static.libsyn.com/p/assets/7/1/f/3/71f3014e14ef2722/JREiTunesImage2.jpg"},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "http://static.libsyn.com/p/assets/7/1/f/3/71f3014e14ef2722/JREiTunesImage2.jpg"},]

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = joeroganexperiencepodcast.get_soup(URL)
    
    playable_podcast = joeroganexperiencepodcast.get_playable_podcast(soup)
    
    items = joeroganexperiencepodcast.compile_playable_podcast(playable_podcast)

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = joeroganexperiencepodcast.get_soup(URL)
    
    playable_podcast1 = joeroganexperiencepodcast.get_playable_podcast1(soup)
    
    items = joeroganexperiencepodcast.compile_playable_podcast1(playable_podcast1)

    return items


if __name__ == '__main__':
    plugin.run()
