import { Outlet } from "react-router-dom";

const Content = () => {
   return (
      <table id="siteContentArea">
         <tr>
            <td align="left">
               <Outlet />
            </td>
         </tr>
      </table>
   );
};

export default Content;
