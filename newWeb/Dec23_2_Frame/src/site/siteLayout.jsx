import { Link, Outlet } from "react-router-dom";
import Home from "./home";
import "./siteLayout.css";
const SiteLayout = () => {
   return (
      <>
         <table id="site">
            <tr>
               <td id="siteTitle">Dec23</td>
            </tr>
            <tr>
               <td id="siteMenuArea">
                  <Link to={"/"}>홈</Link>&nbsp;&nbsp;
                  <Link to={"/product.go"}>상품</Link>&nbsp;&nbsp;
                  <Link to={"/player.go"}>선수</Link>&nbsp;&nbsp;
               </td>
            </tr>
            <tr>
               <td id="siteContentArea">
                  <Outlet />
               </td>
            </tr>
         </table>
      </>
   );
};

export default SiteLayout;
