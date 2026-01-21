import { useSelector, useDispatch, type TypedUseSelectorHook } from 'react-redux'
import { increment, decrement, incrementByAmount } from '../store/slices/counterSlice'
import { RootState, AppDispatch } from '../store'

import ExampleButton from './ExampleButton'

const useAppSelector: TypedUseSelectorHook<RootState> = useSelector
const useAppDispatch: () => AppDispatch = useDispatch

function ReduxCounter() {
  const count = useAppSelector((state) => state.counter.value)
  const dispatch = useAppDispatch()

  return (
    <div className="text-center p-6">
      <h2 className="text-2xl font-bold mb-4">Redux Counter Example</h2>
      <div className="mb-4">
        <p className="text-xl">Count: <span className="font-bold text-blue-600">{count}</span></p>
      </div>
      <div className="space-x-2">
        <ExampleButton onClick={() => dispatch(decrement())}>
          -
        </ExampleButton>
        <ExampleButton onClick={() => dispatch(increment())}>
          +
        </ExampleButton>
        <ExampleButton onClick={() => dispatch(incrementByAmount(5))}>
          +5
        </ExampleButton>
      </div>
      <div className="mt-4 text-sm text-gray-600">
        <p>This counter demonstrates Redux state management in action!</p>
      </div>
    </div>
  )
}

export default ReduxCounter
