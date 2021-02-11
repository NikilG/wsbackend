# wsbackend 
<b>NOTE: Tested below steps on Windows System</b>

<h6> Install python3 <h6>
  
<h6> Install virtual environment and activate it. <h6>

Using git clone, download this environment into your system.

Run, <h6> pip install -r requirements.txt </h6>

Run, <h6> SET FLASK_ENV=development </h6> 

Before running below command ensure you create a database_name in your system and apply same db configurations over below command
Run, <h6> SET DATABASE_URL = postgresql://username:password@localhost/dbname </h6>

Next Run, Below commands ( This commands creates tables in database and some migrations scripts in your workspace )
<h6> python manager.py db inint

python manager.py db migrate

python manager.py db upgrade </h6>

Now start your flask server <h6> python app.py <h6>

<h6> If all the above steps are working fine, go to postman and start using your API's </h6>


