# Project Overview

## Project Schedule

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Project Description | Complete
|Day 1| Wireframes / Priority Matrix / Timeline `backend` and `frontend`| Complete
|Day 1| Authorization/Authentication | Complete
|Day 1| Create models for genre and book | Incomplete
|Day 1| Create serializers for genre | Incomplete
|Day 1| Create serializers for book | Incomplete
|Day 3| Create views and urls for genre | Incomplete
|Day 3| Create views and urls for book | Incomplete
|Day 3| Test views on Postman | Incomplete


## Frontend
Click [here](https://github.com/krislee/project4-frontend) to view frontend repository.

## Live Website
Click [here](https://project4-ga.netlify.app/#/) to view live website.

## Project Description

The Book Collection Tracker is a tracker for book lovers to keep track of the books they are reading. The application is built using Python Django framework for the backend server and Postgres SQL for the database to store all the user's books. It consists of three models, which are the user, genre, and book models. These models have a one to many relationship, where one user has many genres and books, and one genre has many books under that genre. By setting up the models and serializers, the tracker has a RESTful API that allows book lovers to create, read, update, and delete the books they are reading. 

## Wireframe

- [Wireframe](https://res.cloudinary.com/dhiwn0i0g/image/upload/v1600044219/Screen_Shot_2020-09-13_at_8.43.21_PM_wgkmuk.png)

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
| Create user model | H | 1hr | hr | hr|
| Creare genre model | H | 1hr | hr | hr|
| Create video model | H | 1hr | hr | hr|
| Build user authentication | H | 1hr| hr | hr |
| Create list and create view for genre model| H | 3hr | hr | hr|
| Create retrieve and update view for genre model| H | 3hr | hr | hr|
| Create destroy view for genre model| H | 4hr | hr | hr|
| Create list and create view for video model | H | 3hrs| hr | hr |
| Create retrieve and update view for video model | H | 3hr | hr | hr|
| Create destroy view for video model | H | 1hr | hr | hr|
| Test genre view with user authentication locally| H | 2hr | hr | hr|
| Test book view with user authentication locally| H | 2hr | hr | hr|
| Test genre view with user authentication using Heroku| H | hr | hr | hr|
| Test book view with user authentication using Heroku| H | hr | hr | hr|
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


