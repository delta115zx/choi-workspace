/* eslint-disable react-refresh/only-export-components */
/* eslint-disable react-hooks/globals */
import Content from "./layout/content/content";
import Menu from "./layout/menu/menu";
import Title from "./layout/title/title";
import "./layout/layout.css";
import "./layout/title/loginSystem/login.css";
import "./layout/content/member/signUp.css";
import "./layout/content/forum/forum.css";
import axios from "axios";
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { setLoginMember } from "./slice/memberSlice";
import Weather from "./layout/weather/weather";
import { useNavigate } from "react-router-dom";

let d = null;
let nav = null;
let signUpPage = null;

export const logInCheck = () => {
   axios
      .get(
         `http://localhost:7777/member.info.get?member=${sessionStorage.getItem(
            "loginMember"
         )}`
      )
      .then((res) => {
         d(setLoginMember(res.data.member));
         if (!signUpPage && res.data.member === undefined) {
            // 로그인 풀렸을때
            nav("/");
         } else {
            axios
               .get(
                  `http://localhost:7777/sign.in.exp.refresh?member=${sessionStorage.getItem(
                     "loginMember"
                  )}`
               )
               .then((res2) => {
                  sessionStorage.setItem("loginMember", res2.data.member);
               });
         }
      });
};
const CookingCommunityMain = () => {
   d = useDispatch();
   nav = useNavigate();
   signUpPage = useSelector((s) => s.ms.signUpPage);

   useEffect(() => {
      document.addEventListener("click", logInCheck);

      return () => {
         document.removeEventListener("click", logInCheck);
      };
   }, []);

   return (
      <>
         <Title />
         <Menu />
         <Content />
         <Weather />
      </>
   );
};

export default CookingCommunityMain;
