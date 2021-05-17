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

- Currently there is a potential bug related to Django & Django REST Framework backend system. This won't affect user experience but could cause some trouble if someone really uses the webpage to add material data (which is seriously deprecated, you should use database tool to add new data to the backend database). See [Django DRF create new object with primary key "id: null" after axios post method - Stack Overflow](https://stackoverflow.com/questions/66947419/django-drf-create-new-object-with-primary-key-id-null-after-axios-post-method/66948240#66948240) for possible solutions or give your suggestions, thanks!

