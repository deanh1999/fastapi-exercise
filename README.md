# fastapi-exercise


## how to run:
- First add your OpenWeatherMap API Key to the .env file
- Next run docker build: docker build -t my-fastapi-app .
- Then start the docker container: docker run -d -p 80:80 --env-file .env my-fastapi-app
- Go to http://0.0.0.0/docs#/ to test the weather endpoint

## how to run unit tests: 
- run the command 'pytest'

## how to run, test script:
- start the server locally: uvicorn main:app --reload  
- Run: python test_api.py


## What to do next:
- CICD; Use github actions, create a file `.github/workflows/cicd.yml` on build add steps; lint, unit tests, docker build/push if deploying to azure
- Create a local database; install sqlite, create new directory, create weather data model, initialize db 
- Use infra as code: terraform? add a terraform directory and include your .tf files (main, provider, variables), in github actions could add steps(init, plan, apply)