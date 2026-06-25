# Samstrack - Complete Attendance Management System

A full-stack student attendance management system with React frontend and Python Django backend.

## 🏗️ Project Structure

```
samstrack/
├── src/                        # React.js Frontend
│   ├── components/            # React Components
│   ├── App.jsx               # Main App Component
│   └── main.jsx              # Entry Point
├── backend/
│   └── python-api/           # Django REST API
│       └── attendance_project/
├── package.json
├── README.md
├── SAMSTRACK_API.postman_collection.json
└── PROJECT_README.md         # This file
```

## 🚀 Quick Start

### Frontend Setup
```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

### Backend Setup

```bash
cd backend/python-api/attendance_project
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8091
```

## 📋 Features

- **Admin Dashboard**: User & subject management, attendance reports
- **Faculty Portal**: Mark attendance, view records
- **Student Portal**: View personal attendance
- **Real-time Updates**: Live attendance tracking
- **Role-based Access**: Admin, Faculty, Student roles

## 🔧 Technology Stack

**Frontend:**
- React.js + Vite
- Tailwind CSS
- React Router

**Backend:**
- Python: Django REST Framework
- Database: SQLite

## 📡 API Endpoints

Import `SAMSTRACK_API.postman_collection.json` into Postman for complete API documentation.

**Base URL:** `http://localhost:8091`

### Key Endpoints:
- `POST /user/login-user/` - User authentication
- `GET /user/get-all-user/` - Get all users
- `POST /attendance/take-attendance/` - Mark attendance
- `GET /attendance/get-all-attendance-records/` - View records

## 🔐 Default Login

**Admin:**
- Username: admin
- Password: admin123

## 📖 Documentation

- [Frontend README](README.md) - React app setup & usage
- [Backend README](BACKEND_README.md) - API documentation
- [Postman Collection](SAMSTRACK_API.postman_collection.json) - API testing

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

## 📄 License

MIT License - see LICENSE file for details.