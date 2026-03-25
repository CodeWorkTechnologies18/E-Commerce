# Authentication (All public routes)

**Register -** `POST http://127.0.0.1:8000/api/auth/register/`

### Request
```json
{
    "email": "sandycheeks@gmail.com",
    "username": "SandyCheeks",
    "first_name": "Sandy",
    "last_name": "Cheeks",
    "password": "admin@123"
}
```

### Response
```json
{
    "email": "sandycheeks@gmail.com",
    "username": "SandyCheeks",
    "first_name": "Sandy",
    "last_name": "Cheeks"
}
```

**Login -** `POST http://127.0.0.1:8000/api/auth/login/`

### Request

```json
{
    "email": "sandycheeks@gmail.com",
    "password": "admin@123"
}
```

### Response
```json
{
    "refresh":"eyJhbGciOiJIUzI1NiI...",
    "access":"eyJhbGciOiJIUzI1NiIsInR5cCI...",
    "user":{
        "id":2,
        "email":"sandycheeks@gmail.com",
        "username":"SandyCheeks","first_name":"Sandy",
        "last_name":"Cheeks",
        "is_active":true,
        "is_email_verified":false}
}
```

**User details -**
