import { useEffect } from "react";

const ChoiScrollEvent = () => {
   const scrollEventtt = () => {
      const htmlHeight = document.documentElement.scrollHeight;
      const browserHeight = window.innerHeight;
      const scrollOffset = window.scrollY;
      const scrollOffsetBottom = scrollOffset + browserHeight;
      if (scrollOffsetBottom >= htmlHeight - 10) {
         alert("바닥");
      }
   };

   useEffect(() => {
      window.addEventListener("scroll", scrollEventtt);

      return () => {
         window.removeEventListener("scroll", scrollEventtt);
      };
   }, []);

   return (
      <>
         <h1>ㅋㅋㅋ</h1>
         <h1>ㅋㅋㅋ</h1>
         <h1>ㅋㅋㅋ</h1>
         <h1>ㅋㅋㅋ</h1>
         <h1>ㅋㅋㅋ</h1>
         <h1>ㅋㅋㅋ</h1>
         <h1>ㅋㅋㅋ</h1>
         <h1>ㅋㅋㅋ</h1>
         <h1>ㅋㅋㅋ</h1>
         <h1>ㅋㅋㅋ</h1>
         <h1>ㅋㅋㅋ</h1>
         <h1>ㅋㅋㅋ</h1>
         <h1>ㅋㅋㅋ</h1>
         <h1>ㅋㅋㅋ</h1>
      </>
   );
};

export default ChoiScrollEvent;
