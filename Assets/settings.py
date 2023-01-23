from random import randint

floor = "X" * 32 
platform = " " * randint(0, 18) + "X" * 3
empty = " " * 32
player = " " * 15 + "P" + " " * 15 

level_map = [ 
platform,
empty,
empty,  
empty,  
platform,  
empty,  
empty,
platform,  
empty,  
empty, 
player,  
floor,
]

SCROLL_THRESH = 600
tile_size = 64
WIDTH = 1280
HEIGHT = len(level_map) * tile_size
