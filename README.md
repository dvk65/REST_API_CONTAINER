The repository contains python files inside the api directory. </br>
The rest_api.py file has the REST API calls with status codes while the test_api.py file has tests to assert this behavior. </br>
To run these files the following steps can be followed:</br>
  - clone the repository
  - cd into the project directory
  - to start running the Flask app "python ./api/rest_api.py"
  - to test the endpoints "python ./api/test_api.py" </br>

The Dockerfile contains code to run the Flask api till it is manually stopped:
  - to build the docker image "docker build -t rest-api-app ."
  - to run the image "docker run -p 5000:5000 rest-api-app" </br>

The Dockerfile.test contains code to test the endpoints of Flask api:
  - to build the docker image "docker build -f Dockerfile.test -t rest-api-app-test ."
  - to run the image "docker run --rm rest-api-app-test"</br>

There is a workflow setup that can be triggered on push and pull requests on the main branch as well as manually.
