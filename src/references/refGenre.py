class RefGenre(object):

    # Allowed genres and style according to the naming convention
    genres = ['2-Step-Garage', 'Abstract Hip-Hop', 'Acid House', 'Acid Techno', 'Acoustic',
              'African Blues', 'Afrobeat', 'Alternative Hip-Hop', 'Alternative Metal',
              'Alternative Rock', 'Ambient', 'Ambient Pop', 'Arena Rock', 'Avant-Garde',
              'Avant-Garde Metal', 'Ballroom', 'Baroque Pop', 'Bass House', 'Bassline',
              'Big Beat', 'Big Room', 'Bitpop', 'Black Metal', 'Blues', 'Blues Rock',
              'Boogaloo', 'Boogie Rock', 'Bossa Nova', 'Bounce', 'Breakbeat', 'Breakcore',
              'Breaks', 'Britpop', 'Broken Beat', 'Brostep', 'Celtic', 'Celtic Rock',
              'Chanson Française', 'Chillgressive', 'Chill-Out', 'Chillstep', 'Chill Trap',
              'Chillwave', 'Chiptune', 'Christian Rock', 'Classic Rock', 'Cloud Rap',
              'Comedy Rock', 'Complextro', 'Country', 'Country Rock', 'Dance', 'Dancehall',
              'Dance Pop', 'Dark Ambient', 'Deathcore', 'Death Metal', 'Deep House',
              'Desert Rock', 'Dirty Dutch', 'Dirty Electro', 'Disco', 'Doom Metal',
              'Downtempo', 'Dream Pop', 'Drum & Bass', 'Drumstep', 'Dub', 'Dubstep',
              'Dutch House', 'East Coast Hip-Hop', 'Electric Blues', 'Electro', 'Electroclash',
              'Electro Funk', 'Electro House', 'Electro Jazz', 'Electronic', 'Electropop',
              'Electro Soul', 'Electro Swing', 'Eurodance', 'Experimental', 'Fidget House',
              'Flamenco', 'Folk', 'Folk Rock', 'Frenchcore', 'French House', 'Funk',
              'Funk Metal', 'Funk Rock', 'Funkstep', 'Future Bass', 'Future Beats',
              'Future Bounce', 'Future Funk', 'Future House', 'Gabber', 'Gangsta Rap',
              'Garage House', 'Garage Rock', 'G-Funk', 'G-House', 'Glam Metal', 'Glam Rock',
              'Glitch Hop', 'Goa Trance', 'Gospel', 'Gothic Rock', 'Grime', 'Groove Metal',
              'Grunge', 'Halftime', 'Handsup', 'Happy Hardcore', 'Hard Beat', 'Hard Bop',
              'Hardcore', 'Hardcore Hip-Hop', 'Hardcore Punk', 'Hard Dance', 'Hard House',
              'Hard Rock', 'Hardstyle', 'Hardtek', 'Hard Trance', 'Heavy Metal', 'Hip-Hop',
              'Hip-House', 'Horrorcore', 'House', 'Hybrid', 'Hybrid Trap', 'IDM',
              'Indian Classical Music', 'Indie', 'Indie Dance', 'Indie Folk', 'Indie Pop',
              'Indie Rock', 'Industrial', 'Industrial Metal', 'Instrumental Rock', 'Jazz',
              'Jazz Funk', 'Jazz Fusion', 'Jazz Rap', 'Jazz Rock', 'J-Pop', 'Jumpstyle',
              'Jungle', 'Jungle Terror', 'Kawaii Metal', 'K-Pop', 'Latin', 'Latin Rock',
              'Leftfield', 'Liquid Funk', 'Lolicore', 'Mambo', 'Mashup', 'Melodic Death Metal',
              'Metal', 'Metalcore', 'Metalstep', 'Mid-Tempo', 'Minimal', 'Modal Jazz',
              'Modern Classical', 'Moombahcore', 'Moombahton', 'Neo Soul', 'Neue Deutsche Härte',
              'Neue Deutsche Welle', 'Neurofunk', 'Neurohop', 'Neuro Trap', 'New Age',
              'New Beat', 'New Jack Swing', 'New Wave', 'Nu Disco', 'Nu Funk', 'Nu Jazz',
              'Nu Metal', 'Oi!', 'Oriental Metal', 'Pop', 'Pop Jazz', 'Pop Punk', 'Pop Rap',
              'Pop Rock', 'Post-Britpop', 'Post-Disco', 'Post-Grunge', 'Post-Hardcore',
              'Post-Punk', 'Post-Punk Revival', 'Post-Rock', 'Power Metal', 'Power Pop',
              'Power Rock', 'Primus', 'Progressive Death Metal', 'Progressive House',
              'Progressive Metal', 'Progressive Metalcore', 'Progressive Psytrance',
              'Progressive Rock', 'Progressive Trance', 'Psychedelic Blues', 'Psychedelic Funk',
              'Psychedelic Pop', 'Psychedelic Rock', 'Psychedelic Soul', 'Psychill', 'Psytrance',
              'Punk', 'Punk Rock', 'Raga Rock', 'Ragga', 'Raggatek', 'Rap', 'Rap Be', 'Rap Fr',
              'Rap Rock', 'Rap Uk', 'Rap Us', 'Rawstyle', 'R&B', 'Reggae', 'Reggae Metal',
              'Reggaestep', 'Riddim', 'Rock', 'Rockabilly', "Rock'n'Roll", 'Rocksteady',
              'Roots Reggae', 'Shoegaze', 'Ska', 'Ska Punk', 'Slowcore', 'Slow Rock',
              'Smooth Jazz', 'Soft Rock', 'Soul', 'Southern Rock', 'Southern Soul', 'Space Rock',
              'Speedcore', 'Speed Garage', 'Speed Metal', 'Stoner Rock', 'Sunshine Pop',
              'Surf Rock', 'Swing', 'Symphonic Metal', 'Symphonic Rock', 'Synthpop', 'Synthwave',
              'Tech House', 'Techno', 'Texas Blues', 'Thrash Metal', 'Tradional Pop',
              'Trance', 'Trap', 'Tribal', 'Tribal House', 'Tribecore', 'Trip-Hop',
              'Tropical House', 'Turntablism', 'UK Garage', 'Vocal', 'Vocal Jazz',
              'West Coast Hip-Hop', 'World Music', 'Zeuhl', 'Zouk']
