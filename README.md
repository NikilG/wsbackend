# wsbackend
<h1> Install python3 <h1>
Install virtual environment and activate it.

Using git clone, download this environment into your system.

Run, SET FLASK_ENV=development ( In Windows )

Before running below command ensure you create a database in your system and apply same configurations over below command
Run, SET DATABASE_URL = postgres://username:password@host:port/dbname ( In Windows )

Next Run, Below commands
python manager.py db inint

python manager.py db migrate

python manager.py db upgrade

Now start your flask server python app.py

If all the above steps are working fine, go to postman and start using your API's


