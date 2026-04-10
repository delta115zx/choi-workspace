import { useState } from "react";

const ChoiMouseEvent = () => {
   const divCss = { width: 200, height: 200, border: "black solid 2px" };
   const [moveInfo, setMoveInfo] = useState("");
   const [xyInfo, setXyInfo] = useState("");
   const [xyInfo2, setXyInfo2] = useState("");
   const [clickInfo, setClickInfo] = useState("");

   const changeCilckInfo = (msg) => {
      setClickInfo(msg)
   };

   return (
      <>
         <div
            style={divCss}
            onMouseEnter={() => {
               setMoveInfo("mouseenter");
            }}
            onMouseMove={(e) => {
               setXyInfo(e.clientX + "," + e.clientY); // browser기준
               setXyInfo2(e.nativeEvent.offsetX + "," + e.nativeEvent.offsetY); // 객체기준
            }}
            onMouseLeave={() => {
               setMoveInfo("mouseleave");
            }}
            onMouseDown={(e) => {
               changeCilckInfo("mousedown : " + e.button);
            }}
            onMouseUp={(e) => {
               changeCilckInfo("mouseup : " + e.button);
            }}
         ></div>
         <h2>{moveInfo}</h2>
         <h2>{xyInfo}</h2>
         <h2>{xyInfo2}</h2>
         <h2>{clickInfo}</h2>
      </>
   );
};

export default ChoiMouseEvent;
