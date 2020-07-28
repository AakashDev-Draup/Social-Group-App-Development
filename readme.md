#Tech Stack: Python, Flask, Mongo, and RQ


#Work Completed 1:
	
	1. Updating the corrections discussed at Friday's meeting.				(Friday)
	2. Updating document schema to insert create and update time variables. 		(Friday)
	3. Setting up remaining requests such as DELETE and GET for post and comment view.	(Monday)
	4. Scheduler task of deleting inactive users.						(Monday)
	5. Scheduler task for Daily feed via mail.						(Tuesday)
	6. Queue task for sending post activity via mail. 					(Tuesday)


#Work Ahead:

	1. Suggested corrections.					(Wednesday)
	2. Testing the application with a data dump.			(Wednesday) 






#The application architecture


	SocialGroup		...The main app folder

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

	*Entities:
	    * Permission
		* ID 
		* Name

	    * Role
		* ID
		* NAME
		* Permission[]
	    * User
		* ID
		* NAME
		* email
		* groups =[]
		* posts = []
		* comments = []
	    * GROUP
		* ID
		* Name
		* Users {} with id and role
		* Visibilty = PUBLIC | PRIVATE
	    * POST
		* ID
		* UserId
		* GroupId
		* approval boolean
		* content
	    
	    * Comment
		* Id
		* PostId
		* userId
		* content
	


#List of APIS

1. api.add_resource(roleapi, '/api/role/<id>')  # create role and assign permission, id is special key here
2. api.add_resource(Userapi, '/api/User')                      # create user
3. api.add_resource(CreateGroupApi, '/api/<id>/Group')               # create group with user id
4. api.add_resource(AddUserGroup, '/api/addtogroup/<id>')       # add user to the group
5. api.add_resource(RemoveGroupApi, '/api/removefromgroup/<id>')   # Remove user from the group
6. api.add_resource(PostApi, '/api/Group/<id>/post')               # add post
7. api.add_resource(CommentApi, '/api/<gid>/<pid>/comment')        # add comment





