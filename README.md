# crud_app (Recipes)
Recipes is a CRUD app, built using Python, HTML, CSS and SQL. It allows user to browse recipes that other users have added. Includes sign up/ log in functionality. Users can Create, Read, Update or Delete their recipes from app.

## :computer: [Click here](https://www.google.com) to see my live project!
## :page_facing_up: About

![project.png]
![project.png]
![project.png]
![project.png]
![project.png]
## :pencil2: Planning & Problem Solving
![project.png](https://github.com/sadiausmann/crud_app/blob/main/crud_app_wireframe.png)
![project.png](https://github.com/sadiausmann/crud_app/blob/main/app_planning_db_tables.png)

LOGIC:
If user is not logged in:
-Display all recipes.
-Browser shows the option of Log in and Sign up.
-User can click on individual recipe and it takes to recipe page.
-They can’t like or comment but they can read comments.

If user sign up and is logged in:
-Display all the recipe and log out button.
-User can click on individual recipe and it takes to recipe page.
    -Display all the comments. Logged in users can like and comment on recipes. 
	-If user is the owner of the recipe:
		User can Edit and Delete the recipe. 
	Else:
		Can only like and comment on a recipe.


Pages:
-Home page
-Individual recipe page
-Edit recipe page
-Add a new recipe 
-User login 
-User Sign up page



![project.png]
## :rocket: Cool tech
In my project, I utilized the following technologies and tools to achieve the desired outcome:

- Flask: I utilized the Flask web framework to develop a web application with Python. 
- Python: I used Python, a popular high-level programming language, to write the backend code for my web application.
- Bcrypt: I utilized Bcrypt, a password-hashing function, for password storage and authentication. Bcrypt is a widely-used encryption algorithm that is known for its strength and security.
- CSS and HTML: I used CSS and HTML to create the frontend of my web application. CSS enabled me to style the web pages, while HTML allowed me to structure the content and create a responsive layout.
- Psycopg2: I used Psycopg2, a PostgreSQL adapter for the Python programming language, to connect to my PostgreSQL database. 
- SQL: I used SQL, a standard language for managing and manipulating data stored in relational databases, to interact with my PostgreSQL database. SQL enabled me to create tables, insert data, and execute queries to retrieve data as needed.


## :scream: Bugs to fix :poop:
- My application is not responsive to different screen sizes, which means that the layout and design of the application do not adjust to fit the screen size of the user's device. This can result in a poor user experience and may make the application difficult to use on devices with smaller screens. To address this issue, I plan to implement a responsive design that will ensure the application is optimized for use on any device, regardless of the screen size.  

## :sob: Lessons learnt
Stick to a plan. I was jumping between ideas and have put in lot of time in changing code and fixing it.

## :white_check_mark: Future features
- Add categories to recipes.
- Make a shopping list with the ingredients required for recipes selected by user.
- Search recipes by dietry requirements.
- User be able to upload pictures.
