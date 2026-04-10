import { useState } from "react";

const Clicker = () => {
   const [cnt, setCnt] = useState(0);
   const changeCnt = () => {
      setCnt(cnt + 1);
   };
   return <button onClick={changeCnt}>{cnt}</button>;
};

export default Clicker;
