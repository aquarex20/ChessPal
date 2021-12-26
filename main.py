# -*-coding:Latin-1 -*
import pygame
# specs du plateau
""" écart entre bande de gauche et cases 20pixel, bande du bas et pixel 20.
milieu d'une case 20 pixel en partant de l'extrémité gauche du pixel.
si t'a bien compris et que t'es pas un sale retardé autiste, tu comprends
que tu dois additionner +20 pixel aux x et y pour toucher les cases.
Un côté d'une case mesure 45/45 pixel.À partir de ça, les mesures ne sont plus
requises. utilise le calcul normal et casse pas lec

J'ai aussi redimensionné les pièces pour qu'elles fasses 30 pixel au lieu de 60
Donc, mtn, tout ce que t'a à faire c'est les centrer et programmer tes morts



Autres notes:
Concernant les problèmes d'autodestruction (friendly fire), une solution  simple pour  implémenter le:
if piècecase2[0]!="bpion1" and piècecase2[0]!="bpion2" and piècecase2[0]!="bpion3" and piècecase2[0]!= "bpion4" and piècecase2[0]!= "bpion5" and piècecase2[0]!= "bpion6" and piècecase2[0]!= "bpion7" and piècecase2[0]!= "bpion8" and piècecase2[0]!= "btour1" and piècecase2[0]!= "btour2" and piècecase2[0]!= "bcheval1" and piècecase2[0]!= "bcheval2" and piècecase2[0]!= "bfou1" and piècecase2[0]!= "bfou2" and piècecase2[0]!= "breine" and piècecase2[0]!= "broi" and piècecase2[0]!= "nroi":
serait de les mettre directement sous les conditions de pièce (exemple: if pièce cliquée==Roi/Fou/Reine/pion: if  piècecase2[0]!=piècealliée1, pièce alliée2 etc.
)Cela marche car, s'il n'y a pas de pièce dans la seconde case (donc qu'on a qu'un simple déplacement, donc piècedanscase2=False), dans tous les cas, cela
n'empechera pas la condition de s'exécuter normalement, comme c'est une question ("Est-ce que ça c'est égal à ça"), et puis si il y a une pièce dans la
seconde case, alors sous aucun cas sommes-nous autorisé de toutes les manières dans le jeu d'échec de nous déplacer dans celle-ci si la pièce est alliée
ou si elle est le roi opposé. Jusqu'ici je l'ai pas implémenté comme ça, (sous forme de conditions) ce qui fait en sorte que c'est un peu redondant et risqué.
Mais dans l'éventualité ou on aurait des problèmes du genre, il suffirait tout simplement de recoller cela dans chaque pièce comme ça on économise énormément
de temps. 
"""

# importation

import pygame
import os
import timeit

from time import *
from pygame.locals import *

# temps
start = timeit.timeit()

# construction

pygame.init()

size = width, height = 500, 500

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Échecs")

# couleurs
RED = (255, 0, 0)
GRAY = (150, 150, 150)

# import images

plateau = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\bleu.jpg')

# blanc
ibpion1 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\bpion.png')
ibpion2 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\bpion.png')
ibpion3 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\bpion.png')
ibpion4 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\bpion.png')
ibpion5 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\bpion.png')
ibpion6 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\bpion.png')
ibpion7 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\bpion.png')
ibpion8 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\bpion.png')
ibtour1 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\btour.png')
ibtour2 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\btour.png')
ibcheval1 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\bcheval.png')
ibcheval2 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\bcheval.png')
ibfou1 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\bfou.png')
ibfou2 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\bfou.png')
ibreine = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\breine.png')
ibroi = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\broi.png')

# noir
inpion1 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\npion.png')
inpion2 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\npion.png')
inpion3 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\npion.png')
inpion4 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\npion.png')
inpion5 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\npion.png')
inpion6 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\npion.png')
inpion7 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\npion.png')
inpion8 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\npion.png')
intour1 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\ntour.png')
intour2 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\ntour.png')
incheval1 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\ncheval.png')
incheval2 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\ncheval.png')
infou1 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\nfou.png')
infou2 = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\nfou.png')
inreine = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\nreine.png')
inroi = pygame.image.load(r'C:\Users\Hmili\Pictures\échecs\nroi.png')

# variables importantes

"""
x et y sont l'intro le (0,0) du plateau. Ensuite, xx et yy sont le nombre
de cases à droite et en bas.
"""
# composantes images pièces de sorte à ce qu'elles soient centrées. En effet, les images ne sont pas centrées de la même manière que les pièces rectangulaires
x = 21
y = 21
yy = 56
xx = 56
# composantes pièces, cases sur l'échiquier
xa = 52
xxa = 56
ya = 52
yya = 56

# passer de images pièces ( dict coordonnées) à coordonnées rectangulaires des pièces sur l'échiquier, il suffit d'ajouter ces coefficients:
i_à_r = -x + xa
# passer des coordonnées rectangulaires des pièces sur l'échiquier aux coordonnées d'image ( dict coordonnées)
r_à_i = -xa + x

# Ordre de commencement:

noir = False  # Blancs commencent

action = False
piècedanscase2 = False  # assure toi qu'il est actualisé dans le code

écheceursn, écheceursb = [], []  # on fait simplement en sorte qu'on ne commence pas avec des échecs.
béchec, néchec = False, False

# code modifié par l'utilisateur

"""
Il faut garderen tête le fait que la position des pièces va changer tout
au long d'une partie d'échec. Il est crucial de séparer l'état initial
d'une boucle infinie while True qui risque de réinitialiser constamment
les valeurs
"""

"""
Le code suivant sert à attribuer une forme rectangulaire définie à chacune
des aires attribuées aux pièces. Cette aire correspond à la case mais
réduite un  peu pour éviter des contacts avec les autres cases.
Donc  au lieu de prendre 55 longueur,55largeur; j'ai pris
50longueur, 50largeur."""

# noir
npion1 = Rect(0, 0, 55, 55)
npion2 = Rect(0, 0, 55, 55)
npion3 = Rect(0, 0, 55, 55)
npion4 = Rect(0, 0, 55, 55)
npion5 = Rect(0, 0, 55, 55)
npion6 = Rect(0, 0, 55, 55)
npion7 = Rect(0, 0, 55, 55)
npion8 = Rect(0, 0, 55, 55)

ntour1 = Rect(0, 0, 55, 55)
ntour2 = Rect(0, 0, 55, 55)
ncheval1 = Rect(0, 0, 55, 55)
ncheval2 = Rect(0, 0, 55, 55)
nfou1 = Rect(0, 0, 55, 55)
nfou2 = Rect(0, 0, 55, 55)
nreine = Rect(0, 0, 55, 55)
nroi = Rect(0, 0, 55, 55)

# blanc

bpion1 = Rect(0, 0, 55, 55)
bpion2 = Rect(0, 0, 55, 55)
bpion3 = Rect(0, 0, 55, 55)
bpion4 = Rect(0, 0, 55, 55)
bpion5 = Rect(0, 0, 55, 55)
bpion6 = Rect(0, 0, 55, 55)
bpion7 = Rect(0, 0, 55, 55)
bpion8 = Rect(0, 0, 55, 55)

btour1 = Rect(0, 0, 55, 55)
btour2 = Rect(0, 0, 55, 55)
bcheval1 = Rect(0, 0, 55, 55)
bcheval2 = Rect(0, 0, 55, 55)
bfou1 = Rect(0, 0, 55, 55)
bfou2 = Rect(0, 0, 55, 55)
breine = Rect(0, 0, 55, 55)
broi = Rect(0, 0, 55, 55)

"""
Ici je me contente de centrer les rectangles des pièces sur les cases de
départ. Donc les pièces sont exactement dans les cases de départ.
"""
# noir

npion1.center = (xa, ya + 1 * yya)

npion2.center = (xa + xxa, ya + 1 * yya)

npion3.center = (xa + 2 * xxa, ya + 1 * yya)

npion4.center = (xa + 3 * xxa, ya + 1 * yya)

npion5.center = (xa + 4 * xxa, ya + 1 * yya)

npion6.center = (xa + 5 * xxa, ya + 1 * yya)

npion7.center = (xa + 6 * xxa, ya + 1 * yya)

npion8.center = (xa + 7 * xxa, ya + 1 * yya)

ntour1.center = (xa, ya)

ntour2.center = (xa + 7 * xx, ya)

ncheval1.center = (xa + xx, ya)

ncheval2.center = (xa + 6 * xx, ya)

nfou1.center = (xa + 2 * xx, ya)

nfou2.center = (xa + 5 * xx, ya)

nreine.center = (xa + 3 * xx, ya)

nroi.center = (xa + 4 * xx, ya)

##blanc

bpion1.center = (xa, ya + 6 * yya)

bpion2.center = (xa + xxa, ya + 6 * yya)

bpion3.center = (xa + 2 * xxa, ya + 6 * yya)

bpion4.center = (xa + 3 * xxa, ya + 6 * yya)

bpion5.center = (xa + 4 * xxa, ya + 6 * yya)

bpion6.center = (xa + 5 * xxa, ya + 6 * yya)

bpion7.center = (xa + 6 * xxa, ya + 6 * yya)

bpion8.center = (xa + 7 * xxa, ya + 6 * yya)

btour1.center = (xa, ya + 7 * yya)

btour2.center = (xa + 7 * xx, ya + 7 * yya)

bcheval1.center = (xa + xx, ya + 7 * yya)

bcheval2.center = (xa + 6 * xx, ya + 7 * yya)

bfou1.center = (xa + 2 * xx, ya + 7 * yya)

bfou2.center = (xa + 5 * xx, ya + 7 * yya)

breine.center = (xa + 3 * xx, ya + 7 * yya)

broi.center = (xa + 4 * xx, ya + 7 * yya)

# données de base

ixntour1 = x
iyntour1 = y
ixncheval1 = x + xx
iyncheval1 = y
ixnfou1 = x + 2 * xx
iynfou1 = y
ixnreine = x + 3 * xx
iynreine = y

ixnroi = x + 4 * xx
iynroi = y

ixnfou2 = x + 5 * xx
iynfou2 = y
ixncheval2 = x + 6 * xx
iyncheval2 = y
ixntour2 = x + 7 * xx
iyntour2 = y
ixnpion1 = x
iynpion1 = y + yy
ixnpion2 = x + xx
iynpion2 = y + yy
ixnpion3 = x + 2 * xx
iynpion3 = y + yy
ixnpion4 = x + 3 * xx
iynpion4 = y + yy
ixnpion5 = x + 4 * xx
iynpion5 = y + yy

ixnpion6 = x + 5 * xx
iynpion6 = y + yy
ixnpion7 = x + 6 * xx
iynpion7 = y + yy
ixnpion8 = x + 7 * xx
iynpion8 = y + yy
ixbtour1 = x
iybtour1 = y + 7 * yy
ixbcheval1 = x + xx
iybcheval1 = y + 7 * yy

ixbfou1 = x + 2 * xx
iybfou1 = y + 7 * yy
ixbreine = x + 3 * xx
iybreine = y + 7 * yy
ixbroi = x + 4 * xx
iybroi = y + 7 * yy
ixbfou2 = x + 5 * xx
iybfou2 = y + 7 * yy
ixbcheval2 = x + 6 * xx
iybcheval2 = y + 7 * yy
ixbtour2 = x + 7 * xx
iybtour2 = y + 7 * yy
ixbpion1 = x
iybpion1 = y + 6 * yy
ixbpion2 = x + xx
iybpion2 = y + 6 * yy
ixbpion3 = x + 2 * xx
iybpion3 = y + 6 * yy
ixbpion4 = x + 3 * xx
iybpion4 = y + 6 * yy
ixbpion5 = x + 4 * xx
iybpion5 = y + 6 * yy
ixbpion6 = x + 5 * xx
iybpion6 = y + 6 * yy
ixbpion7 = x + 6 * xx
iybpion7 = y + 6 * yy
ixbpion8 = x + 7 * xx
iybpion8 = y + 6 * yy

coordonnées = dict(
    ntour1=(ixntour1, iyntour1),
    ncheval1=(ixncheval1, iyncheval1),
    nfou1=(ixnfou1, iynfou1),
    nreine=(ixnreine, iynreine),
    nroi=(ixnroi, iynroi),
    nfou2=(ixnfou2, iynfou2),
    ncheval2=(ixncheval2, iyncheval2),
    ntour2=(ixntour2, iyntour2),
    npion1=(ixnpion1, iynpion1),
    npion2=(ixnpion2, iynpion2),
    npion3=(ixnpion3, iynpion3),
    npion4=(ixnpion4, iynpion4),
    npion5=(ixnpion5, iynpion5),
    npion6=(ixnpion6, iynpion6),
    npion7=(ixnpion7, iynpion7),
    npion8=(ixnpion8, iynpion8),
    btour1=(ixbtour1, iybtour1),
    bcheval1=(ixbcheval1, iybcheval1),
    bfou1=(ixbfou1, iybfou1),
    breine=(ixbreine, iybreine),
    broi=(ixbroi, iybroi),
    bfou2=(ixbfou2, iybfou2),
    bcheval2=(ixbcheval2, iybcheval2),
    btour2=(ixbtour2, iybtour2),
    bpion1=(ixbpion1, iybpion1),
    bpion2=(ixbpion2, iybpion2),
    bpion3=(ixbpion3, iybpion3),
    bpion4=(ixbpion4, iybpion4),
    bpion5=(ixbpion5, iybpion5),
    bpion6=(ixbpion6, iybpion6),
    bpion7=(ixbpion7, iybpion7),
    bpion8=(ixbpion8, iybpion8))

# Échiquier-attribution d'aires de cases

a1 = Rect(0, 0, 55, 55)
a2 = Rect(0, 0, 55, 55)
a3 = Rect(0, 0, 55, 55)
a4 = Rect(0, 0, 55, 55)
a5 = Rect(0, 0, 55, 55)
a6 = Rect(0, 0, 55, 55)
a7 = Rect(0, 0, 55, 55)
a8 = Rect(0, 0, 55, 55)

b1 = Rect(0, 0, 55, 55)
b2 = Rect(0, 0, 55, 55)
b3 = Rect(0, 0, 55, 55)
b4 = Rect(0, 0, 55, 55)
b5 = Rect(0, 0, 55, 55)
b6 = Rect(0, 0, 55, 55)
b7 = Rect(0, 0, 55, 55)
b8 = Rect(0, 0, 55, 55)

c1 = Rect(0, 0, 55, 55)
c2 = Rect(0, 0, 55, 55)
c3 = Rect(0, 0, 55, 55)
c4 = Rect(0, 0, 55, 55)
c5 = Rect(0, 0, 55, 55)
c6 = Rect(0, 0, 55, 55)
c7 = Rect(0, 0, 55, 55)
c8 = Rect(0, 0, 55, 55)

d1 = Rect(0, 0, 55, 55)
d2 = Rect(0, 0, 55, 55)
d3 = Rect(0, 0, 55, 55)
d4 = Rect(0, 0, 55, 55)
d5 = Rect(0, 0, 55, 55)
d6 = Rect(0, 0, 55, 55)
d7 = Rect(0, 0, 55, 55)
d8 = Rect(0, 0, 55, 55)

e1 = Rect(0, 0, 55, 55)
e2 = Rect(0, 0, 55, 55)
e3 = Rect(0, 0, 55, 55)
e4 = Rect(0, 0, 55, 55)
e5 = Rect(0, 0, 55, 55)
e6 = Rect(0, 0, 55, 55)
e7 = Rect(0, 0, 55, 55)
e8 = Rect(0, 0, 55, 55)

f1 = Rect(0, 0, 55, 55)
f2 = Rect(0, 0, 55, 55)
f3 = Rect(0, 0, 55, 55)
f4 = Rect(0, 0, 55, 55)
f5 = Rect(0, 0, 55, 55)
f6 = Rect(0, 0, 55, 55)
f7 = Rect(0, 0, 55, 55)
f8 = Rect(0, 0, 55, 55)

g1 = Rect(0, 0, 55, 55)
g2 = Rect(0, 0, 55, 55)
g3 = Rect(0, 0, 55, 55)
g4 = Rect(0, 0, 55, 55)
g5 = Rect(0, 0, 55, 55)
g6 = Rect(0, 0, 55, 55)
g7 = Rect(0, 0, 55, 55)
g8 = Rect(0, 0, 55, 55)

h1 = Rect(0, 0, 55, 55)
h2 = Rect(0, 0, 55, 55)
h3 = Rect(0, 0, 55, 55)
h4 = Rect(0, 0, 55, 55)
h5 = Rect(0, 0, 55, 55)
h6 = Rect(0, 0, 55, 55)
h7 = Rect(0, 0, 55, 55)
h8 = Rect(0, 0, 55, 55)

# Échiquier-Positionnement


a1.center = (xa, ya + 7 * yy)
a2.center = (xa, ya + 6 * yy)
a3.center = (xa, ya + 5 * yy)
a4.center = (xa, ya + 4 * yy)
a5.center = (xa, ya + 3 * yy)
a6.center = (xa, ya + 2 * yy)
a7.center = (xa, ya + 1 * yy)
a8.center = (xa, ya)

b1.center = (xa + xx, ya + 7 * yy)
b2.center = (xa + xx, ya + 6 * yy)
b3.center = (xa + xx, ya + 5 * yy)
b4.center = (xa + xx, ya + 4 * yy)
b5.center = (xa + xx, ya + 3 * yy)
b6.center = (xa + xx, ya + 2 * yy)
b7.center = (xa + xx, ya + 1 * yy)
b8.center = (xa + xx, ya)

c1.center = (xa + 2 * xx, ya + 7 * yy)
c2.center = (xa + 2 * xx, ya + 6 * yy)
c3.center = (xa + 2 * xx, ya + 5 * yy)
c4.center = (xa + 2 * xx, ya + 4 * yy)
c5.center = (xa + 2 * xx, ya + 3 * yy)
c6.center = (xa + 2 * xx, ya + 2 * yy)
c7.center = (xa + 2 * xx, ya + 1 * yy)
c8.center = (xa + 2 * xx, ya)

d1.center = (xa + 3 * xx, ya + 7 * yy)
d2.center = (xa + 3 * xx, ya + 6 * yy)
d3.center = (xa + 3 * xx, ya + 5 * yy)
d4.center = (xa + 3 * xx, ya + 4 * yy)
d5.center = (xa + 3 * xx, ya + 3 * yy)
d6.center = (xa + 3 * xx, ya + 2 * yy)
d7.center = (xa + 3 * xx, ya + 1 * yy)
d8.center = (xa + 3 * xx, ya)

e1.center = (xa + 4 * xx, ya + 7 * yy)
e2.center = (xa + 4 * xx, ya + 6 * yy)
e3.center = (xa + 4 * xx, ya + 5 * yy)
e4.center = (xa + 4 * xx, ya + 4 * yy)
e5.center = (xa + 4 * xx, ya + 3 * yy)
e6.center = (xa + 4 * xx, ya + 2 * yy)
e7.center = (xa + 4 * xx, ya + 1 * yy)
e8.center = (xa + 4 * xx, ya)

f1.center = (xa + 5 * xx, ya + 7 * yy)
f2.center = (xa + 5 * xx, ya + 6 * yy)
f3.center = (xa + 5 * xx, ya + 5 * yy)
f4.center = (xa + 5 * xx, ya + 4 * yy)
f5.center = (xa + 5 * xx, ya + 3 * yy)
f6.center = (xa + 5 * xx, ya + 2 * yy)
f7.center = (xa + 5 * xx, ya + 1 * yy)
f8.center = (xa + 5 * xx, ya)

g1.center = (xa + 6 * xx, ya + 7 * yy)
g2.center = (xa + 6 * xx, ya + 6 * yy)
g3.center = (xa + 6 * xx, ya + 5 * yy)
g4.center = (xa + 6 * xx, ya + 4 * yy)
g5.center = (xa + 6 * xx, ya + 3 * yy)
g6.center = (xa + 6 * xx, ya + 2 * yy)
g7.center = (xa + 6 * xx, ya + 1 * yy)
g8.center = (xa + 6 * xx, ya)

h1.center = (xa + 7 * xx, ya + 7 * yy)
h2.center = (xa + 7 * xx, ya + 6 * yy)
h3.center = (xa + 7 * xx, ya + 5 * yy)
h4.center = (xa + 7 * xx, ya + 4 * yy)
h5.center = (xa + 7 * xx, ya + 3 * yy)
h6.center = (xa + 7 * xx, ya + 2 * yy)
h7.center = (xa + 7 * xx, ya + 1 * yy)
h8.center = (xa + 7 * xx, ya)

"""
On crée un dictionnaire qui sert à parcourir plus facilement les
aires rectangulaires des pièces. Il faudra changer les aires rectangulaires dans la section de mouvements.
En effet, lors d'un mouvement, non seulement les coordonnées d'image changent, (changeant ainsi le blit par le biais d'un changement dans le
dictionnaire coordonnées. Mais en plus, il y a changement de l'aire rectangulaire des pièces. En effet, chaque pièce possède une coordonnée image,
et une coordonnée rectangulaire et une coordonnée position (implémentée dans la coordonnée rectangulaire. Ainsi, il faudra aussi recentrer chaque pièce
par le biais de npièece.center (x,y). Cela ne changera que le rectangle de la pièce correspondante, rien d'autre. Il donne littéralement les aires rectangulaires.
Il est utile en bas, dans la branche
des évênements, quon on utilise la méthode collidedict(dictionnaire)
qui évite de faire des branches à la: for element in: do:
"""

pièces = dict(
    ntour1=ntour1,
    ncheval1=ncheval1,
    nfou1=nfou1,
    nreine=nreine,
    nroi=nroi,
    nfou2=nfou2,
    ncheval2=ncheval2,
    ntour2=ntour2,
    npion1=npion1,
    npion2=npion2,
    npion3=npion3,
    npion4=npion4,
    npion5=npion5,
    npion6=npion6,
    npion7=npion7,
    npion8=npion8,
    btour1=btour1,
    bcheval1=bcheval1,
    bfou1=bfou1,
    breine=breine,
    broi=broi,
    bfou2=bfou2,
    bcheval2=bcheval2,
    btour2=btour2,
    bpion1=bpion1,
    bpion2=bpion2,
    bpion3=bpion3,
    bpion4=bpion4,
    bpion5=bpion5,
    bpion6=bpion6,
    bpion7=bpion7,
    bpion8=bpion8)

# clonage
# pièces clone simplement pour les tests d'éventuels échecs auto infligés.
pièces_échec = dict(pièces)

while True:

    screen.fill((255, 255, 255))
    screen.blit(plateau, (0, 0))

    """
    Le code suivant est lié aux aires rectangulaires. Ces dernières sont centrées selon les données du dictionnaire pièces. Ce dernier est évidemment
    updated par les mouvements des pièces.

    """

    # noir

    # ntour1.center=(pièces['ntour1'].x,pièces['ntour1'].y)
    ntour1 = pièces['ntour1']

    ncheval1 = pièces['ncheval1']

    nfou1 = pièces['nfou1']

    nreine = pièces['nreine']

    nroi = pièces['nroi']

    nfou2 = pièces['nfou2']

    ncheval2 = pièces['ncheval2']

    ntour2 = pièces['ntour2']

    npion1 = pièces['npion1']

    npion2 = pièces['npion2']

    npion3 = pièces['npion3']

    npion4 = pièces['npion4']

    npion5 = pièces['npion5']

    npion6 = pièces['npion6']

    npion7 = pièces['npion7']

    npion8 = pièces['npion8']

    # blanc

    btour1 = pièces['btour1']

    bcheval1 = pièces['bcheval1']

    bfou1 = pièces['bfou1']

    breine = pièces['breine']

    broi = pièces['broi']

    bfou2 = pièces['bfou2']

    bcheval2 = pièces['bcheval2']

    btour2 = pièces['btour2']

    bpion1 = pièces['bpion1']

    bpion2 = pièces['bpion2']

    bpion3 = pièces['bpion3']

    bpion4 = pièces['bpion4']

    bpion5 = pièces['bpion5']

    bpion6 = pièces['bpion6']

    bpion7 = pièces['bpion7']

    bpion8 = pièces['bpion8']

    """
    Le code blit suivant seulement dédié à l'affichage,
    ca n'a aucune incidence
    sur les coordonnés
    """

    screen.blit(intour1, (coordonnées['ntour1'][0], coordonnées['ntour1'][1]))

    screen.blit(incheval1, (coordonnées['ncheval1'][0], coordonnées['ncheval1'][1]))

    screen.blit(infou1, (coordonnées['nfou1'][0], coordonnées['nfou1'][1]))

    screen.blit(inreine, (coordonnées['nreine'][0], coordonnées['nreine'][1]))

    screen.blit(inroi, (coordonnées['nroi'][0], coordonnées['nroi'][1]))

    screen.blit(infou2, (coordonnées['nfou2'][0], coordonnées['nfou2'][1]))

    screen.blit(incheval2, (coordonnées['ncheval2'][0], coordonnées['ncheval2'][1]))

    screen.blit(intour2, (coordonnées['ntour2'][0], coordonnées['ntour2'][1]))

    screen.blit(inpion1, (coordonnées['npion1'][0], coordonnées['npion1'][1]))

    screen.blit(inpion2, (coordonnées['npion2'][0], coordonnées['npion2'][1]))

    screen.blit(inpion3, (coordonnées['npion3'][0], coordonnées['npion3'][1]))

    screen.blit(inpion4, (coordonnées['npion4'][0], coordonnées['npion4'][1]))

    screen.blit(inpion5, (coordonnées['npion5'][0], coordonnées['npion5'][1]))

    screen.blit(inpion6, (coordonnées['npion6'][0], coordonnées['npion6'][1]))

    screen.blit(inpion7, (coordonnées['npion7'][0], coordonnées['npion7'][1]))

    screen.blit(inpion8, (coordonnées['npion8'][0], coordonnées['npion8'][1]))

    # blanc

    screen.blit(ibtour1, (coordonnées['btour1'][0], coordonnées['btour1'][1]))

    screen.blit(ibcheval1, (coordonnées['bcheval1'][0], coordonnées['bcheval1'][1]))

    screen.blit(ibfou1, (coordonnées['bfou1'][0], coordonnées['bfou1'][1]))

    screen.blit(ibreine, (coordonnées['breine'][0], coordonnées['breine'][1]))

    screen.blit(ibroi, (coordonnées['broi'][0], coordonnées['broi'][1]))

    screen.blit(ibfou2, (coordonnées['bfou2'][0], coordonnées['bfou2'][1]))

    screen.blit(ibcheval2, (coordonnées['bcheval2'][0], coordonnées['bcheval2'][1]))

    screen.blit(ibtour2, (coordonnées['btour2'][0], coordonnées['btour2'][1]))

    screen.blit(ibpion1, (coordonnées['bpion1'][0], coordonnées['bpion1'][1]))

    screen.blit(ibpion2, (coordonnées['bpion2'][0], coordonnées['bpion2'][1]))

    screen.blit(ibpion3, (coordonnées['bpion3'][0], coordonnées['bpion3'][1]))

    screen.blit(ibpion4, (coordonnées['bpion4'][0], coordonnées['bpion4'][1]))

    screen.blit(ibpion5, (coordonnées['bpion5'][0], coordonnées['bpion5'][1]))

    screen.blit(ibpion6, (coordonnées['bpion6'][0], coordonnées['bpion6'][1]))

    screen.blit(ibpion7, (coordonnées['bpion7'][0], coordonnées['bpion7'][1]))

    screen.blit(ibpion8, (coordonnées['bpion8'][0], coordonnées['bpion8'][1]))

    """
    il faudra éventuellement changer ixntour1 et iyn pour coordonnées[ntour1][0] et [1], afin que
    lorsqu'on bouge les pièces on puisse modifier directement le dictionnaire sans avoir à changer ixntour1, et toutes les autres valeurs.
    de ixn et ixb. En effet, je n'utilise les coordonnées ixn ou ixb seulement dans coordonnées, sinon, ils servent de coordonnées de base lorsque le jeu débute.
    La synthaxe à adopter dans les mouvements de pièces sera: de modifier les valeurs x (0) et y(1) du dictionnaire des coordonnées directement.
    Ensuite, on aurait directement un blit différent. Le Blit avec ixn n'est initial que pour la position initiale. 
    """

    # dictionnaire de cases

    cases = dict(

        a1=a1,
        a2=a2,
        a3=a3,
        a4=a4,
        a5=a5,
        a6=a6,
        a7=a7,
        a8=a8,
        b1=b1,
        b2=b2,
        b3=b3,
        b4=b4,
        b5=b5,
        b6=b6,
        b7=b7,
        b8=b8,
        c1=c1,
        c2=c2,
        c3=c3,
        c4=c4,
        c5=c5,
        c6=c6,
        c7=c7,
        c8=c8,
        d1=d1,
        d2=d2,
        d3=d3,
        d4=d4,
        d5=d5,
        d6=d6,
        d7=d7,
        d8=d8,
        e1=e1,
        e2=e2,
        e3=e3,
        e4=e4,
        e5=e5,
        e6=e6,
        e7=e7,
        e8=e8,
        f1=f1,
        f2=f2,
        f3=f3,
        f4=f4,
        f5=f5,
        f6=f6,
        f7=f7,
        f8=f8,
        g1=g1,
        g2=g2,
        g3=g3,
        g4=g4,
        g5=g5,
        g6=g6,
        g7=g7,
        g8=g8,
        h1=h1,
        h2=h2,
        h3=h3,
        h4=h4,
        h5=h5,
        h6=h6,
        h7=h7,
        h8=h8)

    # évênements
    déjapassé = False  # le code finira par avoir déjapassé=False comme on est dans un  while(True)
    piècedanscase2 = False


    if déjapassé == False:  # on  inclus cette boucle car on veut différencier 2 clics. Or, on ne peut  les différencier si on considère le meme event.
        # il faut donc sortir de la boucle event afin d'attendre le prochain.
        # ici voir si les blancs sont en échecs et si les noirs sont en échec

        """ ...............................................................................................................................
            Fonctions bool.....................................................................................................................
        """
        """ Noirs mettent en échec les blancs par le move des blancs? """


        ####################################################################################
        # Noirs mettent en échec les blancs ?

        def coup_safe_pour_blancs():
            global pièces_échec
            coup_safe = True

            for pièce in pièces_échec:

                if (pièce == "npion1" or pièce == "npion2" or pièce == "npion3" or
                        pièce == "npion4" or pièce == "npion5" or pièce == "npion6" or
                        pièce == "npion7" or pièce == "npion8"):

                    # Si le pion noir est en mesure de manger à droite ou à gauche, où se trouve le nroi
                    if pièces_échec[pièce] == Rect(pièces['broi'].x - xxa, pièces['broi'].y - yya, 55, 55) or \
                            pièces_échec[pièce] == Rect(pièces['broi'].x + xxa, pièces['broi'].y - yya, 55, 55):
                        return False

                if (pièce == "ntour1" or pièce == "ntour2"):

                    if pièces['broi'].x == pièces_échec[pièce].x:  # même x

                        if pièces_échec[pièce].y < pièces[
                            'broi'].y:  # tour en haut, elle va parcourir en bas, donc y monte
                            j = +1  # variable d'incrémentation pour parcourir tous les rectangles vers le bas
                            obstrué = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pièces_échec[pièce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]

                        while j <= 8:  # le maximum de cases parcourable.
                            liste_Rec.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55))

                            if Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55).collidedict(pièces_échec,
                                                                                                 True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)

                            j += 1

                        if liste_RecObstruction != []:

                            if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                                print(
                                    "Liste_RecObstruction détecte une collision, reste plus qu'à voir avec quelle pièce")
                                if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "broi":
                                    print("Le roi serait en échec, non safe")

                                    return False

                        if pièces_échec[pièce].y > pièces[
                            'broi'].y:  # tour en bas, elle va parcourir en haut, donc y descend

                            j = -1  # variable d'incrémentation pour parcourir tous les rectangles vers le bas
                            obstrué = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []

                            assert pièces_échec[pièce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]

                        while -j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55))
                            # print(j, ": ", liste_RecObstruction, "\n")

                            if Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55).collidedict(pièces_échec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            j -= 1
                        if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "broi":
                                # print(pièce, "met  le roi blanc en échec!")

                                return False

                    if pièces['broi'].y == pièces_échec[pièce].y:  # même y

                        if pièces_échec[pièce].x < pièces[
                            'broi'].x:  # tour à gauche, elle va parcourir à droite, donc x augmente.
                            j = +1  # variable d'incrémentation pour parcourir tous les rectangles vers la droite
                            obstrué = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []

                            assert pièces_échec[pièce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]

                        while j <= 8:  # le maximum de cases parcourable.
                            liste_Rec.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55))

                            if Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55).collidedict(pièces_échec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)

                            j += 1

                        print("Liste Rec Obstruction est", liste_RecObstruction)
                        if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "broi":
                                # print(pièce, "met  le roi blanc en échec!")

                                return False

                        if pièces_échec[pièce].x > pièces[
                            'broi'].x:  # tour à droite, elle va parcourir à gauche, donc x diminue.
                            j = -1  # variable d'incrémentation pour parcourir tous les rectangles vers la droite
                            obstrué = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pièces_échec[pièce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]

                        while -j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55))

                            if Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55).collidedict(pièces_échec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            j -= 1

                        if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "broi":
                                # print(pièce, "met  le roi blanc en échec!")

                                return False

                if (pièce == "ncheval1" or pièce == "ncheval2"):

                    if ((pièces['broi'].y == pièces_échec[pièce].y - 2 * yy and pièces['broi'].x == pièces_échec[
                        pièce].x - xx)  # 1
                            or (pièces['broi'].y == pièces_échec[pièce].y - 2 * yy and pièces['broi'].x == pièces_échec[
                                pièce].x + xx)  # 2
                            or (pièces['broi'].y == pièces_échec[pièce].y - yy and pièces['broi'].x == pièces_échec[
                                pièce].x + 2 * xx)  # 3
                            or (pièces['broi'].y == pièces_échec[pièce].y - yy and pièces['broi'].x == pièces_échec[
                                pièce].x - 2 * xx)  # 4
                            or (pièces['broi'].y == pièces_échec[pièce].y + 2 * yy and pièces['broi'].x == pièces_échec[
                                pièce].x - xx)  # 5
                            or (pièces['broi'].y == pièces_échec[pièce].y + 2 * yy and pièces['broi'].x == pièces_échec[
                                pièce].x + xx)  # 6
                            or (pièces['broi'].y == pièces_échec[pièce].y + yy and pièces['broi'].x == pièces_échec[
                                pièce].x + 2 * xx)  # 7
                            or (pièces['broi'].y == pièces_échec[pièce].y + yy and pièces['broi'].x == pièces_échec[
                                pièce].x - 2 * xx)  # 8
                    ):
                        return False

                if (
                        pièce == "nfou1" or pièce == "nfou2"):  # pour le fou, on sait pas si le roi est sur une des diagonales, donc on va essayer
                    # dans toutes les directions

                    # haut droite

                    # Code obstruction

                    if pièces['broi'].y < pièces_échec[pièce].y and pièces['broi'].x > pièces_échec[
                        pièce].x:  # cela revient à monter et aller à droite

                        liste_RecObstruction, liste_Rec = [], []
                        assert pièces_échec[pièce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]
                        j, jx = 1, 1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                        jy = -1  # variable d'incrémentation pourc parcourir tous les rectangles en y dans le cas d'une montée.
                        onlyroi, obstrué = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            # liste_Rec.append(Rect(case_de_base.x+jx*xx, case_de_base.y+jy*yy,55,55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pièces_échec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            jy -= 1  # vers le haut
                            jx += 1  # vers la droite
                            j += 1
                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                                if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "broi":
                                    # print(pièce, "met  le roi blanc en échec! via haut droite")
                                    print("\n La liste est", liste_RecObstruction)

                                    return False

                    # haut gauche
                    if pièces['broi'].y < pièces_échec[pièce].y and pièces['broi'].x < pièces_échec[
                        pièce].x:  # cela revient à monter et aller à gauche

                        liste_RecObstruction, liste_Rec = [], []
                        assert pièces_échec[pièce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]
                        j, jx = 1, -1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la gauche.
                        jy = -1  # variable d'incrémentation pour parcourir tous les rectangles en y dans le cas d'une montée.
                        onlyroi, obstrué = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            # liste_Rec.append(Rect(case_de_base.x+jx*xx, case_de_base.y+jy*yy,55,55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pièces_échec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            jy -= 1  # vers le haut
                            jx -= 1  # vers la gauche
                            j += 1

                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "broi":
                                # print(pièce, "met  le roi blanc en échec! via haut gauche")
                                print("\n La liste est", liste_RecObstruction, "et la liste sans obs est ", liste_Rec)

                                return False

                    # bas droite
                    if pièces['broi'].y > pièces_échec[pièce].y and pièces['broi'].x > pièces_échec[
                        pièce].x:  # cela revient à descendre et aller à droite

                        liste_RecObstruction, liste_Rec = [], []
                        assert pièces_échec[pièce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]
                        j, jx = 1, +1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                        jy = +1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'une descente.
                        onlyroi, obstrué = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            # liste_Rec.append(Rect(case_de_base.x+jx*xx, case_de_base.y+jy*yy,55,55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pièces_échec,True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            jy += 1  # vers le bas
                            jx += 1  # vers la droite
                            j += 1

                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "broi":
                                # print(pièce, "met  le roi blanc en échec!")

                                return False

                    # bas gauche

                    if pièces['broi'].y > pièces_échec[pièce].y and pièces['broi'].x < pièces_échec[
                        pièce].x:  # cela revient à descendre et aller à gauche

                        liste_RecObstruction, liste_Rec = [], []
                        assert pièces_échec[pièce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]
                        j, jx = 1, -1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la gauched.
                        jy = +1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'une descente.
                        onlyroi, obstrué = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            # liste_Rec.append(Rect(case_de_base.x+jx*xx, case_de_base.y+jy*yy,55,55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pièces_échec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            jy += 1  # vers le bas
                            jx -= 1  # vers la gauche
                            j += 1
                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "broi":
                                # print(pièce, "met  le roi blanc en échec!")

                                return False

                if (pièce == "nreine"):

                    """

                    Cette fois-ci, on va relier 2 codes obstruction! Celui de la tour et celui  du fou, comme ce sont les fonctions
                    inhérentes de la reine. Comme la reine effectue exactement les mêmes fonctions que le fou et la tour. Alors,
                    on va juste les copier coller...
                    Ses fonctions sont:
                    1. Haut jusqu'à limite sans échec
                    2. Bas jusqu'à limite sans échec
                    3. Droite jusqu'à  limite sans échec
                    4. Gauche jusqu'à limite sans échec
                    5. Diagonale Haut Droite jusqu'à limite sans échec
                    6. Diagonale Haut Gauche jusqu'à limite sans échec
                    7. Diagonale Bas Droite jusqu'à limite sans échec
                    8. Diagonale Bas Gauche jusqu'à limite sans échec

                        """
                    # fonction tour (haut,bas, gauche, droite)
                    if pièces['broi'].x == pièces_échec[pièce].x:  # même x

                        if pièces_échec[pièce].y < pièces[
                            'broi'].y:  # tour en haut, elle va parcourir en bas, donc y monte
                            j = +1  # variable d'incrémentation pour parcourir tous les rectangles vers le bas
                            obstrué = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pièces_échec[pièce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]

                        while j <= 8:  # le maximum de cases parcourable.
                            liste_Rec.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55))

                            if Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55).collidedict(pièces_échec,
                                                                                                 True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)

                            j += 1

                        if liste_RecObstruction != []:

                            if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                                print(
                                    "Liste_RecObstruction détecte une collision, reste plus qu'à voir avec quelle pièce. Par ailleurs:",
                                    liste_RecObstruction[0].collidedict(pièces_échec, True))
                                if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "broi":
                                    print("Le roi serait en échec, non safe")

                                    return False

                        if pièces_échec[pièce].y > pièces[
                            'broi'].y:  # tour en bas, elle va parcourir en haut, donc y descend

                            j = -1  # variable d'incrémentation pour parcourir tous les rectangles vers le bas
                            obstrué = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []

                            assert pièces_échec[pièce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]

                        while -j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55))
                            # print(j, ": ", liste_RecObstruction, "\n")

                            if Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55).collidedict(pièces_échec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            j -= 1
                        if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "broi":
                                # print(pièce, "met  le roi blanc en échec!")

                                return False

                    if pièces['broi'].y == pièces_échec[pièce].y:  # même y

                        if pièces_échec[pièce].x < pièces[
                            'broi'].x:  # tour à gauche, elle va parcourir à droite, donc x augmente.
                            j = +1  # variable d'incrémentation pour parcourir tous les rectangles vers la droite
                            obstrué = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pièces_échec[pièce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]

                        while j <= 8:  # le maximum de cases parcourable.
                            liste_Rec.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55))

                            if Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55).collidedict(pièces_échec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)

                            j += 1

                        print("Liste Rec Obstruction est", liste_RecObstruction)
                        if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "broi":
                                # print(pièce, "met  le roi blanc en échec!")

                                return False

                        if pièces_échec[pièce].x > pièces[
                            'broi'].x:  # tour à droite, elle va parcourir à gauche, donc x diminue.
                            j = -1  # variable d'incrémentation pour parcourir tous les rectangles vers la droite
                            obstrué = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pièces_échec[pièce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]

                        while -j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55))

                            if Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55).collidedict(pièces_échec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            j -= 1

                        if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "broi":
                                # print(pièce, "met  le roi blanc en échec!")

                                return False

                    # haut droite

                    # Code obstruction

                    if pièces['broi'].y < pièces_échec[pièce].y and pièces['broi'].x > pièces_échec[
                        pièce].x:  # cela revient à monter et aller à droite

                        liste_RecObstruction, liste_Rec = [], []
                        assert pièces_échec[pièce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]
                        j, jx = 1, 1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                        jy = -1  # variable d'incrémentation pour parcourir tous les rectangles en y dans le cas d'une montée.
                        onlyroi, obstrué = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pièces_échec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            jy -= 1  # vers le haut
                            jx += 1  # vers la droite
                            j += 1
                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                                if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "broi":
                                    # print(pièce, "met  le roi blanc en échec!")

                                    return False

                    # haut gauche
                    if pièces['broi'].y < pièces_échec[pièce].y and pièces['broi'].x < pièces_échec[
                        pièce].x:  # cela revient à monter et aller à gauche

                        liste_RecObstruction, liste_Rec = [], []
                        assert pièces_échec[pièce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]
                        j, jx = 1, -1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la gauche.
                        jy = -1  # variable d'incrémentation pour parcourir tous les rectangles en y dans le cas d'une montée.
                        onlyroi, obstrué = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pièces_échec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            jy -= 1  # vers le haut
                            jx -= 1  # vers la gauche
                            j += 1
                        if liste_RecObstruction != []:

                            if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                                if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "broi":
                                    # print(pièce, "met  le roi blanc en échec!")

                                    return False

                    # bas droite
                    if pièces['broi'].y > pièces_échec[pièce].y and pièces['broi'].x > pièces_échec[
                        pièce].x:  # cela revient à descendre et aller à droite

                        liste_RecObstruction, liste_Rec = [], []
                        assert pièces_échec[pièce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]
                        j, jx = 1, +1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                        jy = +1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'une descente.
                        onlyroi, obstrué = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pièces_échec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            jy += 1  # vers le bas
                            jx += 1  # vers la droite
                            j += 1
                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "broi":
                                # print(pièce, "met  le roi blanc en échec!")

                                return False

                    # bas gauche
                    if pièces['broi'].y > pièces_échec[pièce].y and pièces['broi'].x < pièces_échec[
                        pièce].x:  # cela revient à descendre et aller à gauche

                        liste_RecObstruction, liste_Rec = [], []
                        assert pièces_échec[pièce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]
                        j, jx = 1, -1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la gauched.
                        jy = +1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'une descente.
                        onlyroi, obstrué = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.

                            liste_Rec.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pièces_échec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            jy += 1  # vers le bas
                            jx -= 1  # vers la gauche
                            j += 1

                        if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "broi":
                                # print(pièce, "met  le roi blanc en échec!")

                                return False
            return True


        """ Blancs mettent en échec les noirs par le move des noirs? """


        #########################################################

        # Blancs mettent en échec les noirs ?

        def coup_safe_pour_noirs():
            global pièces_échec

            for pièce in pièces_échec:

                if (pièce == "bpion1" or pièce == "bpion2" or pièce == "bpion3" or
                        pièce == "bpion4" or pièce == "bpion5" or pièce == "bpion6" or
                        pièce == "bpion7" or pièce == "bpion8"):

                    # Si le pion blanc est en mesure de manger à droite ou à gauche, où se trouve le nroi
                    if pièces_échec[pièce] == Rect(pièces_échec['nroi'].x - xxa, pièces_échec['nroi'].y + yya, 55, 55) or \
                            pièces_échec[pièce] == Rect(pièces_échec['nroi'].x + xxa, pièces_échec['nroi'].y + yya, 55, 55):
                        return False

                if (pièce == "btour1" or pièce == "btour2"):
                    if pièces_échec['nroi'].x == pièces_échec[pièce].x:  # même x

                        if pièces_échec[pièce].y < pièces[
                            'nroi'].y:  # tour en haut, elle va parcourir en bas, donc y monte
                            j = +1  # variable d'incrémentation pour parcourir tous les rectangles vers le bas
                            obstrué = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []

                            assert pièces_échec[pièce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]

                        while j <= 8:  # le maximum de cases parcourable.
                            liste_Rec.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55))

                            if Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55).collidedict(pièces_échec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)

                            j += 1

                        if liste_RecObstruction != []:

                            if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                                if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "nroi":
                                    # print(pièce, "met le roi noir en échec!")

                                    return False

                        if pièces_échec[pièce].y > pièces[
                            'nroi'].y:  # tour en bas, elle va parcourir en haut, donc y descend

                            j = -1  # variable d'incrémentation pour parcourir tous les rectangles vers le bas
                            obstrué = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pièces_échec[pièce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]

                        while -j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55))
                            # print(j, ": ", liste_RecObstruction, "\n")

                            if Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55).collidedict(pièces_échec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            j -= 1
                        if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "nroi":
                                # print(pièce, "met le roi noir en échec!")

                                return False

                    if pièces_échec['nroi'].y == pièces_échec[pièce].y:  # même y

                        if pièces_échec[pièce].x < pièces[
                            'nroi'].x:  # tour à gauche, elle va parcourir à droite, donc x augmente.
                            j = +1  # variable d'incrémentation pour parcourir tous les rectangles vers la droite
                            obstrué = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pièces_échec[pièce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]

                        while j <= 8:  # le maximum de cases parcourable.
                            liste_Rec.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55))

                            if Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55).collidedict(pièces_échec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)

                            j += 1

                        print("Liste Rec Obstruction est", liste_RecObstruction)
                        if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "nroi":
                                # print(pièce, "met le roi noir en échec!")

                                return False

                        if pièces_échec[pièce].x > pièces[
                            'nroi'].x:  # tour à droite, elle va parcourir à gauche, donc x diminue.
                            j = -1  # variable d'incrémentation pour parcourir tous les rectangles vers la droite
                            obstrué = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pièces_échec[pièce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]

                        while -j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55))

                            if Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55).collidedict(pièces_échec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            j -= 1

                        if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "nroi":
                                # print(pièce, "met le roi noir en échec!")

                                return False

                if (pièce == "bcheval1" or pièce == "bcheval2"):

                    if ((pièces_échec['nroi'].y == pièces_échec[pièce].y - 2 * yy and pièces_échec['nroi'].x == pièces_échec[
                        pièce].x - xx)  # 1
                            or (pièces_échec['nroi'].y == pièces_échec[pièce].y - 2 * yy and pièces_échec['nroi'].x == pièces_échec[
                                pièce].x + xx)  # 2
                            or (pièces_échec['nroi'].y == pièces_échec[pièce].y - yy and pièces_échec['nroi'].x == pièces_échec[
                                pièce].x + 2 * xx)  # 3
                            or (pièces_échec['nroi'].y == pièces_échec[pièce].y - yy and pièces_échec['nroi'].x == pièces_échec[
                                pièce].x - 2 * xx)  # 4
                            or (pièces_échec['nroi'].y == pièces_échec[pièce].y + 2 * yy and pièces_échec['nroi'].x == pièces_échec[
                                pièce].x - xx)  # 5
                            or (pièces_échec['nroi'].y == pièces_échec[pièce].y + 2 * yy and pièces_échec['nroi'].x == pièces_échec[
                                pièce].x + xx)  # 6
                            or (pièces_échec['nroi'].y == pièces_échec[pièce].y + yy and pièces_échec['nroi'].x == pièces_échec[
                                pièce].x + 2 * xx)  # 7
                            or (pièces_échec['nroi'].y == pièces_échec[pièce].y + yy and pièces_échec['nroi'].x == pièces_échec[
                                pièce].x - 2 * xx)  # 8
                    ):
                        return False

                if (pièce == "bfou1" or pièce == "bfou2"):  # pour le fou, on sait pas si le roi est sur une des diagonales, donc on va essayer
                    # dans toutes les directions

                    # haut droite

                    # Code obstruction

                    if pièces_échec['nroi'].y < pièces_échec[pièce].y and pièces_échec['nroi'].x > pièces_échec[
                        pièce].x:  # cela revient à monter et aller à droite

                        liste_RecObstruction, liste_Rec = [], []
                        assert pièces_échec[pièce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]
                        #haut droite
                        j, jx = 1, 1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                        jy = -1  # variable d'incrémentation pourc parcourir tous les rectangles en y dans le cas d'une montée.
                        onlyroi, obstrué = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            # liste_Rec.append(Rect(case_de_base.x+jx*xx, case_de_base.y+jy*yy,55,55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pièces_échec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            jy -= 1  # vers le haut
                            jx += 1  # vers la droite
                            j += 1
                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                                if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "nroi":
                                    # print(pièce, "met le roi noir en échec! via haut droite")
                                    print("\n La liste est", liste_RecObstruction)

                                    return False

                    # haut gauche
                    if pièces_échec['nroi'].y < pièces_échec[pièce].y and pièces_échec['nroi'].x < pièces_échec[
                        pièce].x:  # cela revient à monter et aller à gauche

                        case_de_base = pièces_échec[pièce].collidedict(cases, True)
                        liste_RecObstruction, liste_Rec = [], []
                        assert pièces_échec[pièce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]
                        j, jx = 1, -1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la gauche.
                        jy = -1  # variable d'incrémentation pour parcourir tous les rectangles en y dans le cas d'une montée.
                        onlyroi, obstrué = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            # liste_Rec.append(Rect(case_de_base.x+jx*xx, case_de_base.y+jy*yy,55,55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pièces_échec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            jy -= 1  # vers le haut
                            jx -= 1  # vers la gauche
                            j += 1

                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "nroi":
                                # print(pièce, "met le roi noir en échec! via haut gauche")
                                print("\n La liste est", liste_RecObstruction, "et la liste sans obs est ", liste_Rec)

                                return False

                    # bas droite
                    if pièces_échec['nroi'].y > pièces_échec[pièce].y and pièces_échec['nroi'].x > pièces_échec[
                        pièce].x:  # cela revient à descendre et aller à droite

                        liste_RecObstruction, liste_Rec = [], []
                        assert pièces_échec[pièce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]
                        j, jx = 1, +1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                        jy = +1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'une descente.
                        onlyroi, obstrué = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            # liste_Rec.append(Rect(case_de_base.x+jx*xx, case_de_base.y+jy*yy,55,55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pièces_échec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            jy += 1  # vers le bas
                            jx += 1  # vers la droite
                            j += 1

                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "nroi":
                                # print(pièce, "met le roi noir en échec!")

                                return False

                    # bas gauche

                    if pièces_échec['nroi'].y > pièces_échec[pièce].y and pièces_échec['nroi'].x < pièces_échec[
                        pièce].x:  # cela revient à descendre et aller à gauche

                        liste_RecObstruction, liste_Rec = [], []
                        assert pièces_échec[pièce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]
                        j, jx = 1, -1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la gauched.
                        jy = +1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'une descente.
                        onlyroi, obstrué = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            # liste_Rec.append(Rect(case_de_base.x+jx*xx, case_de_base.y+jy*yy,55,55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pièces_échec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            jy += 1  # vers le bas
                            jx -= 1  # vers la gauche
                            j += 1
                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "nroi":
                                # print(pièce, "met le roi noir en échec!")

                                return False

                if (pièce == "breine"):

                    """

                    Cette fois-ci, on va relier 2 codes obstruction! Celui de la tour et celui  du fou, comme ce sont les fonctions
                    inhérentes de la reine. Comme la reine effectue exactement les mêmes fonctions que le fou et la tour. Alors,
                    on va juste les copier coller...
                    Ses fonctions sont:
                    1. Haut jusqu'à limite sans échec
                    2. Bas jusqu'à limite sans échec
                    3. Droite jusqu'à  limite sans échec
                    4. Gauche jusqu'à limite sans échec
                    5. Diagonale Haut Droite jusqu'à limite sans échec
                    6. Diagonale Haut Gauche jusqu'à limite sans échec
                    7. Diagonale Bas Droite jusqu'à limite sans échec
                    8. Diagonale Bas Gauche jusqu'à limite sans échec

                        """
                    # fonction tour (haut,bas, gauche, droite)
                    print(' les x du roi sont',pièces_échec['nroi'].x,'tandis que les x de la reine sont',pièces_échec[pièce].x)
                    if pièces_échec['nroi'].x == pièces_échec[pièce].x:  # même x

                        if pièces_échec[pièce].y < pièces[
                            'nroi'].y:  # tour en haut, elle va parcourir en bas, donc y monte
                            j = +1  # variable d'incrémentation pour parcourir tous les rectangles vers le bas
                            obstrué = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pièces_échec[pièce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]

                        while j <= 8:  # le maximum de cases parcourable.
                            liste_Rec.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55))

                            if Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55).collidedict(pièces_échec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)

                            j += 1

                        if liste_RecObstruction != []:

                            if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                                if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "nroi":
                                    # print(pièce, "met le roi noir en échec!")

                                    return False

                        if pièces_échec[pièce].y > pièces[
                            'nroi'].y:  # tour en bas, elle va parcourir en haut, donc y descend

                            j = -1  # variable d'incrémentation pour parcourir tous les rectangles vers le bas
                            obstrué = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pièces_échec[pièce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]

                        while -j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55))
                            # print(j, ": ", liste_RecObstruction, "\n")

                            if Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55).collidedict(pièces_échec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            j -= 1
                        if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "nroi":
                                # print(pièce, "met le roi noir en échec!")

                                return False

                    if pièces_échec['nroi'].y == pièces_échec[pièce].y:  # même y

                        if pièces_échec[pièce].x < pièces[
                            'nroi'].x:  # tour à gauche, elle va parcourir à droite, donc x augmente.
                            j = +1  # variable d'incrémentation pour parcourir tous les rectangles vers la droite
                            obstrué = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pièces_échec[pièce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]

                        while j <= 8:  # le maximum de cases parcourable.
                            liste_Rec.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55))

                            if Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55).collidedict(pièces_échec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)

                            j += 1

                        print("Liste Rec Obstruction est", liste_RecObstruction)
                        if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "nroi":
                                # print(pièce, "met le roi noir en échec!")

                                return False

                        if pièces_échec[pièce].x > pièces[
                            'nroi'].x:  # tour à droite, elle va parcourir à gauche, donc x diminue.
                            j = -1  # variable d'incrémentation pour parcourir tous les rectangles vers la droite
                            obstrué = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pièces_échec[pièce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]

                        while -j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55))

                            if Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55).collidedict(pièces_échec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            j -= 1

                        if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "nroi":
                                # print(pièce, "met le roi noir en échec!")

                                return False

                    # haut droite

                    # Code obstruction

                    if pièces_échec['nroi'].y < pièces_échec[pièce].y and pièces_échec['nroi'].x > pièces_échec[pièce].x:
                        # cela revient à monter et aller à droite

                        liste_RecObstruction, liste_Rec = [], []
                        assert pièces_échec[pièce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]
                        j, jx = 1, 1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                        jy = -1  # variable d'incrémentation pour parcourir tous les rectangles en y dans le cas d'une montée.
                        onlyroi, obstrué = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pièces_échec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            jy -= 1  # vers le haut
                            jx += 1  # vers la droite
                            j += 1
                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                                if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "nroi":
                                    # print(pièce, "met le roi noir en échec!")

                                    return False

                    # haut gauche
                    if pièces_échec['nroi'].y < pièces_échec[pièce].y and pièces_échec['nroi'].x < pièces_échec[pièce].x:  # cela revient à monter et aller à gauche
                        liste_RecObstruction, liste_Rec = [], []
                        #ici on essaye de trouver la case correspondant à notre reine :D
                        assert pièces_échec[pièce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]
                        j, jx = 1, -1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la gauche.
                        jy = -1  # variable d'incrémentation pour parcourir tous les rectangles en y dans le cas d'une montée.
                        onlyroi, obstrué = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pièces_échec,True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,55))
                                # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            print('Contenu à l\'itération', j,' :',liste_RecObstruction,pièces_échec==pièces)
                            jy -= 1  # vers le haut
                            jx -= 1  # vers la gauche
                            j += 1
                        if liste_RecObstruction != []:

                            if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                                if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "nroi":
                                    # print(pièce, "met le roi noir en échec!")

                                    return False

                    # bas droite
                    if pièces_échec['nroi'].y > pièces_échec[pièce].y and pièces_échec['nroi'].x > pièces_échec[
                        pièce].x:  # cela revient à descendre et aller à droite

                        liste_RecObstruction, liste_Rec = [], []
                        assert pièces_échec[pièce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]
                        j, jx = 1, +1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                        jy = +1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'une descente.
                        onlyroi, obstrué = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pièces_échec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            jy += 1  # vers le bas
                            jx += 1  # vers la droite
                            j += 1
                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "nroi":
                                # print(pièce, "met le roi noir en échec!")

                                return False

                    # bas gauche
                    if pièces_échec['nroi'].y > pièces_échec[pièce].y and pièces_échec['nroi'].x < pièces_échec[
                        pièce].x:  # cela revient à descendre et aller à gauche

                        liste_RecObstruction, liste_Rec = [], []
                        assert pièces_échec[pièce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pièces_échec[pièce].collidelist(list(cases.values()))]
                        j, jx = 1, -1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la gauched.
                        jy = +1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'une descente.
                        onlyroi, obstrué = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.

                            liste_Rec.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pièces_échec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                            jy += 1  # vers le bas
                            jx -= 1  # vers la gauche
                            j += 1

                        if liste_RecObstruction[0].collidedict(pièces_échec, True) != None:
                            if liste_RecObstruction[0].collidedict(pièces_échec, True)[0] == "nroi":
                                # print(pièce, "met le roi noir en échec!")

                                return False

            return True



        for event in pygame.event.get():

            # fermeture
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # clic gauche sur cases
            if action == False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:

                        pos = pygame.mouse.get_pos()
                        for case in cases:
                            if Rect.collidepoint(cases[case], pos):
                                # clic gauche dans quelle case
                                case1 = case
                                if cases[case].collidedict(pièces, True) != None:
                                    # est-ce qu'il y a pièce dans case cliquée?

                                    piècecase1 = cases[case].collidedict(pièces,
                                                                         True)  # piècecase1 possède 2 coordonnées, la première est le nom de la pièce et la seconde est
                                    # une coordonnée en Rect(1,2,3,4) de la case correspondante.

                                    print("pièce de la  première case est",piècecase1[0])

                                    action = True
                                    déjapassé = True

            if action == True and déjapassé == False:

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        for case in cases:

                            if Rect.collidepoint(cases[case], pos):
                                # clic gauche dans quelle case

                                case2intermédiaire = case
                                case2 = case2intermédiaire

                                if cases[case2].collidedict(pièces, True) != None:
                                    # est-ce qu'il y a pièce dans case cliquée?

                                    piècecase2 = cases[case].collidedict(pièces,
                                                                         True)  # piècecase2[0]='nomdelapièce', piècecase2[1]=Rect(pièce)
                                    print(piècecase2)
                                    piècedanscase2 = True
                                print(piècedanscase2 and piècecase1[0])

                                # cas pion

                                # attribution de coordonnés de la case1

                                xcase1 = cases[case1].x
                                ycase1 = cases[case1].y

                                print(écheceursn)
                                pièces_échec=dict(pièces)

                                if noir == False:  # les blancs commencent
                                    print("Tours des blancs")


                                    def tour_des_blancs():
                                        global noir,action,déjapassé,pièces_échec

                                        "Ici on met les pouvoirs des pièces"
                                        #pouvoir tour
                                        def pouvoir_tour_b():
                                            global noir, action, déjapassé,pièces_échec


                                            # haut:
                                            # Code obstruction

                                            if cases[case2].y < cases[case1].y and cases[case2].x == cases[
                                                case1].x:  # cela revient à monter

                                                liste_RecObstruction, liste_Rec = [], []
                                                j = -1  # variable d'incrémentation pour parcourir tous les rectangles vers le haut
                                                obstrué, oké = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...

                                                while cases[case1].y + yy + j * yy != cases[
                                                    case2].y:  # il faudra créer un while différent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x, cases[case1].y + j * yy, 55, 55))

                                                    if Rect(cases[case1].x, cases[case1].y + j * yy, 55,
                                                            55).collidedict(pièces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x, cases[case1].y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                                                    j -= 1
                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la ligne
                                                    obstrué = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la ligneé parcourue précédmnt, et 2, la pièce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if piècecase2[0] != "bpion1" and piècecase2[0] != "bpion2" and \
                                                                piècecase2[0] != "bpion3" and piècecase2[
                                                            0] != "bpion4" and piècecase2[0] != "bpion5" and piècecase2[
                                                            0] != "bpion6" and piècecase2[0] != "bpion7" and piècecase2[
                                                            0] != "bpion8" and piècecase2[0] != "btour1" and piècecase2[
                                                            0] != "btour2" and piècecase2[0] != "bcheval1" and \
                                                                piècecase2[0] != "bcheval2" and piècecase2[
                                                            0] != "bfou1" and piècecase2[0] != "bfou2" and piècecase2[
                                                            0] != "breine" and piècecase2[0] != "broi" and piècecase2[
                                                            0] != "nroi":
                                                            oké = True
                                                # test sans obstruction (éviter la téléportation) on veut juste voir si la case cliquée est bien dans la liste des rectangles linéaires
                                                téléportation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        téléportation = False
                                                if len(liste_RecObstruction) == 0 and téléportation == False:  # pas d'obstacles.
                                                    oké = True

                                                # place au test mtn

                                                if obstrué == False and oké == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec

                                                    confirmation_move_b()

                                                    # bas

                                            if cases[case2].y > cases[case1].y and cases[case2].x == cases[
                                                case1].x:  # cela revient à descendre

                                                liste_RecObstruction, liste_Rec = [], []
                                                j = 1  # variable d'incrémentation pour parcourir tous les rectangles du haut vers le bas
                                                obstrué, oké = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...

                                                while cases[case1].y - yy + j * yy != cases[
                                                    case2].y:  # il faudra créer un while différent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x, cases[case1].y + j * yy, 55, 55))

                                                    if Rect(cases[case1].x, cases[case1].y + j * yy, 55,
                                                            55).collidedict(pièces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x, cases[case1].y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                                                    j += 1
                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la ligne
                                                    obstrué = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la ligneé parcourue précédmnt, et 2, la pièce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if piècecase2[0] != "bpion1" and piècecase2[0] != "bpion2" and \
                                                                piècecase2[0] != "bpion3" and piècecase2[
                                                            0] != "bpion4" and piècecase2[0] != "bpion5" and piècecase2[
                                                            0] != "bpion6" and piècecase2[0] != "bpion7" and piècecase2[
                                                            0] != "bpion8" and piècecase2[0] != "btour1" and piècecase2[
                                                            0] != "btour2" and piècecase2[0] != "bcheval1" and \
                                                                piècecase2[0] != "bcheval2" and piècecase2[
                                                            0] != "bfou1" and piècecase2[0] != "bfou2" and piècecase2[
                                                            0] != "breine" and piècecase2[0] != "broi" and piècecase2[
                                                            0] != "nroi":
                                                            oké = True
                                                # test sans obstruction (éviter la téléportation) on veut juste voir si la case cliquée est bien dans la liste des rectangles linéaires
                                                téléportation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        téléportation = False
                                                if len(liste_RecObstruction) == 0 and téléportation == False:  # pas d'obstacles.
                                                    oké = True

                                                # place au test mtn

                                                if obstrué == False and oké == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_b()
                                                    # droite

                                            if cases[case2].y == cases[case1].y and cases[case2].x > cases[
                                                case1].x:  # cela revient à aller à droite

                                                liste_RecObstruction, liste_Rec = [], []
                                                j = 1  # variable d'incrémentation pour parcourir tous les rectangles du haut vers le bas
                                                obstrué, oké = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...

                                                while cases[case1].x - xx + j * xx != cases[
                                                    case2].x:  # il faudra créer un while différent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + j * xx, cases[case1].y, 55, 55))

                                                    if Rect(cases[case1].x + j * xx, cases[case1].y, 55,
                                                            55).collidedict(pièces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + j * xx, cases[case1].y, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                                                    j += 1
                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la ligne
                                                    obstrué = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la ligneé parcourue précédmnt, et 2, la pièce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if piècecase2[0] != "bpion1" and piècecase2[0] != "bpion2" and \
                                                                piècecase2[0] != "bpion3" and piècecase2[
                                                            0] != "bpion4" and piècecase2[0] != "bpion5" and piècecase2[
                                                            0] != "bpion6" and piècecase2[0] != "bpion7" and piècecase2[
                                                            0] != "bpion8" and piècecase2[0] != "btour1" and piècecase2[
                                                            0] != "btour2" and piècecase2[0] != "bcheval1" and \
                                                                piècecase2[0] != "bcheval2" and piècecase2[
                                                            0] != "bfou1" and piècecase2[0] != "bfou2" and piècecase2[
                                                            0] != "breine" and piècecase2[0] != "broi" and piècecase2[
                                                            0] != "nroi":
                                                            oké = True
                                                # test sans obstruction (éviter la téléportation) on veut juste voir si la case cliquée est bien dans la liste des rectangles linéaires
                                                téléportation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        téléportation = False
                                                if len(liste_RecObstruction) == 0 and téléportation == False:  # pas d'obstacles.
                                                    oké = True

                                                # place au test mtn

                                                if obstrué == False and oké == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec

                                                    confirmation_move_b()

                                                    # gauche

                                            if cases[case2].y == cases[case1].y and cases[case2].x < cases[
                                                case1].x:  # cela revient à aller à gauche

                                                liste_RecObstruction, liste_Rec = [], []
                                                j = -1  # variable d'incrémentation pour parcourir tous les rectangles du haut vers le bas
                                                obstrué, oké = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...

                                                while cases[case1].x + xx + j * xx != cases[
                                                    case2].x:  # il faudra créer un while différent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + j * xx, cases[case1].y, 55, 55))

                                                    if Rect(cases[case1].x + j * xx, cases[case1].y, 55,
                                                            55).collidedict(pièces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + j * xx, cases[case1].y, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                                                    j -= 1
                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la ligne
                                                    obstrué = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la ligneé parcourue précédmnt, et 2, la pièce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if piècecase2[0] != "bpion1" and piècecase2[0] != "bpion2" and \
                                                                piècecase2[0] != "bpion3" and piècecase2[
                                                            0] != "bpion4" and piècecase2[0] != "bpion5" and piècecase2[
                                                            0] != "bpion6" and piècecase2[0] != "bpion7" and piècecase2[
                                                            0] != "bpion8" and piècecase2[0] != "btour1" and piècecase2[
                                                            0] != "btour2" and piècecase2[0] != "bcheval1" and \
                                                                piècecase2[0] != "bcheval2" and piècecase2[
                                                            0] != "bfou1" and piècecase2[0] != "bfou2" and piècecase2[
                                                            0] != "breine" and piècecase2[0] != "broi" and piècecase2[
                                                            0] != "nroi":
                                                            oké = True
                                                # test sans obstruction (éviter la téléportation) on veut juste voir si la case cliquée est bien dans la liste des rectangles linéaires
                                                téléportation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        téléportation = False
                                                if len(liste_RecObstruction) == 0 and téléportation == False:  # pas d'obstacles.
                                                    oké = True

                                                # place au test mtn

                                                if obstrué == False and oké == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec

                                                    confirmation_move_b()

                                        #pouvoir fou
                                        def pouvoir_fou_b():
                                            global noir, action, déjapassé,pièces_échec

                                            # 1.haut droite

                                            # Code obstruction

                                            if cases[case2].y < cases[case1].y and cases[case2].x > cases[
                                                case1].x:  # cela revient à monter et aller à droite

                                                liste_RecObstruction, liste_Rec = [], []
                                                jx = 1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                                                jy = -1  # variable d'incrémentation pour parcourir tous les rectangles en y dans le cas d'une montée.
                                                obstrué, oké = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...

                                                while cases[case1].y + yy + jy * yy != cases[
                                                    case2].y:  # il faudra créer un while différent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                             55))

                                                    if Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                            55).collidedict(pièces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                                                    jy -= 1  # vers le haut
                                                    jx += 1  # vers la droite

                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la diagonale
                                                    obstrué = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la diagonale, et 2, la pièce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if piècecase2[0] != "bpion1" and piècecase2[0] != "bpion2" and \
                                                                piècecase2[0] != "bpion3" and piècecase2[
                                                            0] != "bpion4" and piècecase2[0] != "bpion5" and piècecase2[
                                                            0] != "bpion6" and piècecase2[0] != "bpion7" and piècecase2[
                                                            0] != "bpion8" and piècecase2[0] != "btour1" and piècecase2[
                                                            0] != "btour2" and piècecase2[0] != "bcheval1" and \
                                                                piècecase2[0] != "bcheval2" and piècecase2[
                                                            0] != "bfou1" and piècecase2[0] != "bfou2" and piècecase2[
                                                            0] != "breine" and piècecase2[0] != "broi" and piècecase2[
                                                            0] != "nroi":
                                                            oké = True
                                                # test sans obstruction (éviter la téléportation) on veut juste voir si la case cliquée est bien dans la liste des rectangles diagonaux
                                                téléportation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        téléportation = False
                                                if len(liste_RecObstruction) == 0 and téléportation == False:
                                                    oké = True

                                                # place au test mtn
                                                print("oké est", oké)

                                                if obstrué == False and oké == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_b()
                                                    # 2.haut gauche

                                            # Code obstruction

                                            if cases[case2].y < cases[case1].y and cases[case2].x < cases[
                                                case1].x:  # cela revient à monter et aller à gauche

                                                liste_RecObstruction, liste_Rec = [], []
                                                jx = -1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                                                jy = -1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'une montée.
                                                obstrué, oké = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...

                                                while cases[case1].y + yy + jy * yy != cases[
                                                    case2].y:  # il faudra créer un while différent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                             55))
                                                    if Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                            55).collidedict(pièces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                                                    jy -= 1  # vers le haut
                                                    jx -= 1  # vers la gauche

                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la diagonale
                                                    obstrué = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la diagonale, et 2, la pièce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if piècecase2[0] != "bpion1" and piècecase2[0] != "bpion2" and \
                                                                piècecase2[0] != "bpion3" and piècecase2[
                                                            0] != "bpion4" and piècecase2[0] != "bpion5" and piècecase2[
                                                            0] != "bpion6" and piècecase2[0] != "bpion7" and piècecase2[
                                                            0] != "bpion8" and piècecase2[0] != "btour1" and piècecase2[
                                                            0] != "btour2" and piècecase2[0] != "bcheval1" and \
                                                                piècecase2[0] != "bcheval2" and piècecase2[
                                                            0] != "bfou1" and piècecase2[0] != "bfou2" and piècecase2[
                                                            0] != "breine" and piècecase2[0] != "broi" and piècecase2[
                                                            0] != "nroi":
                                                            oké = True
                                                # test sans obstruction (éviter la téléportation) on veut juste voir si la case cliquée est bien dans la liste des rectangles diagonaux
                                                téléportation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        téléportation = False
                                                if len(liste_RecObstruction) == 0 and téléportation == False:
                                                    oké = True

                                                # place au test mtn

                                                if obstrué == False and oké == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_b()
                                                    # 3.bas droite

                                            # Code obstruction

                                            if cases[case2].y > cases[case1].y and cases[case2].x > cases[
                                                case1].x:  # cela revient à descendre et aller à droite

                                                liste_RecObstruction, liste_Rec = [], []
                                                jx = 1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                                                jy = 1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'une montée.
                                                obstrué, oké = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...

                                                while cases[case1].y - yy + jy * yy != cases[
                                                    case2].y:  # il faudra créer un while différent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                             55))
                                                    if Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                            55).collidedict(pièces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                                                    jy += 1  # vers le bas
                                                    jx += 1  # vers la droite

                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la diagonale
                                                    obstrué = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la diagonale, et 2, la pièce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if piècecase2[0] != "bpion1" and piècecase2[0] != "bpion2" and \
                                                                piècecase2[0] != "bpion3" and piècecase2[
                                                            0] != "bpion4" and piècecase2[0] != "bpion5" and piècecase2[
                                                            0] != "bpion6" and piècecase2[0] != "bpion7" and piècecase2[
                                                            0] != "bpion8" and piècecase2[0] != "btour1" and piècecase2[
                                                            0] != "btour2" and piècecase2[0] != "bcheval1" and \
                                                                piècecase2[0] != "bcheval2" and piècecase2[
                                                            0] != "bfou1" and piècecase2[0] != "bfou2" and piècecase2[
                                                            0] != "breine" and piècecase2[0] != "broi" and piècecase2[
                                                            0] != "nroi":
                                                            oké = True
                                                # test sans obstruction (éviter la téléportation) on veut juste voir si la case cliquée est bien dans la liste des rectangles diagonaux
                                                téléportation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        téléportation = False
                                                if len(liste_RecObstruction) == 0 and téléportation == False:
                                                    oké = True

                                                # place au test mtn

                                                if obstrué == False and oké == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_b()
                                                    # 4.bas gauche

                                            # Code obstruction

                                            if cases[case2].y > cases[case1].y and cases[case2].x < cases[
                                                case1].x:  # cela revient à descendre et aller à gauche

                                                liste_RecObstruction, liste_Rec = [], []
                                                jx = -1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                                                jy = +1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'une montée.
                                                obstrué, oké = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...

                                                while cases[case1].y - yy + jy * yy < cases[
                                                    case2].y:  # il faudra créer un while différent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                             55))

                                                    if Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                            55).collidedict(pièces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                                                    jy += 1  # vers le bas
                                                    jx -= 1  # vers la gauche

                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la diagonale
                                                    obstrué = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la diagonale, et 2, la pièce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if piècecase2[0] != "bpion1" and piècecase2[0] != "bpion2" and \
                                                                piècecase2[0] != "bpion3" and piècecase2[
                                                            0] != "bpion4" and piècecase2[0] != "bpion5" and piècecase2[
                                                            0] != "bpion6" and piècecase2[0] != "bpion7" and piècecase2[
                                                            0] != "bpion8" and piècecase2[0] != "btour1" and piècecase2[
                                                            0] != "btour2" and piècecase2[0] != "bcheval1" and \
                                                                piècecase2[0] != "bcheval2" and piècecase2[
                                                            0] != "bfou1" and piècecase2[0] != "bfou2" and piècecase2[
                                                            0] != "breine" and piècecase2[0] != "broi" and piècecase2[
                                                            0] != "nroi":
                                                            oké = True
                                                # test sans obstruction (éviter la téléportation) on veut juste voir si la case cliquée est bien dans la liste des rectangles diagonaux
                                                téléportation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        téléportation = False
                                                if len(liste_RecObstruction) == 0 and téléportation == False:
                                                    oké = True

                                                # place au test mtn

                                                if obstrué == False and oké == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_b()

                                        def confirmation_move_b():
                                            global noir, action, déjapassé,pièces_échec

                                            pièces_échec = dict(pièces)
                                            safe = True
                                            if piècedanscase2 == True:
                                                pièces_échec[piècecase2[0]] = Rect(-100, -100, 55, 55)
                                            pièces_échec[piècecase1[0]] = cases[
                                                case2]  # remplacer ça par pièces[piècecase1[0]]=cases[case2] on a alors la même case, on évite les problèmes de décalages dus à l'imprécision.
                                            assert pièces_échec != pièces
                                            if not coup_safe_pour_blancs():
                                                coordonnées[piècecase1[0]] = cases[case1]
                                                action, déjapassé, pièces_échec = False, True, dict(pièces)
                                                safe = False

                                            if coup_safe_pour_blancs() and safe:
                                                pièces[piècecase1[0]] = cases[
                                                    case2]  # remplacer ça par pièces[piècecase1[0]]=cases[case2] on a alors la même case, on évite les problèmes de décalages dus à l'imprécision.
                                                coordonnées[piècecase1[0]] = (cases[case2][0], cases[case2][1])

                                                if piècedanscase2 == True:
                                                    pièces[piècecase2[0]] = Rect(-100, -100, 55, 55)
                                                    coordonnées[piècecase2[0]] = (-100, -100)

                                                noir, action, déjapassé, pièces_échec = True, False, True, dict(
                                                    pièces)  # remplacer le break par un breaker de condition, soit, joueur1=False et joueur 2 = True
                                            pièces_échec=dict(pièces)

                                        if (piècecase1[0] == "bpion1" or piècecase1[0] == "bpion2" or piècecase1[
                                            0] == "bpion3" or piècecase1[0] == "bpion4" or
                                                piècecase1[0] == "bpion5" or piècecase1[0] == "bpion6" or
                                                piècecase1[0] == "bpion7" or piècecase1[0] == "bpion8"):
                                            # 1.on avance de 2 si à la ligne de départ
                                            print("on est bien dans le pion")

                                            # ligne de départ
                                            if (
                                                    case1 == "a2" or case1 == "b2" or case1 == "c2" or case1 == "d2" or case1 == "e2" or case1 == "f2" or case1 == "g2" or case1 == "h2"):

                                                if cases[case2] == Rect(cases[case1].x, cases[case1].y - 2 * yya, 55,
                                                                        55) and piècedanscase2 == False:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec

                                                    """
                                                       Attention, il se trouve que Python te laisse pas modifier dict['a'][0]!!!! Je sais c bizarre. Il te laisse
                                                     juste modifier dict['a'], mais donc tu dois tout recréer. 
                                                     on ne modifie que la coordonnée en y. Cela devrait modifier le blitz comme ce dernier dépend du dict coordonnées.
                                                     il ne reste plus qu'à modifier  l'aire rectangulaire de la case.

                                                     """

                                                    confirmation_move_b()
                                                    print("juste après le move ud pion qui avance de 2 on a que noir==",
                                                          noir)

                                            # 2. On avance de 1 si pas à la ligne de départ ou si à la ligne de départ

                                            if cases[case2] == Rect(cases[case1].x, cases[case1].y - yya, 55,
                                                                    55) and piècedanscase2 == False:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                confirmation_move_b()

                                            # 3. une pièce bloque l'avancée de 1
                                            # pas besoin d'écrire quoi que ce soit, puisque la condition exclue cela par le biais du bool piècedanscase2 l.829

                                            # 4 On mange en diagonale à droite ou à gauche.
                                            # à droite
                                            if cases[case2] == Rect(cases[case1].x + xxa, cases[case1].y - yya, 55,
                                                                    55) and piècedanscase2 == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec

                                                if piècecase2[0] != "bpion1" and piècecase2[0] != "bpion2" and \
                                                        piècecase2[0] != "bpion3" and piècecase2[0] != "bpion4" and \
                                                        piècecase2[0] != "bpion5" and piècecase2[0] != "bpion6" and \
                                                        piècecase2[0] != "bpion7" and piècecase2[0] != "bpion8" and \
                                                        piècecase2[0] != "btour1" and piècecase2[0] != "btour2" and \
                                                        piècecase2[0] != "bcheval1" and piècecase2[0] != "bcheval2" and \
                                                        piècecase2[0] != "bfou1" and piècecase2[0] != "bfou2" and \
                                                        piècecase2[0] != "breine" and piècecase2[0] != "broi" and \
                                                        piècecase2[
                                                            0] != "nroi":  # and pas en échec sauf si le mouvement permet d'empêcher l'échec

                                                    confirmation_move_b()

                                            # à gauche
                                            if cases[case2] == Rect(cases[case1].x - xxa, cases[case1].y - yya, 55,
                                                                    55) and piècedanscase2 == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec

                                                if piècecase2[0] != "bpion1" and piècecase2[0] != "bpion2" and \
                                                        piècecase2[0] != "bpion3" and piècecase2[0] != "bpion4" and \
                                                        piècecase2[0] != "bpion5" and piècecase2[0] != "bpion6" and \
                                                        piècecase2[0] != "bpion7" and piècecase2[0] != "bpion8" and \
                                                        piècecase2[0] != "btour1" and piècecase2[0] != "btour2" and \
                                                        piècecase2[0] != "bcheval1" and piècecase2[0] != "bcheval2" and \
                                                        piècecase2[0] != "bfou1" and piècecase2[0] != "bfou2" and \
                                                        piècecase2[0] != "breine" and piècecase2[0] != "broi" and \
                                                        piècecase2[
                                                            0] != "nroi":  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_b()




                                            # 5. Avancer le pion rend instantanément le joueur en échec.
                                            # inclus dans les conditions en haut, comme la réalisation de chacune dépend du fait qu'il soit en échec ou pas

                                            # 6. l'utilisateur clique autre part, et il se passe rien.
                                            else:
                                                # print("on est dans else")
                                                action, déjapassé, pièces_échec = False, True, dict(pièces)
                                                # Cela marche comme nous sommes dans la boucle du  second clic, en faisant action,déjapassé,pièces_échec=False,True,dict(pièces), on sort du second clic et on recommence.

                                            # on sort du if de bpion, on démarre le if des autres pièces...

                                        if (piècecase1[0] == "btour1" or piècecase1[0] == "btour2"):

                                            pouvoir_tour_b()
                                            if False:
                                                pass
                                            else:
                                                action, déjapassé, pièces_échec = False, True, dict(pièces)

                                        if (piècecase1[0] == "bcheval1" or piècecase1[0] == "bcheval2"):

                                            if ((cases[case2].y == cases[case1].y - 2 * yy and cases[case2].x == cases[
                                                case1].x - xx)  # 1
                                                    or (cases[case2].y == cases[case1].y - 2 * yy and cases[case2].x ==
                                                        cases[case1].x + xx)  # 2
                                                    or (cases[case2].y == cases[case1].y - yy and cases[case2].x ==
                                                        cases[case1].x + 2 * xx)  # 3
                                                    or (cases[case2].y == cases[case1].y - yy and cases[case2].x ==
                                                        cases[case1].x - 2 * xx)  # 4
                                                    or (cases[case2].y == cases[case1].y + 2 * yy and cases[case2].x ==
                                                        cases[case1].x - xx)  # 5
                                                    or (cases[case2].y == cases[case1].y + 2 * yy and cases[case2].x ==
                                                        cases[case1].x + xx)  # 6
                                                    or (cases[case2].y == cases[case1].y + yy and cases[case2].x ==
                                                        cases[case1].x + 2 * xx)  # 7
                                                    or (cases[case2].y == cases[case1].y + yy and cases[case2].x ==
                                                        cases[case1].x - 2 * xx)  # 8
                                            ) :
                                                if piècedanscase2==True:
                                                    if piècecase2[0]!="bpion1" and piècecase2[0]!="bpion2" and piècecase2[0]!="bpion3" and piècecase2[0]!= "bpion4" and piècecase2[0]!= "bpion5" and piècecase2[0]!= "bpion6" and piècecase2[0]!= "bpion7" and piècecase2[0]!= "bpion8" and piècecase2[0]!= "btour1" and piècecase2[0]!= "btour2" and piècecase2[0]!= "bcheval1" and piècecase2[0]!= "bcheval2" and piècecase2[0]!= "bfou1" and piècecase2[0]!= "bfou2" and piècecase2[0]!= "breine" and piècecase2[0]!= "broi" and piècecase2[0]!= "nroi": #and pas en échec sauf si le mouvement permet d'empêcher l'échec

                                                        confirmation_move_b()
                                                if piècedanscase2==False:
                                                    confirmation_move_b()




                                        if (piècecase1[0] == "bfou1" or piècecase1[0] == "bfou2"):

                                            pouvoir_fou_b()
                                            if False:
                                                pass
                                            else:
                                                action, déjapassé, pièces_échec = False, True, dict(pièces)

                                        if (piècecase1[0] == "breine"):

                                            pouvoir_tour_b()
                                            pouvoir_fou_b()

                                            if False:
                                                pass

                                            else:
                                                action, déjapassé, pièces_échec = False, True, dict(pièces)

                                        if (piècecase1[0] == "broi"):

                                            if piècecase2[0] != "bpion1" and piècecase2[0] != "bpion2" and piècecase2[
                                                0] != "bpion3" and piècecase2[0] != "bpion4" and piècecase2[
                                                0] != "bpion5" and piècecase2[0] != "bpion6" and piècecase2[
                                                0] != "bpion7" and piècecase2[0] != "bpion8" and piècecase2[
                                                0] != "btour1" and piècecase2[0] != "btour2" and piècecase2[
                                                0] != "bcheval1" and piècecase2[0] != "bcheval2" and piècecase2[
                                                0] != "bfou1" and piècecase2[0] != "bfou2" and piècecase2[
                                                0] != "breine" and piècecase2[0] != "broi" and piècecase2[0] != "nroi":

                                                """

                                                Le roi peut effectuer les mêmes fonctions que la reine, sauf qu'il est limité à un pas au lieu d'une infinité.
                                                On peut donc tout copier, mais retirer la seconde moitié du code obstruer, comme le roi ne peut s'obstruer, sauf
                                                lorsqu'il castle. Ainsi, je vais autoriser les fonctions gauche et droite dans une optique d'implémentée le castle.

                                                Ses fonctions sont:
                                                1. Haut de un sans limite, sans échec
                                                2. Bas de un  sans limite, sans échec
                                                3. Droite de un sans limite, sans échec
                                                4. Gauche de un sans limite sans échec
                                                5. Diagonale Haut Droite de un sans limite sans échec
                                                6. Diagonale Haut Gauche de un sans limite sans échec
                                                7. Diagonale Bas Droite de un sans limite sans échec
                                                8. Diagonale Bas Gauche de un sans limite sans échec


                                                """
                                                # haut:

                                                if cases[case2].y == cases[case1].y - yy and cases[case2].x == cases[
                                                    case1].x and piècecase2[0] != "bpion1" and piècecase2[
                                                    0] != "bpion2" and piècecase2[0] != "bpion3" and piècecase2[
                                                    0] != "bpion4" and piècecase2[0] != "bpion5" and piècecase2[
                                                    0] != "bpion6" and piècecase2[0] != "bpion7" and piècecase2[
                                                    0] != "bpion8" and piècecase2[0] != "btour1" and piècecase2[
                                                    0] != "btour2" and piècecase2[0] != "bcheval1" and piècecase2[
                                                    0] != "bcheval2" and piècecase2[0] != "bfou1" and piècecase2[
                                                    0] != "bfou2" and piècecase2[0] != "breine" and piècecase2[
                                                    0] != "broi" and piècecase2[0] != "nroi":  # cela revient à monter

                                                    confirmation_move_b()

                                                # bas

                                                if cases[case2].y == cases[case1].y + yy and cases[case2].x == cases[
                                                    case1].x and piècecase2[0] != "bpion1" and piècecase2[
                                                    0] != "bpion2" and piècecase2[0] != "bpion3" and piècecase2[
                                                    0] != "bpion4" and piècecase2[0] != "bpion5" and piècecase2[
                                                    0] != "bpion6" and piècecase2[0] != "bpion7" and piècecase2[
                                                    0] != "bpion8" and piècecase2[0] != "btour1" and piècecase2[
                                                    0] != "btour2" and piècecase2[0] != "bcheval1" and piècecase2[
                                                    0] != "bcheval2" and piècecase2[0] != "bfou1" and piècecase2[
                                                    0] != "bfou2" and piècecase2[0] != "breine" and piècecase2[
                                                    0] != "broi" and piècecase2[
                                                    0] != "nroi":  # cela revient à descendre

                                                    confirmation_move_b()
                                                # droite

                                                if cases[case2].y == cases[case1].y and cases[case2].x == cases[
                                                    case1].x + xx:  # cela revient à aller à droite

                                                    confirmation_move_b()

                                                # gauche

                                                if cases[case2].y == cases[case1].y and cases[case2].x == cases[
                                                    case1].x - xx:  # cela revient à aller à gauche

                                                    confirmation_move_b()

                                                # 1.haut droite

                                                if cases[case2].y == cases[case1].y - yy and cases[case2].x == cases[
                                                    case1].x + xx:  # cela revient à monter et aller à droite

                                                    confirmation_move_b()

                                                # 2.haut gauche

                                                if cases[case2].y == cases[case1].y - yy and cases[case2].x == cases[
                                                    case1].x - xx:  # cela revient à monter et aller à gauche

                                                    confirmation_move_b()

                                                # 3.bas droite

                                                if cases[case2].y == cases[case1].y + yy and cases[case2].x == cases[
                                                    case1].x + xx:  # cela revient à descendre et aller à droite

                                                    confirmation_move_b()

                                                # 4.bas gauche

                                                if cases[case2].y == cases[case1].y + yy and cases[case2].x == cases[
                                                    case1].x - xx:  # cela revient à descendre et aller à gauche

                                                    confirmation_move_b()

                                                else:
                                                    action, déjapassé, pièces_échec = False, True, dict(pièces)



                                        else:
                                            action, déjapassé, pièces_échec = False, True, dict(pièces)


                                    if coup_safe_pour_blancs() == False:  # blancs en échec
                                        print("blancs en échec")

                                    tour_des_blancs()
                                    print("juste après tour des blancs, ona que noir==", noir)

                                print("noir est", noir)
                                if noir == True:  # les noirs commencent
                                    print("Tours des noirs")

                                    def tour_des_noirs():
                                        global noir,action,déjapassé,pièces_échec


                                        "Ici on met les pouvoirs des pièces"

                                        #pouvoir tour n
                                        def pouvoir_tour_n():
                                            global noir, action, déjapassé,pièces_échec

                                            pièces_échec = dict(pièces)

                                            # haut:
                                            # Code obstruction

                                            if cases[case2].y < cases[case1].y and cases[case2].x == cases[
                                                case1].x:  # cela revient à monter

                                                liste_RecObstruction, liste_Rec = [], []
                                                j = -1  # variable d'incrémentation pour parcourir tous les rectangles vers le haut
                                                obstrué, oké = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...

                                                while cases[case1].y + yy + j * yy != cases[
                                                    case2].y:  # il faudra créer un while différent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x, cases[case1].y + j * yy, 55, 55))

                                                    if Rect(cases[case1].x, cases[case1].y + j * yy, 55,
                                                            55).collidedict(pièces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x, cases[case1].y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                                                    j -= 1
                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la ligne
                                                    obstrué = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la ligneé parcourue précédmnt, et 2, la pièce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                                piècecase2[0] != "npion3" and piècecase2[
                                                            0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                            0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                            0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                            0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                                piècecase2[0] != "ncheval2" and piècecase2[
                                                            0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                            0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                            0] != "broi":
                                                            oké = True
                                                # test sans obstruction (éviter la téléportation) on veut juste voir si la case cliquée est bien dans la liste des rectangles linéaires
                                                téléportation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        téléportation = False
                                                if len(liste_RecObstruction) == 0 and téléportation == False:  # pas d'obstacles.
                                                    oké = True

                                                # place au test mtn

                                                if obstrué == False and oké == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_n()

                                            # bas

                                            if cases[case2].y > cases[case1].y and cases[case2].x == cases[
                                                case1].x:  # cela revient à descendre

                                                liste_RecObstruction, liste_Rec = [], []
                                                j = 1  # variable d'incrémentation pour parcourir tous les rectangles du haut vers le bas
                                                obstrué, oké = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...

                                                while cases[case1].y - yy + j * yy != cases[
                                                    case2].y:  # il faudra créer un while différent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x, cases[case1].y + j * yy, 55, 55))

                                                    if Rect(cases[case1].x, cases[case1].y + j * yy, 55,
                                                            55).collidedict(pièces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x, cases[case1].y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                                                    j += 1
                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la ligne
                                                    obstrué = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la ligneé parcourue précédmnt, et 2, la pièce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                                piècecase2[0] != "npion3" and piècecase2[
                                                            0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                            0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                            0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                            0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                                piècecase2[0] != "ncheval2" and piècecase2[
                                                            0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                            0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                            0] != "broi":
                                                            oké = True
                                                # test sans obstruction (éviter la téléportation) on veut juste voir si la case cliquée est bien dans la liste des rectangles linéaires
                                                téléportation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        téléportation = False
                                                if len(liste_RecObstruction) == 0 and téléportation == False:  # pas d'obstacles.
                                                    oké = True

                                                # place au test mtn

                                                if obstrué == False and oké == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_n()
                                            # droite

                                            if cases[case2].y == cases[case1].y and cases[case2].x > cases[
                                                case1].x:  # cela revient à aller à droite

                                                liste_RecObstruction, liste_Rec = [], []
                                                j = 1  # variable d'incrémentation pour parcourir tous les rectangles du haut vers le bas
                                                obstrué, oké = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...

                                                while cases[case1].x - xx + j * xx != cases[
                                                    case2].x:  # il faudra créer un while différent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + j * xx, cases[case1].y, 55, 55))

                                                    if Rect(cases[case1].x + j * xx, cases[case1].y, 55,
                                                            55).collidedict(pièces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + j * xx, cases[case1].y, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                                                    j += 1
                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la ligne
                                                    obstrué = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la ligneé parcourue précédmnt, et 2, la pièce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                                piècecase2[0] != "npion3" and piècecase2[
                                                            0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                            0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                            0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                            0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                                piècecase2[0] != "ncheval2" and piècecase2[
                                                            0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                            0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                            0] != "broi":
                                                            oké = True
                                                # test sans obstruction (éviter la téléportation) on veut juste voir si la case cliquée est bien dans la liste des rectangles linéaires
                                                téléportation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        téléportation = False
                                                if len(liste_RecObstruction) == 0 and téléportation == False:  # pas d'obstacles.
                                                    oké = True

                                                # place au test mtn

                                                if obstrué == False and oké == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_n()

                                            # gauche

                                            if cases[case2].y == cases[case1].y and cases[case2].x < cases[
                                                case1].x:  # cela revient à aller à gauche

                                                liste_RecObstruction, liste_Rec = [], []
                                                j = -1  # variable d'incrémentation pour parcourir tous les rectangles du haut vers le bas
                                                obstrué, oké = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...

                                                while cases[case1].x + xx + j * xx != cases[
                                                    case2].x:  # il faudra créer un while différent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + j * xx, cases[case1].y, 55, 55))

                                                    if Rect(cases[case1].x + j * xx, cases[case1].y, 55,
                                                            55).collidedict(pièces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + j * xx, cases[case1].y, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                                                    j -= 1
                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la ligne
                                                    obstrué = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la ligneé parcourue précédmnt, et 2, la pièce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                                piècecase2[0] != "npion3" and piècecase2[
                                                            0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                            0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                            0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                            0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                                piècecase2[0] != "ncheval2" and piècecase2[
                                                            0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                            0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                            0] != "broi":
                                                            oké = True
                                                # test sans obstruction (éviter la téléportation) on veut juste voir si la case cliquée est bien dans la liste des rectangles linéaires
                                                téléportation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        téléportation = False
                                                if len(liste_RecObstruction) == 0 and téléportation == False:  # pas d'obstacles.
                                                    oké = True

                                                # place au test mtn

                                                if obstrué == False and oké == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_n()
                                        #pouvoir fou n
                                        def pouvoir_fou_n():
                                            global noir, action, déjapassé, pièces_échec

                                            # 1.haut droite

                                            # Code obstruction

                                            if cases[case2].y < cases[case1].y and cases[case2].x > cases[
                                                case1].x:  # cela revient à monter et aller à droite

                                                liste_RecObstruction, liste_Rec = [], []
                                                jx = 1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                                                jy = -1  # variable d'incrémentation pour parcourir tous les rectangles en y dans le cas d'une montée.
                                                obstrué, oké = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...

                                                while cases[case1].y + yy + jy * yy != cases[
                                                    case2].y:  # il faudra créer un while différent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                             55))

                                                    if Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                            55).collidedict(pièces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                                                    jy -= 1  # vers le haut
                                                    jx += 1  # vers la droite

                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la diagonale
                                                    obstrué = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la diagonale, et 2, la pièce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                                piècecase2[0] != "npion3" and piècecase2[
                                                            0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                            0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                            0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                            0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                                piècecase2[0] != "ncheval2" and piècecase2[
                                                            0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                            0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                            0] != "broi":
                                                            oké = True
                                                # test sans obstruction (éviter la téléportation) on veut juste voir si la case cliquée est bien dans la liste des rectangles diagonaux
                                                téléportation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        téléportation = False
                                                if len(liste_RecObstruction) == 0 and téléportation == False:
                                                    oké = True

                                                # place au test mtn
                                                print("oké est", oké)

                                                if obstrué == False and oké == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_n()
                                            # 2.haut gauche

                                            # Code obstruction

                                            if cases[case2].y < cases[case1].y and cases[case2].x < cases[
                                                case1].x:  # cela revient à monter et aller à gauche

                                                liste_RecObstruction, liste_Rec = [], []
                                                jx = -1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                                                jy = -1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'une montée.
                                                obstrué, oké = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...

                                                while cases[case1].y + yy + jy * yy != cases[
                                                    case2].y:  # il faudra créer un while différent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                             55))
                                                    if Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                            55).collidedict(pièces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                                                    jy -= 1  # vers le haut
                                                    jx -= 1  # vers la gauche

                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la diagonale
                                                    obstrué = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la diagonale, et 2, la pièce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                                piècecase2[0] != "npion3" and piècecase2[
                                                            0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                            0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                            0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                            0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                                piècecase2[0] != "ncheval2" and piècecase2[
                                                            0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                            0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                            0] != "broi":
                                                            oké = True
                                                # test sans obstruction (éviter la téléportation) on veut juste voir si la case cliquée est bien dans la liste des rectangles diagonaux
                                                téléportation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        téléportation = False
                                                if len(liste_RecObstruction) == 0 and téléportation == False:
                                                    oké = True

                                                # place au test mtn

                                                if obstrué == False and oké == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_n()
                                            # 3.bas droite

                                            # Code obstruction

                                            if cases[case2].y > cases[case1].y and cases[case2].x > cases[
                                                case1].x:  # cela revient à descendre et aller à droite

                                                liste_RecObstruction, liste_Rec = [], []
                                                jx = 1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                                                jy = 1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'une montée.
                                                obstrué, oké = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...

                                                while cases[case1].y - yy + jy * yy != cases[
                                                    case2].y:  # il faudra créer un while différent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                             55))
                                                    if Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                            55).collidedict(pièces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                                                    jy += 1  # vers le bas
                                                    jx += 1  # vers la droite

                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la diagonale
                                                    obstrué = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la diagonale, et 2, la pièce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                                piècecase2[0] != "npion3" and piècecase2[
                                                            0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                            0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                            0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                            0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                                piècecase2[0] != "ncheval2" and piècecase2[
                                                            0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                            0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                            0] != "broi":
                                                            oké = True
                                                # test sans obstruction (éviter la téléportation) on veut juste voir si la case cliquée est bien dans la liste des rectangles diagonaux
                                                téléportation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        téléportation = False
                                                        print("teleportation check")
                                                if len(liste_RecObstruction) == 0 and téléportation == False:
                                                    oké = True

                                                # place au test mtn

                                                if obstrué == False and oké == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_n()
                                            # 4.bas gauche

                                            # Code obstruction

                                            if cases[case2].y > cases[case1].y and cases[case2].x < cases[
                                                case1].x:  # cela revient à descendre et aller à gauche

                                                liste_RecObstruction, liste_Rec = [], []
                                                jx = -1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                                                jy = +1  # variable d'incrémentation pour parcourir tous les rectangles en x dans le cas d'une montée.
                                                obstrué, oké = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire démontré par le for ChaqueRec, alors...

                                                while cases[case1].y - yy + jy * yy < cases[
                                                    case2].y:  # il faudra créer un while différent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                             55))

                                                    if Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                            55).collidedict(pièces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la première case (comme elle contient la tour initiale)
                                                    jy += 1  # vers le bas
                                                    jx -= 1  # vers la gauche

                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la diagonale
                                                    obstrué = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la diagonale, et 2, la pièce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                                piècecase2[0] != "npion3" and piècecase2[
                                                            0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                            0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                            0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                            0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                                piècecase2[0] != "ncheval2" and piècecase2[
                                                            0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                            0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                            0] != "broi":
                                                            oké = True
                                                # test sans obstruction (éviter la téléportation) on veut juste voir si la case cliquée est bien dans la liste des rectangles diagonaux
                                                téléportation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        téléportation = False
                                                if len(liste_RecObstruction) == 0 and téléportation == False:
                                                    oké = True

                                                # place au test mtn

                                                if obstrué == False and oké == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_n()

                                        def confirmation_move_n():
                                            global noir, action, déjapassé,pièces_échec

                                            pièces_échec = dict(pièces)
                                            safe = True

                                            if piècedanscase2 == True:
                                                pièces_échec[piècecase2[0]] = Rect(-100, -100, 55, 55)
                                            pièces_échec[piècecase1[0]] = cases[case2]  # remplacer ça par pièces[piècecase1[0]]=cases[case2] on a alors la même case, on évite les problèmes de décalages dus à l'imprécision.
                                            assert pièces_échec != pièces
                                            print('le dernier coup_safe_pour_noirs est',coup_safe_pour_noirs())
                                            if not coup_safe_pour_noirs():
                                                coordonnées[piècecase1[0]] = cases[case1]
                                                action, déjapassé, pièces_échec = False, True, dict(pièces)
                                                safe = False
                                            print('Coup safe pour noirs:',coup_safe_pour_noirs(),'safe',safe)
                                            if coup_safe_pour_noirs() and safe:
                                                pièces[piècecase1[0]] = cases[
                                                    case2]  # remplacer ça par pièces[piècecase1[0]]=cases[case2] on a alors la même case, on évite les problèmes de décalages dus à l'imprécision.
                                                coordonnées[piècecase1[0]] = (cases[case2][0], cases[case2][1])

                                                if piècedanscase2 == True:
                                                    pièces[piècecase2[0]] = Rect(-100, -100, 55, 55)
                                                    coordonnées[piècecase2[0]] = (-100, -100)

                                                noir, action, déjapassé, pièces_échec = False, False, True, dict(
                                                    pièces)  # remplacer le break par un breaker de condition, soit, joueur1=False et joueur 2 = True
                                            pièces_échec=dict(pièces)

                                        if (piècecase1[0] == "npion1" or piècecase1[0] == "npion2" or
                                                piècecase1[0] == "npion3" or
                                                piècecase1[0] == "npion4" or piècecase1[0] == "npion5" or
                                                piècecase1[0] == "npion6" or
                                                piècecase1[0] == "npion7" or piècecase1[0] == "npion8"):
                                            print("je  détecte bien que t,as touché un pion, en effet, c'est le",piècecase1[0])
                                            # 1.on avance de 2 si à la ligne de départ

                                            # ligne de départ
                                            if (case1 == "a7" or case1 == "b7" or case1 == "c7" or case1 == "d7" or case1 == "e7" or case1 == "f7" or case1 == "g7" or case1 == "h7"):

                                                if cases[case2] == Rect(cases[case1].x,
                                                                        cases[case1].y + 2 * yya, 55,
                                                                        55) and piècedanscase2 == False:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_n()

                                            # 2. On avance de 1 si pas à la ligne de départ ou si à la ligne de départ

                                            if cases[case2] == Rect(cases[case1].x, cases[case1].y + yya, 55,
                                                                    55) and piècedanscase2 == False:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                confirmation_move_n()
                                                # 3. une pièce bloque l'avancée de 1
                                                # pas besoin d'écrire quoi que ce soit, puisque la condition exclue cela par le biais du bool piècedanscase2 l.829

                                            # 4 On mange en diagonale à droite ou à gauche.
                                            # à droite
                                            if cases[case2] == Rect(cases[case1].x + xxa, cases[case1].y + yya,
                                                                    55,
                                                                    55) and piècedanscase2 == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec

                                                if piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                        piècecase2[0] != "npion3" and piècecase2[
                                                    0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                    0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                    0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                    0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                        piècecase2[0] != "ncheval2" and piècecase2[
                                                    0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                    0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                    0] != "broi":  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_n()

                                                    # à gauche
                                            if cases[case2] == Rect(cases[case1].x - xxa, cases[case1].y + yya,
                                                                    55,
                                                                    55) and piècedanscase2 == True:  # and pas en échec sauf si le mouvement permet d'empêcher l'échec

                                                if piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                        piècecase2[0] != "npion3" and piècecase2[
                                                    0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                    0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                    0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                    0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                        piècecase2[0] != "ncheval2" and piècecase2[
                                                    0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                    0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                    0] != "broi":  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_n()

                                                    # 5. Avancer le pion rend instantanément le joueur en échec.
                                                    # inclus dans les conditions en haut, comme la réalisation de chacune dépend du fait qu'il soit en échec ou pas

                                            # 6. l'utilisateur clique autre part, et il se passe rien.
                                            else:
                                                # print("on est dans else")
                                                action, déjapassé, pièces_échec = False, True, dict(pièces)
                                                # Cela marche comme nous sommes dans la boucle du  second clic, en faisant action,déjapassé,pièces_échec=False,True,dict(pièces), on sort du second clic et on recommence.

                                        if (piècecase1[0] == "ntour1" or piècecase1[0] == "ntour2"):


                                            pouvoir_tour_n()
                                            if False:
                                                pass
                                            else:
                                                action, déjapassé, pièces_échec = False, True, dict(pièces)

                                        if (piècecase1[0] == "ncheval1" or piècecase1[0] == "ncheval2"):

                                            if ((cases[case2].y == cases[case1].y - 2 * yy and cases[case2].x ==
                                                 cases[case1].x - xx)  # 1
                                                    or (cases[case2].y == cases[case1].y - 2 * yy and cases[
                                                        case2].x == cases[case1].x + xx)  # 2
                                                    or (cases[case2].y == cases[case1].y - yy and cases[
                                                        case2].x == cases[case1].x + 2 * xx)  # 3
                                                    or (cases[case2].y == cases[case1].y - yy and cases[
                                                        case2].x == cases[case1].x - 2 * xx)  # 4
                                                    or (cases[case2].y == cases[case1].y + 2 * yy and cases[
                                                        case2].x == cases[case1].x - xx)  # 5
                                                    or (cases[case2].y == cases[case1].y + 2 * yy and cases[
                                                        case2].x == cases[case1].x + xx)  # 6
                                                    or (cases[case2].y == cases[case1].y + yy and cases[
                                                        case2].x == cases[case1].x + 2 * xx)  # 7
                                                    or (cases[case2].y == cases[case1].y + yy and cases[
                                                        case2].x == cases[case1].x - 2 * xx)  # 8
                                            ):
                                                if piècedanscase2==True:
                                                    if piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                            piècecase2[0] != "npion3" and piècecase2[0] != "npion4" and \
                                                            piècecase2[0] != "npion5" and piècecase2[0] != "npion6" and \
                                                            piècecase2[0] != "npion7" and piècecase2[0] != "npion8" and \
                                                            piècecase2[0] != "ntour1" and piècecase2[0] != "ntour2" and \
                                                            piècecase2[0] != "ncheval1" and piècecase2[
                                                        0] != "ncheval2" and piècecase2[0] != "nfou1" and piècecase2[
                                                        0] != "nfou2" and piècecase2[0] != "nreine" and piècecase2[
                                                        0] != "nroi" and piècecase2[
                                                        0] != "broi":  # and pas en échec sauf si le mouvement permet d'empêcher l'échec

                                                        confirmation_move_n()
                                                if piècedanscase2==False:
                                                    confirmation_move_n()


                                        if (piècecase1[0] == "nfou1" or piècecase1[0] == "nfou2"):


                                            pouvoir_fou_n()
                                            if False:
                                                pass
                                            else:
                                                action, déjapassé, pièces_échec = False, True, dict(pièces)

                                        if (piècecase1[0] == "nreine"):
                                            pouvoir_fou_n()
                                            pouvoir_tour_n()
                                            if False:
                                                pass
                                            else:
                                                action, déjapassé, pièces_échec = False, True, dict(pièces)

                                        if (piècecase1[0] == "nroi"):

                                            # haut:

                                            if cases[case2].y == cases[case1].y - yy and cases[case2].x == \
                                                    cases[case1].x:  # cela revient à monter
                                                if piècedanscase2==False or (piècedansase2==True and piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                        piècecase2[0] != "npion3" and piècecase2[
                                                    0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                    0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                    0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                    0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                        piècecase2[0] != "ncheval2" and piècecase2[
                                                    0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                    0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                    0] != "broi"):  # and pas en échec sauf si le mouvement permet d'empêcher l'échec


                                                    confirmation_move_n()

                                            # bas

                                            if cases[case2].y == cases[case1].y + yy and cases[case2].x == \
                                                    cases[case1].x:  # cela revient à descendre

                                                if piècedanscase2==False or (piècedanscase2==True and piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                        piècecase2[0] != "npion3" and piècecase2[
                                                    0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                    0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                    0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                    0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                        piècecase2[0] != "ncheval2" and piècecase2[
                                                    0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                    0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                    0] != "broi"):  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_n()
                                            # droite

                                            if cases[case2].y == cases[case1].y and cases[case2].x == cases[
                                                case1].x + xx:  # cela revient à aller à droite
                                                if piècedanscase2==False or (piècedanscase2==True and piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                        piècecase2[0] != "npion3" and piècecase2[
                                                    0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                    0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                    0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                    0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                        piècecase2[0] != "ncheval2" and piècecase2[
                                                    0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                    0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                    0] != "broi"):  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                        confirmation_move_n()
                                            # gauche

                                            if cases[case2].y == cases[case1].y and cases[case2].x == cases[
                                                case1].x - xx:  # cela revient à aller à gauche

                                                if piècedanscase2==False or (piècedanscase2==True and piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                        piècecase2[0] != "npion3" and piècecase2[
                                                    0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                    0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                    0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                    0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                        piècecase2[0] != "ncheval2" and piècecase2[
                                                    0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                    0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                    0] != "broi"):  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_n()

                                            # 1.haut droite

                                            if cases[case2].y == cases[case1].y - yy and cases[case2].x == \
                                                    cases[
                                                        case1].x + xx:  # cela revient à monter et aller à droite

                                                if piècedanscase2==False or (piècedanscase2==True and piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                        piècecase2[0] != "npion3" and piècecase2[
                                                    0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                    0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                    0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                    0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                        piècecase2[0] != "ncheval2" and piècecase2[
                                                    0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                    0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                    0] != "broi"):  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_n()

                                            # 2.haut gauche

                                            if cases[case2].y == cases[case1].y - yy and cases[case2].x == \
                                                    cases[
                                                        case1].x - xx:  # cela revient à monter et aller à gauche

                                                if piècedanscase2==False or (piècedanscase2==True and piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                        piècecase2[0] != "npion3" and piècecase2[
                                                    0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                    0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                    0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                    0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                        piècecase2[0] != "ncheval2" and piècecase2[
                                                    0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                    0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                    0] != "broi"):  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_n()
                                            # 3.bas droite

                                            if cases[case2].y == cases[case1].y + yy and cases[case2].x == \
                                                    cases[
                                                        case1].x + xx:  # cela revient à descendre et aller à droite

                                                if piècedanscase2==False or (piècedanscase2==True and piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                        piècecase2[0] != "npion3" and piècecase2[
                                                    0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                    0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                    0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                    0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                        piècecase2[0] != "ncheval2" and piècecase2[
                                                    0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                    0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                    0] != "broi"):  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_n()
                                            # 4.bas gauche

                                            if cases[case2].y == cases[case1].y + yy and cases[case2].x == \
                                                    cases[
                                                        case1].x - xx:  # cela revient à descendre et aller à gauche

                                                if piècedanscase2==False or (piècedanscase2==True and piècecase2[0] != "npion1" and piècecase2[0] != "npion2" and \
                                                        piècecase2[0] != "npion3" and piècecase2[
                                                    0] != "npion4" and piècecase2[0] != "npion5" and piècecase2[
                                                    0] != "npion6" and piècecase2[0] != "npion7" and piècecase2[
                                                    0] != "npion8" and piècecase2[0] != "ntour1" and piècecase2[
                                                    0] != "ntour2" and piècecase2[0] != "ncheval1" and \
                                                        piècecase2[0] != "ncheval2" and piècecase2[
                                                    0] != "nfou1" and piècecase2[0] != "nfou2" and piècecase2[
                                                    0] != "nreine" and piècecase2[0] != "nroi" and piècecase2[
                                                    0] != "broi"):  # and pas en échec sauf si le mouvement permet d'empêcher l'échec
                                                    confirmation_move_n()

                                            else:
                                                action, déjapassé, pièces_échec = False, True, dict(pièces)



                                        else:
                                            action, déjapassé, pièces_échec = False, True, dict(pièces)


                                    if coup_safe_pour_noirs() == False:  # noirs en échec
                                        print("noirs en échec")

                                    tour_des_noirs()

    pygame.display.update()

# fermer programme en cliquant sur x

from sys import exit


