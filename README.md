# Dinner For Two

The backend server for the dinner for two application. The backend is written in python with graphql. The main libraries that the server is built off are:

## Setup
First you'll need to setup your local environment, with the dependencies. Using venv will help with this.

```
virtualenv venv

source venv/Scripts/activate
or
venv/bin/activate


pip install -r requirements.txt
```

### JWT Authentication
In order to have jwt authentication working with the application you'll need to setup a secret key that only the server knows in order to generate the tokens. The server will attempt to pull the secret key from the environment variable JWT_SECRET_KEY. A simple random key generation with can be done as followed.


Once you've got the following up and running you can then create a local db and run the application

```
python create_db_info.pu
python app.py
```

visit http://127.0.0.1:5000/graphql

From here you can query the server with graphql queries. A few simple examples are as follows

### All Users
```
{
  allUsers {
    edges {
      node {
        name
        email
        created
      }
    }
  }
}

```

### Add User
```
mutation {
  createUser(email: "someone@somewhere", password: "password123") {
    user {
      name
      created
      email
    }
    ok
    error
  }
}
```
