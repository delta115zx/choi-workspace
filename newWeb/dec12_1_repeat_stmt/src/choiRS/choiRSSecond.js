import { useState } from "react";

const ChoiRSSecond = () => {
   const [snacks, setSnacks] = useState([
      { name: "빼빼로", price: 2000, color: "brown" },
      { name: "새콤달콤", price: 500, color: "red" },
      { name: "새우깡", price: 4000, color: "orange" },
      { name: "콘칲", price: 5000, color: "yellow" },
      { name: "홈런볼", price: 3000, color: "orange" },
      { name: "칸쵸", price: 2500, color: "orange" },
      { name: "꼬북칩", price: 3000, color: "orange" },
   ]);

   const filteredSnacks = snacks.filter((s) => s.price >= 1000);
   const sortedSnacks = filteredSnacks.sort((s1, s2) => {
      if (s1.name > s2.name) {
         return 1;
      }
      return -1;
   });
   const snackTrs = sortedSnacks.map((s, i) => {
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

export default ChoiRSSecond;
