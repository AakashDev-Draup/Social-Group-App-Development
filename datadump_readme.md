## Data dump

The working of the data dump is shown below with example:

Dump the data in the database before running the app and making queries. Lets take an example where 15000 users are <br>
there in the app.

_Note: All the commands are run from the project directory Social-Group-App-Development. Make sure your path is right._
<br>

1. First users are created using the make user function. Open the terminal and run the command in the following format.
<br>

**ex : python3 -c 'from socialgroupmain.datadump.functions import makeuser; makeuser(15000)'**
<br>
2. Then groups are made. Make sure you make sufficient no of groups as in the data dump script max user in group is 300.<br>
 So for 15000 users create at least 50 groups.
<br>

**ex : python3 -c 'from socialgroupmain.datadump.functions import makegroup; makegroup(50)'**
 <br>
3. Then run the add user to group function which distributes all the users in these groups say 15000 users in 50 groups.<br>
 No argument is supplied to the function this time it distributes the users in group with max group size of 300.
<br>  
**ex : python3 -c 'from socialgroupmain.datadump.functions import addusergroup; addusergroup()'**
<br>

4. Finally run the add post and comment function which makes a post and comment from each user. No argument is supplied<br>
 to the function every user makes a post and a comment.
<br>

**ex : python3 -c 'from socialgroupmain.datadump.functions import addpostcomment; addpostcomment()'**
<br>

  

   
