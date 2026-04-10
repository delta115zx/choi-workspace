import { useState } from "react";
import "./product.css";
const ProductBBS = () => {
   const [inputs, setinputs] = useState({
      pname: "",
      pprice: 0,
   });
   const changeInputs = (e) => {
      setinputs({ ...inputs, [e.target.name]: e.target.value });
   };

   const appendTr2 = () => {
      <tr className="dataTr">
         <td>{inputs.pname}</td>
         <td>{inputs.pprice}</td>
      </tr>;
   };
   return (
      <div id="productArea">
         품명 :{" "}
         <input
            name="pname"
            className="txtType"
            value={inputs.pname}
            onChange={changeInputs}
         />
         <br />
         가격 :{" "}
         <input
            name="pprice"
            className="txtType"
            value={inputs.pprice}
            onChange={changeInputs}
         />
         <br />
         <button onClick={appendTr2}>등록</button>
         <hr />
         <table id="productBBSTbl" border={1}>
            <tr>
               <th>품명</th>
               <th>가격</th>
            </tr>
            {/* <tr className="dataTr">
               <td>마우스</td>
               <td>10000</td>
            </tr>
            <tr className="dataTr">
               <td>키보드</td>
               <td>15000</td>
            </tr> */}
            {appendTr2}
         </table>
      </div>
   );
};

export default ProductBBS;
