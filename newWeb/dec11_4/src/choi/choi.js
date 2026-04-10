import { useState } from "react";

const Choi = () => {
   const [txt1, settxt1] = useState(200);
   const [txt2, settxt2] = useState(200);
   return (
      <>
         <table border={1} style={{ width: txt1, height: txt2 }}>
            <tr>
               <td>
                  <input
                     value={txt1}
                     onChange={(e) => {
                        settxt1(e.target.value * 1);
                     }}
                  />
               </td>
            </tr>
            <tr>
               <td>
                  <input
                     value={txt2}
                     onChange={(e) => {
                        settxt2(e.target.value * 1);
                     }}
                  />
               </td>
            </tr>
         </table>
      </>
   );
};

export default Choi;
