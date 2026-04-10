import "./App.css";
import ChoiHookFirst from "./hook/choiHookFirst";
import ChoiHookFourth from "./hook/choiHookFourth";
import ChoiHookSecond from "./hook/choiHookSecond";
import ChoiHookThird from "./hook/choiHookThird";

function App() {
   return (
      <>
         <ChoiHookFirst />
         <hr />
         <ChoiHookSecond />
         <hr />
         <ChoiHookThird />
         <hr />
         <ChoiHookFourth />
      </>
   );
}

export default App;
