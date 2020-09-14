# Project Overview

## Project Schedule

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Project Description | Complete
|Day 1| Wireframes / Priority Matrix / Timeline `backend` and `frontend`| Complete
|Day 2| Working RestAPI | Incomplete
|Day 3| Core Application Structure (HTML, CSS, etc.) | Incomplete
|Day 4| MVP & Bug Fixes | Incomplete
|Day 5| Final Touches and Present | Incomplete

## Project Description

The Book Collection Tracker is a tracker for book lovers to keep track of the books they are reading. The application is built using Python Django framework for the backend server and Postgres SQL for the database to store all the user's books. It consists of three models, which are the user, genre, and book models. These models have a one to many relationship, where one user has many genres and books, and one genre has many books under that genre. By setting up the models and serializers, the tracker has a RESTful API that allows book lovers to create, read, update, and delete the books they are reading. 

## Wireframe

- [Wireframe](https://res.cloudinary.com/dhiwn0i0g/image/upload/v1600036729/Screen_Shot_2020-09-12_at_11.47.47_AM_fue0tb.png)

## Time/Priority Matrix 
- [Time/Priority Matrix] (https://res.cloudinary.com/dhiwn0i0g/image/upload/v1600040003/My_First_Board_2_twhkpr.jpg)

### MVP/PostMVP 
#### MVP (examples)

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

| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Create user model | H | 1hr | 1hr | 1hr|
| Creare genre model | H | 1hr | 0.5hr | 0.5hr|
| Create video model | H | H | 0.5hr | 0.5hr|
| Build user authentication | H | 1hr| 1hr | 1hr |
| Create list and create view for genre model| H | 3hr | 2hr | 2hr|
| Create retrieve and update view for genre model| H | 3hr | 0hr | 0hr|
| Create destroy view for genre model| H | 4hr | 0hr | 0hr|
| Create list and create view for video model | H | 3hrs| 1.5hr | 1.5hr |
| Create retrieve and update view for video model | H | 3hr | 1.5hr | 1.5hr|
| Create destroy view for video model | H | 1hr | 0hr | 0hr|
| Test genre view with user authentication locally| H | 2hr | 1hr | 1hr|
| Test book view with user authentication locally| H | 2hr | 3hr | 3hr|
| Test genre view with user authentication using Heroku| H | 1hr | 0.5hr | 1hr|
| Test book view with user authentication using Heroku| H | 2hr | 1hr | 1hr|
| Total | H | 27.5hrs| -hrs | -hrs |

#### PostMVP

| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Create file upload function for book | L | 3hr | -hr | -hr|
| Share book recommendations to other users | L | 12hr | -hr | -hr|
| Create Favorite books model | M | 2hr | -hr | -hr|
| Create Favorite book view | M | 4hr | -hr | -hr|
| Add rate book field| M | 2hr | -hr | -hr|
| Create another application to list top rated books | L | 12hr | -hr | -hr|
| Total | H | 35hrs| -hrs | -hrs |

## Additional Libraries

- Django REST Framework
- Django Heroku
- Django Rest Framework JWT

## Code Snippet

Use this section to include a brief code snippet of functionality that you are proud of an a brief description  

```
function reverse(string) {
	// here is the code to reverse a string of text
}
```

## Issues and Resolutions
 Use this section to list of all major issues encountered and their resolution.

#### SAMPLE.....
**ERROR**: app.js:34 Uncaught SyntaxError: Unexpected identifier                                
**RESOLUTION**: Missing comma after first object in sources {} object


