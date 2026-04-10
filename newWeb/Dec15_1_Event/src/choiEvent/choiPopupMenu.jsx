import { useEffect, useState } from "react";

const ChoiPopupMenu = () => {
   const [tableCSS, setTableCSS] = useState({
      position: "fixed",
      opacity: 0,
      top: -100,
      left: -100,
      transition: "opacity 0.5s ease-out",
   });
   const summonPopup = (ee) => {
      ee.preventDefault(); // 기존 기능 삭제
   };
   const summonMyPopup = (e) => {
      if (e.button === 2) {
         setTableCSS({
            ...tableCSS,
            top: e.clientY + 5,
            left: e.clientX + 5,
            opacity: 1,
         });

         setTimeout(() => {
            setTableCSS({
               ...tableCSS,
               opacity: 0,
            });
            setTimeout(() => {
               setTableCSS({ ...tableCSS, top: -100, left: -100 });
            }, 500);
         }, 2000);
      }
   };

   useEffect(() => {
      document.addEventListener("contextmenu", summonPopup);
      document.addEventListener("mouseup", summonMyPopup);

      return () => {
         document.removeEventListener("contextmenu", summonPopup);
         document.removeEventListener("mouseup", summonMyPopup);
      };
   }, []);

   return (
      <>
         <table border={1} style={tableCSS}>
            <tr>
               <td>
                  <a href="https://www.naver.com">네이버로</a>
               </td>
            </tr>
            <tr>
               <td>
                  <a href="https://www.google.com">구글로</a>
               </td>
            </tr>
            <tr>
               <td>
                  <a href="https://www.daum.net">다음으로</a>
               </td>
            </tr>
         </table>
      </>
   );
};

export default ChoiPopupMenu;
