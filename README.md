# Subway Challenge by Kadir
The complex office issue with ordering Subway, making life easier.

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Git:
- status: public


    https://github.com/KadirB/subway_challenge/

Pull from ssh:


    git@github.com:KadirB/subway_challenge.git

## Basic Commands

### Setting Up Your Users
note: when I say python manage.py it could be python3 manage.py. Unless you run the following:

        $ source env/bin/activate

- To create a **normal user account**, (Only admins can do) first create a superuser as mentioned below. After that you can run the project by doing:


        $ python manage.py createsuperuser

- To create a **superuser account**, use this command:


        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Working with the project
Running the project and working with it.


        $ python manage.py runserver

Go to localhost:8000/admin, login with your superuser and create your first user account.

All profiles, meals and orders depend on the username and token in the link, and if the meal/order is open or close.

For example create meal in the admin side, fill all the foodtype and foodoptions.


### Profile
NOTE: after going to a magic link the users will be logged in automaticly.

* After creating a normal user they will be in the profiles model with a generated token.
* Go to the profile where we can see all the users orders (now it will be empty right):


    localhost:8000/profile/{username}/<token>

### Meals 
* In the backend you can choose open or close for a meal. Default is open
* After creating a meal. Go the following link


    localhost:8000/meal/{mealname}/{username}/{token}

* Select your options and save.
* Go back to your profile page again and check.

### Orders 
* In the backend you can choose open or close for a meal. Default is open
* After selecting options there is an order you can access it if order is open:


    localhost:8000/profile/order/{order-id}/{username}/{token}

* Play with the open/closed options in the backend to see if it works.

### Docker

Not yet implemented.
