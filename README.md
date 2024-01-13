# Jumper Game
#### Video Demo:  https://www.youtube.com/watch?v=pTeQceHpiQ0
#### Description: This simple game is created using Python with the Pygame library.

## How to play
Import the entire Python folder into your text editor such as VSCode and install the Pygame library.
Here is a link to check if you have installed the Pygame library successfully: https://www.pygame.org/wiki/GettingStarted

Once done, run the Python program to start the game.

## Objective
The objective of the game is simple. The player has to jump onto various platforms to reach as high as he can without falling off the screen or dying to an obstacle. The score achieved by the player is the highest height (in meters) achieved by the player before dying. Therefore, the player has to aim to jump as high as possible to achieve a high score.

## Controls
There are a few keyboard inputs for the player to control his character:
1. The player can press the left and right arrow keys to move left and right respectively.
2. The player can jump by pressing the spacebar key to jump. The player is only allowed to initiate a jump if he is standing and he is allowed to jump once more in mid-air by pressing the spacebar key again if necessary.
3. If the player dies and encounters the results page, he can click the spacebar key again to restart the game.

## Obstacles
There are 3 types of obstacles(platforms) for the player to navigate through as he jumps upwards: regular platforms, lava platforms and ice platforms.

1. Regular platforms: These are safe platforms for the player to stand on and the platforms are stationary.
2. Ice platform: These are safe platforms for the player but they move from side to side. The player will also move along with an ice platform if he is standing on it.
3. Lava platforms: These platforms are lethal for the player and the player will die instantly if he comes into contact with them. A lava platform will be accompanied by a regular platform placed adjacent to it and an ice platform placed slightly below the lava platform (that moves to the right/left) so the player can jump onto the ice platform to go to either side of the screen to then jump onto the regular platform to survive.

Do take note that the player will be 'blocked' if he collides with the underneath or sides of the platform. Therefore, he has to maneuver around the platform and land on it to successfully stand on it.

As for the spawning of the obstacles, when the game starts, the first 4 platforms will all be regular platforms. After that, the platform type is randomly picked and generated. The x-positions of the platforms are also randomly assigned so the platforms will appear in unpredictable and different positions.

## Difficulty
Throughout the game, the player and the platforms are coded to move down a certain number of pixels downwards per frame making it seem like the screen is 'moving downwards'. Thus, the player will eventually die if he simply stands still as the player will soon fall off the screen. As the game progresses, the speed at which the screen appears to move down increases, requiring the player to now react and jump more quickly in order to stay alive. 

## Other minor details 
Some other features of the game:
1. The player will first spawn on a ground.
2. The player will engage in a jumping animation whenever he jumps, with a sound effect as well!
3. Gravity is being imitated in the sense that the player will rise as he jumps, and reach a highest point before falling back down.
4. The player will engage in a walking animation whenever he is walking such as on the ground or ice/regular platform
5. There is an intro music that is played at the intro page and the results page.
6. There is background music when the actual game starts, that changes to a different song with a higher tempo when the difficulty of the game increases in the first two instances. After which, the same song will be played on repeat until the player dies.
7. The ice platform is defaulted to move right at first, once it reaches the right edge of the screen, it will move left, then when it reaches the left edge of the screen, it will move right and so on.
8. The obstacles that fall below the display screen will eventually be deleted to ensure that not too many obstacles are present as the game progresses to ensure a decent frame rate.

## Implementation
Credits to Kenney at www.kenney.nl for providing free open-source graphics that I used in this game.

I simply wanted to create something with Python and I felt that creating a simple game would allow me to familiarise myself with the language especially the use of classes. Thus, I started working on this with the Pygame library after watching an online tutorial on how to effectively use that library in the creation of 2D games.

A single Python file named 'Jumper_Final.py' contains all the code I have written. I have created a folder named 'graphics' to store all the images, a folder named 'audio' for all the audio files and a folder named 'fonts' for different fonts (though I ultimately only used one font).

### Classes
Within the Python file, we can see two sprite classes - one for the player, and one for the obstacles:
1. Player class for the player: I constantly check for keyboard inputs, update the gravity value (to imitate gravity), check if the player is walking or jumping to alter the animation (by simply changing the image of the surface used for the player) and update the coordinates of the player.

2. Obstacle class for the obstacles: I first create 4 default regular platforms at the start of the game, before creating platforms of random types. We also update the position of the platforms (making them move downwards every frame so that the screen appears to be moving down as well as the sideways motion for the ice platforms). An obstacle is also designed to destroy itself (the object is removed from the class) when it falls a certain level below the screen.

### Functions
There are 2 main functions - one to check for collisions between the player and the obstacles, and one to constantly update the score. Usually, the collisions are when rectangles of surfaces (essentially a rectangle bordering the player/platform) overlap.

1. collision_sprite() constantly checks for any collisions between the player and the obstacles. If the player collides with an obstacle, if the obstacle if lava, the player dies immediately. Otherwise, the player will not die but we have to consider if the player will stand on the platform or get blocked by the right, left, or bottom sides of the platforms. For this, I used the rect.clipline() method that takes in two coordinates. Essentially, I drew lines on the 4 sides of the platform and checked which sides of the rectangle of the player, the collisions with the lines occur. That will help me decide if the player successfully stands on a platform or gets blocked by it.
  
2. display_score(max_score) takes in the max_score variable that is set to 0 when the game is initialised and set to 0.1 when the actual game starts. Thus, if max_score > 0 when the game_state is False means that I need to show the player the results page. If max_score is equal to 0 when the game_state is False means I need to show the player the intro page. The main purpose of the max_score however, is to constantly check the y-position of the player to constantly update the max_score if (y-position of the player / 100) is greater than the max_score (meaning the player has successfully reached a new highest height). This max_score will be truncated to an int and displayed in terms of meters. The max_score is cast onto the screen on the top-left when the game is being played and also when the player has died and reached the results page.

## Conclusion
Ultimately, this entire project took me about a week to learn the basics of video game creation and to finish implementing my game. I would definitely say that this was a good opportunity for me to practice Python programming while creating something fun.
