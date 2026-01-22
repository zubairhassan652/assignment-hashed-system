### Run project
Run project using:

 `docker-compose up`


### Run migrations
Run migrations using below commands `change container name` if you have different one.
```
docker exec -it assignment-hashed-system-web-1 python manage.py migrate_schemas --shared

docker exec -it assignment-hashed-system-web-1 python manage.py migrate_schemas --tenant
```

### Make tenant for localhost
Make tenant for localhost using shell commands

```
docker exec -it assignment-hashed-system-web-1 python manage.py shell
```

```
from tenants.models import Tenant, Domain 


# 1. Create the Public Tenant
# The schema_name MUST be 'public'
tenant = Tenant(schema_name='public', name='Public Tenant')
tenant.save()

# 2. Link the domain to the tenant
# For local development, this is 'localhost'
Domain.objects.create(
    domain='localhost', 
    tenant=tenant, 
    is_primary=True
)

exit()
```

### Create superuser
Create super user using below command
```
docker exec -it assignment-hashed-system-web-1 python manage.py createsuperuser
```
Follow the instructions.

### Visit admin
`http://localhost:8000/admin/`

### Create tenants
```
schema: shope_one
name: Shop One

```
Repeate this to create multiple tenants

### Create Domains
```
domain: shop1.localhost
tenant: shope_one
```
Repeate this to create multiple domains for tenants

### Visit tenants domains
```
http://shop1.localhost:8000/admin/
http://shop2.localhost:8000/admin/
...
```
Create objects of projects and subscriptions in different tenant domains and visit these objects accordingly like below.

```
http://shop1.localhost:8000/api/projects/
http://shop2.localhost:8000/api/projects/
...
```
Here you will see the tenants only data.
