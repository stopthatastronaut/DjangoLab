Push-Location ./quickstart

virtualenv env

./env/bin/activate

pip install django

django-admin startproject quickstart .

python manage.py migrate

python manage.py runserver

Pop-Location


# password is just 'Password'. It's a Lab, there's nothing important in here.