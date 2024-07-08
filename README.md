# Stratiphy-App

Stratiphy-App is a Django-based application designed to manage stock portfolios.

## Installation and Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/stratiphy-app.git
    cd stratiphy-app
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Collect static files**:
    ```bash
    python manage.py collectstatic
    ```

## Dockerizing the Project

**Run Docker Compose**:
    ```bash
    sudo docker-compose up --build
    ```

## Running the Project

Access the application at `http://127.0.0.1:8000`.

## Admin and User Accounts

### Creating an Admin Account

To access the Django admin panel, go to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials created earlier. If you need to create another admin account, follow these steps:

1. **Access the admin panel**:
    Go to `http://127.0.0.1:8000/admin/`.

2. **Log in with the superuser credentials**.

3. **Navigate to the Users section** and add a new user.

4. **Set the new user's permissions**:
    - Check the "Staff status" box to grant admin access.
    - Assign the user to the appropriate groups.

### Creating a User Account

Users can register through the API or the Django admin panel:

1. **Through the API**:
    Send a POST request to `/api/register/` with the following payload:
    ```json
    {
        "username": "newusername",
        "password": "newpassword"
    }
    ```

2. **Through the Django Admin Panel**:
    - Go to `http://127.0.0.1:8000/admin/`.
    - Log in with superuser credentials.
    - Navigate to the Users section and add a new user.

## Authentication

The application uses JWT (JSON Web Token) for authentication.

1. **Obtain a token**:
    Send a POST request to `/api/token/` with the following payload:
    ```json
    {
        "username": "yourusername",
        "password": "yourpassword"
    }
    ```
    You will receive an access token and a refresh token.

2. **Use the access token**:
    Include the access token in the Authorization header for subsequent requests:
    ```http
    Authorization: Bearer <your-access-token>
    ```

## API Usage

### Stock Endpoints
- **List Stocks**: `GET /api/stocks/`
- **Retrieve Stock**: `GET /api/stocks/<id>/`
- **Search Stocks**: `GET /api/stocks/?search=<query>`

### Holding Endpoints
- **View Holdings**: `GET /api/holdings/`
- **Buy/Sell Stock**: `POST /api/stocks/buy-sell/`

For example, this would let user 1 buy 10 stocks of stock 1. 

curl -X POST http://127.0.0.1:8000/api/stocks/buy-sell/ \
-H "Authorization: Bearer <your-access-token>" \
-H "Content-Type: application/json" \
-d '{
  "user": 1,
  "stock": 1,
  "transaction_type": "BUY",
  "quantity": 10
}'

For example, this would add New Stock to the DB of value 100.50. 

curl -X POST http://127.0.0.1:8000/api/stocks/ \
-H "Authorization: Bearer <your-access-token>" \
-H "Content-Type: application/json" \
-d '{
  "name": "New Stock",
  "symbol": "NEWSTK",
  "price": 100.50
}'


