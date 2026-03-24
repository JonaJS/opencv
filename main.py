# %% Cell 1
import cv2
import matplotlib.pyplot as plt

# %% Cell 2
cb_img = cv2.imread(f"./assets/images/chapter1/checkerboard_18x18.png", 0)
print(cb_img)
# %% Cell 3
print(f"Image size (H, W) is: {cb_img.shape}")
print(f"Data type of image is: {cb_img.dtype}")

# %% Cell 4
plt.imshow(cb_img)
# %% Cell 5
plt.imshow(cb_img, cmap="gray")
# %% Cell 6
cb_img_fuzzy = cv2.imread(f"./assets/images/chapter1/checkerboard_fuzzy_18x18.jpg",0)
print(cb_img_fuzzy)
plt.imshow(cb_img_fuzzy, cmap="gray")
# %% Cell 7
# Read in image
coke_img = cv2.imread(f"./assets/images/chapter1/coca-cola-logo.png", 1)
# print the size of the image
print(f"Image size (H, W, C): {coke_img.shape}")
# print data-type of the image
print(f"The data type of the image is: {coke_img.dtype}")

# %% Cell 8
plt.imshow(coke_img)
# %% Cell 9
coke_image_channels_reversed = coke_img[:, :, ::-1]
plt.imshow(coke_image_channels_reversed)

# Splitting and merging color channels
# %% Cell 10
# Split the image into the B,G,R components
img_NZ_bgr = cv2.imread(f"./assets/images/chapter1/New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)
b, g, r = cv2.split(img_NZ_bgr)

plt.figure(figsize=[20, 5])
plt.subplot(141);plt.imshow(r, cmap="gray");plt.title("Red Channel")
plt.subplot(142);plt.imshow(g, cmap="gray");plt.title("Green Channel")
plt.subplot(143);plt.imshow(b, cmap="gray");plt.title("Blue Channel")

# Merge the individual channels into a BGR image
imgMerged = cv2.merge((r, g, b))
plt.subplot(144)
plt.imshow(imgMerged) # plt.imshow(imgMerged[:, :, ::-1])
plt.title("Merged Output")
