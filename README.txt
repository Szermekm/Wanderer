Introduction
Stories should be followed by implementation. Completing a story means you made a little progress on the project.
Keep in mind, that you have to develop the complete game. So when working on a specific story, you should be able to reuse the implementation later in other parts of the game.
Draw a screen with tiles

1. Draw a single tile
•	Given the launched game
•	Then it should show a tile like this:
2. Fill the screen with the tile
•	Given the launched game
•	Then it should show a map of tiles like this:

3. Add wall tiles
•	Given the launched game
•	When the map is rendered on the screen
•	Then it should show floor and wall type tiles as well like on this layout (you can arrange wall differently if you wish):
Place a character on it and move with key bindings
4. Add the Hero
•	Given the launched game
•	When the map is rendered on the screen
•	Add the player character called the hero
•	Then it should show a hero on the top-left corner:
 
Interactions
The player should be able to move the hero by using their arrow keys.
5. Move around
•	Given the launched game
•	When any of the arrow keys are pressed by the user
•	Then the hero should move to that direction
6. Hero direction
•	Given the launched game
•	When the hero is moved by the arrow keys
•	Then the hero should face the direction where he went
7. Map boundaries
•	Given the hero on any edge of the map
•	When the hero is moved by the arrow keys towards the edge
•	Then it should not move or leave the map, only its direction should change if necessary
8. Walls
•	Given the hero next to a wall tile
•	When the hero is moved by the arrow keys towards the wall tile
•	Then it should not move, only its direction should change if necessary
