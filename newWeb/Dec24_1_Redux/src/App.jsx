import "./App.css";
import ChoiTest from "./choiTest/choiTest";
import ChoiTest2 from "./choiTest2/choiTest2";
import ChoiTest3 from "./choiTest3/choiTest3";

// yarn add @reduxjs/toolkit react-redux
function App() {
   return (
      <>
         <ChoiTest />
         <hr />
         <ChoiTest2 />
         <hr />
         <ChoiTest3 />
      </>
   );
}

export default App;
