import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'

interface Approver {
  id: string
  name: string
  email: string
}

function Register() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [approverSearch, setApproverSearch] = useState('')
  const [approvers, setApprovers] = useState<Approver[]>([])
  const [selectedApprover, setSelectedApprover] = useState<Approver | null>(null)
  const [selectedRoles, setSelectedRoles] = useState<string[]>(['member']) // Default to member
  const [loading, setLoading] = useState(false)
  const [searching, setSearching] = useState(false)
  const [error, setError] = useState('')
  const navigate = useNavigate()

  const availableRoles = [
    { id: 'member', name: 'Member', description: 'Regular church member', color: 'bg-blue-100 text-blue-800 border-blue-300' },
    { id: 'youth', name: 'Youth', description: 'Young church member', color: 'bg-green-100 text-green-800 border-green-300' },
    { id: 'elder', name: 'Elder', description: 'Church elder', color: 'bg-purple-100 text-purple-800 border-purple-300' },
    { id: 'treasurer', name: 'Treasurer', description: 'Church treasurer', color: 'bg-orange-100 text-orange-800 border-orange-300' }
    // Pastor requires admin approval, so not included here
  ]

  const handleRoleChange = (roleId: string, checked: boolean) => {
    if (checked) {
      setSelectedRoles(prev => [...prev, roleId])
    } else {
      setSelectedRoles(prev => prev.filter(r => r !== roleId))
    }
  }

  const handleApproverSearch = async (searchTerm: string) => {
    if (searchTerm.length < 2) {
      setApprovers([])
      return
    }

    setSearching(true)
    try {
      const response = await axios.get(`approvers/search?role=member&q=${encodeURIComponent(searchTerm)}`)
      setApprovers(response.data)
    } catch (err) {
      console.error('Search failed', err)
    } finally {
      setSearching(false)
    }
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (password !== confirmPassword) {
      setError('Passwords do not match')
      return
    }
    if (!selectedApprover) {
      setError('Please select an approver')
      return
    }

    setLoading(true)
    setError('')

    try {
      const response = await axios.post('auth/register', {
        email,
        password,
        approver_id: selectedApprover.id,
        intended_roles: selectedRoles
      })

      // Registration successful, pending approval
      alert('Registration successful! Your account is pending approval. You will be notified once approved.')
      navigate('/login')
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Registration failed')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Create your account
          </h2>
          <p className="mt-2 text-center text-sm text-gray-600">
            Register to access SDA church features
          </p>
        </div>
        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          {error && (
            <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
              {error}
            </div>
          )}
          <div className="rounded-md shadow-sm -space-y-px">
            <div>
              <label htmlFor="email" className="sr-only">
                Email address
              </label>
              <input
                id="email"
                name="email"
                type="email"
                autoComplete="email"
                required
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
                placeholder="Email address"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <div>
              <label htmlFor="password" className="sr-only">
                Password
              </label>
              <input
                id="password"
                name="password"
                type="password"
                autoComplete="new-password"
                required
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
            <div>
              <label htmlFor="confirmPassword" className="sr-only">
                Confirm Password
              </label>
              <input
                id="confirmPassword"
                name="confirmPassword"
                type="password"
                autoComplete="new-password"
                required
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
                placeholder="Confirm Password"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
              />
            </div>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Select Your Roles (click to add/remove)
            </label>
            <div className="flex flex-wrap gap-2">
              {availableRoles.map((role) => (
                <button
                  key={role.id}
                  type="button"
                  onClick={() => handleRoleChange(role.id, !selectedRoles.includes(role.id))}
                  className={`inline-flex items-center px-3 py-1 rounded-full text-sm font-medium transition-colors ${
                    selectedRoles.includes(role.id)
                      ? `${role.color} border`
                      : 'bg-gray-100 text-gray-800 border border-gray-300 hover:bg-gray-200'
                  }`}
                  title={role.description}
                >
                  {role.name}
                  {selectedRoles.includes(role.id) && (
                    <svg className="ml-1 h-4 w-4" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                    </svg>
                  )}
                </button>
              ))}
            </div>
            <p className="mt-1 text-sm text-gray-600">
              Selected roles: {selectedRoles.map(roleId => availableRoles.find(r => r.id === roleId)?.name).join(', ') || 'None'}
            </p>
            {selectedRoles.length === 0 && (
              <p className="mt-1 text-sm text-red-600">Please select at least one role</p>
            )}
          </div>

          <div>
            <label htmlFor="approverSearch" className="block text-sm font-medium text-gray-700">
              Search for Approver (Pastor or Admin)
            </label>
            <input
              id="approverSearch"
              name="approverSearch"
              type="text"
              required
              className="mt-1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
              placeholder="Type pastor or admin name"
              value={approverSearch}
              onChange={(e) => {
                setApproverSearch(e.target.value)
                handleApproverSearch(e.target.value)
              }}
            />
            {searching && <p className="mt-1 text-sm text-gray-500">Searching...</p>}
            {approvers.length > 0 && (
              <div className="mt-2 max-h-40 overflow-y-auto border border-gray-300 rounded-md">
                {approvers.map((approver) => (
                  <div
                    key={approver.id}
                    className={`px-3 py-2 cursor-pointer hover:bg-gray-100 ${
                      selectedApprover?.id === approver.id ? 'bg-blue-100' : ''
                    }`}
                    onClick={() => setSelectedApprover(approver)}
                  >
                    <div className="font-medium">{approver.name}</div>
                    <div className="text-sm text-gray-500">{approver.email}</div>
                  </div>
                ))}
              </div>
            )}
            {selectedApprover && (
              <p className="mt-2 text-sm text-green-600">
                Selected: {selectedApprover.name}
              </p>
            )}
          </div>

          <div>
            <button
              type="submit"
              disabled={loading || !selectedApprover}
              className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? 'Registering...' : 'Register'}
            </button>
          </div>

          <div className="text-center">
            <button
              type="button"
              onClick={() => navigate('/login')}
              className="text-blue-600 hover:text-blue-500"
            >
              Already have an account? Sign in here
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default Register
