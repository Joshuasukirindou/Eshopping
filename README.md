# Ecommerce Website 

## 1 - About us

Our website application used Django for the database and its creation, and edit operations. This website application allows users to shopping online  with login , which means that clients should browse as a user. 

## 2 - Main features

* Buy some items online
* Add some items into cart
* Search some items online
* Different views for the items 
* Message system station
* Login and add account

## 3 - Database overview

![](https://ibb.co/JzPkLdd)

## 4 - Installation

### 4.1 If you are using Codio:

#### 4.1.1 Create a virtual environment and activate it in the terminal of Codio
``` shell
    python3 -m venv .venv 
```

``` shell
    source .venv/bin/activate 
```

#### 4.1.2 Clone the repository or pull the code from Github
``` shell
    git clone git@github.com:LucasZhengrui/Enterprise_Software_Dev_Note.git
```
Or if you have cloned before

``` shell
    git pull origin main
```

#### 4.1.3 Changed the site details in **ALLOWED_HOSTS** of ```soloproject/setting.py```

For example:

``` shell
    ALLOWED_HOSTS = ['127.0.0.1','estroeassignment.onrender.com','enjoytavern-latinspray-8000.codio-box.uk']
```

#### 4.1.4 Install Django and Plotly in terminal

As for the Django installation

``` shell
    pip install django
```
As for the Behave installation

``` shell
    pip install Behave
```

As for the Django_behave installation

``` shell
    pip install django-behave
```

As for the Pillow in terminal

``` shell
    pip install pillow
```

#### 4.1.5 Run the website application

``` shell
    python3 manage.py runserver 0.0.0.0:8000
```

P.S **8000** is decided by what did you input in 3.1.3

### 4.2 If you are using a local editor, such as Visual Studio Code, or Mac Terminal:

#### 4.2.1 Create a virtual environment and activate it in the terminal
``` shell
    python3 -m venv .venv 
```

``` shell
    source .venv/bin/activate 
```

#### 4.2.2 Clone the repository or pull the code from Github
``` shell
    git clone https://github.com/LucasZhengrui/Enterprise_Software_Dev_Note.git
```
Or if you have cloned before

``` shell
    git pull origin main
```

#### 4.2.3 Changed the site details in **ALLOWED_HOSTS** of ```soloproject/setting.py```

For example:

``` shell
    ALLOWED_HOSTS = ['127.0.0.1','localhost']
```

#### 4.2.4 Install Django and Plotly in terminal

As for the Django installation

``` shell
    pip install django
```

As for the Pillow in terminal

``` shell
    pip install pillow
```

#### 4.2.5 Run the website application

``` shell
    python3 manage.py runserver
```

## 5 - Test

Besides the estore table app, we have done unit testing for other apps. The table app does not need us to test inside the app, but we have their related testing in other apps. 

## 6 - Details of deploying the website application

The website application has been deployed to Render, here is its URL: https://estroeassignment.onrender.com .

Build command:

``` shell
    pip install --upgrade pip && pip install -r requirements.txt
```

Start command:

``` shell
    gunicorn soloproject.wsgi:application --worker-class=gevent --worker-connections=1000 --workers=4 --bind=0.0.0.0:$PORT
```