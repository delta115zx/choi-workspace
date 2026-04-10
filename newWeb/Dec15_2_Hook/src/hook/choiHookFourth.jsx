// vanillaJS/jQuery : 객체를 선택해서...
// React : 객체에 state를 연동시켜놓고... -> 객체 선택x

import { useState } from "react";
import { useEffect } from "react";
import { useRef } from "react";

// useRef : vanillaJS/jQuery스러운 객체 선택
const ChoiHookFourth = () => {
   const paper = useRef();
   const [pen, setPen] = useState();

   useEffect(() => {
      // useRef한거 실제 사용 : ???.current...
      setPen(paper.current.getContext("2d"));
   }, []);

   return (
      <>
         <canvas
            ref={paper}
            style={{ border: "black solid 2px" }}
            width={300}
            height={300}
            onClick={(e) => {
               pen.fillRect(
                  e.nativeEvent.offsetX - 10,
                  e.nativeEvent.offsetY - 10,
                  20,
                  20
               );
            }}
         />
      </>
   );
};

export default ChoiHookFourth;
