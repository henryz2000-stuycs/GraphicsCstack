from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 21, 244, 238 ]
edges = []
polygons = []
transform = new_matrix()

#dw test file
parse_file( 'script', edges, polygons, transform, screen, color )

#henry
#parse_file( 'spinningdisc', edges, polygons, transform, screen, color )
