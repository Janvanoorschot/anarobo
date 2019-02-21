
# Robomind Academy Data

The anonymised Robomind Academy data can be found in this ./data directory. I consists
of the following compressed JSON formatted data:

* *sittings-<date>.gz* : every line describes one session/sitting of a person in the Academy
* *course.gz*: ids of the courses in the Academy
* *storyline.gz*: ids of the storyline's by course in the Academy
* *storylineitem.gz*: ids of the items in the storyline's in the course's in the Academy and their linked Challenge
* *challenge.gz*: ids of the Challenges in the Academy
* *teacher.gz*: ids and details from persons that are teachers in the Academy
* *ipupil.gz*: ids and details from persons that are Identified pupils in the Academy, with links to their teachers
* *apupil.gz*: ids and details from persons that are not Identified pupils in the Academy, with links to their teachers


## Sittings

For every week there is a sittings-<date>.gz file. Every line in this compressed is JSON formatted and describes 
a sitting (session) in the Robomind Academy. The top-level attributes are:

* *id*: a unique id of the sitting
* *person*: id of the person in this sitting
* *starttime*: time this sitting was started
* *endtime*: time this is sitting was ended
* *active*: true if this sitting is still open, false otherwise
* *realsitting*: true if this sitting contains a 'runscript' operation, false otherwise
* *actions*: a list of actions performand in this sitting (in order)

Each action in the list of actions looks like this:

* *type*: either gotostorylineitem, runscript, storylinecompleted or coursecompleted
* *toffset*: time in seconds from the start of this sitting to the start of this action
* *storylineitem*: the storyline-item in currently in context
* *details*: when the type is 'runscript', this field contains the details about the run

When the type of the action is 'runscript', the details blob will contain the attributes:

* *script*: the script in english that was run
* *guessedLang*: the original language of the script
* *duration*: the duration of the run
* *success*: true if the run was successful, false otherwise
* *firsttime*: true if this was the first time this storyline-item was succesfully run, false otherwise
* *score*: the score of the successful run
* *profile*: when the run was successful, this contains the details about the run 

When the type of action is 'runscript' and the run was successful, the profile attribute contain 
the following attributes:

* *paintWhites*: the number of tiles painted white during the run
* *robotHasBumped*: the number of times the robot bumped
* *scriptTotalCharacters*: total number of characters in the original script
* *scriptCalls*: number of calls in the script
* *scriptBasicCommands*: number of commands in the script
* *total*: total number of steps performed duing the run
* *see*: number of see commands in the run
* *robotHasBeacon*: 1 if the robot holds a beacon at the end of the run, 0 otherwise
* *paintBlacks*: the number of tiles painted black during the run
* *scriptCharacters*: effective number of characters in the original script
* *flipCoins*: number of times the robot flipped a coin
* *exploredTileCount*:number of tiles the robot has visited during the run
* *scriptRecursive*: 1 if the script uses recursive calls, 0 otherwise
* *successfulGets*: number of successful gets
* *robotOrientation*: orientation (in degrees) of the robot at the end of the run
* *gets*: total number of pickUp commands performed
* *successfulEats*: number of successful Eat commands performed
* *puts*: total number of putDown commands performed
* *eats*:total number of Eat commands
* *moves*: total number of moves
* *explored*: total number of tiles explored
* *blackPaintUsed*: number of tiles painted black
* *robotActions*: total number of robot actions
* *robotX*: X coordinate of final location of the robot
* *robotY*: Y coordinate of final location of the robot
* *successfulPuts*: number of succesful puts
* *whitePaintUsed*: number of tiles painted white
* *score*: score of this run