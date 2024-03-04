import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

# lines = tuple(i_start, j_start, i_end, j_end)
def see_lines(height, width, lines):
    img = np.zeros(((height,width)))

    for line in lines:
        tracerSegment(img, line[0], line[1], line[2], line[3], height)

    plt.imshow(img)
    plt.show()
    
    return img

def see_lines_complete(height, width, lines):
    img = np.zeros(((height,width)))

    for line in lines:
        tracerSegment(img, line[0], line[1], line[2], line[3], height)

    plt.imshow(img)
    plt.show()
    
    return img

# procédure tracerSegment(entier x1, entier y1, entier x2, entier y2) est
#     déclarer entier dx, dy ;
#     déclarer entier e ; // valeur d’erreur
#     e  ← x2 - x1 ;        // -e(0,1)
#     dx ← e × 2 ;          // -e(0,1)
#     dy ← (y2 - y1) × 2 ;  // e(1,0)
#     tant que x1 ≤ x2 faire
#         tracerPixel(x1, y1) ;
#         x1 ← x1 + 1 ;  // colonne du pixel suivant
#         si (e ← e - dy) ≤ 0 alors  // erreur pour le pixel suivant de même rangée
#             y1 ← y1 + 1 ;  // choisir plutôt le pixel suivant dans la rangée supérieure
#             e ← e + dx ;  // ajuste l’erreur commise dans cette nouvelle rangée
#         fin si ;
#     fin faire ;
# fin procédure ;

# boucle sans fin  // déplacements horizontaux
            #   tracePixel(x1, y1) ;
            #   interrompre boucle si (x1 ← x1 + 1) = x2 ;
            #   si (e ← e - dy) < 0 alors
            #     y1 ← y1 + 1 ;  // déplacement diagonal
            #     e ← e + dx ;
            #   fin si ;
            # fin boucle ;

def tracerSegment(img, y1, x1, y2, x2, height):
    y1 = height - y1
    y2 = height - y2

    print(f'({x1},{y1}) to ({x2}, {y2})')

    if(y2 < y1): # put all vectors in first or second quadrant
        xTemp = x2
        yTemp = y2
        x2 = x1
        y2 = y1
        x1 = xTemp
        y1 = yTemp

    if(x2 == x1):
        while(y1 <= y2):
            img[(height - y1), x1] = 1
            y1 += 1
        return
    elif(y2 == y1):
        while(x1 <= x2):
            img[(height - y1), x1] = 1
            x1 += 1
        return

    if((y2 - y1) <= (x2 - x1) and x2 > x1): # 1er octant
        e = x2 - x1
        dx = e * 2
        dy = (y2 - y1) * 2
        print(f'1er octant. ({x1},{y1}) to ({x2}, {y2})')
        while(x1 <= x2):
            img[(height - y1), x1] = 1
            x1 = x1 + 1
            e = e - dy
            if(e <= 0):
                y1 = y1 + 1
                e = e + dx
    elif((y2 - y1) > (x2 - x1) and x2 > x1): # 2eme octant
        e = y2 - y1
        dx = (x2 - x1) * 2
        dy = (y2 - y1) * 2
        print(f'2eme octant. ({x1},{y1}) to ({x2}, {y2})')
        while(y1 <= y2):
            img[(height - y1), x1] = 1
            y1 = y1 + 1
            e = e - dx
            if(e <= 0):
                x1 = x1 + 1
                e = e + dy
    elif((y2 - y1) > (x1 - x2) and x2 < x1): # 3eme octant
        e = y2 - y1
        dx = (x1 - x2) * 2 #?
        dy = (y2 - y1) * 2
        print(f'3eme octant. ({x1},{y1}) to ({x2}, {y2})')
        while(y1 <= y2):
            img[(height - y1), x1] = 1
            y1 = y1 + 1
            e = e - dx #?
            if(e <= 0):
                x1 = x1 - 1
                e = e + dy #?
    elif((y2 - y1) <= (x1 - x2) and x2 < x1): # 4eme octant
        e = x1 - x2
        dx = e * 2 #?
        dy = (y2 - y1) * 2 #?
        print(f'4eme octant. ({x1},{y1}) to ({x2}, {y2})')
        while(x1 >= x2):
            img[(height - y1), x1] = 1
            x1 = x1 - 1
            e = e - dy #?
            if(e <= 0):
                y1 = y1 + 1
                e = e + dx #?

see_lines_complete(100, 100, [(99, 1, 90, 75)])