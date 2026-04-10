import { useState } from "react";

const ChoiRSThird = () => {
   const [snacks, setSnacks] = useState([
      { name: "빼빼로", price: 2000, color: "brown" },
      { name: "새콤달콤", price: 500, color: "red" },
      { name: "새우깡", price: 4000, color: "orange" },
   ]);
   const snackTrs = snacks.map((s, i) => {
      return (
         <tr style={{ color: s.color }}>
            <td>{s.name}</td>
            <td>{s.price}</td>
         </tr>
      );
   });
   return (
      <table border={1}>
         <tr>
            <th>이름</th>
            <th>가격</th>
         </tr>
         {snackTrs}
      </table>
   );
};

export default ChoiRSThird;
