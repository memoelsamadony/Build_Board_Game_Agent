# Build_Board_Game_Agent
This is a project to implement an AI agent to play a board game, it is made as a project demanded in cairo university at faculty of computers and artificial intelligence
at the AI course.

## Table of contents
- [About](#about)
- [How to run the program](#how-to-run-the-program)
- [Libraries](#libraries)
- [How to use the program](#how-to-use-the-program)
- [credits](#credits)



## About 
This program starts with a menu displayed and relaxing music played in the background, the user get to choose the algorithm he would like the agent to use,
as well as the search tool,color and difficulty. Afterwards the game begins and the user get to watch each of the two AI agents try to win over the other.

Main project Files :

1. Chess_Class.py :

             - That is where the chess game is implemented
2. Chess_GUI.py :

             - That is where the GUI is made, also that is where the program is run from
3. data.txt :

             - The file that contains the data used to measure the performance of each agent
4. report.ipynb :

             - jupyter notebook file which uses the data in data.txt to generate graphs that describes each agent performance 
             - And how they compare to one another
5. Performance Measure Report.pdf :

             - pdf file which contains the full report about the two agents
6. images and report images folders :

             - folders that contain images used by the GUI and the report


This project required a shared post on linkedin [here](https://www.linkedin.com/feed/update/urn:li:activity:7065762603544772608/)

## How to run the program
After downloading the above files:

Make sure you are in the project's root directory and then run the following command:
`python Chess_GUI.py` or `py Chess_GUI.py`

Then you should see that menu displayed :

![image](https://github.com/memoelsamadony/Build_Board_Game_Agent/assets/91777656/75c52efc-1f33-4ac8-90e9-900ed9bcfd0f)


## Libraries
1. pygame
2. multiprocessing
3. pygame_menu
4. PIL
5. time
6. sys
7. random
8. matplotlib.pyplot
9. seaborn
10. numpy
11. re

you can install any library of the above using the following command :
`pip install library_name` or `py -m pip install library_name`


## How to use the program
After running the program and the above menu displayed :

The user get to choose from each option like this :

![image](https://github.com/memoelsamadony/Build_Board_Game_Agent/assets/91777656/7c688a95-b618-4e2a-a1e8-0e9972bb1742)

Then the game start playing like this : 

![image](https://github.com/memoelsamadony/Build_Board_Game_Agent/assets/91777656/9aa49458-ab30-45e5-bd90-ea6f399053b1)


You can find the report in the 'Performance Measure Report.pdf' , here is a sample of it :

![image](https://github.com/memoelsamadony/Build_Board_Game_Agent/assets/91777656/54b2fc5a-30fa-4d35-b134-9f29d58aebc3)


## credits 

We would like to thank all our peers at college , Cairo University















