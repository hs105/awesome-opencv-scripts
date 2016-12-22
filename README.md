This is a collection of OpenCV scripts. Hope you will find them useful to your projects!  

## Cropping by selecting a rectangle area in an opened image. 
See "cropping.py". 




## Template Matching
* "detect_templates.py" shows how to match a template given an image and draws a rectangle area around it. The templates we are using are a player and a monster (from the game of Doom):

So we have an image like this

![Alt text](images/img.png)

We'd like to find the player and monster in this image:

![Alt text](images/player.png)

![Alt text](images/monster.png)

The script finds the two objects and draws them on the image in rectangles:

![Alt text](screenshots/detection_of_monster_player.png)

* "detect_best_matching_template.py" is an extension of "detect_templates.py". It shows how to select the best matching template from a few templates given an image. 
The templates we are using are monster facing front, left and right:

![Alt text](images/monster.png)

![Alt text](images/monster_left.png)

![Alt text](images/monster_right.png)

The script finds the most matching and draws on the image:

![Alt text](screenshots/detection_of_monster_from_best_matching.png)




