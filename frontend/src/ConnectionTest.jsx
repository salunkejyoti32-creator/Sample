import { useState } from "react";

function ConnectionTest() {
  const [results, setResults] = useState([]);
  const [testing, setTesting] = useState(false);

  const addResult = (message, status) => {
    setResults(prev => [...prev, { message, status, time: new Date().toLocaleTimeString() }]);
  };

  const testAllConnections = async () => {
    setTesting(true);
    setResults([]);
    
    // Test 1: Basic server connection
    addResult("Testing basic server connection...", "info");
    try {
      const response = await fetch("http://localhost:8091");
      if (response.ok) {
        addResult("✅ Backend server is running on port 8091", "success");
      } else {
        addResult(`❌ Server responded with status: ${response.status}`, "error");
      }
    } catch (err) {
      addResult(`❌ Cannot connect to backend: ${err.message}`, "error");
    }

    // Test 2: Login endpoint
    addResult("Testing login endpoint...", "info");
    try {
      const response = await fetch("http://localhost:8091/user/login-user", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: "test", password: "test" }),
      });
      addResult(`Login endpoint status: ${response.status}`, response.ok ? "success" : "warning");
    } catch (err) {
      addResult(`❌ Login endpoint error: ${err.message}`, "error");
    }

    // Test 3: Register endpoint
    addResult("Testing register endpoint...", "info");
    try {
      const response = await fetch("http://localhost:8091/user/register-user/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          username: "test", 
          password: "test",
          email: "test@test.com",
          role: "admin",
          firstName: "Test",
          lastName: "User"
        }),
      });
      addResult(`Register endpoint status: ${response.status}`, response.ok ? "success" : "warning");
    } catch (err) {
      addResult(`❌ Register endpoint error: ${err.message}`, "error");
    }

    // Test 4: Alternative ports
    const ports = [8080, 3000, 5000, 9090];
    for (const port of ports) {
      try {
        const response = await fetch(`http://localhost:${port}`);
        if (response.ok) {
          addResult(`✅ Found server running on port ${port}`, "success");
        }
      } catch {
        addResult(`❌ No server on port ${port}`, "error");
      }
    }

    setTesting(false);
  };

  return (
    <div className="p-4 bg-white border rounded-lg shadow-lg mb-4">
      <h3 className="text-lg font-bold mb-4">Backend Connection Test</h3>
      
      <button 
        onClick={testAllConnections}
        className="bg-blue-500 text-white px-4 py-2 rounded mb-4"
        disabled={testing}
      >
        {testing ? "Testing..." : "Test Backend Connection"}
      </button>

      <div className="max-h-60 overflow-y-auto">
        {results.map((result, index) => (
          <div 
            key={index} 
            className={`p-2 mb-2 rounded text-sm ${
              result.status === 'success' ? 'bg-green-100 text-green-800' :
              result.status === 'error' ? 'bg-red-100 text-red-800' :
              result.status === 'warning' ? 'bg-yellow-100 text-yellow-800' :
              'bg-blue-100 text-blue-800'
            }`}
          >
            <span className="text-xs text-gray-500">[{result.time}]</span> {result.message}
          </div>
        ))}
      </div>

      {results.length > 0 && (
        <div className="mt-4 p-3 bg-gray-100 rounded">
          <h4 className="font-semibold mb-2">Quick Diagnosis:</h4>
          {results.some(r => r.message.includes("✅ Backend server is running")) ? (
            <p className="text-green-600">✅ Backend is connected and running properly</p>
          ) : results.some(r => r.message.includes("Found server running on port")) ? (
            <p className="text-yellow-600">⚠️ Backend is running on different port. Update your API URLs.</p>
          ) : (
            <p className="text-red-600">❌ Backend is not running. Start your backend server first.</p>
          )}
        </div>
      )}
    </div>
  );
}

export default ConnectionTest;