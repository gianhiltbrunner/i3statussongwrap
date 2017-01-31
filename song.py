from unidecode import unidecode
import dbus
session_bus = dbus.SessionBus()
spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
                                             "/org/mpris/MediaPlayer2")
spotify_properties = dbus.Interface(spotify_bus,
                                            "org.freedesktop.DBus.Properties")
metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")

if (len(metadata['xesam:title']) < 55):#If song name is too long dont print artist
    print (unidecode(metadata['xesam:title']) + " by " + unidecode(metadata['xesam:artist'][0]))
elif (len(metadata['xesam:title']) > 70):#If song is too long too display, only disp first 70 chars
    print (unidecode(metadata['xesam:title'])[:70] + "...")
else:
    print (unidecode(metadata['xesam:title']))
