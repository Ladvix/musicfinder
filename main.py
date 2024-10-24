from pyrogram import Client, filters
import modules.musicfinder.music_finder as music_finder

def init(app):

    @app.on_message(filters.command('search', prefixes = '.') & filters.me)
    def _(client, message):

        text = message.text.split(' ', maxsplit = 1)
        music_name = text[1]

        music_name = music_name.replace(' ', '+')

        response = 'ㅤ'

        music_finder.HitmoParser.__init__(music_finder.HitmoParser)
        music_finder.HitmoParser.find_song(music_finder.HitmoParser, music_name)
        tracks = music_finder.HitmoParser.get_songs(music_finder.HitmoParser, music_finder.HitmoParser.res_link)        

        lenght = len(tracks) < 10 and len(tracks) or 10

        for i in range(0, lenght):

            track = tracks[i]

            response = response + '\n<b>🎤 ' + track['title'] + '</b>' + '\n' + '<b> 🗣' + track['artist'] + '</b>' + '\n' + '<b>' + track['download_link'] + '</b>\n'
    
        response = response + 'ㅤ'
        
        message.edit_text(response)
