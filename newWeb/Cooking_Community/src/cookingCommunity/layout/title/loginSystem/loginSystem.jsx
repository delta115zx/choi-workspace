import { useSelector } from "react-redux";
import LoginForm from "./loginForm";
import Logined from "./logined";
const LoginSystem = () => {
   const loginSystemCSS = useSelector((s) => s.lsss);
   const loginMember = useSelector((s) => s.ms.loginMember);

   let loginFormPage = null;
   if (loginMember === undefined) {
      loginFormPage = <LoginForm />;
   } else {
      loginFormPage = <Logined />;
   }

   return (
      <table id="loginSystem" style={loginSystemCSS}>
         <tr>
            <td align="right">{loginFormPage}</td>
         </tr>
      </table>
   );
};

export default LoginSystem;
