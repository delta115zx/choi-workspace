import "./App.css";
import ChoiCSSFirst from "./choiCSS/choiCSSFirst";
import ChoiCSSSecond from "./choiCSS/choiCSSSecond";
import ChoiCSSThird from "./choicss/choiCSSThird";

function App() {
   return (
      <>
         <ChoiCSSFirst />
         <hr />
         <ChoiCSSSecond c="white" bgc="black" w="100" h="50">
            ㅋㅋㅋ
         </ChoiCSSSecond>
         <hr />
         <ChoiCSSThird />
      </>
   );
}

export default App;
