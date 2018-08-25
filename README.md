This is the read me thats pretty medicore

assuming you have all the right pip stuff installed in /server

do the following 
python create_db_info.py
python app.py
visit http://0.0.0.0:5000/graphql

enter the following in the graphql query view to see an example of the data
{
  allUsers{
    edges {
      node{
        name
        id
        email
        menus {
          edges{
            node
          		{
                name
                recipes{
                  edges{
                    node{
                      name
                      id
                      serves
                      ingredients{
                        edges {
                          node{
                            name
                            quantity
                            unit
                          }
                        }
                      }
                    }
                }
              }
          }
        }
      }
    }
  }
}
}

