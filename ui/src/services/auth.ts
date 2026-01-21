import axios from 'axios';

const ACCESS_TOKEN_KEY = 'access_token';
const REFRESH_TOKEN_KEY = 'refresh_token';

export const authService = {
  login: async (email: string, password: string) => {
    const response = await axios.post('/auth/login', { email, password });
    const { access_token, refresh_token } = response.data;
    localStorage.setItem(ACCESS_TOKEN_KEY, access_token);
    localStorage.setItem(REFRESH_TOKEN_KEY, refresh_token);
    return response.data;
  },

  logout: () => {
    localStorage.removeItem(ACCESS_TOKEN_KEY);
    localStorage.removeItem(REFRESH_TOKEN_KEY);
    // Optionally, call a backend endpoint to invalidate the refresh token
  },

  getAccessToken: (): string | null => {
    return localStorage.getItem(ACCESS_TOKEN_KEY);
  },

  getRefreshToken: (): string | null => {
    return localStorage.getItem(REFRESH_TOKEN_KEY);
  },

  setAccessToken: (token: string) => {
    localStorage.setItem(ACCESS_TOKEN_KEY, token);
  },

  refreshAccessToken: async (): Promise<string> => {
    const refreshToken = authService.getRefreshToken();
    if (!refreshToken) {
      throw new Error('No refresh token available');
    }
    try {
      const response = await axios.post('/auth/refresh', { refresh_token: refreshToken });
      const newAccessToken = response.data.access_token;
      authService.setAccessToken(newAccessToken);
      return newAccessToken;
    } catch (error) {
      authService.logout(); // Clear tokens on refresh failure
      throw error;
    }
  },

  initiateAuthInterceptor: () => {
    axios.interceptors.request.use(
      (config) => {
        const token = authService.getAccessToken();
        if (token) {
          config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
      },
      (error) => {
        return Promise.reject(error);
      }
    );

    axios.interceptors.response.use(
      (response) => {
        return response;
      },
      async (error) => {
        const originalRequest = error.config;
        // If the error is 401 Unauthorized and it's not the refresh request itself
        if (error.response?.status === 401 && !originalRequest._retry) {
          originalRequest._retry = true;
          try {
            const newAccessToken = await authService.refreshAccessToken();
            originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
            return axios(originalRequest);
          } catch (refreshError) {
            // If refresh fails, log out the user
            window.location.href = '/#/login'; // Redirect to login page
            return Promise.reject(refreshError);
          }
        }
        return Promise.reject(error);
      }
    );
  },
};
