# %% Cell 1
import cv2
import matplotlib.pyplot as plt

# %% Cell 2
# READING IMAGES USING OPENCV
# Read image as gray scale (0)
cb_img = cv2.imread(f"./assets/images/chapter1/checkerboard_18x18.png", 0)
# Print the image data (pixel values), element of a 2D numpy array.
# Each pixel value is 8-bits [0,255]
print(cb_img)
# %% Cell 3
# DISPLAY IMAGE ATTRIBUTES
# print the size of image
print(f"Image size (H, W) is: {cb_img.shape}")
# print the dtype of image
print(f"Data type of image is: {cb_img.dtype}")

# %% Cell 4
# DISPLAY IMAGES USING MATPLOTLIB
# display image
plt.imshow(cb_img)
# %% Cell 5
# Even though the image was read in as a gray scale, it won't necessarily display
# in gray scale when using imshow(). Matplotlib uses different color maps and
# it's possible that the gray scale color map is not set.

# Set color map to gray scale for proper rendering.
plt.imshow(cb_img, cmap="gray")
# %% Cell 6
# read image as a gray scale
cb_img_fuzzy = cv2.imread(f"./assets/images/chapter1/checkerboard_fuzzy_18x18.jpg",0)
# print the image
print(cb_img_fuzzy)
# display image
plt.imshow(cb_img_fuzzy, cmap="gray")
# %% Cell 7
# WORKING WITH COLOR IMAGES. READ AND DISPLAY COLOR IMAGES.
# read in image
coke_img = cv2.imread(f"./assets/images/chapter1/coca-cola-logo.png", 1)
# print the size of the image
print(f"Image size (H, W, C): {coke_img.shape}")
# print data-type of the image
print(f"The data type of the image is: {coke_img.dtype}")

# %% Cell 8
# what happened?
# the color displayed below is different from the actual image. Matplotlib
# expects the image in RGB format whereas OpenCV stores images in BGR format.
# Thus, for correct display, we need to reverse the channels of the image.
plt.imshow(coke_img)
# %% Cell 9
coke_image_channels_reversed = coke_img[:, :, ::-1]
plt.imshow(coke_image_channels_reversed)

# Splitting and merging color channels
# %% Cell 10
# SPLITTING AND MERGING COLOR CHANNELS.

# split the image into the B,G,R components
img_NZ_bgr = cv2.imread(f"./assets/images/chapter1/New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)
b, g, r = cv2.split(img_NZ_bgr)

# show the channels
plt.figure(figsize=[20, 5])
plt.subplot(141);plt.imshow(r, cmap="gray");plt.title("Red Channel")
plt.subplot(142);plt.imshow(g, cmap="gray");plt.title("Green Channel")
plt.subplot(143);plt.imshow(b, cmap="gray");plt.title("Blue Channel")

# Merge the individual channels into a BGR image
imgMerged = cv2.merge((b, g, r)) # Merged in RGB order
plt.subplot(144)
plt.imshow(imgMerged[:, :, ::-1])
plt.title("Merged Output")
# %% Cell 11
# CONVERTING TO DIFFERENT COLOR SPACES.
# Changing from BGR to RGB.
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB)
plt.imshow(img_NZ_rgb)
# %% Cell 12
# CHANGING TO HSV COLOR SPACE
img_NZ_hsv = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2HSV)
plt.imshow(img_NZ_hsv)
