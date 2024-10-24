from pyrogram import Client, filters
import modules.musicfinder.music_finder as music_finder

def init(app):

    @app.on_message(filters.command('search', prefixes = '.') & filters.me)
    def _(client, message):

        text = message.text.split(' ', maxsplit = 1)
        music_name = text[1]

        response = 'ㅤ'

        music_finder.HitmoParser.__init__(music_finder.HitmoParser)
        music_finder.HitmoParser.find_song(music_finder.HitmoParser, music_name)
        music_finder.HitmoParser.get_songs(music_finder.HitmoParser, music_finder.HitmoParser.res_link)

        for i in range(0, 25):

            track = music_finder.HitmoParser.track_list[i]

            response = response + '\n<b>🎤 ' + track['title'] + '</b>' + '\n' + '<b> 🗣' + track['artist'] + '</b>' + '\n' + '<b>' + track['download_link'] + '</b>\n'
    
        response = response + 'ㅤ'
        
        message.edit_text(response)
