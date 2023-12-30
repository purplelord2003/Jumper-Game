# Jumper Game
#### Video Demo:  <URL HERE>
#### Description: This simple game is created using Python with the Pygame library.

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
2. Lava platforms: These platforms are lethal for the player and the player will die instantly if he comes into contact with them. A lava platform will be accompanied by a regular platform placed adjacent to it so the player has to choose the correct platform to jump onto.
3. Ice platform: These are safe platforms for the player but they move from side to side. The player will also move along with an ice platform if he is standing on it.

Do take note that the player will be 'blocked' if he collides with the underneath or sides of the platform. Therefore, he has to maneuver around the platform and land on it to successfully stand on it.

As for the spawning of the obstacles, when the game starts, the first 4 platforms will all be regular platforms. After that, the platform type is randomly picked and generated. The x-positions of the platforms are also randomly assigned so the platforms will appear in unpredictable and different positions.

## Difficulty
Throughout the game, the player and the platforms are coded to move down a certain number of pixels downwards per frame making it seem like the screen is 'moving downwards'. Thus, the player will eventually die if he simply stands still as the player will soon fall off the screen. As the game progresses, the speed at which the screen appears to move down increases, requiring the player to now react and jump more quickly in order to stay alive. 

## Other minor details 
Some other features of the game:
1. The player will first spawn on a ground.
2. The player will engage in a jumping animation whenever he jumps, with a sound effect as well!
3. The player will engage in a walking animation whenever he is walking such as on the ground or ice/regular platform
4. There is an intro music that is played at the intro page and the results page.
5. There is background music when the actual game starts, that changes to a different song with a higher tempo when the difficulty of the game increases in the first two instances. After which, the same song will be played on repeat until the player dies.
6. 
