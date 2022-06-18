# machine_learning_project_test1
This is machine_learning_project_test1

## Software required

1. [Github Account](https://github.com/)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT documentation](https://git-scm.com/docs/gittutorial)

## Create virtual envirment

> virtualenv --version

> virtualenv venv

> venv\Scripts\activate

## Create requirement.txt

> pip install -r requirements.txt

## Write flask code
'''
app.py

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return '<h1>Hello Flask</h1>'

if __name__ == '__main__':
    app.run(debug=True)

'''

## To create CI/CD pipeline with heroku we need 3 things:

1. EMAIL_ID : mungekarkiran05@gmail.com
2. HEROKU_API_KEY : <HEROKU_API_KEY>
3. HEROKU_APP_NAME : ml-cicd-pipeline

## Create a enpty **Dockerfile**
'''
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
'''

## Create a enpty **.dockerignore**
'''
venv/
.git
.gitignore
'''

## BUILD DOCKER IMAGE

> docker build -t <image_name>:<tagname> .

'''Note: Image name for docker must be lowercase'''

## To list docker image

> docker images

## Run docker image

> docker run -p 5000:5000 -e PORT=5000 <container_id>

## To check running container in docker

> docker ps

## To stop docker conatiner

> docker stop <container_id>



## 18062022

python .\setup.py install

pip install -e .