# Big-Tag

https://pypi.python.org/pypi/python-firebase/1.2

So far the basic skeleton of the game is being created

HTML/CSS functional Website: 
  Users are invited to make an account
  Users can create a game with other Users
  Users can log tags in currently ongoing games
  Users can check the statistics from ongoing games
  
Users are invited to make an account:
 Required inputs:
    name
    email
    passwords
  
Users can create a game
  Using Python in order to create the functionality of the game 
    Game class will be used to intialize seperate games with ID numbers
    Ajax to take in information:
      Create a Game
      Name of the Game
      Users invited
  
Users can log/check tags in currently ongoing games
  Required inputs:
      Selecting a game to look at
      Entering a tagged persons code
  Outputs:
      the Tagged Persons Name
      if the code is correct Changes the name and displays good job
      if the code is wrong, asks again
  
Users can check the statistics from ongoing games
  Required inputs: 
    Selecting the game to look at
