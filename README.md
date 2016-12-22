This is a collection of OpenCV scripts. Hope you will find them useful to your projects!  

## Template Matching

So we have an image like this

![Alt text](images/img.png)

We'd like to find the monster and the player:

![Alt text](images/monster.png)

![Alt text](images/player.png)

in this image. The script finds the two objects and draws them on the image in rectangles:

![Alt text](screenshots/detection_of_monster_player.png)

See "detect_templates.py".

## Best Template Matching

The monster can move and turn left and turn right. We want to keep track of its position and direction. 
We can use templates of this monster facing front, left and right:

![Alt text](images/monster.png)

![Alt text](images/monster_left.png)

![Alt text](images/monster_right.png)

The script finds the most matching and draws on the image:

![Alt text](screenshots/detection_of_monster_from_best_matching.png)

See "detect_best_matching_template.py" 

## Cropping. 
Say you want to implement a cropping function in an image editor. User draws a rectangle on an image. The script crops it and save the crop in another image. 

See "cropping.py". 
