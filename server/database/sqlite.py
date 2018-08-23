"""Module to allow connection and execution of sql to main db"""
import sqlite3


def execute_sql(sql, *params):
    """Main db execution function which allows arbitrary execution of sql
    SQL input format is a simple string
    params are the input into the SQL
    """
    connection = sqlite3.connect('./db/test.db')
    c = connection.cursor()
    c.execute(sql, params)
    connection.commit()
    connection.close()


def create_database():
    """Basic database creation function"""
    query = 'CREATE TABLE User (ID INTEGER PRIMARY KEY AUTOINCREMENT, Email TEXT, Password TEXT )'
    execute_sql(query)


def create_user(email, password):
    """Create a User with username and password"""
    query = 'INSERT INTO User (Email, Password) VALUES (?, ?)'
    execute_sql(query, email, password)



