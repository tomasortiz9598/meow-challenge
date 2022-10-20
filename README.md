Run it: 

    Give read/write acces to fake_db files
    $python -m app


Test it:
    
Create customer:

    curl --location --request POST 'localhost:5000/customer' \ --header 'Content-Type: application/json' \ --data-raw '{"name": "tomas"}'

Create account:

    curl --location --request POST 'localhost:5000/account/f58bd061-ab45-4b20-86ce-2ecfdb3d8efc' \ --header 'Content-Type: application/json' \ --data-raw '{"money": 400}'

Transfer:

    curl --location --request POST 'localhost:5000/transfer' \ --header 'Content-Type: application/json' \ --data-raw '{"account_from": "fd06b265-219c-445f-85ac-e8373797a93a", "account_to": "b756fc8a-0bdc-4b7c-99f0-c8907af0b6c6", "amount": 500}'


Balances:

    curl --location --request GET 'localhost:5000/balances/fd06b265-219c-445f-85ac-e8373797a93a' \ --header 'Content-Type: application/json'

History:

    curl --location --request GET 'localhost:5000/history/fd06b265-219c-445f-85ac-e8373797a93a' \ --header 'Content-Type: application/json'


I didn't add any security at all in order to keep the scope smaller. 
But i would use some kind of session management

Possible changes:
-  
- Login endpoint that returns a sessionId and with that session ID, validate identity on other endpoints. That id could be stored on REDIS or MEMCACHE for a limited amount of time 
- Frontend 
- Classes for Customers, Accounts and Transfers. SQLAlchemy (Or any similar ORM) and a real SQL DB 
- Error handling for all endpoint 
- Unit and Integration tests
- Move Balances and History endpoints to another service. Given that they only read on DB and probably we could have different amount of traffic for this endpoints, it could be a good idea to move them to another service and assign different amount of resources
- Dockerize the application
- A good README

