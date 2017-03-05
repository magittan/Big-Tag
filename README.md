# Big-Tag

AIzaSyDANsv5pR_ChVtexCZbd5RXBiLoH-0EEls
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
 Outputs:
    if the user inputs the data in correctly, a true will be outputted => suggestion, prompted to go to the create a game page
    else a false will be outputted with an error message => suggestion, prompted to try again
  
Users can create a game
  Required inputs:
    Create a Game
    Name of the Game
    Users invited
  Required inputs:
      if the game is created successfully, a true will be outputted => suggestion: a prompt will be issued to view the log tag page
      if the game fails to be created, a false will be outputted with an error message=> redirected to the page once again
  
Users can log/check tags in currently ongoing games
  Required inputs:
      Selecting a game to look at
      Entering a tagged persons code
  Outputs:
      the Tagged Persons Name
      statistics // to be determined
      if the code is correct, returns true => suggestion changes the name and displays good job
      if the code is wrong, returns false  with an error message => suggestion asks again 
  
  
Going to be developed later!
########################################################################################################################################
Users can check the statistics from ongoing games
  Required inputs: 
    Selecting the game to look at
    
Next steps: JS would pull user information from FB with FB API https://developers.facebook.com/docs/javascript/howto/jquery/v2.8
Next steps: Location of Tag will be recorded (Working on)
Next steps: Time of Tags will be recorded (Working on)
Next steps: Map of Tags https://developers.google.com/maps/documentation/javascript/geolocation

