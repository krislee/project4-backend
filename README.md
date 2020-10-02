# Project Overview

## Project Schedule

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Project Description | Complete
|Day 1| Wireframes / Priority Matrix / Timeline `backend` and `frontend`| Complete
|Day 1| Authorization/Authentication | Complete
|Day 1| Create models for genre and book | Complete
|Day 1| Create serializers for genre | Complete
|Day 1| Create serializers for book | Complete
|Day 2| Make create view for genre | Complete
|Day 2| Make list view for genre | Complete
|Day 2| Make retrieve view for genre | Complete
|Day 2| Make update view for genre | Complete
|Day 2| Make delete view for genre | Complete
|Day 2| Make create view for book | Complete
|Day 2| Make list view for book | Complete
|Day 2| Make retrieve view for book | Complete
|Day 2| Make update view for book | Complete
|Day 2| Make delete view for book | Complete
|Day 2| Make urls for genre and book views | Complete
|Day 2| Test views on Postman | Complete


## Frontend
Click [here](https://github.com/krislee/project4-frontend) to view frontend repository.

## Live Website
Click [here](https://official-library.netlify.app/#/) to view live website.

## Project Description

The Book Collection Tracker is a tracker for book lovers to keep track of the books they are reading. The application is built using Python Django framework for the backend server and Postgres SQL for the database to store all the user's books. It consists of three models, which are the user, genre, and book models. These models have a one to many relationship, where one user has many genres and books, and one genre has many books under that genre. By setting up the models and serializers, the tracker has a RESTful API that allows book lovers to create, read, update, and delete the books they are reading. 

## ERD

- [ERD](https://res.cloudinary.com/dhiwn0i0g/image/upload/v1600044219/Screen_Shot_2020-09-13_at_8.43.21_PM_wgkmuk.png)

## Time/Priority Matrix 
- [Time/Priority Matrix](https://res.cloudinary.com/dhiwn0i0g/image/upload/v1600040003/My_First_Board_2_twhkpr.jpg)

### MVP/PostMVP 
#### MVP

- Create user, genre, and book model
- Create user authentication
- Create genre and book serializers
- Create views for genre model
- Create views for book model 
- Create urls for user login and registration
- Create url for genre view
- Create urls for book view
- Test API with local server on Postman
- Heroku deployment
- Test API with Heroku server on Postman

#### PostMVP 

- Create file upload to upload book reports
- User can share book recommendation to another user 
- User can favorite books
- User can see the favorite books under favorites category
- User can also rate each book
- Make another application for the public to see top rated books by users in each genre

## Functional Components
#### MVP

| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Create user model | H | 1hr | 1hr | 1hr|
| Creare genre model | H | 1hr | 0.5hr | 0.5hr|
| Create video model | H | 1hr | 0.5hr | 0.5hr|
| Build user authentication | H | 1hr| 1hr | 1hr |
| Create list and create view for genre model| H | 3hr | 2hr | 2hr|
| Create retrieve and update view for genre model| H | 3hr | 5hr | 5hr|
| Create destroy view for genre model| H | 4hr | 0.5hr | 0.5hr|
| Create list and create view for video model | H | 3hrs| 3hr | 3hr |
| Create retrieve and update view for video model | H | 3hr | 5hr | 5hr|
| Create destroy view for video model | H | 1hr | 0.5hr | 0.5hr|
| Test genre view with user authentication locally| H | 2hr | 1hr | 1hr|
| Test book view with user authentication locally| H | 2hr | 2hr | 2hr|
| Test genre view with user authentication using Heroku| H | 1hr | 0.5hr | 0.5hr|
| Test book view with user authentication using Heroku| H | 2hr | 1hr | 1hr|
| Total | H | 27.5hrs| 23.5hrs | 23.5hrs |

#### PostMVP

| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Create file upload function for book | L | 3hr | 0hr | 0hr|
| Share book recommendations to other users | L | 12hr | 0hr | 0hr|
| Create Favorite books model | M | 2hr | 0hr | 0hr|
| Create Favorite book view | M | 4hr | 0hr | 0hr|
| Add rate book field| M | 2hr | 0hr | 0hr|
| Create another application to list top rated books | L | 12hr | 0hr | 0hr|
| Total | H | 35hrs| 0hrs | 0hrs |

## Additional Libraries

- Django REST Framework
- Django Heroku
- Django Rest Framework JWT

## Code Snippet
To have unique genre and book names, unique=True attribute was initially assigned in both Genre name field and Book title field. Although this solved the issue of one user not being able to create or update to the same genre and book names, this caused one user to be unable to create or update to the same genre and book name as another user. Therefore, for both Genre and Book views needed to have custom update and create methods, overriding those from viewset and APIViews. 

In the create methods of Genre and Book, the .get() method is used to check if there is a genre or book object based on the genre name or book title. If the genre or book objects does exist with that genre name or book title, then the super().create() methods will not run and raise an error. In the Genre and Book update methods, the .get() method is also used. If there is a genre or book object with the name or title under the user, then another checkpoint is needed where we check the genre name or book title against the name or title the user is trying to update. If the updated name or title is the same or different from the genre name or book title in the database, then the update will proceed. Otherwise, an error is thrown.

```python
# Genre update:
def update(self, request, *args, **kwargs):
	genre = Genre.objects.filter(
		name=self.request.data['name'],
		user=self.request.user
	)
	if genre:
		if Genre.objects.get(pk=self.kwargs['pk']).name != self.request.data['name']:
			return Response({
				"message": "This genre already exists"
			})
		else:
			return super().update(request, *args, **kwargs)
	else:
		return super().update(request, *args, **kwargs)

# Book update:
def update(self, request, *args, **kwargs):
	try:
		if self.request.user.genres.get(pk=self.request.data['genre']):
			book = Book.objects.filter(
				user=self.request.user,
				title=request.data.get('title')
			)
			if book:
				if Book.objects.get(pk=self.kwargs['pk']).title != self.request.data['title']:
					return Response({
						"message": "This books exists already"
					})
				else:
					return super().update(request, *args, **kwargs)
			else:
				return super().update(request, *args, **kwargs)
	except Genre.DoesNotExist:
		raise ValidationError("You cannot update the book in a genre that you do not have access to")
```

## Issues and Resolutions

**ERROR**: User was registered but error was raised: raise serializers.ValidationError('A user with that username or password is not found')                            
**RESOLUTION**: Had to switch from username_field = ‘email’ to username_field = ‘username’ in the User model

**ERROR**: During Heroku authorization migration: django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency authorization.0001_initial on database 'default'.
**RESOLUTION**: Comment out the following:
'django.contrib.admin' in INSTALLED_APPS
ath('admin/', admin.site.urls) in url.py

**ERROR**: During Heroku authorization migration: 
You are trying to change the nullable field 'first_name' on user to non-nullable without a default; we can't do that (the database needs something to populate existing rows)
**RESOLUTION**: Had to add back null=True to first_name and last_name User model


