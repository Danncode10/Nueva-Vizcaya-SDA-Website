import clsx from 'clsx'

interface ExampleButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children: React.ReactNode;
  className?: string;
}

function ExampleButton({ children, className, ...props }: ExampleButtonProps) {
  return (
    <button
      className={clsx(

        'bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded', // Tailwind classes
        className
      )}
      {...props}
    >
      {children}
    </button>
  )
}

export default ExampleButton
