# Samstrack Backend - Student Attendance Management System API

Backend API server for the Samstrack attendance management system.

## Technology Stack

- **Framework**: Spring Boot / Django / Node.js (based on your implementation)
- **Database**: MySQL / PostgreSQL / MongoDB
- **Authentication**: JWT / Session-based
- **API**: RESTful API
- **Port**: 8091

## API Documentation

### Base URL
```
http://localhost:8091
```

## Authentication Endpoints

### User Registration
```http
POST /user/register-user/
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123",
  "email": "admin@example.com",
  "role": "admin",
  "firstName": "Admin",
  "lastName": "User"
}
```

### User Login
```http
POST /user/login-user/
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123"
}
```

**Response:**
```json
{
  "username": "admin",
  "role": "admin"
}
```

## User Management Endpoints

### Get All Users
```http
GET /user/get-all-user/
```

### Get All Faculty
```http
GET /user/get-all-faculty/
```

### Get User by Username
```http
GET /user/get-user-by-username/{username}/
```

### Update User
```http
PUT /user/update-user/
Content-Type: application/json

{
  "username": "admin",
  "password": "newpassword",
  "firstName": "Updated",
  "lastName": "Name",
  "email": "updated@example.com",
  "role": "admin"
}
```

### Delete User
```http
DELETE /user/delete-user-by-username/?username={username}
```

## Subject Management Endpoints

### Get All Subjects
```http
GET /subject/get-all-subjects/
```

### Add Subject
```http
POST /subject/add-subject/
Content-Type: application/json

{
  "name": "Mathematics"
}
```

### Update Subject
```http
PUT /subject/update-subject/
Content-Type: application/json

{
  "id": 1,
  "name": "Advanced Mathematics"
}
```

### Delete Subject
```http
DELETE /subject/delete-subject/{id}/
```

## Student Management Endpoints

### Get All Students
```http
GET /student/get-all-students/
```

### Add Student
```http
POST /student/add-student/
Content-Type: application/json

{
  "id": "STU001",
  "name": "John Doe",
  "email": "john@example.com",
  "course": "Computer Science"
}
```

## Attendance Management Endpoints

### Mark Attendance
```http
POST /attendance/take-attendance/
Content-Type: application/json

{
  "username": "faculty1",
  "subjectId": 1,
  "date": "2024-01-15",
  "time": "10:00",
  "students": [
    {"id": "STU001"},
    {"id": "STU002"}
  ]
}
```

### Get All Attendance Records
```http
GET /attendance/get-all-attendance-records/
```

### Get Filtered Attendance
```http
GET /attendance/get-attendance/{faculty}/{subjectId}/{date}
```

**Example:**
```http
GET /attendance/get-attendance/faculty1/1/2024-01-15
```

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    role ENUM('admin', 'faculty') NOT NULL
);
```

### Subjects Table
```sql
CREATE TABLE subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);
```

### Students Table
```sql
CREATE TABLE students (
    id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    course VARCHAR(50)
);
```

### Attendance Table
```sql
CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    subject_id INT,
    date DATE,
    time TIME,
    number_of_students INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (username) REFERENCES users(username),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);
```

### Attendance Students Table
```sql
CREATE TABLE attendance_students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    attendance_id INT,
    student_id VARCHAR(20),
    FOREIGN KEY (attendance_id) REFERENCES attendance(id),
    FOREIGN KEY (student_id) REFERENCES students(id)
);
```

## Installation & Setup

### Prerequisites
- Java 11+ (for Spring Boot) / Python 3.8+ (for Django) / Node.js 16+ (for Express)
- MySQL / PostgreSQL database
- Maven / Gradle (for Java) / pip (for Python) / npm (for Node.js)

### Database Setup
1. Create database named `samstrack`
2. Run migration scripts or create tables manually
3. Update database connection settings

### Configuration
Update `application.properties` (Spring Boot) or equivalent config file:

```properties
# Database Configuration
spring.datasource.url=jdbc:mysql://localhost:3306/samstrack
spring.datasource.username=root
spring.datasource.password=password

# Server Configuration
server.port=8091

# CORS Configuration
cors.allowed.origins=http://localhost:5173
```

### Running the Server

**Spring Boot:**
```bash
mvn spring-boot:run
```

**Django:**
```bash
python manage.py runserver 0.0.0.0:8091
```

**Node.js:**
```bash
npm start
```

## Error Handling

### Common HTTP Status Codes
- `200 OK` - Success
- `201 Created` - Resource created successfully
- `400 Bad Request` - Invalid request data
- `401 Unauthorized` - Authentication required
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

### Error Response Format
```json
{
  "error": "Error message",
  "status": 400,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

## Security Features

- Password hashing
- Input validation
- SQL injection prevention
- CORS configuration
- Authentication middleware

## Testing

### API Testing with Postman
1. Import the provided Postman collection
2. Set environment variables
3. Test all endpoints

### Unit Tests
```bash
# Spring Boot
mvn test

# Django
python manage.py test

# Node.js
npm test
```

## Deployment

### Production Configuration
- Use environment variables for sensitive data
- Enable HTTPS
- Configure production database
- Set up logging
- Configure CORS for production frontend URL

### Docker Deployment
```dockerfile
FROM openjdk:11-jre-slim
COPY target/samstrack-backend.jar app.jar
EXPOSE 8091
ENTRYPOINT ["java", "-jar", "/app.jar"]
```

## Monitoring & Logging

- Application logs
- Database query logs
- API request/response logs
- Error tracking

## Contributing

1. Follow coding standards
2. Write unit tests
3. Update API documentation
4. Test all endpoints before committing

## License

This project is licensed under the MIT License.