import operator
import cv2

""" This script shows:
Given an image, how to select the most matching template from a few template images.
"""

img = cv2.imread("images/img.png")
monster_front = cv2.imread("images/monster.png")
monster_left = cv2.imread("images/monster_left.png")
monster_right = cv2.imread("images/monster_right.png")
templates = [monster_front, monster_left, monster_right]


def find_template(template):
    method = 'cv2.TM_CCOEFF'
    w, h = template.shape[::-1][1:] # this reverse the order of the array
    res = cv2.matchTemplate(img, template, eval(method))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print("matching score is %f" % max_val)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return top_left, bottom_right, res, max_val


def find_most_matching():
    list = []
    for tem in templates:
        list.append(find_template(tem))
    return max(list, key=operator.itemgetter(3))


biggest_match = find_most_matching()
print("the biggest ,matching score is %f ", biggest_match[3])

img_copy = img.copy()
cv2.rectangle(img_copy, biggest_match[0], biggest_match[1], 255, 0)
cv2.imwrite("screenshots/detection_of_monster_from_best_matching.png", img_copy)
cv2.imshow("image_copy", img_copy)
cv2.waitKey(0)







