import sqlite3
try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter

# ===== DB connect =====
conn = sqlite3.connect('music.sqlite')


# ===== Scrollbar class for UI =====
class Scrollbox(tkinter.Listbox):
    """This class generates the scrollbar for the UI listboxes

    Attributes:
        scrollbar (tkinter.Scrollbar): The parameters for the scrollbar

    Methods:
        grid: overwrites the tkinter grid() method. Sets the parameters for the scrollbar using the
            provided arguments
    """
    
    def __init__(self, window, **kwargs):
        # tkinter.Listbox.__init__self, window, **kwargs) # Python 2
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky="nse", rowspan=1, columnspan=1, **kwargs):
        # tkinter.Listbox.grid(self, row=row, column=column, sticky=sticky, rowspawn=rowspan,
        # **kwargs) # Python 2
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan,
                     **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


def get_albums(event):
    """Uses the selection from the artistList widget to query DB artists table with the artist name
        provided by the selection to find the artist._id field. Uses the artist._id field to query
        the DB albums table to populate a list of albums with the artist._id. Pipes the list into
        the albumsLV widget"""

    lb = event.widget
    index = lb.curselection()[0]
    # necessary comma due to tuple for single argument parameter
    # substitution
    artist_name = lb.get(index),

    # get the artist ID from the database row
    artist_id = conn.execute("SELECT artists._id FROM artists WHERE artists.name = ?",
                             artist_name).fetchone()
    alist = []
    for row in conn.execute("SELECT albums.name FROM albums WHERE albums.artist = ?"
                            " ORDER BY albums.name", artist_id):
        alist.append(row[0])
    albumnLV.set(tuple(alist))
    songLV.set(("Choose an album",))


def get_songs(event):
    """Uses the selection from the albumList widget to query DB albums table with the album name
        provided by the selection to find the album._id field. Uses the album._id field to query
        the DB songs table to populate a list of songs with the album._id. Pipes the list into
        the songsLV widget"""
    lb = event.widget
    index = int(lb.curselection()[0])
    album_name = lb.get(index),

    # get the album ID from the database row
    album_id = conn.execute("SELECT albums._id FROM albums WHERE albums.name = ?",
                            album_name).fetchone()
    alist = []
    for x in conn.execute("SELECT songs.title FROM songs WHERE songs.album = ?"
                            " ORDER BY songs.track", album_id):
        alist.append(x[0])
    songLV.set(tuple(alist))



# ===== UI Window =====
mainWindow = tkinter.Tk()
mainWindow.title('Music DB Browser')
mainWindow.geometry('1024x768')

# === UI grid ===
# == columns ==
mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)

# == rows ==
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# === UI components ===
# == labels ==
tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# == Artist Listbox ==
artistList = Scrollbox(mainWindow)
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

# = DB Query = 
for artist in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
    artistList.insert(tkinter.END, artist[0])

# = Artist Select Binding =
artistList.bind('<<ListboxSelect>>', get_albums)

# == Albums Listbox ==
# display for if no artist selected
albumnLV = tkinter.Variable(mainWindow)
albumnLV.set(("Choose and artist",))
# display
albumList = Scrollbox(mainWindow, listvariable=albumnLV)
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

# = Album Select Binding =
albumList.bind('<<ListboxSelect>>', get_songs)

# == Songs Listbox ==
# display for if no album selected
songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose an album",))
# display
songList = Scrollbox(mainWindow, listvariable=songLV)
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(border=2, relief='sunken')

# === Main Loop ===
mainWindow.mainloop()
print("closing database connection")
conn.close()