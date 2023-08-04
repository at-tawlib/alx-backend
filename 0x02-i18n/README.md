# 0x02. i18n
## Tasks

### 0. Basic Flask app
#### Files: [0-app.py](0-app.py)  ,  [templates/0-index.html](templates/0-index.htm)
First you will setup a basic Flask app in  `0-app.py`. Create a single  `/`  route and an  `index.html`  template that simply outputs “Welcome to Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).

### 1. Basic Babel setup
#### Files:  [1-app.py](1-app.py),  [templates/1-index.html](templates/1-index.html)
Install the Babel Flask extension:
```
$ pip3 install flask_babel==2.0.0
```
Then instantiate the  `Babel`  object in your app. Store it in a module-level variable named  `babel`.

In order to configure available languages in our app, you will create a  `Config`  class that has a  `LANGUAGES`  class attribute equal to  `["en", "fr"]`.

Use  `Config`  to set Babel’s default locale (`"en"`) and timezone (`"UTC"`).

Use that class as config for your Flask app.

### 2. Get locale from request
#### Files:  [2-app.py](2-app.py), [templates/2-index.html](templates/2-index.html)
Create a  `get_locale`  function with the  `babel.localeselector`  decorator. Use  `request.accept_languages`  to determine the best match with our supported languages.

### 3. Parametrize templates
#### Files:  [3-app.py](3-app.py), [babel.cfg](babel.cfg),  [templates/3-index.html](templates/3-index.html) 
Use the  `_`  or  `gettext`  function to parametrize your templates. Use the message IDs  `home_title`  and  `home_header`.

Create a  `babel.cfg`  file containing
Then initialize your translations with
```
$ pybabel extract -F babel.cfg -o messages.pot .
```
and your two dictionaries with
```
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```
Then edit files  `translations/[en|fr]/LC_MESSAGES/messages.po`  to provide the correct value for each message ID for each language. Use the following translations:

| msgid | English | French |
|--|--|--|
| `home_title` | `"Welcome to Holberton"` | `"Bienvenue chez Holberton"` |
|`home_header`| `"Hello world!"` | `"Bonjour monde!"` |
Then compile your dictionaries with

```
$ pybabel compile -d translations
```
Reload the home page of your app and make sure that the correct messages show up.

### 4. Force locale with URL parameter
#### Files:  [4-app.py](4-app.py) ,  [babel.cfg](babel.cfg)  ,   [templates/4-index.html](templates/4-index.html) 
In this task, you will implement a way to force a particular locale by passing the  `locale=fr`  parameter to your app’s URLs.

In your  `get_locale`  function, detect if the incoming request contains  `locale`  argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting  `http://127.0.0.1:5000?locale=[fr|en]`.

**Visiting  `http://127.0.0.1:5000/?locale=fr`  should display this level 1 heading:**  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/f958f4a1529b535027ce.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230801%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230801T211224Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ba77887eeef18059aa13c37d0e4bfa7a5f311a3481c7a572475cafe7747f405f)


### 5. Mock logging in

#### Files:  [5-app.py](5-app.py) ,  [babel.cfg](babel.cfg)  ,   [templates/5-index.html](templates/4-index.html) 

Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in  `5-app.py`.

This will mock a database user table. Logging in will be mocked by passing  `login_as`  URL parameter containing the user ID to log in as.

Define a  `get_user`  function that returns a user dictionary or  `None`  if the ID cannot be found or if  `login_as`  was not passed.

Define a  `before_request`  function and use the  `app.before_request`  decorator to make it be executed before all other functions.  `before_request`  should use  `get_user`  to find a user if any, and set it as a global on  `flask.g.user`.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.
| msgid | English | French |
|--|--|--|
| `logged_in_as` | `"You are logged in as %(username)s."` | `"Vous êtes connecté en tant que %(username)s."` |
| `not_logged_in` | `"You are not logged in."` | `"Vous n'êtes pas connecté."` |
|  |  |  |
**Visiting  `http://127.0.0.1:5000/`  in your browser should display this:**

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/2c5b2c8190f88c6b4668.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230801%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230801T211224Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2be6933840f0c62ebe032249c1ac5363a25141a4d14b97d56894e522bc1b201f)

**Visiting  `http://127.0.0.1:5000/?login_as=2`  in your browser should display this:**  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/277f24308c856a09908c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230801%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230801T211224Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=09e3a1aa6393bb84a5147d9729affae51caadee48d22c2d2b35c11d50fba014e)


### 6. Use user locale
#### Files:  [6-app.py](6-app.py) ,  [babel.cfg](babel.cfg)  ,   [templates/6-index.html](templates/6-index.html) 

Change your  `get_locale`  function to use a user’s preferred local if it is supported.

The order of priority should be
1.  Locale from URL parameters
2.  Locale from user settings
3.  Locale from request header
4.  Default locale

Test by logging in as different users

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/9941b480b0b9d87dc5de.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230801%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230801T211224Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=dd7fd09126cb71e2b74b5fe2873505de54ac2b110f7f3b98de6b1b2d4c802d09)

### 7. Infer appropriate time zone
#### Files:  [7-app.py](7-app.py),  [templates/7-index.html](templates/7-index.html)
Define a  `get_timezone`  function and use the  `babel.timezoneselector`  decorator.

The logic should be the same as  `get_locale`:

1.  Find  `timezone`  parameter in URL parameters
2.  Find time zone from user settings
3.  Default to UTC
Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use  `pytz.timezone`  and catch the  `pytz.exceptions.UnknownTimeZoneError`  exception.

### 8. Display the current time
#### Files:  [8-app.py](8-app.py),  [templates/8-index.html](templates/8-index.html)
Based on the inferred time zone, display the current time on the home page in the default format. For example:

`Jan 21, 2020, 5:55:39 AM`  or  `21 janv. 2020 à 05:56:28`

Use the following translations
| msgid | English | French |
|--|--|--|
| `current_time_is` | `"The current time is %(current_time)s."` |  `"Nous sommes le %(current_time)s."`|

**Displaying the time in French looks like this:**

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/bba4805d6dca0a46a0f6.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230804%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230804T115534Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e130cff71272ff91977e63a83b1b147769d2fc5b7fc69831f9770c215e3e7fca)

**Displaying the time in English looks like this:**

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/54f3be802024dbcf06f4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230804%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230804T115534Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=39e2436994fa3c0d461f2bc7341fee826327d99265650194ca234220b14b580b)

> Written with [StackEdit](https://stackedit.io/).
