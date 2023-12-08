# Flask-JWT-Extended

## JWT Authentication with Flask

### Description

This project demonstrates a simple implementation of JWT (JSON Web Token) authentication using Flask and Flask-JWT-Extended. It includes user authentication, token generation, and protected routes.

### Prerequisites

- Python 3.x
- Flask 3.0.0
- Flask-JWT-Extended 4.5.3
- Flask-SQLAlchemy
- Flask-Marshmallow
- MySQL database

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the MySQL database. Update the `app.config['SQLALCHEMY_DATABASE_URI']` in `app.py` with your database connection details.

4. Run the application:

    ```bash
    python app.py
    ```

### Configuration

- MySQL Database: Update the `app.config['SQLALCHEMY_DATABASE_URI']` in `app.py` with your database connection details.

- JWT Configuration: Update the `app.config["JWT_SECRET_KEY"]` in `app.py` with a secure secret key.

### Usage

1. **Login without Cookies:**

    ```bash
    POST /login_without_cookies
    ```

    Authenticate and receive a JWT token.

2. **Login with Cookies:**

    ```bash
    POST /login_with_cookies
    ```

    Authenticate and receive a JWT token, which is also stored in the cookies.

3. **Logout with Cookies:**

    ```bash
    POST /logout_with_cookies
    ```

    Log out and remove the JWT token from cookies.

4. **Protected Route:**

    ```bash
    GET /protected
    ```

    Access a protected route by providing a valid JWT token (can be in headers, cookies, JSON, or query string).

5. **Protected Route with Headers:**

    ```bash
    GET /only_headers
    ```

    Access a protected route by providing a valid JWT token only in headers.

### Models

- **Role Model:**

    - `id_rol`: Integer, primary key
    - `nombre_rol`: String(50)

- **User Model:**

    - `id`: Integer, primary key
    - `username`: Text, unique
    - `full_name`: String(50)
    - `password`: String(50)
    - `rol_id`: Integer, foreign key referencing `tblRol.id_rol`

### Schemas

- **Role Schema:**

    - `id_rol`
    - `nombre_rol`

- **User Schema:**

    - `id`
    - `username`
    - `full_name`
    - `password`
    - `rol_id`
    - `rol`

### Routes

- `/login_without_cookies`: Authenticate without storing the token in cookies.
- `/login_with_cookies`: Authenticate and store the token in cookies.
- `/logout_with_cookies`: Log out and remove the token from cookies.
- `/protected`: Access a protected route (token can be in headers, cookies, JSON, or query string).
- `/only_headers`: Access a protected route with the token only in headers.

### Additional Notes

- Ensure that your MySQL server is running and the database is created.

- Customize the JWT secret key and database URI according to your security requirements.

- This project is intended as a basic demonstration and may need further enhancements for a production environment.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
