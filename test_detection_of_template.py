import gym
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import gym
import ppaquette_gym_doom
import cv2

#only read in one color channel 
monster = cv2.imread("monster.png", 0)
player = cv2.imread("player.png", 0)

img = cv2.imread("img.png", 0)
height, width = img.shape

env = gym.make('ppaquette/DoomBasic-v0')

def find_template(template):
    method = 'cv2.TM_CCOEFF'
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, eval(method))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return top_left, bottom_right, res

top_left_monster, bottom_right_monster, res1 = find_template(monster)

img2 = img.copy()
plt.subplot(131),plt.imshow(res1,cmap = 'gray')
plt.title('Matching Result for Monster'), plt.xticks([]), plt.yticks([])
cv2.rectangle(img2, top_left_monster, bottom_right_monster, 255, 2)

top_left_player, bottom_right_player, res2 = find_template(player)
plt.subplot(132),plt.imshow(res2,cmap = 'gray')
plt.title('Matching Result for Player'), plt.xticks([]), plt.yticks([])
cv2.rectangle(img2, top_left_player, bottom_right_player, 255, 2)

plt.subplot(133),plt.imshow(img2,cmap = 'gray')
plt.title('Detected Point for Player and Monster'), plt.xticks([]), plt.yticks([])

plt.show()

env = gym.make('ppaquette/DoomBasic-v0')
action_set = []
observation_set = []
for i_episode in range(1):
    observation = env.reset()
    for t in range(10):
        env.render()
        action = env.action_space.sample()

        action_set.append(action)

        observation, reward, done, info = env.step(action)

        observation_set.append(observation)

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break


