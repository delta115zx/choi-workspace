import "./App.css";
import ChoiDesignFirst from "./cdf/choiDesignFirst";
import ChoiDesignSecond from "./cds/choiDesignSecond";
import ChoiDesignThird from "./cdt/choiDesignThird";

// index.css : 규칙, 사이트 전체에서 공유하는
// App.css : 사이트 전체 레이아웃

function App() {
   return (
      <>
         <ChoiDesignFirst />
         <hr />
         <ChoiDesignSecond />
         <hr />
         <ChoiDesignThird />
      </>
   );
}

export default App;
