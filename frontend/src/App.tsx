import { useState, useEffect } from 'react';
import axios from 'axios';
import { Button, Card, CardContent, Typography, CircularProgress, Box, TextField } from '@mui/material';

import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  onAuthStateChanged,
  signOut,
 type User
} from 'firebase/auth';
import { auth } from './firebaseConfig'; // Import auth from your config

const API_URL = 'http://127.0.0.1:8000/api';

function App() {
  const [backendMessage, setBackendMessage] = useState('');
  const [backendLoading, setBackendLoading] = useState(true);
  const [backendError, setBackendError] = useState<string | null>(null);

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [user, setUser] = useState<User | null>(null);
  const [authError, setAuthError] = useState<string | null>(null);
  const [authLoading, setAuthLoading] = useState(true);

  // Inside your App.tsx component, e.g., in a new button's onClick handler
  const fetchProtectedData = async () => {
    if (!user) {
      setAuthError("You must be logged in to access protected data.");
      return;
    }
    setBackendLoading(true);
    setBackendError(null);
    try {
      // Get Firebase ID token
      const idToken = await user.getIdToken();
      const response = await axios.get(`${API_URL}/protected-data/`, {
        headers: {
          Authorization: `Bearer ${idToken}`
        }
      });
      setBackendMessage(response.data.message); // Display protected data message
    } catch (err: any) {
      if (err.response && err.response.status === 401) {
        setBackendError("Access Denied: You are not authorized to view this data.");
      } else {
        setBackendError("Failed to fetch protected data.");
      }
      console.error("Error fetching protected data:", err);
    } finally {
      setBackendLoading(false);
    }
  };

  // Effect for checking backend health
  const fetchHealthCheck = async () => {
    setBackendLoading(true);
    setBackendError(null);
    try {
      const response = await axios.get(`${API_URL}/health-check/`);
      setBackendMessage(response.data.message);
    } catch (err) {
      setBackendError('Failed to connect to the backend. Is the Django server running?');
      console.error(err);
    } finally {
      setBackendLoading(false);
    }
  };

  // Effect for Firebase Auth state changes
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      setUser(currentUser);
      setAuthLoading(false);
    });

    // Cleanup subscription on unmount
    return () => unsubscribe();
  }, []);

  // Initial backend health check when component mounts
  useEffect(() => {
    fetchHealthCheck();
  }, []);

  const handleSignUp = async () => {
    setAuthError(null);
    setAuthLoading(true);
    try {
      await createUserWithEmailAndPassword(auth, email, password);
      // User will be automatically set by onAuthStateChanged listener
    } catch (error: any) {
      setAuthError(error.message);
      console.error("Error signing up:", error);
    } finally {
      setAuthLoading(false);
    }
  };

  const handleSignIn = async () => {
    setAuthError(null);
    setAuthLoading(true);
    try {
      await signInWithEmailAndPassword(auth, email, password);
      // User will be automatically set by onAuthStateChanged listener
    } catch (error: any) {
      setAuthError(error.message);
      console.error("Error signing in:", error);
    } finally {
      setAuthLoading(false);
    }
  };

  const handleSignOut = async () => {
    setAuthError(null);
    setAuthLoading(true);
    try {
      await signOut(auth);
    } catch (error: any) {
      setAuthError(error.message);
      console.error("Error signing out:", error);
    } finally {
      setAuthLoading(false);
    }
  };

  return (
    <div className="container d-flex flex-column justify-content-center align-items-center vh-100 bg-light">
      <Card sx={{ minWidth: 275, maxWidth: 600, backgroundColor: '#f0f0f0', boxShadow: 3, marginBottom: 3 }}>
        <CardContent className="text-center p-4">
          <Typography variant="h4" component="div" sx={{ color: '#333', marginBottom: 2 }}>
            DailyToolbox Phase 1
          </Typography>
          <Typography sx={{ mb: 1.5, color: '#555' }}>
            Backend Connection Status
          </Typography>

          <Box sx={{ my: 3, p: 2, border: '1px dashed #ccc', borderRadius: '8px', minHeight: '80px', display: 'flex', alignItems: 'center', justifyContent: 'center', backgroundColor: '#fff' }}>
            {backendLoading ? (
              <CircularProgress color="primary" />
            ) : backendError ? (
              <Typography color="error" sx={{ color: '#d32f2f' }}>{backendError}</Typography>
            ) : (
              <Typography variant="h6" sx={{ color: '#28a745', fontWeight: 'bold' }}>
                {backendMessage}
              </Typography>
            )}
          </Box>

          <Button
            variant="contained"
            onClick={fetchHealthCheck}
            disabled={backendLoading}
            sx={{ backgroundColor: '#007bff', '&:hover': { backgroundColor: '#0056b3' } }}
          >
            Test Backend Connection
          </Button>

          {/* Add a button in your App component's return statement: */}
          {user && (
            <Button
              variant="contained"
              onClick={fetchProtectedData}
              disabled={backendLoading}
              sx={{ backgroundColor: '#28a745', '&:hover': { backgroundColor: '#218838' }, mt: 2 }}
            >
              Fetch Protected Data
            </Button>
          )}
        </CardContent>
      </Card>

      <Card sx={{ minWidth: 275, maxWidth: 600, backgroundColor: '#f0f0f0', boxShadow: 3 }}>
        <CardContent className="text-center p-4">
          <Typography variant="h5" component="div" sx={{ color: '#333', marginBottom: 2 }}>
            Firebase Authentication
          </Typography>

          {authLoading ? (
            <CircularProgress color="secondary" />
          ) : user ? (
            <Box>
              <Typography variant="h6" sx={{ color: '#28a745', mb: 1 }}>
                Logged In as: {user.email}
              </Typography>
              <Button
                variant="outlined"
                onClick={handleSignOut}
                sx={{ borderColor: '#dc3545', color: '#dc3545', '&:hover': { backgroundColor: '#dc35451a' } }}
              >
                Sign Out
              </Button>
            </Box>
          ) : (
            <Box className="d-flex flex-column gap-3">
              <TextField
                label="Email"
                variant="outlined"
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                fullWidth
                sx={{ mb: 2 }}
              />
              <TextField
                label="Password"
                variant="outlined"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                fullWidth
                sx={{ mb: 2 }}
              />
              {authError && (
                <Typography color="error" sx={{ mb: 2 }}>{authError}</Typography>
              )}
              <Button
                variant="contained"
                onClick={handleSignIn}
                disabled={authLoading || !email || !password}
                sx={{ backgroundColor: '#17a2b8', '&:hover': { backgroundColor: '#138496' }, mb: 1 }}
              >
                Sign In
              </Button>
              <Button
                variant="outlined"
                onClick={handleSignUp}
                disabled={authLoading || !email || !password}
                sx={{ borderColor: '#6c757d', color: '#6c757d', '&:hover': { backgroundColor: '#6c757d1a' } }}
              >
                Sign Up
              </Button>
            </Box>
          )}
        </CardContent>
      </Card>
    </div>
  );
}

export default App;