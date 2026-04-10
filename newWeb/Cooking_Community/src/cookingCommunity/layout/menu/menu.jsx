import React from "react";
import { useNavigate } from "react-router-dom";

const Menu = () => {
   const nav = useNavigate();
   return (
      <table id="siteMenuArea">
         <tr>
            <td
               onClick={() => {
                  nav("/");
               }}
            >
               홈
            </td>
            &nbsp;&nbsp;
            <td
               onClick={() => {
                  nav("/forum.go");
               }}
            >
               게시판
            </td>
            &nbsp;&nbsp;
            <td>22</td>&nbsp;&nbsp;
            <td>33</td>&nbsp;&nbsp;
            <td>44</td>
         </tr>
      </table>
   );
};

export default Menu;
