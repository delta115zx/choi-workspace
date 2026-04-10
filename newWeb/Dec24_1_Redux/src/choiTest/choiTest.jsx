import { useState } from "react";

// class, Java진영 클래스명 대문자로
const ChoiTest = () => {
   const [h1CSS, setH1CSS] = useState({ fontSize: 30 });

   const sizeUp = () => {
      setH1CSS({ fontSize: h1CSS.fontSize + 5 });
   };

   const sizeDown = () => {
      setH1CSS({ fontSize: h1CSS.fontSize - 5 });
   };

   return (
      <>
         <button onClick={sizeUp}>크게</button>
         <button onClick={sizeDown}>작게</button>
         <h1 style={h1CSS}>ㅋㅋㅋ</h1>
      </>
   );
};

export default ChoiTest;
