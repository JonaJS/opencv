# %% Cell 1
import cv2
import matplotlib.pyplot as plt

# %% Cell 2
cb_img = cv2.imread("assets/images/chapter1/checkerboard_color.png")
coke_img = cv2.imread("assets/images/chapter1/coca-cola-logo.png")

# %% Cell 3
# Use matplotlib imshow()
plt.imshow(cb_img)
plt.title("matplotlib imshow")
plt.show()
# %% Cell 4
# Use OpenCV imshow(), display for 8 seconds
window1 = cv2.namedWindow("w1")
cv2.imshow(window1, cb_img)
cv2.waitKey(8000)
cv2.destroyAllWindows()

# %% Cell 5
# Use OpenCV imshow(), display for 8 seconds
window2 = cv2.namedWindow("w2")
cv2.imshow(window2, coke_img)
cv2.waitKey(8000)
cv2.destroyAllWindows()

# %% Cell 6
# Use OpenCV imshow(), display until a key is pressed.
window3 = cv2.namedWindow("w3")
cv2.imshow(window3, cb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %% Cell 7
window4 = cv2.namedWindow("w4")
alive = True

while alive:
    cv2.imshow(window4, coke_img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        alive = False
    
cv2.destroyAllWindows()
