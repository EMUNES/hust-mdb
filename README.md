# HUST material cloud database

This repo holds the demo for HUST material cloud database, based on Django3, Vue3 and tailwind css.

## Prepare the environment

To run the website, you should download the project source code, and prepare the environment for both frontend and backend:

- Download the repo source code and unzip it, you should see *frontend* and *backend* folder under the project root folder.
- For frontend: First run `cd frontend`; then run `npm install`.
- For backend: Back to the project root folder, first run `cd backend`; then run `python install -r requirements.txt`.

Now you should be set with the environment containing all dependencies.

## Run the website.

As you should be prepared by now, running the website is an easy task:

- Back to the root folder: First run `cd backend`; then run `python manage.py runserver`.
- Back to the root folder: First run `cd frontend`; then run `npm run dev`.

You can check the frontend logging console to see the address of this website. By default, it's at *http://127.0.0.1:3000*

## Dealing with authentication

If you don't have an account to login, you can create your own superuser using the backend terminal or contact the author for default account. 

## Important notices for potential bugs and breakdowns

- An local database mutation (hell know where from) will break the token authentication for the project, causing users unable to login no matter in frontend or backend. To avoid such "accidents" happen again and disable the login system, **always test login functionality before you push your code to github especially when git shows that your local sqlite3 database file is *modified***. --- 2021.4.18.


