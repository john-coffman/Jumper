from random import randint

floor = "X" * 32 
platform = " " * randint(0, 18) + "X" * 3

level_map = [ 
'                               ',
'                               ',
'                               ',  
'                               ',  
'                               ',  
'     XXX                       ',  
'                               ',
platform,  
'                               ',  
'                               ', 
'                P              ',  
floor,
]
tile_size = 64
WIDTH = 1280
HEIGHT = len(level_map) * tile_size

