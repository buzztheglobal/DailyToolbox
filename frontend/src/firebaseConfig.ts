// Import the functions you need from the SDKs you need

import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore'; // Import Firestore

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional

const firebaseConfig = {
  apiKey: "AIzaSyD4OLp3L4N7ZUnGt6g7J6kiHOD-QDjMz_Q",
  authDomain: "dailytoolbox-5d842.firebaseapp.com",
  projectId: "dailytoolbox-5d842",
  storageBucket: "dailytoolbox-5d842.firebasestorage.app",
  messagingSenderId: "391083117371",
  appId: "1:391083117371:web:e259f8c7e09a01ae6a451e",
  measurementId: "G-B6T97GV0Q7"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app); // Initialize Firestore

export { auth, db };
