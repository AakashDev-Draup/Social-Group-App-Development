## Data dump

The working of the data dump is shown below with example:

Dump the data in the database before running the app and making queries. 

_Note: set the PATH to the directory properly before running the file.



1. First users are created using the make user function. Open the terminal and run the command in the following format.

   **ex : python3 -c 'from functions import makeuser; makeuser(<No of users>)'**

2. Then groups are made. Make sure you make sufficient no of groups as in the data dump script max user in group is 100. 

    **ex : python3 -c 'from functions import makegroup; makegroup(<No of groups>)'**

3. Then run the add user to group function which distributes all the users in these groups. No argument is supplied to the function this time it distributes the users in group with max group size of 100.  
    **ex : python3 -c 'from functions import addusergroup; addusergroup()'**

4. Finally run the add post and comment function which makes a post and comment from each user. No argument is supplied to the function every user makes a post and a comment.

    **ex : python3 -c 'from functions import addpostcomment; addpostcomment()'**

  

   
