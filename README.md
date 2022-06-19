# The Zone
The Zone is a neighborhood  a web application that allows you to be in the loop about everything happening in your neighborhood. </br>
From contact information of different handyman to meeting announcements or even alerts. </br>
You can sign up and join a neighborhood, leave the neighborhood and create a new neighborhood.</br>
You can also create a new businesses, schools, hospitals and posts, that will only be visible in your current neighborhood.


## Getting Started

To get a copy of the Zone running loccally on your end, you can:

1. Clone this repository, by running git clone then:

for ssh:
```
git@github.com:AtienoObwanda/TheZone.git
```

or for https: 
```
https://github.com/AtienoObwanda/TheZone.git
```

2. Set up a python environment to run the application:
```
$ python3 -m venv env
$ source env/bin/activate
(env) $ pip install Django
```

### Prerequisites

Before you begin running the application, you must first install all the dependencies listed in the requirements.txt file.

```
 (env) $ pip install -r requirements.txt

```

### Installing

1. Create a database:
  ```
(env) $ psql CREATE DATABASE *DATABASE_NAME*;
(env) $ pip install psycopg2
```

2. Create a new .env file and set up the following configurations:

 * Database name, host, password and user.

3. Make your first migrations: 


```
(env) $ python manage.py migrate 
```

4. Make migrations for the hood application: 

```
(env) $ python manage.py makemigrations hood
(env) $ python manage.py migrate
```

5. Make migrations for the members application: 

```
(env) $ python manage.py makemigrations members
(env) $ python manage.py migrate
```
6. Create a super user / admin:


```
(env) $ python manage.py createsuperuser
```

## Running the tests

To test the two applications, you can run two different tests:
* Test the first application (hood):

```
(env) $ python3 manage.py test hood
```

* Test the second  application (members):

```
(env) $ python3 manage.py test members
```

## Deployment

To get this application deployed live on a server, you can follow the following guide: [How to Deploy Django Applications on Heroku
](https://gist.github.com/AtienoObwanda/5c506e167e3672a1cc93bbf55fac984b)

## Built With

* Python3.9 - Backend

* Django4 - Python Framework

* PostgreSQL - Database 

* Heroku - Deployment

## User Stories:
As as user, you can be able to: 
*  Sign in with the application to start using.
*  Set up a profile about you and a general location and your neighborhood name.
*  Find a list of different businesses in YOUR neighborhood.
*  Find Contact Information for the health department, Police authorities, schools, and businesses near YOUR neighborhood.
*  Create Posts that will be visible to everyone in your neighborhood.
* Change YOUR neighborhood when you decide to move out.
* Only view details of a single neighborhood.
* YOu can also join an existing neighborhood.

## BDD

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **Choose** to login or sign up | Login / Sign up page. User your credentials to access the application|
|Join a hood or create one| Choose whether you want to join a hood, or better yet, create your new hood, specify a location, number of occupants and upload a hood picture| Joining a hood, redirects you to an existing hood, where you can view what the hood is all about. Creating a new hood redirects you to a page where you can create your new hood|
|Create set up new police station/ business/ school or hospital|Each amenity section has a + button which redirects you to a form to add either a hospital, shool, police station, or school depending on what you chose| Upon redirect to create a new social ameninity, fill in the form as prompted, then submit to save|
|Create a post visible only to your neighborhood| You can also create posts by selectiong the + button| Upon redirect, add the new post title and body then proceed to save. Your post is now visible to your neighborhood members|
|Leave Neighborhood| The leave button removes you from the neighborhood the redirects you to the join hooh page| Upon redirect, you can either opt to create a new hood, join an existing one or log out|

## Authors

* **Atieno Obwanda**- [GitHub](https://github.com/AtienoObwanda)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
