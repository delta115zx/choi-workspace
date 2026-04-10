import { useSelector } from "react-redux";
import { logInCheck } from "../../../cookingCommunityMain";
import { useNavigate } from "react-router-dom";

const Logined = () => {
   const loginMember = useSelector((s) => s.ms.loginMember);
   const nav = useNavigate();

   const goMemberInfo = () => {
      nav("/memberinfo.go");
   };
   const signOut = () => {
      sessionStorage.removeItem("loginMember");
      logInCheck();
   };
   return (
      <table id="loginForm">
         <tr>
            <td rowSpan={2} align="center" className="imgTd">
               <img
                  src={`http://localhost:7777/member.info.photo.get?file=${loginMember.photo}`}
               />
            </td>
            <td className="idTd">{loginMember.id}</td>
         </tr>
         <tr>
            <td align="right">
               <button onClick={goMemberInfo}>정보확인</button>
               <button onClick={signOut}>로그아웃</button>
            </td>
         </tr>
      </table>
   );
};

export default Logined;
