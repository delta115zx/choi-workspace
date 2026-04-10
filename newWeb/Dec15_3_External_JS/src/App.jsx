import { useEffect } from 'react'
import './App.css'

// React에서 외부 JS파일
//    index.html에 넣고
//    사용은 window.xxx

function App() {
  
  useEffect(() => {
    window.io.connect("http://195.168.9.80:7777")
  }, [])
  

  return (
    <>

    </>
  )
}

export default App
