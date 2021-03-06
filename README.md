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
### CORS issue
ensure your pip install is up to date. 
then add to your .env file
```
#the following will allow it to accept all incomming connections, this should be changed for production.
DOMAIN=* 
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

### Add Menu
```
mutation {
	addMenu(name: "menu2", userID: 1, token: "sometoken") {
		ok
		error
		menu {
			name
			created
		}
	}
}
```


### Add Recipe
```
mutation {
	addRecipe(input: {
		name: "Beef Stew",
		menuId: 4,
		method: "Cook the stew then eat it",
		time: "1 hour",
		serves: 2,
		equipment: "Big pot",
		comments: "The beef is good",
		ingredients: [{
			name: "Beef",
			quantity: 1.0,
			unit: "kg"
		}, {
			name: "Potato",
			quantity: 500,
			unit: "grams"
		}, {
			name: "Stock",
			quantity: 1,
			unit: "Litre"
		}]
	}) {
		ok
		recipe {
			id
			name
			createdOn
			method
			time
			ingredients {
				edges {
					node {
						name
						quantity
						unit
					}
				}
			}
		}
	}
}
```
