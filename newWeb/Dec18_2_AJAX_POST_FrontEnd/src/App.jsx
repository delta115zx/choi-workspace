import "./App.css";
import ChoiAJAXGET from "./choiAJAXGET/choiAJAXGET";
import ChoiAJAXPOST from "./choiAJAXGET/choiAJAXPOST";
import ChoiAJAXPOST2 from "./choiAJAXGET/choiAJAXPOST2";

function App() {
   return (
      <>
         <ChoiAJAXGET />
         <hr />
         <ChoiAJAXPOST />
         <hr />
         <ChoiAJAXPOST2 />
      </>
   );
}

export default App;
