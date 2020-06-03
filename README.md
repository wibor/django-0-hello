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
    django-admin startproject test_project .
    tree
    python manage.py runserver
    -> ConnectionResetError: [WinError 10054]
    
 3. python manage.py startapp pages
    add to INSTALLED_APPS 'pages.apps.PagesConfig', # new
    -> if Linux: touch pages/urls.py
    -> Windows: cd pages copy NUL urls.py
 
