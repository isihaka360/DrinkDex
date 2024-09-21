# DrinkDex 

Welcome to the Drink API! This API allows you to perform CRUD (Create, Read, Update, Delete) operations on drink data stored in a database. Each drink has attributes including the name of the drink, description, and price.

## Table of Contents

## About

The DrinkDex is a RESTful web service built using Django and Django REST Framework. It provides endpoints to manage drink data, allowing users to create, retrieve, update, and delete drinks.

## Features

- Create a new drink with name, description, and price.
- Retrieve details of all drinks or a specific drink.
- Update the details of an existing drink.
- Delete a drink from the database.

## Installation

To install and run the DrinkDex locally, follow these steps:

1. Clone the repository:
   $ git clone https://github.com/yourusername/drink-api.git
   $ cd drink-api

## Usage
Once the server is running, you can interact with the API using HTTP requests. You can use tools like cURL, Postman, or your web browser to send requests to the provided endpoints.

## DrinkDex API Endpoints
>> GET /drinks/: Retrieve a list of all drinks.
>> POST /drinks/: Create a new drink.
>> GET /drinks/<id>/: Retrieve details of a specific drink.
>> PUT /drinks/<id>/: Update details of a specific drink.
>> DELETE /drinks/<id>/: Delete a specific drink.

## Contributing
Contributions to the DrinkDex are welcome! If you would like to contribute, please follow these guidelines:

1. Fork the repository and create a new branch for your feature or bug fix.
2. Make your changes and ensure that the code passes any existing tests.
3. Write new tests to cover your changes if necessary.
4. Submit a pull request, explaining the purpose of your changes and any relevant details.
