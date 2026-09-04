# FastAPI Task Management System

fastapi  python  rest-api  jwt  postgresql  docker  clean-architecture . A comprehensive REST API application built with FastAPI for enterprise-level task management. This system provides secure user authentication, efficient database operations, and extensive testing coverage suitable for production environments.

## Overview

This application demonstrates modern Python web development practices using FastAPI framework, implementing industry-standard patterns for authentication, data validation, and API design. The system is architected for scalability and maintainability in professional development environments.

## Core Features

- **JWT Authentication System**: Secure token-based authentication with user registration and login capabilities
- **Task Management Operations**: Complete CRUD functionality for task creation, modification, and deletion
- **Database Integration**: SQLAlchemy ORM implementation with SQLite database (PostgreSQL production-ready)
- **Data Validation**: Comprehensive input validation using Pydantic models
- **API Documentation**: Auto-generated interactive documentation with Swagger UI
- **Testing Suite**: Extensive unit testing coverage using pytest framework
- **Error Handling**: Robust exception management with standardized error responses

## Technology Stack

- **FastAPI**: High-performance web framework for building APIs with Python 3.7+
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping library
- **Pydantic**: Data validation and settings management using Python type annotations
- **JWT**: JSON Web Tokens for stateless authentication
- **SQLite**: Embedded database for development (PostgreSQL/MySQL for production)
- **pytest**: Testing framework for comprehensive test coverage
- **uvicorn**: ASGI server implementation for production deployment

## Installation and Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/leonardolugi1218/fastapi-task-manager.git
cd fastapi-task-manager

# Install dependencies
pip install -r requirements-fixed.txt

# Start the development server
python -m uvicorn app.main:app --reload
```

### Access Points
- API Base URL: http://127.0.0.1:8000
- Interactive Documentation: http://127.0.0.1:8000/docs
- Alternative Documentation: http://127.0.0.1:8000/redoc

## API Endpoints

### Authentication
- `POST /auth/register` - User registration with email and password
- `POST /auth/login` - User authentication and JWT token generation

### Task Management
- `GET /tasks/` - Retrieve all tasks for authenticated user
- `POST /tasks/` - Create new task with title, description, and priority
- `GET /tasks/{task_id}` - Retrieve specific task by ID
- `PUT /tasks/{task_id}` - Update existing task information
- `DELETE /tasks/{task_id}` - Remove task from system

### User Profile
- `GET /users/me` - Retrieve current user profile information

## Testing

Execute the test suite to verify functionality:

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=app

# Run specific test file
pytest tests/test_auth.py
```

## Project Structure

```
fastapi-task-manager/
├── app/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── auth.py              # Authentication utilities
│   └── routes/
│       ├── auth.py          # Authentication endpoints
│       ├── tasks.py         # Task management endpoints
│       └── users.py         # User profile endpoints
├── tests/
│   ├── __init__.py
│   ├── test_auth.py         # Authentication tests
│   ├── test_tasks.py        # Task management tests
│   └── test_users.py        # User profile tests
├── requirements-fixed.txt   # Project dependencies
└── README.md
```

## Configuration

Create a `.env` file for environment-specific settings:

```env
DATABASE_URL=sqlite:///./tasks.db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Security Implementation

- Password hashing using bcrypt algorithm
- JWT tokens with configurable expiration
- Input validation preventing injection attacks
- CORS middleware for cross-origin request handling
- Rate limiting for API endpoint protection

## Development Features

- Hot reload development server
- Comprehensive error logging
- Request/response validation
- Database migration support
- Automated API documentation generation

## Production Deployment

### Docker Deployment
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements-fixed.txt .
RUN pip install -r requirements-fixed.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Cloud Platform Deployment
```bash
# For Heroku deployment
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

## Contributing

This project follows standard software development practices:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Open Pull Request

## License

This project is licensed under the MIT License. See LICENSE file for details.

## Author

**Leonardo Luigi**
- GitHub: [@leonardolugi1218](https://github.com/leonardolugi1218)
- Email: Contact through GitHub profile

## Additional Information

This application serves as a demonstration of modern Python web development practices and can be extended for enterprise use cases. The codebase emphasizes clean architecture, comprehensive testing, and production-ready deployment configurations.
