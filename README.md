# TodoApi
## Install the API

### Install manually

To install it, just clone the repository and run the following command:

pip install -r <TODOAPI_REPOSITORY>/requirements.txt

## Run the server
To run the server simply use: python3 manage.py runserver
 
## jwt authentication
Start postman create a new request for http://127.0.0.1:8000/api/signin Select method as Post, goto body and select raw and the JSON.
In body enter the JSON in the following format and hit the request

{
 "email":"ram@gmail.com",<br>
 "password":"123456",
}

The response should look like this

{
"success": "True",<br>
"status code": 200,<br>
"message": "User logged in  successfully",<br>
"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiODY3Y2E3YjAtZDhjNC00ZTdkLWE1NmYtOWRhYWJkOTAwNmQ1IiwidXNlcm5hbWUiOiJyYW1AZ21haWwuY29tIiwiZXhwIjoxNTgwMTA0MDc4LCJlbWFpbCI6InJhbUBnbWFpbC5jb20ifQ.0cCgOlKrYHrouVJEeIEt6TdGyza2C78J5swXFEaLLFM"
}<br>

to authenticate go to Authorization and select Bearer Token from TYPE, paste the token.
