# django-0-hello
 helloworld django project with git
 
 1.open empty repo with vc code, new terminal:
    pip install pipenv
    pipenv install django 
    -> ValueError: Not a valid python path: 'C:/Users/.../Anaconda3/Scripts/python.exe'
    ? copy Python38 as Anaconda3 folder
    -> ValueError: Not a valid python path: 'C:/Python27/Scripts/python.exe'
    ? python -m site --user-site and replacing site-packages with Scripts
    -> ValueError: Not a valid python path: 'C:/Python27/Scripts/python.exe'
    new project with PyCharm, new interpreter pipenv, install Django
    
 2. pipenv shell
    django-admin startproject name_of_project .
    tree
    python manage.py runserver
    -> ConnectionResetError: [WinError 10054]
    
 3. python manage.py startapp pages
    add to INSTALLED_APPS 'pages.apps.PagesConfig', # new
    -> if Linux: touch pages/urls.py
    -> Windows: cd pages copy NUL urls.py
    
    python manage.py migrate
 
 4. cd pages mkdir templates/pages cd ... copy NUL home.html
    setting.py: TEMPLATES: 'DIRS': [os.path.join(BASE_DIR, 'templates')], # new
 
 5. view based on class, 'base.html' as layout
    {% extends 'base.html' %}
    
 6. write some SimpleTestCase, stop server
    python manage.py test
    
 7. heroku deploy
    • update Pipfile.lock 
    • make a new Procfile file 
    • install gunicorn as our web server 
    • make aone-line change to settings.py file
    
    • create a new app on Heroku and push our code to it 
    • add a git remote “hook” for Heroku 
    • configure the app to ignore static files 
    • start the Heroku server so the app is live 
    • visit the app on Heroku’s provided URL
