import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def see_gaussian(seuil):
    img = mpimg.imread("gaussian.png")

    img_channel1 = 255 * img[:, :, 0]

    image_thresholded = (img_channel1 > seuil).astype(int)
    
    pixels_1 = np.count_nonzero(image_thresholded == 1)
    pixels_0 = np.count_nonzero(image_thresholded == 0)
    proportion = pixels_1 / (pixels_0 + pixels_1)

    return (image_thresholded, pixels_1, proportion)

# Image 0-255
def convert_threshold(img, a, b, channel):
    return ((img[:, :, channel] < b) & (img[:, :, channel] > a)).astype(int)

def see_shapes(object_to_detect):
    img = 255 * mpimg.imread("shapes.png")
    match object_to_detect:
        case "star":
            return (convert_threshold(img, 160, 255, 1))
        case "cat":
            return ((img[:, :, 1] == 148) | (img[:, :, 1] == 198)).astype(int)
        case "heart":
            return ((img[:, :, 2] == 148)).astype(int)
        case "oval":
            return (((img[:, :, 0] == 178) |
                     (img[:, :, 0] == 198))).astype(int)
        case "rectangle":
            return (((img[:, :, 2] == 178))).astype(int)

## In one dimension
def get_image_histogram(img):
    return np.histogram(img, bins = 256, range = (0, 255))[0]

def c_I(histogram, i, N):
    return np.sum(histogram[0: i + 1]) / N

def equal(img_name):
    img = (255 * mpimg.imread(img_name)).astype(np.uint8)
    histogram = get_image_histogram(img)
    N = img.shape[0] * img.shape[1]

    normalized = np.array(
        [[max(0, 255 * c_I(histogram, img[i, j], N)  - 1) for j in range(0, img.shape[1])] for i in range(0, img.shape[0])]
    ).astype(np.uint8)

    return normalized


#(star, cat, heart, oval ou rectangle)
# plt.imshow(see_shapes("star"))
# plt.show()

# plt.imshow(see_shapes("rectangle"))
plt.imshow(equal("landscape.png"), cmap='gray', vmin=0, vmax=255)
plt.show()