import "./App.css";
import ChoiKeyboardEvent from "./choiEvent/choiKeyboardEvent";
import ChoiMouseEvent from "./choiEvent/choiMouseEvent";
import ChoiPopupMenu from "./choiEvent/choiPopupMenu";
import ChoiResizeEvent from "./choiEvent/choiResizeEvent";
import ChoiScrollEvent from "./choiEvent/choiScrollEvent";

function App() {
   return (
      <>
         <ChoiMouseEvent />
         <hr />
         <ChoiKeyboardEvent />
         <hr />
         <ChoiResizeEvent />
         <hr />
         <ChoiScrollEvent />
         <hr />
         <ChoiPopupMenu />
      </>
   );
}

export default App;
