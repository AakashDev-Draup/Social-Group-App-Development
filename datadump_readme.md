### Data dump

The working of the data dump is shown below with example:

Dump the data in the database before running the app and making queries. <br>
Lets take an example where 15000 users are there in the app.

_Note: All the commands are run from the project directory Social-Group-App-Development.<br>
        Make sure your path is right._
<br>
<br>
1. First users are created using the make user function. Open the terminal and run the<br>
 command in the following format.
<br>
<br>
**ex : python3 -c 'from socialgroupmain.datadump.functions import makeuser; makeuser(15000)'**
<br>
<br>
2. Then groups are made. Make sure you make sufficient no of groups as in the data dump <br>
script max user in group is 300. So for 15000 users create at least 50 groups.
<br>
<br>
**ex : python3 -c 'from socialgroupmain.datadump.functions import makegroup; makegroup(50)'**
 <br>
 <br>
3. Then run the add user to group function which distributes all the users in these groups<br>
    say 15000 users in 50 groups. No argument is supplied to the function this time it distributes<br>
     the users in group with max group size of 300.
<br>  
**ex : python3 -c 'from socialgroupmain.datadump.functions import addusergroup; addusergroup()'**
<br>
<br>
4. Finally run the add post and comment function which makes a post and comment from each user.<br>
    No argument is supplied to the function every user makes a post and a comment.
<br>
<br>
**ex : python3 -c 'from socialgroupmain.datadump.functions import addpostcomment; addpostcomment()'**

  

   
