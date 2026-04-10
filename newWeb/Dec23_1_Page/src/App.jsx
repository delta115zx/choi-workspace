import { Route, Routes } from "react-router-dom";
import "./App.css";
import ChoiP1 from "./choiP1/choiP1";
import ChoiP2 from "./choiP2/choiP2";
import ChoiP3 from "./choiP3/choiP3";
import Choip4 from "./choip4/choip4";
import ChoiP5 from "./choiP5/choiP5";
import ChoiP6 from "./choiP6/choiP6";
import ChoiP7 from "./choiP7/choiP7";
import ChoiP8 from "./choiP8/choiP8";
import ChoiP9 from "./choiP9/choiP9";

function App() {
   // 첫페이지는 path="/" or index
   // 등록안한 나머지 주소 path="*"
   return (
      <Routes>
         <Route index element={<ChoiP1 />} />
         <Route path="/p2.go" element={<ChoiP2 />} />
         <Route path="/p3.go" element={<ChoiP3 />} />
         <Route path="/p4.go/:namee/:agee" element={<Choip4 />} />
         <Route path="/p5.go" element={<ChoiP5 />} />
         <Route path="/p6.go" element={<ChoiP6 />} />
         <Route path="/p7.go" element={<ChoiP7 />} />
         <Route path="/p8.go" element={<ChoiP8 />} />
         <Route path="*" element={<ChoiP9 />} />
      </Routes>
   );
}

export default App;
