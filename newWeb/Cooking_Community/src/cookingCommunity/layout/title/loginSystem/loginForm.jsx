import axios from "axios";
import { useRef, useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import { logInCheck } from "../../../cookingCommunityMain";
import { hide } from "../../../slice/loginSystemSummonSlice";
import { setSignUpPage } from "../../../slice/memberSlice";
import { isEmpty } from "../../content/member/choiValidCheckerReact";

const LoginForm = () => {
   const [logInInfo, setLogInInfo] = useState({
      id: "",
      pw: "",
   });
   const logInFD = new FormData();
   logInFD.append("id", logInInfo.id);
   logInFD.append("pw", logInInfo.pw);

   const d = useDispatch();
   const nav = useNavigate();

   const changeInput = (e) => {
      setLogInInfo({ ...logInInfo, [e.target.name]: e.target.value });
   };

   const logInInput = useRef({});

   const goSignUp = () => {
      d(hide());
      d(setSignUpPage(true));
      nav("/signup.go");
   };

   const signIn = () => {
      if (isValid()) {
         axios
            .post("http://localhost:7777/sign.in", logInFD, {
               withCredentials: "true",
            })
            .then((res) => {
               if (res.data.result === "로그인 성공") {
                  sessionStorage.setItem("loginMember", res.data.member);
                  logInCheck();
               } else {
                  alert(res.data.result);
               }
            });
      }
      setLogInInfo({ id: "", pw: "" });
   };

   const signInEnterKey = (e) => {
      if (e.key === "Enter") {
         signIn();
      }
   };

   const isValid = () => {
      if (isEmpty(logInInfo.id)) {
         alert("id?");
         logInInfo.current.id.focus();
         return false;
      }
      if (isEmpty(logInInfo.pw)) {
         alert("pw?");
         logInInfo.current.pw.focus();
         return false;
      }
      return true;
   };

   return (
      <>
         <table id="loginForm">
            <tr>
               <td>
                  <input
                     ref={(thisInput) => {
                        logInInput.current.id = thisInput;
                     }}
                     placeholder="ID"
                     maxLength={10}
                     name="id"
                     value={logInInfo.id}
                     onKeyUp={signInEnterKey}
                     onChange={changeInput}
                  />
               </td>
               <td>
                  <button onClick={signIn}>로그인</button>
               </td>
            </tr>
            <tr>
               <td>
                  <input
                     ref={(thisInput) => {
                        logInInput.current.pw = thisInput;
                     }}
                     placeholder="PW"
                     maxLength={10}
                     name="pw"
                     value={logInInfo.pw}
                     onKeyUp={signInEnterKey}
                     onChange={changeInput}
                     type="password"
                  />
               </td>
               <td>
                  <button onClick={goSignUp}>회원가입</button>
               </td>
            </tr>
         </table>
      </>
   );
};

export default LoginForm;
