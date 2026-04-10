import { useState } from "react";

const Choi3 = () => {
   const [tblCSS, setTblCSS] = useState({
      width: 200,
      height: 200,
   });
   const changeCSS = (e) => { 
      // alert(e); // 발생한 이벤트 전체정보
      // alert(e.target); // 이벤트 발생한 객체
      // alert(e.target.value); // 이벤트 발생한 객체(input)의 값
      // alert(e.target.name); // 이벤트 발생한 객체(input)의 name
      setTblCSS({...tblCSS, [e.target.name]:e.target.value * 1})
    };
   return (
      <>
         <table border={1} style={tblCSS}>
            <tr>
               <td>
                  <input name="width" value={tblCSS.width} onChange={changeCSS} />
               </td>
            </tr>
            <tr>
               <td>
                  <input name="height" value={tblCSS.height} onChange={changeCSS} />
               </td>
            </tr>
         </table>
      </>
   );
};

export default Choi3;
