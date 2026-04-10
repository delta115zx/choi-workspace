import { useDispatch } from "react-redux";
import c from "./img/cook.png";
import LoginSystem from "./loginSystem/loginSystem";
import { summon } from "../../slice/loginSystemSummonSlice";
import l from "./img/logInIcon.png";

const Title = () => {
   const d = useDispatch();
   const summonLoginSystem = () => {
      d(summon());
   };
   return (
      <>
         <table id="siteTitleArea">
            <tr>
               <td>
                  <th id="siteTitle">
                     <img id="siteTitleImg" src={c} />
                     &nbsp;요리커뮤니티&nbsp;&nbsp;
                     <img id="logInImg" src={l} onClick={summonLoginSystem} />
                  </th>
               </td>
            </tr>
         </table>
         <LoginSystem />
      </>
   );
};

export default Title;
