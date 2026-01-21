import React from 'react'

interface MainLayoutProps {
  children: React.ReactNode;
}

function MainLayout({ children }: MainLayoutProps) {
  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-white shadow">
        <div className="container mx-auto px-4 py-4">
          <h1 className="text-xl font-semibold">React Stable Starter</h1>
        </div>
      </header>
      <main className="flex-1">
        {children}
      </main>
      <footer className="bg-white shadow mt-8">
        <div className="container mx-auto px-4 py-4 text-center text-gray-600">
          © 2023 React Stable Starter
        </div>
      </footer>
    </div>
  )
}

export default MainLayout
