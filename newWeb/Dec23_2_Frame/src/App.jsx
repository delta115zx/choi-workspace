import { Route, Routes } from "react-router-dom";
import "./App.css";
import ProductBBS from "./site/product/productBBS";
import SiteLayout from "./site/siteLayout";
import Home from "./site/home";
import PlayerBBS from "./site/player/playerBBS";

function App() {
   return (
      <Routes>
         <Route element={<SiteLayout />}>
            <Route path="/" element={<Home />} />
            <Route path="/product.go" element={<ProductBBS />} />
            <Route path="/player.go" element={<PlayerBBS />} />
         </Route>
      </Routes>
   );
}
export default App;
