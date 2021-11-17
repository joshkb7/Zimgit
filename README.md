# Zimgit Website

# Setup
1. Install python virtual environment (I use conda on mac) 
- https://www.anaconda.com/products/individual

2. Install django onto virtual environment
- python -m pip install Django

3. Install crispy_forms (for login/registration)
- pip install django-crispy-forms

4. Set python interpreter in vscode to conda 
- CMD+SHIFT+P then select conda (base)

5. cd into Zimgit project folder containing manage.py to runserver
- python manage.py runserver [port] (ex: 8000)
- cmd click on ip in terminal if using vscode to take you right to the localhost site


# Creating a new page + linking to navbar
1. create html file

2. add html link to urls.py 

3. add def to views.py

4. create href in base.html navbar
