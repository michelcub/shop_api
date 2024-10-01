### Build postgres image:
`podman build -t shop .`

### Run postgres container:
`podman run --name shop -d -p 5432:5432 shop`

### Run server: 
`python manage.py runserver`

