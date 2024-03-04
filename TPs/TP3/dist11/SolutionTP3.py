import numpy as np
import matplotlib.pyplot as plt
import math

DEBUG = False

def see_illusion(height, width, square_size, rectangle_size, gris1, gris2, blanc, noir):
    img = np.zeros(((height,width)))

    original_gris1 = gris1
    original_gris2 = gris2

    current_i = math.floor((height - square_size) / 2)
    current_j = math.floor(width / 2 - square_size)
    tick = True
    line_count = 0

    rectangle_set = set()
    rectangle_color_map = { gris1 : blanc, gris2 : noir }

    print_line(img, current_i, current_j, rectangle_size, square_size, gris1, gris2, True, rectangle_set, True)
    current_j += square_size
    print_line(img, current_i, current_j, rectangle_size,square_size, gris1, gris2, False, rectangle_set, True)
    
    while(True): ## print upper lines
        current_i -= square_size
        if(current_i + square_size < 0):
            break
        current_j -= math.floor(square_size / 2)
        print_line(img, current_i, current_j, rectangle_size, square_size, gris1, gris2, True, rectangle_set, True)

        if(not tick):
            current_j += square_size

        print_line(img, current_i, current_j, rectangle_size, square_size, gris1, gris2, False, rectangle_set, True)
        line_count += 1
        tick = not tick
        if(line_count % 2 == 1):
            gris1, gris2 = gris2, gris1

    current_i = math.floor((height + square_size) / 2) - square_size
    current_j = math.floor(width / 2 - square_size) + square_size
    tick = True
    line_count = 0
    gris1 = original_gris1
    gris2 = original_gris2

    while(True): ## print bottom lines
        current_i += square_size
        if(current_i > img.shape[0]):
            break
        current_j -= math.floor(square_size / 2)
        print_line(img, current_i, current_j, rectangle_size, square_size, gris1, gris2, True, rectangle_set, False)

        if(not tick):
            current_j += square_size

        print_line(img, current_i, current_j, rectangle_size, square_size, gris1, gris2, False, rectangle_set, False)
        line_count += 1
        tick = not tick
        
        if(line_count % 2 == 1):
            gris1, gris2 = gris2, gris1

    print_rectangles_from_set(img, rectangle_set, square_size, rectangle_color_map)

    print_im(img)

    # img = gray_to_rgb(img)

    plt.imsave("teste.png", img, vmin=0, vmax=255, cmap='gray')

    # f = open("demofile2.txt", "a")
    # f.write(str(img))
    # f.write("////")
    # f.close()

    return img

def gray_to_rgb(img):
    ret = np.zeros((img.shape[0], img.shape[1], 3))
    
    ret[:, :, 0] = img[:, :] / 255
    ret[:, :, 1] = img[:, :] / 255
    ret[:, :, 2] = img[:, :] / 255
    
    return ret

def print_rectangles_from_set(img, rectangle_set, square_size, rectangle_color_map):
    for rectangle in rectangle_set:
        (i_start, j_start, i_end, j_end, color) = rectangle
        if(not(i_start < 0 or i_end > img.shape[0] or j_start < 0 or j_end > img.shape[1]) # not out of bounds
           and not(img.shape[1] / 2 - square_size / 2 < j_start < img.shape[1] / 2 + square_size / 2)): # not in the middle column
            img[i_start : i_end, j_start : j_end] = rectangle_color_map[color]

def print_im(img):
    # plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    # plt.show()
    return

def print_line(img, start_i, start_j, rectangle_size, square_size, color1, color2, go_left, rectangle_set, going_up):
    debug(f'start_i: {start_i}\n')
    current_i = start_i
    current_j = start_j
    tick = True
    while(True):
        color_to_paint = color1 if tick else color2
        
        img[max(current_i, 0) : min(current_i + square_size, img.shape[0]),
            max(current_j, 0) : min(current_j + square_size, img.shape[1])] = color_to_paint
        
        rectangle_j_start = 0
        rectangle_j_end = 0

        if((go_left and going_up) or ((not go_left) and (not going_up))): # 2nd or 4th quadrants
            rectangle_j_start = math.floor(current_j + square_size * 3 / 4 - rectangle_size[1] / 2)
            rectangle_j_end = math.floor(current_j + rectangle_size[1] + square_size * 3 / 4 - rectangle_size[1] / 2)
        else:
            rectangle_j_start = math.floor(current_j + square_size / 4 - rectangle_size[1] / 2)
            rectangle_j_end = math.floor(current_j + rectangle_size[1] + square_size / 4 - rectangle_size[1] / 2)

        rectangle_set.add((
            math.floor(current_i - rectangle_size[0] / 2),
            rectangle_j_start,
            math.floor(current_i - rectangle_size[0] / 2 + rectangle_size[0]),
            rectangle_j_end,
            color_to_paint
        ))
        current_j = current_j - square_size if go_left else current_j + square_size
        if(current_j + square_size < 0 or current_j > img.shape[1]):
            debug("Breaking...")
            break
        tick = not tick

def debug(string):
    return

# see_illusion(1500, 2500, 112, (8, 20), 92, 192, 255, 0)
# see_illusion(1345, 2500, 112, (8, 20), 92, 192, 255, 0)
# see_illusion(631, 1345, 30, (2, 4), 92, 192, 255, 0)
see_illusion(1500, 3000, 112, (8, 20), 92, 192, 255, 0)