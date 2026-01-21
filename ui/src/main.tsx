import React from 'react'
import ReactDOM from 'react-dom/client'
import { Provider } from 'react-redux'
import axios from 'axios';
import { authService } from './services/auth';
import './styles/index.css'
import App from './App.tsx'
import { store } from './store/index.ts'

// Configure axios
axios.defaults.baseURL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

// Initialize Axios interceptors for authentication
authService.initiateAuthInterceptor();

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
)
