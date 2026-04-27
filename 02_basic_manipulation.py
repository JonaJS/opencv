'''
Chapter 2 of opencv bootcamp.
'''
# %% Cell 1
from fileinput import filename

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# %% Cell 2
cb_img = cv2.imread("assets/images/chapter1/checkerboard_18x18.png", 0)
print(cb_img)
plt.imshow(cb_img, cmap="gray")
# %% Cell 3
"""
ACCESSING INDIVIDUAL PIXELS
"""
# Print the first pixel of the first black box.
print(cb_img[0, 0])
# Print the first pixel of the first black box.
print(cb_img[0, 6])
# %% Cell 4
# Modifying image pixels.
cb_img_copy = cb_img.copy()
cb_img_copy[2:4, 2:4] = 200
plt.imshow(cb_img_copy, cmap="grey")
print(cb_img_copy)
# %% Cell 5
# Cropping images.
img_NZ_bgr = cv2.imread(r"assets/images/chapter2/New_Zealand_Boat.jpg", cv2.IMREAD_COLOR)
img_NZ_rgb = img_NZ_bgr[:,:,::-1]
plt.imshow(img_NZ_rgb)
# %% Cell 6
# Crop out the middle region of the image.
img_NZ_rgb_copy = img_NZ_rgb.copy()
cropped_img = img_NZ_rgb_copy[200:400, 300:600]
print(cropped_img.shape)
plt.imshow(cropped_img)

# %% Cell 7
"""

Resizing Images

The function resize resizes the image src down to or up to the specified size. The size and type are derived from the src,dsize,fx, and fy.
Function Syntax

dst = resize( src, dsize[, dst[, fx[, fy[, interpolation]]]] )

dst: output image; it has the size dsize (when it is non-zero) or the size computed from src.size(), fx, and fy; the type of dst is the same as of src.

The function has 2 required arguments:

    src: input image

    dsize: output image size

Optional arguments that are often used include:

    fx: Scale factor along the horizontal axis; when it equals 0, it is computed as (𝚍𝚘𝚞𝚋𝚕𝚎)𝚍𝚜𝚒𝚣𝚎.𝚠𝚒𝚍𝚝𝚑/𝚜𝚛𝚌.𝚌𝚘𝚕𝚜

    fy: Scale factor along the vertical axis; when it equals 0, it is computed as (𝚍𝚘𝚞𝚋𝚕𝚎)𝚍𝚜𝚒𝚣𝚎.𝚑𝚎𝚒𝚐𝚑𝚝/𝚜𝚛𝚌.𝚛𝚘𝚠𝚜

The output image has the size dsize (when it is non-zero) or the size computed from src.size(), fx, and fy; the type of dst is the same as of src.
OpenCV Documentation

resize(): Documentation link



Method 1: Specifying Scaling Factor using fx and fy
"""
resized_cropped_region_2x = cv2.resize(cropped_img, None, fx=2, fy=2)
plt.imshow(resized_cropped_region_2x)

# %% Cell 8
"""
Method 2: Specifying exact size of the output image.
"""
desired_width = 100
desired_height = 200
dim = (desired_width, desired_height)

resize_cropped_region = cv2.resize(cropped_img, dsize=dim, interpolation=cv2.INTER_AREA)
plt.imshow(resize_cropped_region)
# %% Cell 9
# Resize while maintaining aspect ratio.
# Method 2: Using 'dsize'
desired_width = 100
aspect_ratio = desired_width/cropped_img.shape[1]
desired_height = int(aspect_ratio * cropped_img.shape[0])
dim = (desired_width, desired_height)
resize_cropped_region = cv2.resize(cropped_img, dsize=dim, interpolation=cv2.INTER_AREA)
plt.imshow(resize_cropped_region)
# %% Cell 10
"""
Let's actually show the (cropped) resized image.

Swap channel order
"""
resized_cropped_region_2x = resized_cropped_region_2x[:, :, ::-1]
cv2.imwrite("resized_cropped_region_2x.png", resized_cropped_region_2x)

# %% Cell 11
cropped_img = cropped_img[:, :, ::-1]
cv2.imwrite("cropped_img.png", cropped_img)


"""
Flipping Images

The function flip flips the array in one of three different ways (row and column indices are 0-based):
Function Syntax

dst = cv.flip( src, flipCode )

dst: output array of the same size and type as src.

The function has 2 required arguments:

    src: input image
    flipCode: a flag to specify how to flip the array; 0 means flipping around the x-axis and positive value (for example, 1) means flipping around y-axis. Negative value (for example, -1) means flipping around both axes.

OpenCV Documentation

flip: Documentation link
"""
