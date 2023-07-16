# Python Web With Flask

### Configuracion inicial
```
> mkdir python_web
> cd python_web
python_web> virtualenv venv
python_web> source venv/bin/activate
python_web> pip freeze
python_web> pip install Flask
python_web> pip freeze
```

### Run aplicacion
```
python_web> python app.py
o
python_web> flask --app app run 
```

### Deploy aplicacion
```
python_web> touch requirements.txt
python_web> pip freeze > requirements.txt
python_web> cat requirements.txt

python_web> heroku create 'name of the app as one word'
python_web> git push heroku master
python_web> heroku open (to launch the deployed application)

```

