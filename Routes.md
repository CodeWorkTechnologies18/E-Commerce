# Authentication (All public routes)

**Register -** `POST - http://127.0.0.1:8000/api/auth/register/`

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

**Login -** `POST - http://127.0.0.1:8000/api/auth/login/`

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


# Orders

**Get User Orders -** `GET 127.0.0.1:8000/orders/api/v1/get_orders/`

### Request
```
Only send access token, no body
```

### Response
```json
[
    {
        "id":1,
        "items":[
            {
                "product":2,
                "quantity":1
            },
            {
                "product":1,
                "quantity":1
            }
        ],
        "created_at":"2026-03-26T07:40:26.699439Z"
    }
]
```

**Get User Order by ID -** `GET 127.0.0.1:8000/orders/api/v1/get_order/{id:int}/`

### Request
```
Only send access token and order ID, no body
```

### Response
```json
{
    "id":2,
    "items":[
        {
            "product":3,
            "quantity":2
        }
        ],
    "created_at":"2026-03-26T08:12:24.396587Z"
}
```

**Create new order -** `POST 127.0.0.1:8000/orders/api/v1/create_order/`

### Request

- Also needs token

- Body

```json
{
    "items": [
    {
        "product": 2,
        "quantity": 3
    },
    {
        "product": 1,
        "quantity": 2
    },
    {
        "product": 3,
        "quantity": 2
    }
    ]
}
```

### Response

```json
{
    "id":3,
    "items": [
        {
            "product":2,
            "product_name":"Prod 2",
            "quantity": 3
        },
        {
            "product":1,
            "product_name":"Prod 1",
            "quantity":2
        },
        {
            "product":3,
            "product_name":"Prod 3",
            "quantity":2
        }
    ],
    "created_at":"2026-03-26T08:30:22.008135Z"}
```

