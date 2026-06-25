# Samstrack - Student Attendance Management System

A comprehensive web-based attendance management system built with React.js frontend and backend API integration.

## Features

### Admin Features
- **User Management**: Add, view, update, and delete users (Admin/Faculty)
- **Subject Management**: Add, edit, and delete subjects
- **Student Management**: Add and manage student records
- **Attendance Reports**: View comprehensive attendance reports with filters
- **Dashboard**: Admin overview with system statistics

### Faculty Features
- **Mark Attendance**: Take attendance for classes with date/time tracking
- **View Attendance**: View attendance records for their subjects
- **Profile Management**: Update personal profile information
- **Dashboard**: Faculty-specific dashboard

### Student Features
- **View Attendance**: Students can view their attendance records
- **Profile**: View and update profile information

## Technology Stack

- **Frontend**: React.js, Vite, Tailwind CSS
- **State Management**: React Hooks (useState, useEffect)
- **Routing**: React Router DOM
- **HTTP Client**: Fetch API
- **Styling**: Tailwind CSS with gradient backgrounds
- **Build Tool**: Vite

## Project Structure

```
samstrack-react/
├── public/
│   └── vite.svg
├── src/
│   ├── components/
│   │   ├── AddStudent.jsx
│   │   ├── AddUser.jsx
│   │   ├── AdminDashboard.jsx
│   │   ├── AdminMenu.jsx
│   │   ├── AllStudents.jsx
│   │   ├── AllSubject.jsx
│   │   ├── AllUser.jsx
│   │   ├── FacultyDashboard.jsx
│   │   ├── FacultyMenu.jsx
│   │   ├── Footer.jsx
│   │   ├── Login.jsx
│   │   ├── MarkAttendance.jsx
│   │   ├── Profile.jsx
│   │   ├── UpdateUser.jsx
│   │   ├── ViewAttendance.jsx
│   │   └── Welcome.jsx
│   ├── App.jsx
│   ├── App.css
│   ├── index.css
│   └── main.jsx
├── package.json
├── vite.config.js
└── README.md
```

## Installation & Setup

### Prerequisites
- Node.js (v16 or higher)
- npm or yarn
- Backend API server running on port 8091

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ketan-Rahane/Samstrack.git
   cd Samstrack/frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

4. **Open browser**
   Navigate to `http://localhost:5173`

## API Endpoints

The frontend communicates with backend API on `http://localhost:8091`

### User Management
- `POST /user/register-user/` - Register new user
- `POST /user/login-user/` - User login
- `GET /user/get-all-user/` - Get all users
- `GET /user/get-all-faculty/` - Get all faculty
- `PUT /user/update-user/` - Update user
- `DELETE /user/delete-user-by-username/` - Delete user

### Subject Management
- `GET /subject/get-all-subjects/` - Get all subjects
- `POST /subject/add-subject/` - Add new subject
- `PUT /subject/update-subject/` - Update subject
- `DELETE /subject/delete-subject/{id}/` - Delete subject

### Student Management
- `GET /student/get-all-students/` - Get all students
- `POST /student/add-student/` - Add new student

### Attendance Management
- `POST /attendance/take-attendance/` - Mark attendance
- `GET /attendance/get-all-attendance-records/` - Get all attendance
- `GET /attendance/get-attendance/{faculty}/{subject}/{date}` - Get filtered attendance

## User Roles

### Admin
- Full system access
- User management
- Subject management
- Student management
- View all attendance records

### Faculty
- Mark attendance for their classes
- View their attendance records
- Manage their profile

## Usage

### First Time Setup
1. Start the backend server
2. Create an admin user via registration
3. Login as admin
4. Add subjects and students
5. Create faculty users
6. Faculty can start marking attendance

### Daily Workflow
1. **Faculty Login** → **Mark Attendance** → Select subject, date, time → Mark present students → Submit
2. **View Reports** → Select filters → View attendance records → Click "Show Students" for details

## Build for Production

```bash
npm run build
```

The build files will be generated in the `dist/` directory.

## Environment Variables

Create a `.env` file in the root directory:

```env
VITE_API_BASE_URL=http://localhost:8091
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

## License

This project is licensed under the MIT License.

## Support

For support and queries, please contact the development team.