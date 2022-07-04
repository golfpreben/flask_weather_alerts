# flask_weather_alerts
Simple flask app to setup weather alerts. SqlLite is used for persistence.

## To get started (linux only):
- make sure you have pipenv installed and do 
"pipenv install" and "pipenv shell"
- run ./entry_point.sh
- open browser and go to http://0.0.0.0:5000/api/ to find swagger interface
- alerts are persisted and checked when posting to the alerts endpoint