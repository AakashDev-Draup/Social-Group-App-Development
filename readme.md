#Tech Stack: Python, Flask, Mongo, and RQ


#The application architecture


#/SocialGroup		#The main app folder

	run.py		...gets the application running
	app.py		...social group application
	/Exception
		exceptions.py		...file containing the error response
	/templates			...contains the templates for response
	/model
		__init__.py
		models.py		...use data through python objects 
	/config
		__init__.py
		config.py 		...this config file makes connection to the database
	/view
		__init__.py
		mail.py			
		comment.py		...files containing user services
		post.py
		etc

	/urls
		url.py			...assigning the routes
	/auth
		auth.py			...assigning authorisation
	
	/taskqueue			...Queued tasks
		feed.py			...functions handles the daily feed for
		inactive.py		...delete the inactive members
		notify.py		...daily notification for posts
	/datadump
		__init__.py
		dump.py




#Mongodb schema

Entities:
    - Permission
        * ID 
        * Name

    - Role
        * ID
        * NAME
        * Permission[]
    - User
        * ID
        * NAME
        * email
        * groups =[]
	* posts = []
	* comments = []
    - GROUP
        * ID
        * Name
        * Users {} with id and role
        * Visibilty = PUBLIC | PRIVATE
    - POST
        * ID
	* UserId
	* GroupId
	* approval boolean
        * content
    
    - Comment
        * Id
        * PostId
        * userId
        * content
	


#List of APIS

*/api/group				...to create group and see all the groups
*/api/group/<id>				...to open a particular group by id
*/api/group/<id>/posts			...to make edit or read posts for a user by id
*/api/posts/<id>/comment			...to comment on the post


#Expected timeline of things

1. The model, config and basic services from view setup Wednesday
2. continue developing service modules from view and testing with data dump before proceeding Thursday
3. remaining services setup, api routing and testing Friday
3. The authorisation, email setup and testing Saturday
4. The queying tasks setup and testing Sunday



