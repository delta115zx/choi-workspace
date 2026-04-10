import { useState } from "react";

const Choi2 = () => {
   const [tblCSS, setTblCSS] = useState({
      width: 200,
      height: 200,
   });
   const changeWidth = (e) => {
      // {width:200, height:200} -> 300
      // {width:200, height:200} -> {width:300, height:200}

      // tblCSS에서 width만 변경, height는 기존 그대로
      // ...객체 : 그 객체 속성값 그대로 가져와(ES6)
      setTblCSS({ ...tblCSS, width: e.target.value * 1 });
   };
   const changeHeight = (e) => {
      setTblCSS({ ...tblCSS, height: e.target.value * 1 });
   };
   return (
      <>
         <table border={1} style={tblCSS}>
            <tr>
               <td>
                  <input value={tblCSS.width} onChange={changeWidth} />
               </td>
            </tr>
            <tr>
               <td>
                  <input value={tblCSS.height} onChange={changeHeight} />
               </td>
            </tr>
         </table>
      </>
   );
};

export default Choi2;
