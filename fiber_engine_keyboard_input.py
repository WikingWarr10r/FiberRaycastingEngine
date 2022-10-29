import pygame

left_arrow = pygame.K_LEFT
right_arrow = pygame.K_RIGHT
up_arrow = pygame.K_UP
down_arrow = pygame.K_DOWN
q = pygame.K_q
w = pygame.K_w
e = pygame.K_e
r = pygame.K_r
t = pygame.K_t
y = pygame.K_y
u = pygame.K_u
i = pygame.K_i
o = pygame.K_o
p = pygame.K_p
l = pygame.K_l
k = pygame.K_k
j = pygame.K_j
h = pygame.K_h
g = pygame.K_g
f = pygame.K_f
d = pygame.K_d
s = pygame.K_s
a = pygame.K_a
z = pygame.K_z
x = pygame.K_x
c = pygame.K_c
v = pygame.K_v
b = pygame.K_b
n = pygame.K_n
space = pygame.K_SPACE
zero = pygame.K_0
one = pygame.K_1
two = pygame.K_2
three = pygame.K_3
four = pygame.K_4
five = pygame.K_5
six = pygame.K_6
seven = pygame.K_7
eight = pygame.K_8
nine = pygame.K_9
left_shift = pygame.K_LSHIFT
right_shift = pygame.K_RSHIFT
caps_lock = pygame.K_CAPSLOCK

def get_keyboard_input():
    return pygame.key.get_pressed()