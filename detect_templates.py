import matplotlib.pyplot as plt
import cv2

#only read in one color channel 
image = cv2.imread("images/img.png", 0)
monster = cv2.imread("images/monster.png", 0)
player = cv2.imread("images/player.png", 0)


def find_template(template):
    method = 'cv2.TM_CCOEFF'
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(image, template, eval(method))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return top_left, bottom_right, res

top_left_monster, bottom_right_monster, res1 = find_template(monster)

image_copy = image.copy()
# plt.subplot(131),plt.imshow(res1,cmap = 'gray')
# plt.title('Matching Result for Monster'), plt.xticks([]), plt.yticks([])
cv2.rectangle(image_copy, top_left_monster, bottom_right_monster, 255, 2)

top_left_player, bottom_right_player, res2 = find_template(player)
# plt.subplot(132),plt.imshow(res2,cmap = 'gray')
# plt.title('Matching Result for Player'), plt.xticks([]), plt.yticks([])
cv2.rectangle(image_copy, top_left_player, bottom_right_player, 255, 2)
cv2.imwrite("screenshots/detection_of_monster_player.png", image_copy)

# plt.subplot(133),\
plt.imshow(image_copy, cmap ='gray')
plt.title('Detected Point for Player and Monster'), plt.xticks([]), plt.yticks([])

plt.show()



