import { useEffect, useState } from "react";

const ChoiResizeEvent = () => {
   const [wh, setWh] = useState({
      ww: window.innerWidth, // vanilla JS에서 브라우저 사이즈
      hh: window.innerHeight, // vanilla JS에서 브라우저 사이즈
   });
   const updateWH = () => {
      setWh({ ww: window.innerWidth, hh: window.innerHeight });
   };

   useEffect(() => {
      // vanilla JS에서 소스로 이벤트 연결
      window.addEventListener("resize", updateWH);

      return () => {
         // 연결해놓은거 해제
         window.removeEventListener("resize", updateWH);
      };
   }, []);

   return (
      <div>
         {wh.ww},{wh.hh}
      </div>
   );
};

export default ChoiResizeEvent;
