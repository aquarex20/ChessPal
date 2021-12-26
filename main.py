# -*-coding:Latin-1 -*
import pygame
# specs du plateau
""" �cart entre bande de gauche et cases 20pixel, bande du bas et pixel 20.
milieu d'une case 20 pixel en partant de l'extr�mit� gauche du pixel.
si t'a bien compris et que t'es pas un sale retard� autiste, tu comprends
que tu dois additionner +20 pixel aux x et y pour toucher les cases.
Un c�t� d'une case mesure 45/45 pixel.� partir de �a, les mesures ne sont plus
requises. utilise le calcul normal et casse pas lec

J'ai aussi redimensionn� les pi�ces pour qu'elles fasses 30 pixel au lieu de 60
Donc, mtn, tout ce que t'a � faire c'est les centrer et programmer tes morts



Autres notes:
Concernant les probl�mes d'autodestruction (friendly fire), une solution  simple pour  impl�menter le:
if pi�cecase2[0]!="bpion1" and pi�cecase2[0]!="bpion2" and pi�cecase2[0]!="bpion3" and pi�cecase2[0]!= "bpion4" and pi�cecase2[0]!= "bpion5" and pi�cecase2[0]!= "bpion6" and pi�cecase2[0]!= "bpion7" and pi�cecase2[0]!= "bpion8" and pi�cecase2[0]!= "btour1" and pi�cecase2[0]!= "btour2" and pi�cecase2[0]!= "bcheval1" and pi�cecase2[0]!= "bcheval2" and pi�cecase2[0]!= "bfou1" and pi�cecase2[0]!= "bfou2" and pi�cecase2[0]!= "breine" and pi�cecase2[0]!= "broi" and pi�cecase2[0]!= "nroi":
serait de les mettre directement sous les conditions de pi�ce (exemple: if pi�ce cliqu�e==Roi/Fou/Reine/pion: if  pi�cecase2[0]!=pi�cealli�e1, pi�ce alli�e2 etc.
)Cela marche car, s'il n'y a pas de pi�ce dans la seconde case (donc qu'on a qu'un simple d�placement, donc pi�cedanscase2=False), dans tous les cas, cela
n'empechera pas la condition de s'ex�cuter normalement, comme c'est une question ("Est-ce que �a c'est �gal � �a"), et puis si il y a une pi�ce dans la
seconde case, alors sous aucun cas sommes-nous autoris� de toutes les mani�res dans le jeu d'�chec de nous d�placer dans celle-ci si la pi�ce est alli�e
ou si elle est le roi oppos�. Jusqu'ici je l'ai pas impl�ment� comme �a, (sous forme de conditions) ce qui fait en sorte que c'est un peu redondant et risqu�.
Mais dans l'�ventualit� ou on aurait des probl�mes du genre, il suffirait tout simplement de recoller cela dans chaque pi�ce comme �a on �conomise �norm�ment
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

pygame.display.set_caption("�checs")

# couleurs
RED = (255, 0, 0)
GRAY = (150, 150, 150)

# import images

plateau = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\bleu.jpg')

# blanc
ibpion1 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\bpion.png')
ibpion2 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\bpion.png')
ibpion3 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\bpion.png')
ibpion4 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\bpion.png')
ibpion5 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\bpion.png')
ibpion6 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\bpion.png')
ibpion7 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\bpion.png')
ibpion8 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\bpion.png')
ibtour1 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\btour.png')
ibtour2 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\btour.png')
ibcheval1 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\bcheval.png')
ibcheval2 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\bcheval.png')
ibfou1 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\bfou.png')
ibfou2 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\bfou.png')
ibreine = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\breine.png')
ibroi = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\broi.png')

# noir
inpion1 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\npion.png')
inpion2 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\npion.png')
inpion3 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\npion.png')
inpion4 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\npion.png')
inpion5 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\npion.png')
inpion6 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\npion.png')
inpion7 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\npion.png')
inpion8 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\npion.png')
intour1 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\ntour.png')
intour2 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\ntour.png')
incheval1 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\ncheval.png')
incheval2 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\ncheval.png')
infou1 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\nfou.png')
infou2 = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\nfou.png')
inreine = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\nreine.png')
inroi = pygame.image.load(r'C:\Users\Hmili\Pictures\�checs\nroi.png')

# variables importantes

"""
x et y sont l'intro le (0,0) du plateau. Ensuite, xx et yy sont le nombre
de cases � droite et en bas.
"""
# composantes images pi�ces de sorte � ce qu'elles soient centr�es. En effet, les images ne sont pas centr�es de la m�me mani�re que les pi�ces rectangulaires
x = 21
y = 21
yy = 56
xx = 56
# composantes pi�ces, cases sur l'�chiquier
xa = 52
xxa = 56
ya = 52
yya = 56

# passer de images pi�ces ( dict coordonn�es) � coordonn�es rectangulaires des pi�ces sur l'�chiquier, il suffit d'ajouter ces coefficients:
i_�_r = -x + xa
# passer des coordonn�es rectangulaires des pi�ces sur l'�chiquier aux coordonn�es d'image ( dict coordonn�es)
r_�_i = -xa + x

# Ordre de commencement:

noir = False  # Blancs commencent

action = False
pi�cedanscase2 = False  # assure toi qu'il est actualis� dans le code

�checeursn, �checeursb = [], []  # on fait simplement en sorte qu'on ne commence pas avec des �checs.
b�chec, n�chec = False, False

# code modifi� par l'utilisateur

"""
Il faut garderen t�te le fait que la position des pi�ces va changer tout
au long d'une partie d'�chec. Il est crucial de s�parer l'�tat initial
d'une boucle infinie while True qui risque de r�initialiser constamment
les valeurs
"""

"""
Le code suivant sert � attribuer une forme rectangulaire d�finie � chacune
des aires attribu�es aux pi�ces. Cette aire correspond � la case mais
r�duite un  peu pour �viter des contacts avec les autres cases.
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
Ici je me contente de centrer les rectangles des pi�ces sur les cases de
d�part. Donc les pi�ces sont exactement dans les cases de d�part.
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

# donn�es de base

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

coordonn�es = dict(
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

# �chiquier-attribution d'aires de cases

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

# �chiquier-Positionnement


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
On cr�e un dictionnaire qui sert � parcourir plus facilement les
aires rectangulaires des pi�ces. Il faudra changer les aires rectangulaires dans la section de mouvements.
En effet, lors d'un mouvement, non seulement les coordonn�es d'image changent, (changeant ainsi le blit par le biais d'un changement dans le
dictionnaire coordonn�es. Mais en plus, il y a changement de l'aire rectangulaire des pi�ces. En effet, chaque pi�ce poss�de une coordonn�e image,
et une coordonn�e rectangulaire et une coordonn�e position (impl�ment�e dans la coordonn�e rectangulaire. Ainsi, il faudra aussi recentrer chaque pi�ce
par le biais de npi�ece.center (x,y). Cela ne changera que le rectangle de la pi�ce correspondante, rien d'autre. Il donne litt�ralement les aires rectangulaires.
Il est utile en bas, dans la branche
des �v�nements, quon on utilise la m�thode collidedict(dictionnaire)
qui �vite de faire des branches � la: for element in: do:
"""

pi�ces = dict(
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
# pi�ces clone simplement pour les tests d'�ventuels �checs auto inflig�s.
pi�ces_�chec = dict(pi�ces)

while True:

    screen.fill((255, 255, 255))
    screen.blit(plateau, (0, 0))

    """
    Le code suivant est li� aux aires rectangulaires. Ces derni�res sont centr�es selon les donn�es du dictionnaire pi�ces. Ce dernier est �videmment
    updated par les mouvements des pi�ces.

    """

    # noir

    # ntour1.center=(pi�ces['ntour1'].x,pi�ces['ntour1'].y)
    ntour1 = pi�ces['ntour1']

    ncheval1 = pi�ces['ncheval1']

    nfou1 = pi�ces['nfou1']

    nreine = pi�ces['nreine']

    nroi = pi�ces['nroi']

    nfou2 = pi�ces['nfou2']

    ncheval2 = pi�ces['ncheval2']

    ntour2 = pi�ces['ntour2']

    npion1 = pi�ces['npion1']

    npion2 = pi�ces['npion2']

    npion3 = pi�ces['npion3']

    npion4 = pi�ces['npion4']

    npion5 = pi�ces['npion5']

    npion6 = pi�ces['npion6']

    npion7 = pi�ces['npion7']

    npion8 = pi�ces['npion8']

    # blanc

    btour1 = pi�ces['btour1']

    bcheval1 = pi�ces['bcheval1']

    bfou1 = pi�ces['bfou1']

    breine = pi�ces['breine']

    broi = pi�ces['broi']

    bfou2 = pi�ces['bfou2']

    bcheval2 = pi�ces['bcheval2']

    btour2 = pi�ces['btour2']

    bpion1 = pi�ces['bpion1']

    bpion2 = pi�ces['bpion2']

    bpion3 = pi�ces['bpion3']

    bpion4 = pi�ces['bpion4']

    bpion5 = pi�ces['bpion5']

    bpion6 = pi�ces['bpion6']

    bpion7 = pi�ces['bpion7']

    bpion8 = pi�ces['bpion8']

    """
    Le code blit suivant seulement d�di� � l'affichage,
    ca n'a aucune incidence
    sur les coordonn�s
    """

    screen.blit(intour1, (coordonn�es['ntour1'][0], coordonn�es['ntour1'][1]))

    screen.blit(incheval1, (coordonn�es['ncheval1'][0], coordonn�es['ncheval1'][1]))

    screen.blit(infou1, (coordonn�es['nfou1'][0], coordonn�es['nfou1'][1]))

    screen.blit(inreine, (coordonn�es['nreine'][0], coordonn�es['nreine'][1]))

    screen.blit(inroi, (coordonn�es['nroi'][0], coordonn�es['nroi'][1]))

    screen.blit(infou2, (coordonn�es['nfou2'][0], coordonn�es['nfou2'][1]))

    screen.blit(incheval2, (coordonn�es['ncheval2'][0], coordonn�es['ncheval2'][1]))

    screen.blit(intour2, (coordonn�es['ntour2'][0], coordonn�es['ntour2'][1]))

    screen.blit(inpion1, (coordonn�es['npion1'][0], coordonn�es['npion1'][1]))

    screen.blit(inpion2, (coordonn�es['npion2'][0], coordonn�es['npion2'][1]))

    screen.blit(inpion3, (coordonn�es['npion3'][0], coordonn�es['npion3'][1]))

    screen.blit(inpion4, (coordonn�es['npion4'][0], coordonn�es['npion4'][1]))

    screen.blit(inpion5, (coordonn�es['npion5'][0], coordonn�es['npion5'][1]))

    screen.blit(inpion6, (coordonn�es['npion6'][0], coordonn�es['npion6'][1]))

    screen.blit(inpion7, (coordonn�es['npion7'][0], coordonn�es['npion7'][1]))

    screen.blit(inpion8, (coordonn�es['npion8'][0], coordonn�es['npion8'][1]))

    # blanc

    screen.blit(ibtour1, (coordonn�es['btour1'][0], coordonn�es['btour1'][1]))

    screen.blit(ibcheval1, (coordonn�es['bcheval1'][0], coordonn�es['bcheval1'][1]))

    screen.blit(ibfou1, (coordonn�es['bfou1'][0], coordonn�es['bfou1'][1]))

    screen.blit(ibreine, (coordonn�es['breine'][0], coordonn�es['breine'][1]))

    screen.blit(ibroi, (coordonn�es['broi'][0], coordonn�es['broi'][1]))

    screen.blit(ibfou2, (coordonn�es['bfou2'][0], coordonn�es['bfou2'][1]))

    screen.blit(ibcheval2, (coordonn�es['bcheval2'][0], coordonn�es['bcheval2'][1]))

    screen.blit(ibtour2, (coordonn�es['btour2'][0], coordonn�es['btour2'][1]))

    screen.blit(ibpion1, (coordonn�es['bpion1'][0], coordonn�es['bpion1'][1]))

    screen.blit(ibpion2, (coordonn�es['bpion2'][0], coordonn�es['bpion2'][1]))

    screen.blit(ibpion3, (coordonn�es['bpion3'][0], coordonn�es['bpion3'][1]))

    screen.blit(ibpion4, (coordonn�es['bpion4'][0], coordonn�es['bpion4'][1]))

    screen.blit(ibpion5, (coordonn�es['bpion5'][0], coordonn�es['bpion5'][1]))

    screen.blit(ibpion6, (coordonn�es['bpion6'][0], coordonn�es['bpion6'][1]))

    screen.blit(ibpion7, (coordonn�es['bpion7'][0], coordonn�es['bpion7'][1]))

    screen.blit(ibpion8, (coordonn�es['bpion8'][0], coordonn�es['bpion8'][1]))

    """
    il faudra �ventuellement changer ixntour1 et iyn pour coordonn�es[ntour1][0] et [1], afin que
    lorsqu'on bouge les pi�ces on puisse modifier directement le dictionnaire sans avoir � changer ixntour1, et toutes les autres valeurs.
    de ixn et ixb. En effet, je n'utilise les coordonn�es ixn ou ixb seulement dans coordonn�es, sinon, ils servent de coordonn�es de base lorsque le jeu d�bute.
    La synthaxe � adopter dans les mouvements de pi�ces sera: de modifier les valeurs x (0) et y(1) du dictionnaire des coordonn�es directement.
    Ensuite, on aurait directement un blit diff�rent. Le Blit avec ixn n'est initial que pour la position initiale. 
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

    # �v�nements
    d�japass� = False  # le code finira par avoir d�japass�=False comme on est dans un  while(True)
    pi�cedanscase2 = False


    if d�japass� == False:  # on  inclus cette boucle car on veut diff�rencier 2 clics. Or, on ne peut  les diff�rencier si on consid�re le meme event.
        # il faut donc sortir de la boucle event afin d'attendre le prochain.
        # ici voir si les blancs sont en �checs et si les noirs sont en �chec

        """ ...............................................................................................................................
            Fonctions bool.....................................................................................................................
        """
        """ Noirs mettent en �chec les blancs par le move des blancs? """


        ####################################################################################
        # Noirs mettent en �chec les blancs ?

        def coup_safe_pour_blancs():
            global pi�ces_�chec
            coup_safe = True

            for pi�ce in pi�ces_�chec:

                if (pi�ce == "npion1" or pi�ce == "npion2" or pi�ce == "npion3" or
                        pi�ce == "npion4" or pi�ce == "npion5" or pi�ce == "npion6" or
                        pi�ce == "npion7" or pi�ce == "npion8"):

                    # Si le pion noir est en mesure de manger � droite ou � gauche, o� se trouve le nroi
                    if pi�ces_�chec[pi�ce] == Rect(pi�ces['broi'].x - xxa, pi�ces['broi'].y - yya, 55, 55) or \
                            pi�ces_�chec[pi�ce] == Rect(pi�ces['broi'].x + xxa, pi�ces['broi'].y - yya, 55, 55):
                        return False

                if (pi�ce == "ntour1" or pi�ce == "ntour2"):

                    if pi�ces['broi'].x == pi�ces_�chec[pi�ce].x:  # m�me x

                        if pi�ces_�chec[pi�ce].y < pi�ces[
                            'broi'].y:  # tour en haut, elle va parcourir en bas, donc y monte
                            j = +1  # variable d'incr�mentation pour parcourir tous les rectangles vers le bas
                            obstru� = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pi�ces_�chec[pi�ce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]

                        while j <= 8:  # le maximum de cases parcourable.
                            liste_Rec.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55))

                            if Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55).collidedict(pi�ces_�chec,
                                                                                                 True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)

                            j += 1

                        if liste_RecObstruction != []:

                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                                print(
                                    "Liste_RecObstruction d�tecte une collision, reste plus qu'� voir avec quelle pi�ce")
                                if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "broi":
                                    print("Le roi serait en �chec, non safe")

                                    return False

                        if pi�ces_�chec[pi�ce].y > pi�ces[
                            'broi'].y:  # tour en bas, elle va parcourir en haut, donc y descend

                            j = -1  # variable d'incr�mentation pour parcourir tous les rectangles vers le bas
                            obstru� = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []

                            assert pi�ces_�chec[pi�ce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]

                        while -j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55))
                            # print(j, ": ", liste_RecObstruction, "\n")

                            if Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55).collidedict(pi�ces_�chec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            j -= 1
                        if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "broi":
                                # print(pi�ce, "met  le roi blanc en �chec!")

                                return False

                    if pi�ces['broi'].y == pi�ces_�chec[pi�ce].y:  # m�me y

                        if pi�ces_�chec[pi�ce].x < pi�ces[
                            'broi'].x:  # tour � gauche, elle va parcourir � droite, donc x augmente.
                            j = +1  # variable d'incr�mentation pour parcourir tous les rectangles vers la droite
                            obstru� = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []

                            assert pi�ces_�chec[pi�ce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]

                        while j <= 8:  # le maximum de cases parcourable.
                            liste_Rec.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55))

                            if Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55).collidedict(pi�ces_�chec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)

                            j += 1

                        print("Liste Rec Obstruction est", liste_RecObstruction)
                        if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "broi":
                                # print(pi�ce, "met  le roi blanc en �chec!")

                                return False

                        if pi�ces_�chec[pi�ce].x > pi�ces[
                            'broi'].x:  # tour � droite, elle va parcourir � gauche, donc x diminue.
                            j = -1  # variable d'incr�mentation pour parcourir tous les rectangles vers la droite
                            obstru� = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pi�ces_�chec[pi�ce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]

                        while -j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55))

                            if Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55).collidedict(pi�ces_�chec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            j -= 1

                        if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "broi":
                                # print(pi�ce, "met  le roi blanc en �chec!")

                                return False

                if (pi�ce == "ncheval1" or pi�ce == "ncheval2"):

                    if ((pi�ces['broi'].y == pi�ces_�chec[pi�ce].y - 2 * yy and pi�ces['broi'].x == pi�ces_�chec[
                        pi�ce].x - xx)  # 1
                            or (pi�ces['broi'].y == pi�ces_�chec[pi�ce].y - 2 * yy and pi�ces['broi'].x == pi�ces_�chec[
                                pi�ce].x + xx)  # 2
                            or (pi�ces['broi'].y == pi�ces_�chec[pi�ce].y - yy and pi�ces['broi'].x == pi�ces_�chec[
                                pi�ce].x + 2 * xx)  # 3
                            or (pi�ces['broi'].y == pi�ces_�chec[pi�ce].y - yy and pi�ces['broi'].x == pi�ces_�chec[
                                pi�ce].x - 2 * xx)  # 4
                            or (pi�ces['broi'].y == pi�ces_�chec[pi�ce].y + 2 * yy and pi�ces['broi'].x == pi�ces_�chec[
                                pi�ce].x - xx)  # 5
                            or (pi�ces['broi'].y == pi�ces_�chec[pi�ce].y + 2 * yy and pi�ces['broi'].x == pi�ces_�chec[
                                pi�ce].x + xx)  # 6
                            or (pi�ces['broi'].y == pi�ces_�chec[pi�ce].y + yy and pi�ces['broi'].x == pi�ces_�chec[
                                pi�ce].x + 2 * xx)  # 7
                            or (pi�ces['broi'].y == pi�ces_�chec[pi�ce].y + yy and pi�ces['broi'].x == pi�ces_�chec[
                                pi�ce].x - 2 * xx)  # 8
                    ):
                        return False

                if (
                        pi�ce == "nfou1" or pi�ce == "nfou2"):  # pour le fou, on sait pas si le roi est sur une des diagonales, donc on va essayer
                    # dans toutes les directions

                    # haut droite

                    # Code obstruction

                    if pi�ces['broi'].y < pi�ces_�chec[pi�ce].y and pi�ces['broi'].x > pi�ces_�chec[
                        pi�ce].x:  # cela revient � monter et aller � droite

                        liste_RecObstruction, liste_Rec = [], []
                        assert pi�ces_�chec[pi�ce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]
                        j, jx = 1, 1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                        jy = -1  # variable d'incr�mentation pourc parcourir tous les rectangles en y dans le cas d'une mont�e.
                        onlyroi, obstru� = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            # liste_Rec.append(Rect(case_de_base.x+jx*xx, case_de_base.y+jy*yy,55,55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pi�ces_�chec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            jy -= 1  # vers le haut
                            jx += 1  # vers la droite
                            j += 1
                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                                if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "broi":
                                    # print(pi�ce, "met  le roi blanc en �chec! via haut droite")
                                    print("\n La liste est", liste_RecObstruction)

                                    return False

                    # haut gauche
                    if pi�ces['broi'].y < pi�ces_�chec[pi�ce].y and pi�ces['broi'].x < pi�ces_�chec[
                        pi�ce].x:  # cela revient � monter et aller � gauche

                        liste_RecObstruction, liste_Rec = [], []
                        assert pi�ces_�chec[pi�ce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]
                        j, jx = 1, -1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la gauche.
                        jy = -1  # variable d'incr�mentation pour parcourir tous les rectangles en y dans le cas d'une mont�e.
                        onlyroi, obstru� = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            # liste_Rec.append(Rect(case_de_base.x+jx*xx, case_de_base.y+jy*yy,55,55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pi�ces_�chec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            jy -= 1  # vers le haut
                            jx -= 1  # vers la gauche
                            j += 1

                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "broi":
                                # print(pi�ce, "met  le roi blanc en �chec! via haut gauche")
                                print("\n La liste est", liste_RecObstruction, "et la liste sans obs est ", liste_Rec)

                                return False

                    # bas droite
                    if pi�ces['broi'].y > pi�ces_�chec[pi�ce].y and pi�ces['broi'].x > pi�ces_�chec[
                        pi�ce].x:  # cela revient � descendre et aller � droite

                        liste_RecObstruction, liste_Rec = [], []
                        assert pi�ces_�chec[pi�ce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]
                        j, jx = 1, +1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                        jy = +1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'une descente.
                        onlyroi, obstru� = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            # liste_Rec.append(Rect(case_de_base.x+jx*xx, case_de_base.y+jy*yy,55,55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pi�ces_�chec,True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            jy += 1  # vers le bas
                            jx += 1  # vers la droite
                            j += 1

                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "broi":
                                # print(pi�ce, "met  le roi blanc en �chec!")

                                return False

                    # bas gauche

                    if pi�ces['broi'].y > pi�ces_�chec[pi�ce].y and pi�ces['broi'].x < pi�ces_�chec[
                        pi�ce].x:  # cela revient � descendre et aller � gauche

                        liste_RecObstruction, liste_Rec = [], []
                        assert pi�ces_�chec[pi�ce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]
                        j, jx = 1, -1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la gauched.
                        jy = +1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'une descente.
                        onlyroi, obstru� = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            # liste_Rec.append(Rect(case_de_base.x+jx*xx, case_de_base.y+jy*yy,55,55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pi�ces_�chec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            jy += 1  # vers le bas
                            jx -= 1  # vers la gauche
                            j += 1
                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "broi":
                                # print(pi�ce, "met  le roi blanc en �chec!")

                                return False

                if (pi�ce == "nreine"):

                    """

                    Cette fois-ci, on va relier 2 codes obstruction! Celui de la tour et celui  du fou, comme ce sont les fonctions
                    inh�rentes de la reine. Comme la reine effectue exactement les m�mes fonctions que le fou et la tour. Alors,
                    on va juste les copier coller...
                    Ses fonctions sont:
                    1. Haut jusqu'� limite sans �chec
                    2. Bas jusqu'� limite sans �chec
                    3. Droite jusqu'�  limite sans �chec
                    4. Gauche jusqu'� limite sans �chec
                    5. Diagonale Haut Droite jusqu'� limite sans �chec
                    6. Diagonale Haut Gauche jusqu'� limite sans �chec
                    7. Diagonale Bas Droite jusqu'� limite sans �chec
                    8. Diagonale Bas Gauche jusqu'� limite sans �chec

                        """
                    # fonction tour (haut,bas, gauche, droite)
                    if pi�ces['broi'].x == pi�ces_�chec[pi�ce].x:  # m�me x

                        if pi�ces_�chec[pi�ce].y < pi�ces[
                            'broi'].y:  # tour en haut, elle va parcourir en bas, donc y monte
                            j = +1  # variable d'incr�mentation pour parcourir tous les rectangles vers le bas
                            obstru� = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pi�ces_�chec[pi�ce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]

                        while j <= 8:  # le maximum de cases parcourable.
                            liste_Rec.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55))

                            if Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55).collidedict(pi�ces_�chec,
                                                                                                 True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)

                            j += 1

                        if liste_RecObstruction != []:

                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                                print(
                                    "Liste_RecObstruction d�tecte une collision, reste plus qu'� voir avec quelle pi�ce. Par ailleurs:",
                                    liste_RecObstruction[0].collidedict(pi�ces_�chec, True))
                                if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "broi":
                                    print("Le roi serait en �chec, non safe")

                                    return False

                        if pi�ces_�chec[pi�ce].y > pi�ces[
                            'broi'].y:  # tour en bas, elle va parcourir en haut, donc y descend

                            j = -1  # variable d'incr�mentation pour parcourir tous les rectangles vers le bas
                            obstru� = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []

                            assert pi�ces_�chec[pi�ce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]

                        while -j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55))
                            # print(j, ": ", liste_RecObstruction, "\n")

                            if Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55).collidedict(pi�ces_�chec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            j -= 1
                        if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "broi":
                                # print(pi�ce, "met  le roi blanc en �chec!")

                                return False

                    if pi�ces['broi'].y == pi�ces_�chec[pi�ce].y:  # m�me y

                        if pi�ces_�chec[pi�ce].x < pi�ces[
                            'broi'].x:  # tour � gauche, elle va parcourir � droite, donc x augmente.
                            j = +1  # variable d'incr�mentation pour parcourir tous les rectangles vers la droite
                            obstru� = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pi�ces_�chec[pi�ce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]

                        while j <= 8:  # le maximum de cases parcourable.
                            liste_Rec.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55))

                            if Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55).collidedict(pi�ces_�chec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)

                            j += 1

                        print("Liste Rec Obstruction est", liste_RecObstruction)
                        if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "broi":
                                # print(pi�ce, "met  le roi blanc en �chec!")

                                return False

                        if pi�ces_�chec[pi�ce].x > pi�ces[
                            'broi'].x:  # tour � droite, elle va parcourir � gauche, donc x diminue.
                            j = -1  # variable d'incr�mentation pour parcourir tous les rectangles vers la droite
                            obstru� = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pi�ces_�chec[pi�ce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]

                        while -j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55))

                            if Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55).collidedict(pi�ces_�chec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            j -= 1

                        if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "broi":
                                # print(pi�ce, "met  le roi blanc en �chec!")

                                return False

                    # haut droite

                    # Code obstruction

                    if pi�ces['broi'].y < pi�ces_�chec[pi�ce].y and pi�ces['broi'].x > pi�ces_�chec[
                        pi�ce].x:  # cela revient � monter et aller � droite

                        liste_RecObstruction, liste_Rec = [], []
                        assert pi�ces_�chec[pi�ce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]
                        j, jx = 1, 1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                        jy = -1  # variable d'incr�mentation pour parcourir tous les rectangles en y dans le cas d'une mont�e.
                        onlyroi, obstru� = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pi�ces_�chec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            jy -= 1  # vers le haut
                            jx += 1  # vers la droite
                            j += 1
                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                                if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "broi":
                                    # print(pi�ce, "met  le roi blanc en �chec!")

                                    return False

                    # haut gauche
                    if pi�ces['broi'].y < pi�ces_�chec[pi�ce].y and pi�ces['broi'].x < pi�ces_�chec[
                        pi�ce].x:  # cela revient � monter et aller � gauche

                        liste_RecObstruction, liste_Rec = [], []
                        assert pi�ces_�chec[pi�ce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]
                        j, jx = 1, -1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la gauche.
                        jy = -1  # variable d'incr�mentation pour parcourir tous les rectangles en y dans le cas d'une mont�e.
                        onlyroi, obstru� = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pi�ces_�chec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            jy -= 1  # vers le haut
                            jx -= 1  # vers la gauche
                            j += 1
                        if liste_RecObstruction != []:

                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                                if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "broi":
                                    # print(pi�ce, "met  le roi blanc en �chec!")

                                    return False

                    # bas droite
                    if pi�ces['broi'].y > pi�ces_�chec[pi�ce].y and pi�ces['broi'].x > pi�ces_�chec[
                        pi�ce].x:  # cela revient � descendre et aller � droite

                        liste_RecObstruction, liste_Rec = [], []
                        assert pi�ces_�chec[pi�ce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]
                        j, jx = 1, +1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                        jy = +1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'une descente.
                        onlyroi, obstru� = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pi�ces_�chec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            jy += 1  # vers le bas
                            jx += 1  # vers la droite
                            j += 1
                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "broi":
                                # print(pi�ce, "met  le roi blanc en �chec!")

                                return False

                    # bas gauche
                    if pi�ces['broi'].y > pi�ces_�chec[pi�ce].y and pi�ces['broi'].x < pi�ces_�chec[
                        pi�ce].x:  # cela revient � descendre et aller � gauche

                        liste_RecObstruction, liste_Rec = [], []
                        assert pi�ces_�chec[pi�ce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]
                        j, jx = 1, -1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la gauched.
                        jy = +1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'une descente.
                        onlyroi, obstru� = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.

                            liste_Rec.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pi�ces_�chec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            jy += 1  # vers le bas
                            jx -= 1  # vers la gauche
                            j += 1

                        if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "broi":
                                # print(pi�ce, "met  le roi blanc en �chec!")

                                return False
            return True


        """ Blancs mettent en �chec les noirs par le move des noirs? """


        #########################################################

        # Blancs mettent en �chec les noirs ?

        def coup_safe_pour_noirs():
            global pi�ces_�chec

            for pi�ce in pi�ces_�chec:

                if (pi�ce == "bpion1" or pi�ce == "bpion2" or pi�ce == "bpion3" or
                        pi�ce == "bpion4" or pi�ce == "bpion5" or pi�ce == "bpion6" or
                        pi�ce == "bpion7" or pi�ce == "bpion8"):

                    # Si le pion blanc est en mesure de manger � droite ou � gauche, o� se trouve le nroi
                    if pi�ces_�chec[pi�ce] == Rect(pi�ces_�chec['nroi'].x - xxa, pi�ces_�chec['nroi'].y + yya, 55, 55) or \
                            pi�ces_�chec[pi�ce] == Rect(pi�ces_�chec['nroi'].x + xxa, pi�ces_�chec['nroi'].y + yya, 55, 55):
                        return False

                if (pi�ce == "btour1" or pi�ce == "btour2"):
                    if pi�ces_�chec['nroi'].x == pi�ces_�chec[pi�ce].x:  # m�me x

                        if pi�ces_�chec[pi�ce].y < pi�ces[
                            'nroi'].y:  # tour en haut, elle va parcourir en bas, donc y monte
                            j = +1  # variable d'incr�mentation pour parcourir tous les rectangles vers le bas
                            obstru� = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []

                            assert pi�ces_�chec[pi�ce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]

                        while j <= 8:  # le maximum de cases parcourable.
                            liste_Rec.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55))

                            if Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55).collidedict(pi�ces_�chec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)

                            j += 1

                        if liste_RecObstruction != []:

                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                                if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "nroi":
                                    # print(pi�ce, "met le roi noir en �chec!")

                                    return False

                        if pi�ces_�chec[pi�ce].y > pi�ces[
                            'nroi'].y:  # tour en bas, elle va parcourir en haut, donc y descend

                            j = -1  # variable d'incr�mentation pour parcourir tous les rectangles vers le bas
                            obstru� = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pi�ces_�chec[pi�ce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]

                        while -j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55))
                            # print(j, ": ", liste_RecObstruction, "\n")

                            if Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55).collidedict(pi�ces_�chec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            j -= 1
                        if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "nroi":
                                # print(pi�ce, "met le roi noir en �chec!")

                                return False

                    if pi�ces_�chec['nroi'].y == pi�ces_�chec[pi�ce].y:  # m�me y

                        if pi�ces_�chec[pi�ce].x < pi�ces[
                            'nroi'].x:  # tour � gauche, elle va parcourir � droite, donc x augmente.
                            j = +1  # variable d'incr�mentation pour parcourir tous les rectangles vers la droite
                            obstru� = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pi�ces_�chec[pi�ce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]

                        while j <= 8:  # le maximum de cases parcourable.
                            liste_Rec.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55))

                            if Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55).collidedict(pi�ces_�chec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)

                            j += 1

                        print("Liste Rec Obstruction est", liste_RecObstruction)
                        if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "nroi":
                                # print(pi�ce, "met le roi noir en �chec!")

                                return False

                        if pi�ces_�chec[pi�ce].x > pi�ces[
                            'nroi'].x:  # tour � droite, elle va parcourir � gauche, donc x diminue.
                            j = -1  # variable d'incr�mentation pour parcourir tous les rectangles vers la droite
                            obstru� = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pi�ces_�chec[pi�ce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]

                        while -j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55))

                            if Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55).collidedict(pi�ces_�chec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            j -= 1

                        if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "nroi":
                                # print(pi�ce, "met le roi noir en �chec!")

                                return False

                if (pi�ce == "bcheval1" or pi�ce == "bcheval2"):

                    if ((pi�ces_�chec['nroi'].y == pi�ces_�chec[pi�ce].y - 2 * yy and pi�ces_�chec['nroi'].x == pi�ces_�chec[
                        pi�ce].x - xx)  # 1
                            or (pi�ces_�chec['nroi'].y == pi�ces_�chec[pi�ce].y - 2 * yy and pi�ces_�chec['nroi'].x == pi�ces_�chec[
                                pi�ce].x + xx)  # 2
                            or (pi�ces_�chec['nroi'].y == pi�ces_�chec[pi�ce].y - yy and pi�ces_�chec['nroi'].x == pi�ces_�chec[
                                pi�ce].x + 2 * xx)  # 3
                            or (pi�ces_�chec['nroi'].y == pi�ces_�chec[pi�ce].y - yy and pi�ces_�chec['nroi'].x == pi�ces_�chec[
                                pi�ce].x - 2 * xx)  # 4
                            or (pi�ces_�chec['nroi'].y == pi�ces_�chec[pi�ce].y + 2 * yy and pi�ces_�chec['nroi'].x == pi�ces_�chec[
                                pi�ce].x - xx)  # 5
                            or (pi�ces_�chec['nroi'].y == pi�ces_�chec[pi�ce].y + 2 * yy and pi�ces_�chec['nroi'].x == pi�ces_�chec[
                                pi�ce].x + xx)  # 6
                            or (pi�ces_�chec['nroi'].y == pi�ces_�chec[pi�ce].y + yy and pi�ces_�chec['nroi'].x == pi�ces_�chec[
                                pi�ce].x + 2 * xx)  # 7
                            or (pi�ces_�chec['nroi'].y == pi�ces_�chec[pi�ce].y + yy and pi�ces_�chec['nroi'].x == pi�ces_�chec[
                                pi�ce].x - 2 * xx)  # 8
                    ):
                        return False

                if (pi�ce == "bfou1" or pi�ce == "bfou2"):  # pour le fou, on sait pas si le roi est sur une des diagonales, donc on va essayer
                    # dans toutes les directions

                    # haut droite

                    # Code obstruction

                    if pi�ces_�chec['nroi'].y < pi�ces_�chec[pi�ce].y and pi�ces_�chec['nroi'].x > pi�ces_�chec[
                        pi�ce].x:  # cela revient � monter et aller � droite

                        liste_RecObstruction, liste_Rec = [], []
                        assert pi�ces_�chec[pi�ce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]
                        #haut droite
                        j, jx = 1, 1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                        jy = -1  # variable d'incr�mentation pourc parcourir tous les rectangles en y dans le cas d'une mont�e.
                        onlyroi, obstru� = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            # liste_Rec.append(Rect(case_de_base.x+jx*xx, case_de_base.y+jy*yy,55,55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pi�ces_�chec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            jy -= 1  # vers le haut
                            jx += 1  # vers la droite
                            j += 1
                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                                if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "nroi":
                                    # print(pi�ce, "met le roi noir en �chec! via haut droite")
                                    print("\n La liste est", liste_RecObstruction)

                                    return False

                    # haut gauche
                    if pi�ces_�chec['nroi'].y < pi�ces_�chec[pi�ce].y and pi�ces_�chec['nroi'].x < pi�ces_�chec[
                        pi�ce].x:  # cela revient � monter et aller � gauche

                        case_de_base = pi�ces_�chec[pi�ce].collidedict(cases, True)
                        liste_RecObstruction, liste_Rec = [], []
                        assert pi�ces_�chec[pi�ce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]
                        j, jx = 1, -1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la gauche.
                        jy = -1  # variable d'incr�mentation pour parcourir tous les rectangles en y dans le cas d'une mont�e.
                        onlyroi, obstru� = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            # liste_Rec.append(Rect(case_de_base.x+jx*xx, case_de_base.y+jy*yy,55,55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pi�ces_�chec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            jy -= 1  # vers le haut
                            jx -= 1  # vers la gauche
                            j += 1

                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "nroi":
                                # print(pi�ce, "met le roi noir en �chec! via haut gauche")
                                print("\n La liste est", liste_RecObstruction, "et la liste sans obs est ", liste_Rec)

                                return False

                    # bas droite
                    if pi�ces_�chec['nroi'].y > pi�ces_�chec[pi�ce].y and pi�ces_�chec['nroi'].x > pi�ces_�chec[
                        pi�ce].x:  # cela revient � descendre et aller � droite

                        liste_RecObstruction, liste_Rec = [], []
                        assert pi�ces_�chec[pi�ce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]
                        j, jx = 1, +1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                        jy = +1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'une descente.
                        onlyroi, obstru� = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            # liste_Rec.append(Rect(case_de_base.x+jx*xx, case_de_base.y+jy*yy,55,55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pi�ces_�chec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            jy += 1  # vers le bas
                            jx += 1  # vers la droite
                            j += 1

                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "nroi":
                                # print(pi�ce, "met le roi noir en �chec!")

                                return False

                    # bas gauche

                    if pi�ces_�chec['nroi'].y > pi�ces_�chec[pi�ce].y and pi�ces_�chec['nroi'].x < pi�ces_�chec[
                        pi�ce].x:  # cela revient � descendre et aller � gauche

                        liste_RecObstruction, liste_Rec = [], []
                        assert pi�ces_�chec[pi�ce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]
                        j, jx = 1, -1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la gauched.
                        jy = +1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'une descente.
                        onlyroi, obstru� = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            # liste_Rec.append(Rect(case_de_base.x+jx*xx, case_de_base.y+jy*yy,55,55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pi�ces_�chec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            jy += 1  # vers le bas
                            jx -= 1  # vers la gauche
                            j += 1
                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "nroi":
                                # print(pi�ce, "met le roi noir en �chec!")

                                return False

                if (pi�ce == "breine"):

                    """

                    Cette fois-ci, on va relier 2 codes obstruction! Celui de la tour et celui  du fou, comme ce sont les fonctions
                    inh�rentes de la reine. Comme la reine effectue exactement les m�mes fonctions que le fou et la tour. Alors,
                    on va juste les copier coller...
                    Ses fonctions sont:
                    1. Haut jusqu'� limite sans �chec
                    2. Bas jusqu'� limite sans �chec
                    3. Droite jusqu'�  limite sans �chec
                    4. Gauche jusqu'� limite sans �chec
                    5. Diagonale Haut Droite jusqu'� limite sans �chec
                    6. Diagonale Haut Gauche jusqu'� limite sans �chec
                    7. Diagonale Bas Droite jusqu'� limite sans �chec
                    8. Diagonale Bas Gauche jusqu'� limite sans �chec

                        """
                    # fonction tour (haut,bas, gauche, droite)
                    print(' les x du roi sont',pi�ces_�chec['nroi'].x,'tandis que les x de la reine sont',pi�ces_�chec[pi�ce].x)
                    if pi�ces_�chec['nroi'].x == pi�ces_�chec[pi�ce].x:  # m�me x

                        if pi�ces_�chec[pi�ce].y < pi�ces[
                            'nroi'].y:  # tour en haut, elle va parcourir en bas, donc y monte
                            j = +1  # variable d'incr�mentation pour parcourir tous les rectangles vers le bas
                            obstru� = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pi�ces_�chec[pi�ce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]

                        while j <= 8:  # le maximum de cases parcourable.
                            liste_Rec.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55))

                            if Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55).collidedict(pi�ces_�chec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)

                            j += 1

                        if liste_RecObstruction != []:

                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                                if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "nroi":
                                    # print(pi�ce, "met le roi noir en �chec!")

                                    return False

                        if pi�ces_�chec[pi�ce].y > pi�ces[
                            'nroi'].y:  # tour en bas, elle va parcourir en haut, donc y descend

                            j = -1  # variable d'incr�mentation pour parcourir tous les rectangles vers le bas
                            obstru� = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pi�ces_�chec[pi�ce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]

                        while -j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55))
                            # print(j, ": ", liste_RecObstruction, "\n")

                            if Rect(case_de_base.x, case_de_base.y + j * yy, 55, 55).collidedict(pi�ces_�chec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x, case_de_base.y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            j -= 1
                        if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "nroi":
                                # print(pi�ce, "met le roi noir en �chec!")

                                return False

                    if pi�ces_�chec['nroi'].y == pi�ces_�chec[pi�ce].y:  # m�me y

                        if pi�ces_�chec[pi�ce].x < pi�ces[
                            'nroi'].x:  # tour � gauche, elle va parcourir � droite, donc x augmente.
                            j = +1  # variable d'incr�mentation pour parcourir tous les rectangles vers la droite
                            obstru� = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pi�ces_�chec[pi�ce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]

                        while j <= 8:  # le maximum de cases parcourable.
                            liste_Rec.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55))

                            if Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55).collidedict(pi�ces_�chec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)

                            j += 1

                        print("Liste Rec Obstruction est", liste_RecObstruction)
                        if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "nroi":
                                # print(pi�ce, "met le roi noir en �chec!")

                                return False

                        if pi�ces_�chec[pi�ce].x > pi�ces[
                            'nroi'].x:  # tour � droite, elle va parcourir � gauche, donc x diminue.
                            j = -1  # variable d'incr�mentation pour parcourir tous les rectangles vers la droite
                            obstru� = False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...
                            liste_RecObstruction, liste_Rec = [], []
                            assert pi�ces_�chec[pi�ce].collidelist(list(cases.values())) != []
                            case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]

                        while -j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55))

                            if Rect(case_de_base.x + j * xx, case_de_base.y, 55, 55).collidedict(pi�ces_�chec, True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + j * xx, case_de_base.y, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            j -= 1

                        if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "nroi":
                                # print(pi�ce, "met le roi noir en �chec!")

                                return False

                    # haut droite

                    # Code obstruction

                    if pi�ces_�chec['nroi'].y < pi�ces_�chec[pi�ce].y and pi�ces_�chec['nroi'].x > pi�ces_�chec[pi�ce].x:
                        # cela revient � monter et aller � droite

                        liste_RecObstruction, liste_Rec = [], []
                        assert pi�ces_�chec[pi�ce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]
                        j, jx = 1, 1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                        jy = -1  # variable d'incr�mentation pour parcourir tous les rectangles en y dans le cas d'une mont�e.
                        onlyroi, obstru� = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pi�ces_�chec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            jy -= 1  # vers le haut
                            jx += 1  # vers la droite
                            j += 1
                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                                if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "nroi":
                                    # print(pi�ce, "met le roi noir en �chec!")

                                    return False

                    # haut gauche
                    if pi�ces_�chec['nroi'].y < pi�ces_�chec[pi�ce].y and pi�ces_�chec['nroi'].x < pi�ces_�chec[pi�ce].x:  # cela revient � monter et aller � gauche
                        liste_RecObstruction, liste_Rec = [], []
                        #ici on essaye de trouver la case correspondant � notre reine :D
                        assert pi�ces_�chec[pi�ce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]
                        j, jx = 1, -1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la gauche.
                        jy = -1  # variable d'incr�mentation pour parcourir tous les rectangles en y dans le cas d'une mont�e.
                        onlyroi, obstru� = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pi�ces_�chec,True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,55))
                                # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            print('Contenu � l\'it�ration', j,' :',liste_RecObstruction,pi�ces_�chec==pi�ces)
                            jy -= 1  # vers le haut
                            jx -= 1  # vers la gauche
                            j += 1
                        if liste_RecObstruction != []:

                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                                if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "nroi":
                                    # print(pi�ce, "met le roi noir en �chec!")

                                    return False

                    # bas droite
                    if pi�ces_�chec['nroi'].y > pi�ces_�chec[pi�ce].y and pi�ces_�chec['nroi'].x > pi�ces_�chec[
                        pi�ce].x:  # cela revient � descendre et aller � droite

                        liste_RecObstruction, liste_Rec = [], []
                        assert pi�ces_�chec[pi�ce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]
                        j, jx = 1, +1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                        jy = +1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'une descente.
                        onlyroi, obstru� = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.
                            liste_Rec.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pi�ces_�chec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            jy += 1  # vers le bas
                            jx += 1  # vers la droite
                            j += 1
                        if liste_RecObstruction != []:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "nroi":
                                # print(pi�ce, "met le roi noir en �chec!")

                                return False

                    # bas gauche
                    if pi�ces_�chec['nroi'].y > pi�ces_�chec[pi�ce].y and pi�ces_�chec['nroi'].x < pi�ces_�chec[
                        pi�ce].x:  # cela revient � descendre et aller � gauche

                        liste_RecObstruction, liste_Rec = [], []
                        assert pi�ces_�chec[pi�ce].collidelist(list(cases.values()))!= []
                        case_de_base = list(cases.values())[pi�ces_�chec[pi�ce].collidelist(list(cases.values()))]
                        j, jx = 1, -1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la gauched.
                        jy = +1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'une descente.
                        onlyroi, obstru� = [], False

                        while j <= 8:  # le maximum qu'on peut parcourir sur une diagonale est de 8.

                            liste_Rec.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55))

                            if Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55, 55).collidedict(pi�ces_�chec,
                                                                                                            True) != None:
                                liste_RecObstruction.append(Rect(case_de_base.x + jx * xx, case_de_base.y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                            jy += 1  # vers le bas
                            jx -= 1  # vers la gauche
                            j += 1

                        if liste_RecObstruction[0].collidedict(pi�ces_�chec, True) != None:
                            if liste_RecObstruction[0].collidedict(pi�ces_�chec, True)[0] == "nroi":
                                # print(pi�ce, "met le roi noir en �chec!")

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
                                if cases[case].collidedict(pi�ces, True) != None:
                                    # est-ce qu'il y a pi�ce dans case cliqu�e?

                                    pi�cecase1 = cases[case].collidedict(pi�ces,
                                                                         True)  # pi�cecase1 poss�de 2 coordonn�es, la premi�re est le nom de la pi�ce et la seconde est
                                    # une coordonn�e en Rect(1,2,3,4) de la case correspondante.

                                    print("pi�ce de la  premi�re case est",pi�cecase1[0])

                                    action = True
                                    d�japass� = True

            if action == True and d�japass� == False:

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        for case in cases:

                            if Rect.collidepoint(cases[case], pos):
                                # clic gauche dans quelle case

                                case2interm�diaire = case
                                case2 = case2interm�diaire

                                if cases[case2].collidedict(pi�ces, True) != None:
                                    # est-ce qu'il y a pi�ce dans case cliqu�e?

                                    pi�cecase2 = cases[case].collidedict(pi�ces,
                                                                         True)  # pi�cecase2[0]='nomdelapi�ce', pi�cecase2[1]=Rect(pi�ce)
                                    print(pi�cecase2)
                                    pi�cedanscase2 = True
                                print(pi�cedanscase2 and pi�cecase1[0])

                                # cas pion

                                # attribution de coordonn�s de la case1

                                xcase1 = cases[case1].x
                                ycase1 = cases[case1].y

                                print(�checeursn)
                                pi�ces_�chec=dict(pi�ces)

                                if noir == False:  # les blancs commencent
                                    print("Tours des blancs")


                                    def tour_des_blancs():
                                        global noir,action,d�japass�,pi�ces_�chec

                                        "Ici on met les pouvoirs des pi�ces"
                                        #pouvoir tour
                                        def pouvoir_tour_b():
                                            global noir, action, d�japass�,pi�ces_�chec


                                            # haut:
                                            # Code obstruction

                                            if cases[case2].y < cases[case1].y and cases[case2].x == cases[
                                                case1].x:  # cela revient � monter

                                                liste_RecObstruction, liste_Rec = [], []
                                                j = -1  # variable d'incr�mentation pour parcourir tous les rectangles vers le haut
                                                obstru�, ok� = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...

                                                while cases[case1].y + yy + j * yy != cases[
                                                    case2].y:  # il faudra cr�er un while diff�rent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x, cases[case1].y + j * yy, 55, 55))

                                                    if Rect(cases[case1].x, cases[case1].y + j * yy, 55,
                                                            55).collidedict(pi�ces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x, cases[case1].y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                                                    j -= 1
                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la ligne
                                                    obstru� = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la ligne� parcourue pr�c�dmnt, et 2, la pi�ce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if pi�cecase2[0] != "bpion1" and pi�cecase2[0] != "bpion2" and \
                                                                pi�cecase2[0] != "bpion3" and pi�cecase2[
                                                            0] != "bpion4" and pi�cecase2[0] != "bpion5" and pi�cecase2[
                                                            0] != "bpion6" and pi�cecase2[0] != "bpion7" and pi�cecase2[
                                                            0] != "bpion8" and pi�cecase2[0] != "btour1" and pi�cecase2[
                                                            0] != "btour2" and pi�cecase2[0] != "bcheval1" and \
                                                                pi�cecase2[0] != "bcheval2" and pi�cecase2[
                                                            0] != "bfou1" and pi�cecase2[0] != "bfou2" and pi�cecase2[
                                                            0] != "breine" and pi�cecase2[0] != "broi" and pi�cecase2[
                                                            0] != "nroi":
                                                            ok� = True
                                                # test sans obstruction (�viter la t�l�portation) on veut juste voir si la case cliqu�e est bien dans la liste des rectangles lin�aires
                                                t�l�portation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        t�l�portation = False
                                                if len(liste_RecObstruction) == 0 and t�l�portation == False:  # pas d'obstacles.
                                                    ok� = True

                                                # place au test mtn

                                                if obstru� == False and ok� == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec

                                                    confirmation_move_b()

                                                    # bas

                                            if cases[case2].y > cases[case1].y and cases[case2].x == cases[
                                                case1].x:  # cela revient � descendre

                                                liste_RecObstruction, liste_Rec = [], []
                                                j = 1  # variable d'incr�mentation pour parcourir tous les rectangles du haut vers le bas
                                                obstru�, ok� = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...

                                                while cases[case1].y - yy + j * yy != cases[
                                                    case2].y:  # il faudra cr�er un while diff�rent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x, cases[case1].y + j * yy, 55, 55))

                                                    if Rect(cases[case1].x, cases[case1].y + j * yy, 55,
                                                            55).collidedict(pi�ces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x, cases[case1].y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                                                    j += 1
                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la ligne
                                                    obstru� = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la ligne� parcourue pr�c�dmnt, et 2, la pi�ce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if pi�cecase2[0] != "bpion1" and pi�cecase2[0] != "bpion2" and \
                                                                pi�cecase2[0] != "bpion3" and pi�cecase2[
                                                            0] != "bpion4" and pi�cecase2[0] != "bpion5" and pi�cecase2[
                                                            0] != "bpion6" and pi�cecase2[0] != "bpion7" and pi�cecase2[
                                                            0] != "bpion8" and pi�cecase2[0] != "btour1" and pi�cecase2[
                                                            0] != "btour2" and pi�cecase2[0] != "bcheval1" and \
                                                                pi�cecase2[0] != "bcheval2" and pi�cecase2[
                                                            0] != "bfou1" and pi�cecase2[0] != "bfou2" and pi�cecase2[
                                                            0] != "breine" and pi�cecase2[0] != "broi" and pi�cecase2[
                                                            0] != "nroi":
                                                            ok� = True
                                                # test sans obstruction (�viter la t�l�portation) on veut juste voir si la case cliqu�e est bien dans la liste des rectangles lin�aires
                                                t�l�portation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        t�l�portation = False
                                                if len(liste_RecObstruction) == 0 and t�l�portation == False:  # pas d'obstacles.
                                                    ok� = True

                                                # place au test mtn

                                                if obstru� == False and ok� == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_b()
                                                    # droite

                                            if cases[case2].y == cases[case1].y and cases[case2].x > cases[
                                                case1].x:  # cela revient � aller � droite

                                                liste_RecObstruction, liste_Rec = [], []
                                                j = 1  # variable d'incr�mentation pour parcourir tous les rectangles du haut vers le bas
                                                obstru�, ok� = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...

                                                while cases[case1].x - xx + j * xx != cases[
                                                    case2].x:  # il faudra cr�er un while diff�rent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + j * xx, cases[case1].y, 55, 55))

                                                    if Rect(cases[case1].x + j * xx, cases[case1].y, 55,
                                                            55).collidedict(pi�ces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + j * xx, cases[case1].y, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                                                    j += 1
                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la ligne
                                                    obstru� = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la ligne� parcourue pr�c�dmnt, et 2, la pi�ce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if pi�cecase2[0] != "bpion1" and pi�cecase2[0] != "bpion2" and \
                                                                pi�cecase2[0] != "bpion3" and pi�cecase2[
                                                            0] != "bpion4" and pi�cecase2[0] != "bpion5" and pi�cecase2[
                                                            0] != "bpion6" and pi�cecase2[0] != "bpion7" and pi�cecase2[
                                                            0] != "bpion8" and pi�cecase2[0] != "btour1" and pi�cecase2[
                                                            0] != "btour2" and pi�cecase2[0] != "bcheval1" and \
                                                                pi�cecase2[0] != "bcheval2" and pi�cecase2[
                                                            0] != "bfou1" and pi�cecase2[0] != "bfou2" and pi�cecase2[
                                                            0] != "breine" and pi�cecase2[0] != "broi" and pi�cecase2[
                                                            0] != "nroi":
                                                            ok� = True
                                                # test sans obstruction (�viter la t�l�portation) on veut juste voir si la case cliqu�e est bien dans la liste des rectangles lin�aires
                                                t�l�portation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        t�l�portation = False
                                                if len(liste_RecObstruction) == 0 and t�l�portation == False:  # pas d'obstacles.
                                                    ok� = True

                                                # place au test mtn

                                                if obstru� == False and ok� == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec

                                                    confirmation_move_b()

                                                    # gauche

                                            if cases[case2].y == cases[case1].y and cases[case2].x < cases[
                                                case1].x:  # cela revient � aller � gauche

                                                liste_RecObstruction, liste_Rec = [], []
                                                j = -1  # variable d'incr�mentation pour parcourir tous les rectangles du haut vers le bas
                                                obstru�, ok� = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...

                                                while cases[case1].x + xx + j * xx != cases[
                                                    case2].x:  # il faudra cr�er un while diff�rent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + j * xx, cases[case1].y, 55, 55))

                                                    if Rect(cases[case1].x + j * xx, cases[case1].y, 55,
                                                            55).collidedict(pi�ces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + j * xx, cases[case1].y, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                                                    j -= 1
                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la ligne
                                                    obstru� = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la ligne� parcourue pr�c�dmnt, et 2, la pi�ce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if pi�cecase2[0] != "bpion1" and pi�cecase2[0] != "bpion2" and \
                                                                pi�cecase2[0] != "bpion3" and pi�cecase2[
                                                            0] != "bpion4" and pi�cecase2[0] != "bpion5" and pi�cecase2[
                                                            0] != "bpion6" and pi�cecase2[0] != "bpion7" and pi�cecase2[
                                                            0] != "bpion8" and pi�cecase2[0] != "btour1" and pi�cecase2[
                                                            0] != "btour2" and pi�cecase2[0] != "bcheval1" and \
                                                                pi�cecase2[0] != "bcheval2" and pi�cecase2[
                                                            0] != "bfou1" and pi�cecase2[0] != "bfou2" and pi�cecase2[
                                                            0] != "breine" and pi�cecase2[0] != "broi" and pi�cecase2[
                                                            0] != "nroi":
                                                            ok� = True
                                                # test sans obstruction (�viter la t�l�portation) on veut juste voir si la case cliqu�e est bien dans la liste des rectangles lin�aires
                                                t�l�portation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        t�l�portation = False
                                                if len(liste_RecObstruction) == 0 and t�l�portation == False:  # pas d'obstacles.
                                                    ok� = True

                                                # place au test mtn

                                                if obstru� == False and ok� == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec

                                                    confirmation_move_b()

                                        #pouvoir fou
                                        def pouvoir_fou_b():
                                            global noir, action, d�japass�,pi�ces_�chec

                                            # 1.haut droite

                                            # Code obstruction

                                            if cases[case2].y < cases[case1].y and cases[case2].x > cases[
                                                case1].x:  # cela revient � monter et aller � droite

                                                liste_RecObstruction, liste_Rec = [], []
                                                jx = 1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                                                jy = -1  # variable d'incr�mentation pour parcourir tous les rectangles en y dans le cas d'une mont�e.
                                                obstru�, ok� = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...

                                                while cases[case1].y + yy + jy * yy != cases[
                                                    case2].y:  # il faudra cr�er un while diff�rent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                             55))

                                                    if Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                            55).collidedict(pi�ces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                                                    jy -= 1  # vers le haut
                                                    jx += 1  # vers la droite

                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la diagonale
                                                    obstru� = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la diagonale, et 2, la pi�ce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if pi�cecase2[0] != "bpion1" and pi�cecase2[0] != "bpion2" and \
                                                                pi�cecase2[0] != "bpion3" and pi�cecase2[
                                                            0] != "bpion4" and pi�cecase2[0] != "bpion5" and pi�cecase2[
                                                            0] != "bpion6" and pi�cecase2[0] != "bpion7" and pi�cecase2[
                                                            0] != "bpion8" and pi�cecase2[0] != "btour1" and pi�cecase2[
                                                            0] != "btour2" and pi�cecase2[0] != "bcheval1" and \
                                                                pi�cecase2[0] != "bcheval2" and pi�cecase2[
                                                            0] != "bfou1" and pi�cecase2[0] != "bfou2" and pi�cecase2[
                                                            0] != "breine" and pi�cecase2[0] != "broi" and pi�cecase2[
                                                            0] != "nroi":
                                                            ok� = True
                                                # test sans obstruction (�viter la t�l�portation) on veut juste voir si la case cliqu�e est bien dans la liste des rectangles diagonaux
                                                t�l�portation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        t�l�portation = False
                                                if len(liste_RecObstruction) == 0 and t�l�portation == False:
                                                    ok� = True

                                                # place au test mtn
                                                print("ok� est", ok�)

                                                if obstru� == False and ok� == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_b()
                                                    # 2.haut gauche

                                            # Code obstruction

                                            if cases[case2].y < cases[case1].y and cases[case2].x < cases[
                                                case1].x:  # cela revient � monter et aller � gauche

                                                liste_RecObstruction, liste_Rec = [], []
                                                jx = -1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                                                jy = -1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'une mont�e.
                                                obstru�, ok� = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...

                                                while cases[case1].y + yy + jy * yy != cases[
                                                    case2].y:  # il faudra cr�er un while diff�rent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                             55))
                                                    if Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                            55).collidedict(pi�ces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                                                    jy -= 1  # vers le haut
                                                    jx -= 1  # vers la gauche

                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la diagonale
                                                    obstru� = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la diagonale, et 2, la pi�ce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if pi�cecase2[0] != "bpion1" and pi�cecase2[0] != "bpion2" and \
                                                                pi�cecase2[0] != "bpion3" and pi�cecase2[
                                                            0] != "bpion4" and pi�cecase2[0] != "bpion5" and pi�cecase2[
                                                            0] != "bpion6" and pi�cecase2[0] != "bpion7" and pi�cecase2[
                                                            0] != "bpion8" and pi�cecase2[0] != "btour1" and pi�cecase2[
                                                            0] != "btour2" and pi�cecase2[0] != "bcheval1" and \
                                                                pi�cecase2[0] != "bcheval2" and pi�cecase2[
                                                            0] != "bfou1" and pi�cecase2[0] != "bfou2" and pi�cecase2[
                                                            0] != "breine" and pi�cecase2[0] != "broi" and pi�cecase2[
                                                            0] != "nroi":
                                                            ok� = True
                                                # test sans obstruction (�viter la t�l�portation) on veut juste voir si la case cliqu�e est bien dans la liste des rectangles diagonaux
                                                t�l�portation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        t�l�portation = False
                                                if len(liste_RecObstruction) == 0 and t�l�portation == False:
                                                    ok� = True

                                                # place au test mtn

                                                if obstru� == False and ok� == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_b()
                                                    # 3.bas droite

                                            # Code obstruction

                                            if cases[case2].y > cases[case1].y and cases[case2].x > cases[
                                                case1].x:  # cela revient � descendre et aller � droite

                                                liste_RecObstruction, liste_Rec = [], []
                                                jx = 1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                                                jy = 1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'une mont�e.
                                                obstru�, ok� = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...

                                                while cases[case1].y - yy + jy * yy != cases[
                                                    case2].y:  # il faudra cr�er un while diff�rent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                             55))
                                                    if Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                            55).collidedict(pi�ces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                                                    jy += 1  # vers le bas
                                                    jx += 1  # vers la droite

                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la diagonale
                                                    obstru� = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la diagonale, et 2, la pi�ce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if pi�cecase2[0] != "bpion1" and pi�cecase2[0] != "bpion2" and \
                                                                pi�cecase2[0] != "bpion3" and pi�cecase2[
                                                            0] != "bpion4" and pi�cecase2[0] != "bpion5" and pi�cecase2[
                                                            0] != "bpion6" and pi�cecase2[0] != "bpion7" and pi�cecase2[
                                                            0] != "bpion8" and pi�cecase2[0] != "btour1" and pi�cecase2[
                                                            0] != "btour2" and pi�cecase2[0] != "bcheval1" and \
                                                                pi�cecase2[0] != "bcheval2" and pi�cecase2[
                                                            0] != "bfou1" and pi�cecase2[0] != "bfou2" and pi�cecase2[
                                                            0] != "breine" and pi�cecase2[0] != "broi" and pi�cecase2[
                                                            0] != "nroi":
                                                            ok� = True
                                                # test sans obstruction (�viter la t�l�portation) on veut juste voir si la case cliqu�e est bien dans la liste des rectangles diagonaux
                                                t�l�portation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        t�l�portation = False
                                                if len(liste_RecObstruction) == 0 and t�l�portation == False:
                                                    ok� = True

                                                # place au test mtn

                                                if obstru� == False and ok� == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_b()
                                                    # 4.bas gauche

                                            # Code obstruction

                                            if cases[case2].y > cases[case1].y and cases[case2].x < cases[
                                                case1].x:  # cela revient � descendre et aller � gauche

                                                liste_RecObstruction, liste_Rec = [], []
                                                jx = -1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                                                jy = +1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'une mont�e.
                                                obstru�, ok� = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...

                                                while cases[case1].y - yy + jy * yy < cases[
                                                    case2].y:  # il faudra cr�er un while diff�rent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                             55))

                                                    if Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                            55).collidedict(pi�ces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                                                    jy += 1  # vers le bas
                                                    jx -= 1  # vers la gauche

                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la diagonale
                                                    obstru� = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la diagonale, et 2, la pi�ce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if pi�cecase2[0] != "bpion1" and pi�cecase2[0] != "bpion2" and \
                                                                pi�cecase2[0] != "bpion3" and pi�cecase2[
                                                            0] != "bpion4" and pi�cecase2[0] != "bpion5" and pi�cecase2[
                                                            0] != "bpion6" and pi�cecase2[0] != "bpion7" and pi�cecase2[
                                                            0] != "bpion8" and pi�cecase2[0] != "btour1" and pi�cecase2[
                                                            0] != "btour2" and pi�cecase2[0] != "bcheval1" and \
                                                                pi�cecase2[0] != "bcheval2" and pi�cecase2[
                                                            0] != "bfou1" and pi�cecase2[0] != "bfou2" and pi�cecase2[
                                                            0] != "breine" and pi�cecase2[0] != "broi" and pi�cecase2[
                                                            0] != "nroi":
                                                            ok� = True
                                                # test sans obstruction (�viter la t�l�portation) on veut juste voir si la case cliqu�e est bien dans la liste des rectangles diagonaux
                                                t�l�portation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        t�l�portation = False
                                                if len(liste_RecObstruction) == 0 and t�l�portation == False:
                                                    ok� = True

                                                # place au test mtn

                                                if obstru� == False and ok� == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_b()

                                        def confirmation_move_b():
                                            global noir, action, d�japass�,pi�ces_�chec

                                            pi�ces_�chec = dict(pi�ces)
                                            safe = True
                                            if pi�cedanscase2 == True:
                                                pi�ces_�chec[pi�cecase2[0]] = Rect(-100, -100, 55, 55)
                                            pi�ces_�chec[pi�cecase1[0]] = cases[
                                                case2]  # remplacer �a par pi�ces[pi�cecase1[0]]=cases[case2] on a alors la m�me case, on �vite les probl�mes de d�calages dus � l'impr�cision.
                                            assert pi�ces_�chec != pi�ces
                                            if not coup_safe_pour_blancs():
                                                coordonn�es[pi�cecase1[0]] = cases[case1]
                                                action, d�japass�, pi�ces_�chec = False, True, dict(pi�ces)
                                                safe = False

                                            if coup_safe_pour_blancs() and safe:
                                                pi�ces[pi�cecase1[0]] = cases[
                                                    case2]  # remplacer �a par pi�ces[pi�cecase1[0]]=cases[case2] on a alors la m�me case, on �vite les probl�mes de d�calages dus � l'impr�cision.
                                                coordonn�es[pi�cecase1[0]] = (cases[case2][0], cases[case2][1])

                                                if pi�cedanscase2 == True:
                                                    pi�ces[pi�cecase2[0]] = Rect(-100, -100, 55, 55)
                                                    coordonn�es[pi�cecase2[0]] = (-100, -100)

                                                noir, action, d�japass�, pi�ces_�chec = True, False, True, dict(
                                                    pi�ces)  # remplacer le break par un breaker de condition, soit, joueur1=False et joueur 2 = True
                                            pi�ces_�chec=dict(pi�ces)

                                        if (pi�cecase1[0] == "bpion1" or pi�cecase1[0] == "bpion2" or pi�cecase1[
                                            0] == "bpion3" or pi�cecase1[0] == "bpion4" or
                                                pi�cecase1[0] == "bpion5" or pi�cecase1[0] == "bpion6" or
                                                pi�cecase1[0] == "bpion7" or pi�cecase1[0] == "bpion8"):
                                            # 1.on avance de 2 si � la ligne de d�part
                                            print("on est bien dans le pion")

                                            # ligne de d�part
                                            if (
                                                    case1 == "a2" or case1 == "b2" or case1 == "c2" or case1 == "d2" or case1 == "e2" or case1 == "f2" or case1 == "g2" or case1 == "h2"):

                                                if cases[case2] == Rect(cases[case1].x, cases[case1].y - 2 * yya, 55,
                                                                        55) and pi�cedanscase2 == False:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec

                                                    """
                                                       Attention, il se trouve que Python te laisse pas modifier dict['a'][0]!!!! Je sais c bizarre. Il te laisse
                                                     juste modifier dict['a'], mais donc tu dois tout recr�er. 
                                                     on ne modifie que la coordonn�e en y. Cela devrait modifier le blitz comme ce dernier d�pend du dict coordonn�es.
                                                     il ne reste plus qu'� modifier  l'aire rectangulaire de la case.

                                                     """

                                                    confirmation_move_b()
                                                    print("juste apr�s le move ud pion qui avance de 2 on a que noir==",
                                                          noir)

                                            # 2. On avance de 1 si pas � la ligne de d�part ou si � la ligne de d�part

                                            if cases[case2] == Rect(cases[case1].x, cases[case1].y - yya, 55,
                                                                    55) and pi�cedanscase2 == False:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                confirmation_move_b()

                                            # 3. une pi�ce bloque l'avanc�e de 1
                                            # pas besoin d'�crire quoi que ce soit, puisque la condition exclue cela par le biais du bool pi�cedanscase2 l.829

                                            # 4 On mange en diagonale � droite ou � gauche.
                                            # � droite
                                            if cases[case2] == Rect(cases[case1].x + xxa, cases[case1].y - yya, 55,
                                                                    55) and pi�cedanscase2 == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec

                                                if pi�cecase2[0] != "bpion1" and pi�cecase2[0] != "bpion2" and \
                                                        pi�cecase2[0] != "bpion3" and pi�cecase2[0] != "bpion4" and \
                                                        pi�cecase2[0] != "bpion5" and pi�cecase2[0] != "bpion6" and \
                                                        pi�cecase2[0] != "bpion7" and pi�cecase2[0] != "bpion8" and \
                                                        pi�cecase2[0] != "btour1" and pi�cecase2[0] != "btour2" and \
                                                        pi�cecase2[0] != "bcheval1" and pi�cecase2[0] != "bcheval2" and \
                                                        pi�cecase2[0] != "bfou1" and pi�cecase2[0] != "bfou2" and \
                                                        pi�cecase2[0] != "breine" and pi�cecase2[0] != "broi" and \
                                                        pi�cecase2[
                                                            0] != "nroi":  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec

                                                    confirmation_move_b()

                                            # � gauche
                                            if cases[case2] == Rect(cases[case1].x - xxa, cases[case1].y - yya, 55,
                                                                    55) and pi�cedanscase2 == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec

                                                if pi�cecase2[0] != "bpion1" and pi�cecase2[0] != "bpion2" and \
                                                        pi�cecase2[0] != "bpion3" and pi�cecase2[0] != "bpion4" and \
                                                        pi�cecase2[0] != "bpion5" and pi�cecase2[0] != "bpion6" and \
                                                        pi�cecase2[0] != "bpion7" and pi�cecase2[0] != "bpion8" and \
                                                        pi�cecase2[0] != "btour1" and pi�cecase2[0] != "btour2" and \
                                                        pi�cecase2[0] != "bcheval1" and pi�cecase2[0] != "bcheval2" and \
                                                        pi�cecase2[0] != "bfou1" and pi�cecase2[0] != "bfou2" and \
                                                        pi�cecase2[0] != "breine" and pi�cecase2[0] != "broi" and \
                                                        pi�cecase2[
                                                            0] != "nroi":  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_b()




                                            # 5. Avancer le pion rend instantan�ment le joueur en �chec.
                                            # inclus dans les conditions en haut, comme la r�alisation de chacune d�pend du fait qu'il soit en �chec ou pas

                                            # 6. l'utilisateur clique autre part, et il se passe rien.
                                            else:
                                                # print("on est dans else")
                                                action, d�japass�, pi�ces_�chec = False, True, dict(pi�ces)
                                                # Cela marche comme nous sommes dans la boucle du  second clic, en faisant action,d�japass�,pi�ces_�chec=False,True,dict(pi�ces), on sort du second clic et on recommence.

                                            # on sort du if de bpion, on d�marre le if des autres pi�ces...

                                        if (pi�cecase1[0] == "btour1" or pi�cecase1[0] == "btour2"):

                                            pouvoir_tour_b()
                                            if False:
                                                pass
                                            else:
                                                action, d�japass�, pi�ces_�chec = False, True, dict(pi�ces)

                                        if (pi�cecase1[0] == "bcheval1" or pi�cecase1[0] == "bcheval2"):

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
                                                if pi�cedanscase2==True:
                                                    if pi�cecase2[0]!="bpion1" and pi�cecase2[0]!="bpion2" and pi�cecase2[0]!="bpion3" and pi�cecase2[0]!= "bpion4" and pi�cecase2[0]!= "bpion5" and pi�cecase2[0]!= "bpion6" and pi�cecase2[0]!= "bpion7" and pi�cecase2[0]!= "bpion8" and pi�cecase2[0]!= "btour1" and pi�cecase2[0]!= "btour2" and pi�cecase2[0]!= "bcheval1" and pi�cecase2[0]!= "bcheval2" and pi�cecase2[0]!= "bfou1" and pi�cecase2[0]!= "bfou2" and pi�cecase2[0]!= "breine" and pi�cecase2[0]!= "broi" and pi�cecase2[0]!= "nroi": #and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec

                                                        confirmation_move_b()
                                                if pi�cedanscase2==False:
                                                    confirmation_move_b()




                                        if (pi�cecase1[0] == "bfou1" or pi�cecase1[0] == "bfou2"):

                                            pouvoir_fou_b()
                                            if False:
                                                pass
                                            else:
                                                action, d�japass�, pi�ces_�chec = False, True, dict(pi�ces)

                                        if (pi�cecase1[0] == "breine"):

                                            pouvoir_tour_b()
                                            pouvoir_fou_b()

                                            if False:
                                                pass

                                            else:
                                                action, d�japass�, pi�ces_�chec = False, True, dict(pi�ces)

                                        if (pi�cecase1[0] == "broi"):

                                            if pi�cecase2[0] != "bpion1" and pi�cecase2[0] != "bpion2" and pi�cecase2[
                                                0] != "bpion3" and pi�cecase2[0] != "bpion4" and pi�cecase2[
                                                0] != "bpion5" and pi�cecase2[0] != "bpion6" and pi�cecase2[
                                                0] != "bpion7" and pi�cecase2[0] != "bpion8" and pi�cecase2[
                                                0] != "btour1" and pi�cecase2[0] != "btour2" and pi�cecase2[
                                                0] != "bcheval1" and pi�cecase2[0] != "bcheval2" and pi�cecase2[
                                                0] != "bfou1" and pi�cecase2[0] != "bfou2" and pi�cecase2[
                                                0] != "breine" and pi�cecase2[0] != "broi" and pi�cecase2[0] != "nroi":

                                                """

                                                Le roi peut effectuer les m�mes fonctions que la reine, sauf qu'il est limit� � un pas au lieu d'une infinit�.
                                                On peut donc tout copier, mais retirer la seconde moiti� du code obstruer, comme le roi ne peut s'obstruer, sauf
                                                lorsqu'il castle. Ainsi, je vais autoriser les fonctions gauche et droite dans une optique d'impl�ment�e le castle.

                                                Ses fonctions sont:
                                                1. Haut de un sans limite, sans �chec
                                                2. Bas de un  sans limite, sans �chec
                                                3. Droite de un sans limite, sans �chec
                                                4. Gauche de un sans limite sans �chec
                                                5. Diagonale Haut Droite de un sans limite sans �chec
                                                6. Diagonale Haut Gauche de un sans limite sans �chec
                                                7. Diagonale Bas Droite de un sans limite sans �chec
                                                8. Diagonale Bas Gauche de un sans limite sans �chec


                                                """
                                                # haut:

                                                if cases[case2].y == cases[case1].y - yy and cases[case2].x == cases[
                                                    case1].x and pi�cecase2[0] != "bpion1" and pi�cecase2[
                                                    0] != "bpion2" and pi�cecase2[0] != "bpion3" and pi�cecase2[
                                                    0] != "bpion4" and pi�cecase2[0] != "bpion5" and pi�cecase2[
                                                    0] != "bpion6" and pi�cecase2[0] != "bpion7" and pi�cecase2[
                                                    0] != "bpion8" and pi�cecase2[0] != "btour1" and pi�cecase2[
                                                    0] != "btour2" and pi�cecase2[0] != "bcheval1" and pi�cecase2[
                                                    0] != "bcheval2" and pi�cecase2[0] != "bfou1" and pi�cecase2[
                                                    0] != "bfou2" and pi�cecase2[0] != "breine" and pi�cecase2[
                                                    0] != "broi" and pi�cecase2[0] != "nroi":  # cela revient � monter

                                                    confirmation_move_b()

                                                # bas

                                                if cases[case2].y == cases[case1].y + yy and cases[case2].x == cases[
                                                    case1].x and pi�cecase2[0] != "bpion1" and pi�cecase2[
                                                    0] != "bpion2" and pi�cecase2[0] != "bpion3" and pi�cecase2[
                                                    0] != "bpion4" and pi�cecase2[0] != "bpion5" and pi�cecase2[
                                                    0] != "bpion6" and pi�cecase2[0] != "bpion7" and pi�cecase2[
                                                    0] != "bpion8" and pi�cecase2[0] != "btour1" and pi�cecase2[
                                                    0] != "btour2" and pi�cecase2[0] != "bcheval1" and pi�cecase2[
                                                    0] != "bcheval2" and pi�cecase2[0] != "bfou1" and pi�cecase2[
                                                    0] != "bfou2" and pi�cecase2[0] != "breine" and pi�cecase2[
                                                    0] != "broi" and pi�cecase2[
                                                    0] != "nroi":  # cela revient � descendre

                                                    confirmation_move_b()
                                                # droite

                                                if cases[case2].y == cases[case1].y and cases[case2].x == cases[
                                                    case1].x + xx:  # cela revient � aller � droite

                                                    confirmation_move_b()

                                                # gauche

                                                if cases[case2].y == cases[case1].y and cases[case2].x == cases[
                                                    case1].x - xx:  # cela revient � aller � gauche

                                                    confirmation_move_b()

                                                # 1.haut droite

                                                if cases[case2].y == cases[case1].y - yy and cases[case2].x == cases[
                                                    case1].x + xx:  # cela revient � monter et aller � droite

                                                    confirmation_move_b()

                                                # 2.haut gauche

                                                if cases[case2].y == cases[case1].y - yy and cases[case2].x == cases[
                                                    case1].x - xx:  # cela revient � monter et aller � gauche

                                                    confirmation_move_b()

                                                # 3.bas droite

                                                if cases[case2].y == cases[case1].y + yy and cases[case2].x == cases[
                                                    case1].x + xx:  # cela revient � descendre et aller � droite

                                                    confirmation_move_b()

                                                # 4.bas gauche

                                                if cases[case2].y == cases[case1].y + yy and cases[case2].x == cases[
                                                    case1].x - xx:  # cela revient � descendre et aller � gauche

                                                    confirmation_move_b()

                                                else:
                                                    action, d�japass�, pi�ces_�chec = False, True, dict(pi�ces)



                                        else:
                                            action, d�japass�, pi�ces_�chec = False, True, dict(pi�ces)


                                    if coup_safe_pour_blancs() == False:  # blancs en �chec
                                        print("blancs en �chec")

                                    tour_des_blancs()
                                    print("juste apr�s tour des blancs, ona que noir==", noir)

                                print("noir est", noir)
                                if noir == True:  # les noirs commencent
                                    print("Tours des noirs")

                                    def tour_des_noirs():
                                        global noir,action,d�japass�,pi�ces_�chec


                                        "Ici on met les pouvoirs des pi�ces"

                                        #pouvoir tour n
                                        def pouvoir_tour_n():
                                            global noir, action, d�japass�,pi�ces_�chec

                                            pi�ces_�chec = dict(pi�ces)

                                            # haut:
                                            # Code obstruction

                                            if cases[case2].y < cases[case1].y and cases[case2].x == cases[
                                                case1].x:  # cela revient � monter

                                                liste_RecObstruction, liste_Rec = [], []
                                                j = -1  # variable d'incr�mentation pour parcourir tous les rectangles vers le haut
                                                obstru�, ok� = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...

                                                while cases[case1].y + yy + j * yy != cases[
                                                    case2].y:  # il faudra cr�er un while diff�rent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x, cases[case1].y + j * yy, 55, 55))

                                                    if Rect(cases[case1].x, cases[case1].y + j * yy, 55,
                                                            55).collidedict(pi�ces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x, cases[case1].y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                                                    j -= 1
                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la ligne
                                                    obstru� = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la ligne� parcourue pr�c�dmnt, et 2, la pi�ce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                                pi�cecase2[0] != "npion3" and pi�cecase2[
                                                            0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                            0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                            0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                            0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                                pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                            0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                            0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                            0] != "broi":
                                                            ok� = True
                                                # test sans obstruction (�viter la t�l�portation) on veut juste voir si la case cliqu�e est bien dans la liste des rectangles lin�aires
                                                t�l�portation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        t�l�portation = False
                                                if len(liste_RecObstruction) == 0 and t�l�portation == False:  # pas d'obstacles.
                                                    ok� = True

                                                # place au test mtn

                                                if obstru� == False and ok� == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_n()

                                            # bas

                                            if cases[case2].y > cases[case1].y and cases[case2].x == cases[
                                                case1].x:  # cela revient � descendre

                                                liste_RecObstruction, liste_Rec = [], []
                                                j = 1  # variable d'incr�mentation pour parcourir tous les rectangles du haut vers le bas
                                                obstru�, ok� = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...

                                                while cases[case1].y - yy + j * yy != cases[
                                                    case2].y:  # il faudra cr�er un while diff�rent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x, cases[case1].y + j * yy, 55, 55))

                                                    if Rect(cases[case1].x, cases[case1].y + j * yy, 55,
                                                            55).collidedict(pi�ces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x, cases[case1].y + j * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                                                    j += 1
                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la ligne
                                                    obstru� = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la ligne� parcourue pr�c�dmnt, et 2, la pi�ce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                                pi�cecase2[0] != "npion3" and pi�cecase2[
                                                            0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                            0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                            0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                            0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                                pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                            0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                            0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                            0] != "broi":
                                                            ok� = True
                                                # test sans obstruction (�viter la t�l�portation) on veut juste voir si la case cliqu�e est bien dans la liste des rectangles lin�aires
                                                t�l�portation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        t�l�portation = False
                                                if len(liste_RecObstruction) == 0 and t�l�portation == False:  # pas d'obstacles.
                                                    ok� = True

                                                # place au test mtn

                                                if obstru� == False and ok� == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_n()
                                            # droite

                                            if cases[case2].y == cases[case1].y and cases[case2].x > cases[
                                                case1].x:  # cela revient � aller � droite

                                                liste_RecObstruction, liste_Rec = [], []
                                                j = 1  # variable d'incr�mentation pour parcourir tous les rectangles du haut vers le bas
                                                obstru�, ok� = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...

                                                while cases[case1].x - xx + j * xx != cases[
                                                    case2].x:  # il faudra cr�er un while diff�rent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + j * xx, cases[case1].y, 55, 55))

                                                    if Rect(cases[case1].x + j * xx, cases[case1].y, 55,
                                                            55).collidedict(pi�ces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + j * xx, cases[case1].y, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                                                    j += 1
                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la ligne
                                                    obstru� = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la ligne� parcourue pr�c�dmnt, et 2, la pi�ce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                                pi�cecase2[0] != "npion3" and pi�cecase2[
                                                            0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                            0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                            0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                            0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                                pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                            0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                            0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                            0] != "broi":
                                                            ok� = True
                                                # test sans obstruction (�viter la t�l�portation) on veut juste voir si la case cliqu�e est bien dans la liste des rectangles lin�aires
                                                t�l�portation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        t�l�portation = False
                                                if len(liste_RecObstruction) == 0 and t�l�portation == False:  # pas d'obstacles.
                                                    ok� = True

                                                # place au test mtn

                                                if obstru� == False and ok� == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_n()

                                            # gauche

                                            if cases[case2].y == cases[case1].y and cases[case2].x < cases[
                                                case1].x:  # cela revient � aller � gauche

                                                liste_RecObstruction, liste_Rec = [], []
                                                j = -1  # variable d'incr�mentation pour parcourir tous les rectangles du haut vers le bas
                                                obstru�, ok� = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...

                                                while cases[case1].x + xx + j * xx != cases[
                                                    case2].x:  # il faudra cr�er un while diff�rent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + j * xx, cases[case1].y, 55, 55))

                                                    if Rect(cases[case1].x + j * xx, cases[case1].y, 55,
                                                            55).collidedict(pi�ces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + j * xx, cases[case1].y, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                                                    j -= 1
                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la ligne
                                                    obstru� = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la ligne� parcourue pr�c�dmnt, et 2, la pi�ce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                                pi�cecase2[0] != "npion3" and pi�cecase2[
                                                            0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                            0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                            0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                            0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                                pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                            0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                            0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                            0] != "broi":
                                                            ok� = True
                                                # test sans obstruction (�viter la t�l�portation) on veut juste voir si la case cliqu�e est bien dans la liste des rectangles lin�aires
                                                t�l�portation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        t�l�portation = False
                                                if len(liste_RecObstruction) == 0 and t�l�portation == False:  # pas d'obstacles.
                                                    ok� = True

                                                # place au test mtn

                                                if obstru� == False and ok� == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_n()
                                        #pouvoir fou n
                                        def pouvoir_fou_n():
                                            global noir, action, d�japass�, pi�ces_�chec

                                            # 1.haut droite

                                            # Code obstruction

                                            if cases[case2].y < cases[case1].y and cases[case2].x > cases[
                                                case1].x:  # cela revient � monter et aller � droite

                                                liste_RecObstruction, liste_Rec = [], []
                                                jx = 1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                                                jy = -1  # variable d'incr�mentation pour parcourir tous les rectangles en y dans le cas d'une mont�e.
                                                obstru�, ok� = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...

                                                while cases[case1].y + yy + jy * yy != cases[
                                                    case2].y:  # il faudra cr�er un while diff�rent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                             55))

                                                    if Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                            55).collidedict(pi�ces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                                                    jy -= 1  # vers le haut
                                                    jx += 1  # vers la droite

                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la diagonale
                                                    obstru� = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la diagonale, et 2, la pi�ce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                                pi�cecase2[0] != "npion3" and pi�cecase2[
                                                            0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                            0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                            0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                            0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                                pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                            0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                            0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                            0] != "broi":
                                                            ok� = True
                                                # test sans obstruction (�viter la t�l�portation) on veut juste voir si la case cliqu�e est bien dans la liste des rectangles diagonaux
                                                t�l�portation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        t�l�portation = False
                                                if len(liste_RecObstruction) == 0 and t�l�portation == False:
                                                    ok� = True

                                                # place au test mtn
                                                print("ok� est", ok�)

                                                if obstru� == False and ok� == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_n()
                                            # 2.haut gauche

                                            # Code obstruction

                                            if cases[case2].y < cases[case1].y and cases[case2].x < cases[
                                                case1].x:  # cela revient � monter et aller � gauche

                                                liste_RecObstruction, liste_Rec = [], []
                                                jx = -1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                                                jy = -1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'une mont�e.
                                                obstru�, ok� = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...

                                                while cases[case1].y + yy + jy * yy != cases[
                                                    case2].y:  # il faudra cr�er un while diff�rent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                             55))
                                                    if Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                            55).collidedict(pi�ces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                                                    jy -= 1  # vers le haut
                                                    jx -= 1  # vers la gauche

                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la diagonale
                                                    obstru� = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la diagonale, et 2, la pi�ce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                                pi�cecase2[0] != "npion3" and pi�cecase2[
                                                            0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                            0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                            0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                            0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                                pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                            0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                            0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                            0] != "broi":
                                                            ok� = True
                                                # test sans obstruction (�viter la t�l�portation) on veut juste voir si la case cliqu�e est bien dans la liste des rectangles diagonaux
                                                t�l�portation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        t�l�portation = False
                                                if len(liste_RecObstruction) == 0 and t�l�portation == False:
                                                    ok� = True

                                                # place au test mtn

                                                if obstru� == False and ok� == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_n()
                                            # 3.bas droite

                                            # Code obstruction

                                            if cases[case2].y > cases[case1].y and cases[case2].x > cases[
                                                case1].x:  # cela revient � descendre et aller � droite

                                                liste_RecObstruction, liste_Rec = [], []
                                                jx = 1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                                                jy = 1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'une mont�e.
                                                obstru�, ok� = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...

                                                while cases[case1].y - yy + jy * yy != cases[
                                                    case2].y:  # il faudra cr�er un while diff�rent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                             55))
                                                    if Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                            55).collidedict(pi�ces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                                                    jy += 1  # vers le bas
                                                    jx += 1  # vers la droite

                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la diagonale
                                                    obstru� = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la diagonale, et 2, la pi�ce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                                pi�cecase2[0] != "npion3" and pi�cecase2[
                                                            0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                            0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                            0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                            0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                                pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                            0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                            0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                            0] != "broi":
                                                            ok� = True
                                                # test sans obstruction (�viter la t�l�portation) on veut juste voir si la case cliqu�e est bien dans la liste des rectangles diagonaux
                                                t�l�portation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        t�l�portation = False
                                                        print("teleportation check")
                                                if len(liste_RecObstruction) == 0 and t�l�portation == False:
                                                    ok� = True

                                                # place au test mtn

                                                if obstru� == False and ok� == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_n()
                                            # 4.bas gauche

                                            # Code obstruction

                                            if cases[case2].y > cases[case1].y and cases[case2].x < cases[
                                                case1].x:  # cela revient � descendre et aller � gauche

                                                liste_RecObstruction, liste_Rec = [], []
                                                jx = -1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'un mouvement vers la droite.
                                                jy = +1  # variable d'incr�mentation pour parcourir tous les rectangles en x dans le cas d'une mont�e.
                                                obstru�, ok� = False, False  # On part d'une base qu'il n'y a pas d'obstruction.Dans le cas contraire d�montr� par le for ChaqueRec, alors...

                                                while cases[case1].y - yy + jy * yy < cases[
                                                    case2].y:  # il faudra cr�er un while diff�rent pour chaque type de mouvements
                                                    liste_Rec.append(
                                                        Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                             55))

                                                    if Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                            55).collidedict(pi�ces, True) != None:
                                                        liste_RecObstruction.append(
                                                            Rect(cases[case1].x + jx * xx, cases[case1].y + jy * yy, 55,
                                                                 55))  # on ne comptabilise pas la premi�re case (comme elle contient la tour initiale)
                                                    jy += 1  # vers le bas
                                                    jx -= 1  # vers la gauche

                                                if len(liste_RecObstruction) > 1:  # plus d'une obstruction sur la diagonale
                                                    obstru� = True

                                                if len(liste_RecObstruction) == 1:  # on s'assure que 1 on est sur la diagonale, et 2, la pi�ce est mangeable
                                                    if cases[case2] == liste_RecObstruction[0]:
                                                        if pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                                pi�cecase2[0] != "npion3" and pi�cecase2[
                                                            0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                            0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                            0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                            0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                                pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                            0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                            0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                            0] != "broi":
                                                            ok� = True
                                                # test sans obstruction (�viter la t�l�portation) on veut juste voir si la case cliqu�e est bien dans la liste des rectangles diagonaux
                                                t�l�portation = True
                                                for i in liste_Rec:
                                                    if i == cases[case2]:
                                                        t�l�portation = False
                                                if len(liste_RecObstruction) == 0 and t�l�portation == False:
                                                    ok� = True

                                                # place au test mtn

                                                if obstru� == False and ok� == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_n()

                                        def confirmation_move_n():
                                            global noir, action, d�japass�,pi�ces_�chec

                                            pi�ces_�chec = dict(pi�ces)
                                            safe = True

                                            if pi�cedanscase2 == True:
                                                pi�ces_�chec[pi�cecase2[0]] = Rect(-100, -100, 55, 55)
                                            pi�ces_�chec[pi�cecase1[0]] = cases[case2]  # remplacer �a par pi�ces[pi�cecase1[0]]=cases[case2] on a alors la m�me case, on �vite les probl�mes de d�calages dus � l'impr�cision.
                                            assert pi�ces_�chec != pi�ces
                                            print('le dernier coup_safe_pour_noirs est',coup_safe_pour_noirs())
                                            if not coup_safe_pour_noirs():
                                                coordonn�es[pi�cecase1[0]] = cases[case1]
                                                action, d�japass�, pi�ces_�chec = False, True, dict(pi�ces)
                                                safe = False
                                            print('Coup safe pour noirs:',coup_safe_pour_noirs(),'safe',safe)
                                            if coup_safe_pour_noirs() and safe:
                                                pi�ces[pi�cecase1[0]] = cases[
                                                    case2]  # remplacer �a par pi�ces[pi�cecase1[0]]=cases[case2] on a alors la m�me case, on �vite les probl�mes de d�calages dus � l'impr�cision.
                                                coordonn�es[pi�cecase1[0]] = (cases[case2][0], cases[case2][1])

                                                if pi�cedanscase2 == True:
                                                    pi�ces[pi�cecase2[0]] = Rect(-100, -100, 55, 55)
                                                    coordonn�es[pi�cecase2[0]] = (-100, -100)

                                                noir, action, d�japass�, pi�ces_�chec = False, False, True, dict(
                                                    pi�ces)  # remplacer le break par un breaker de condition, soit, joueur1=False et joueur 2 = True
                                            pi�ces_�chec=dict(pi�ces)

                                        if (pi�cecase1[0] == "npion1" or pi�cecase1[0] == "npion2" or
                                                pi�cecase1[0] == "npion3" or
                                                pi�cecase1[0] == "npion4" or pi�cecase1[0] == "npion5" or
                                                pi�cecase1[0] == "npion6" or
                                                pi�cecase1[0] == "npion7" or pi�cecase1[0] == "npion8"):
                                            print("je  d�tecte bien que t,as touch� un pion, en effet, c'est le",pi�cecase1[0])
                                            # 1.on avance de 2 si � la ligne de d�part

                                            # ligne de d�part
                                            if (case1 == "a7" or case1 == "b7" or case1 == "c7" or case1 == "d7" or case1 == "e7" or case1 == "f7" or case1 == "g7" or case1 == "h7"):

                                                if cases[case2] == Rect(cases[case1].x,
                                                                        cases[case1].y + 2 * yya, 55,
                                                                        55) and pi�cedanscase2 == False:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_n()

                                            # 2. On avance de 1 si pas � la ligne de d�part ou si � la ligne de d�part

                                            if cases[case2] == Rect(cases[case1].x, cases[case1].y + yya, 55,
                                                                    55) and pi�cedanscase2 == False:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                confirmation_move_n()
                                                # 3. une pi�ce bloque l'avanc�e de 1
                                                # pas besoin d'�crire quoi que ce soit, puisque la condition exclue cela par le biais du bool pi�cedanscase2 l.829

                                            # 4 On mange en diagonale � droite ou � gauche.
                                            # � droite
                                            if cases[case2] == Rect(cases[case1].x + xxa, cases[case1].y + yya,
                                                                    55,
                                                                    55) and pi�cedanscase2 == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec

                                                if pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                        pi�cecase2[0] != "npion3" and pi�cecase2[
                                                    0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                    0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                    0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                    0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                        pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                    0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                    0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                    0] != "broi":  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_n()

                                                    # � gauche
                                            if cases[case2] == Rect(cases[case1].x - xxa, cases[case1].y + yya,
                                                                    55,
                                                                    55) and pi�cedanscase2 == True:  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec

                                                if pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                        pi�cecase2[0] != "npion3" and pi�cecase2[
                                                    0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                    0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                    0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                    0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                        pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                    0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                    0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                    0] != "broi":  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_n()

                                                    # 5. Avancer le pion rend instantan�ment le joueur en �chec.
                                                    # inclus dans les conditions en haut, comme la r�alisation de chacune d�pend du fait qu'il soit en �chec ou pas

                                            # 6. l'utilisateur clique autre part, et il se passe rien.
                                            else:
                                                # print("on est dans else")
                                                action, d�japass�, pi�ces_�chec = False, True, dict(pi�ces)
                                                # Cela marche comme nous sommes dans la boucle du  second clic, en faisant action,d�japass�,pi�ces_�chec=False,True,dict(pi�ces), on sort du second clic et on recommence.

                                        if (pi�cecase1[0] == "ntour1" or pi�cecase1[0] == "ntour2"):


                                            pouvoir_tour_n()
                                            if False:
                                                pass
                                            else:
                                                action, d�japass�, pi�ces_�chec = False, True, dict(pi�ces)

                                        if (pi�cecase1[0] == "ncheval1" or pi�cecase1[0] == "ncheval2"):

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
                                                if pi�cedanscase2==True:
                                                    if pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                            pi�cecase2[0] != "npion3" and pi�cecase2[0] != "npion4" and \
                                                            pi�cecase2[0] != "npion5" and pi�cecase2[0] != "npion6" and \
                                                            pi�cecase2[0] != "npion7" and pi�cecase2[0] != "npion8" and \
                                                            pi�cecase2[0] != "ntour1" and pi�cecase2[0] != "ntour2" and \
                                                            pi�cecase2[0] != "ncheval1" and pi�cecase2[
                                                        0] != "ncheval2" and pi�cecase2[0] != "nfou1" and pi�cecase2[
                                                        0] != "nfou2" and pi�cecase2[0] != "nreine" and pi�cecase2[
                                                        0] != "nroi" and pi�cecase2[
                                                        0] != "broi":  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec

                                                        confirmation_move_n()
                                                if pi�cedanscase2==False:
                                                    confirmation_move_n()


                                        if (pi�cecase1[0] == "nfou1" or pi�cecase1[0] == "nfou2"):


                                            pouvoir_fou_n()
                                            if False:
                                                pass
                                            else:
                                                action, d�japass�, pi�ces_�chec = False, True, dict(pi�ces)

                                        if (pi�cecase1[0] == "nreine"):
                                            pouvoir_fou_n()
                                            pouvoir_tour_n()
                                            if False:
                                                pass
                                            else:
                                                action, d�japass�, pi�ces_�chec = False, True, dict(pi�ces)

                                        if (pi�cecase1[0] == "nroi"):

                                            # haut:

                                            if cases[case2].y == cases[case1].y - yy and cases[case2].x == \
                                                    cases[case1].x:  # cela revient � monter
                                                if pi�cedanscase2==False or (pi�cedansase2==True and pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                        pi�cecase2[0] != "npion3" and pi�cecase2[
                                                    0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                    0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                    0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                    0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                        pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                    0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                    0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                    0] != "broi"):  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec


                                                    confirmation_move_n()

                                            # bas

                                            if cases[case2].y == cases[case1].y + yy and cases[case2].x == \
                                                    cases[case1].x:  # cela revient � descendre

                                                if pi�cedanscase2==False or (pi�cedanscase2==True and pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                        pi�cecase2[0] != "npion3" and pi�cecase2[
                                                    0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                    0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                    0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                    0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                        pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                    0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                    0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                    0] != "broi"):  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_n()
                                            # droite

                                            if cases[case2].y == cases[case1].y and cases[case2].x == cases[
                                                case1].x + xx:  # cela revient � aller � droite
                                                if pi�cedanscase2==False or (pi�cedanscase2==True and pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                        pi�cecase2[0] != "npion3" and pi�cecase2[
                                                    0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                    0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                    0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                    0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                        pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                    0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                    0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                    0] != "broi"):  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                        confirmation_move_n()
                                            # gauche

                                            if cases[case2].y == cases[case1].y and cases[case2].x == cases[
                                                case1].x - xx:  # cela revient � aller � gauche

                                                if pi�cedanscase2==False or (pi�cedanscase2==True and pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                        pi�cecase2[0] != "npion3" and pi�cecase2[
                                                    0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                    0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                    0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                    0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                        pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                    0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                    0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                    0] != "broi"):  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_n()

                                            # 1.haut droite

                                            if cases[case2].y == cases[case1].y - yy and cases[case2].x == \
                                                    cases[
                                                        case1].x + xx:  # cela revient � monter et aller � droite

                                                if pi�cedanscase2==False or (pi�cedanscase2==True and pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                        pi�cecase2[0] != "npion3" and pi�cecase2[
                                                    0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                    0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                    0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                    0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                        pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                    0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                    0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                    0] != "broi"):  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_n()

                                            # 2.haut gauche

                                            if cases[case2].y == cases[case1].y - yy and cases[case2].x == \
                                                    cases[
                                                        case1].x - xx:  # cela revient � monter et aller � gauche

                                                if pi�cedanscase2==False or (pi�cedanscase2==True and pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                        pi�cecase2[0] != "npion3" and pi�cecase2[
                                                    0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                    0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                    0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                    0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                        pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                    0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                    0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                    0] != "broi"):  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_n()
                                            # 3.bas droite

                                            if cases[case2].y == cases[case1].y + yy and cases[case2].x == \
                                                    cases[
                                                        case1].x + xx:  # cela revient � descendre et aller � droite

                                                if pi�cedanscase2==False or (pi�cedanscase2==True and pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                        pi�cecase2[0] != "npion3" and pi�cecase2[
                                                    0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                    0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                    0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                    0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                        pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                    0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                    0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                    0] != "broi"):  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_n()
                                            # 4.bas gauche

                                            if cases[case2].y == cases[case1].y + yy and cases[case2].x == \
                                                    cases[
                                                        case1].x - xx:  # cela revient � descendre et aller � gauche

                                                if pi�cedanscase2==False or (pi�cedanscase2==True and pi�cecase2[0] != "npion1" and pi�cecase2[0] != "npion2" and \
                                                        pi�cecase2[0] != "npion3" and pi�cecase2[
                                                    0] != "npion4" and pi�cecase2[0] != "npion5" and pi�cecase2[
                                                    0] != "npion6" and pi�cecase2[0] != "npion7" and pi�cecase2[
                                                    0] != "npion8" and pi�cecase2[0] != "ntour1" and pi�cecase2[
                                                    0] != "ntour2" and pi�cecase2[0] != "ncheval1" and \
                                                        pi�cecase2[0] != "ncheval2" and pi�cecase2[
                                                    0] != "nfou1" and pi�cecase2[0] != "nfou2" and pi�cecase2[
                                                    0] != "nreine" and pi�cecase2[0] != "nroi" and pi�cecase2[
                                                    0] != "broi"):  # and pas en �chec sauf si le mouvement permet d'emp�cher l'�chec
                                                    confirmation_move_n()

                                            else:
                                                action, d�japass�, pi�ces_�chec = False, True, dict(pi�ces)



                                        else:
                                            action, d�japass�, pi�ces_�chec = False, True, dict(pi�ces)


                                    if coup_safe_pour_noirs() == False:  # noirs en �chec
                                        print("noirs en �chec")

                                    tour_des_noirs()

    pygame.display.update()

# fermer programme en cliquant sur x

from sys import exit


