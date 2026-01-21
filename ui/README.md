# React Stable Starter

A production-ready, beginner-friendly starter repository for building blank websites with React, Tailwind CSS, and TypeScript. Designed for maximum compatibility, minimal install errors, and clean software engineering practices.

## What This Is

This starter provides a blank canvas for React applications, pre-configured with:
- React 18.2.0 with Vite 5.0.12 for fast development
- TypeScript for type-safety
- Tailwind CSS 3.4.1 for utility-first styling
- Redux Toolkit & React Redux for state management
- Essential libraries like React Router, Axios, and clsx

It's perfect for beginners who want to start coding immediately without wrestling with setup issues, and for experienced developers who need a reliable, stable foundation.

## Why This Starter?

- **Zero Peer Dependency Conflicts**: All packages are pinned to stable, compatible versions
- **No Experimental Features**: Uses proven, widely-supported technologies
- **Easy Cloning**: Works out of the box with minimal setup
- **Beginner-Proof**: Clear documentation and structure
- **Professional Quality**: Follows software engineering best practices

## System Requirements

- Node.js 18.x (LTS)
- npm 9.x or later

## Installation Guide

Follow these steps to set up your new project:

```bash
# Clone the repository
git clone https://github.com/Danncode10/Web-Starter-React.git ui

# Navigate to the project directory
cd my-project

# Remove the git history to start fresh
rm -rf .git

# Install dependencies
npm install

# Start the development server
npm run dev
```

**Why `rm -rf .git`?** This removes the starter's git history, allowing you to initialize a fresh repository for your own project.

## Available Scripts

```bash
npm run dev      # Start development server
npm run build    # Build for production
npm run preview  # Preview production build
```

## Troubleshooting

If installation fails:

1. Delete `node_modules` directory
2. Delete `package-lock.json`
3. Run `npm install` again

**Important Notes:**
- Do not mix npm with yarn or pnpm
- Ensure you have the correct Node.js version (18.x)
- Check that npm is updated to version 9.x or later

## Design Philosophy

### Version Stability
All package versions are pinned to specific, stable releases to prevent unexpected breaking changes. This ensures the starter remains reliable over time.

### No ESLint Included
ESLint is excluded to avoid configuration complexity for beginners. You can add it later when your project matures.

### Stability Over Features
This starter prioritizes compatibility and reliability over cutting-edge features. It's built with proven technologies that work consistently across different environments.

## Project Structure

```
react-stable-starter/
├─ src/
│  ├─ components/
│  │  ├─ ExampleButton.tsx    # Reusable button component
│  │  └─ ReduxCounter.tsx     # Demo component using Redux state
│  ├─ pages/
│  │  └─ Home.tsx             # Home page component
│  ├─ layouts/
│  │  └─ MainLayout.tsx       # Main layout wrapper
│  ├─ store/
│  │  ├─ index.ts             # Main Redux store configuration
│  │  └─ slices/
│  │     └─ counterSlice.ts   # Example Redux slice (counter)
│  ├─ styles/
│  │  └─ index.css            # Global styles with Tailwind
│  ├─ App.tsx                 # Main app component
│  └─ main.tsx                # Entry point with Redux Provider
├─ public/                    # Static assets
├─ .env.example               # Environment variables template
├─ .gitignore                 # Git ignore rules
├─ .nvmrc                     # Node version specification
├─ package.json               # Dependencies and scripts
├─ requirements.txt           # System requirements
├─ tailwind.config.js         # Tailwind configuration
├─ postcss.config.js          # PostCSS configuration
├─ vite.config.js             # Vite configuration
└─ index.html                 # HTML template
```

## Environment Variables

Copy `.env.example` to `.env` and update the values:

```bash
cp .env.example .env
```

Available variables:
- `VITE_APP_NAME`: Your application name
- `VITE_API_BASE_URL`: API base URL for development

## Getting Started with Development

1. **Add New Pages**: Create components in `src/pages/` and add routes in `src/App.tsx`
2. **Create Components**: Use `src/components/` for reusable UI elements
3. **Styling**: Primarily use Tailwind CSS for styling.
4. **API Calls**: Use Axios for HTTP requests (already included)

## Redux State Management

This starter comes pre-configured with Redux Toolkit and React Redux for efficient state management.

### Store Structure

The Redux store is located in `src/store/`:
- `store/index.ts` - Main store configuration using `configureStore`
- `store/slices/` - Directory for Redux slices (reducers + actions)

### Example Usage

Here's how to use Redux in your components:

```tsx
import { useSelector, useDispatch, type TypedUseSelectorHook } from 'react-redux'
import { increment, decrement, incrementByAmount } from '../store/slices/counterSlice'
import { RootState, AppDispatch } from '../store'

const useAppSelector: TypedUseSelectorHook<RootState> = useSelector
const useAppDispatch: () => AppDispatch = useDispatch

function MyComponent() {
  const count = useAppSelector((state) => state.counter.value)
  const dispatch = useAppDispatch()

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={() => dispatch(increment())}>+</button>
      <button onClick={() => dispatch(decrement())}>-</button>
      <button onClick={() => dispatch(incrementByAmount(5))}>+5</button>
    </div>
  )
}
```

### Creating New Slices

To add new state management features, create new slice files in `src/store/slices/`:

```typescript
// src/store/slices/userSlice.ts
import { createSlice, PayloadAction } from '@reduxjs/toolkit'

interface UserState {
  name: string;
  email: string;
}

const initialState: UserState = {
  name: '',
  email: '',
}

export const userSlice = createSlice({
  name: 'user',
  initialState: {
    name: '',
    email: ''
  },
  reducers: {
    setUser: (state, action) => {
      state.name = action.payload.name
      state.email = action.payload.email
    },
    clearUser: (state) => {
      state.name = ''
      state.email = ''
    }
  }
})

export const { setUser, clearUser } = userSlice.actions
export default userSlice.reducer
```

Then add it to your store in `src/store/index.ts`:

```javascript
import userReducer from './slices/userSlice'

export const store = configureStore({
  reducer: {
    counter: counterReducer,
    user: userReducer
  }
})
```

## Contributing

This is a starter template. Feel free to fork and customize for your needs.

## License

ISC
