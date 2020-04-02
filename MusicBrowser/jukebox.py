import sqlite3
try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter

# ===== DB connect =====
conn = sqlite3.connect('music.sqlite')

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
artistList = tkinter.Listbox(mainWindow)
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

# = Artist Scrollbox =
artistScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistList.yview)
artistScroll.grid(row=1, column=0, sticky='nse', rowspan=2)
artistList['yscrollcommand'] = artistScroll.set

# == Albums Listbox ==
# display for if no artist selected
albumnLV = tkinter.Variable(mainWindow)
albumnLV.set(("Choose and artist",))
# display
albumList = tkinter.Listbox(mainWindow, listvariable=albumnLV)
albumList.grid(row=1, column=1, sticky='nesw', padx=(30, 0))
albumList.config(border=2, relief='sunken')

# = Albums Scrollbox =
albumScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=albumList.yview)
albumScroll.grid(row=1, column=1, sticky='nse', rowspan=2)
albumList['yscrollcommand'] = albumScroll.set

# == Songs Listbox ==
# display for if no album selected
songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose an album",))
# display
songList = tkinter.Listbox(mainWindow, listvariable=songLV)
songList.grid(row=1, column=2, sticky='nesw', padx=(30, 0))
songList.config(border=2, relief='sunken')

# = Songs Scrollbox =
songScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=songList.yview)
songScroll.grid(row=1, column=2, sticky='nse', rowspan=2)
songList['yscrollcommand'] = songScroll.set

# === Main Loop ===
mainWindow.mainloop()
print("closing database connection")
conn.close()