### Build postgres image:
`docker build -t shop .`

### Run postgres container:
`docker run --name shop -d -p 5432:5432 shop`

### Run server: 
`python manage.py runserver`

