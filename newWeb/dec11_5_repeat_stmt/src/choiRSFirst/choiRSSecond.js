// vanillaJS/jQuery
//      데이터 받아와서 파싱 -> 반복문 -> tr/td만들어서 -> 존재하던 table에 append
// react
//      데이터 받아와서 파싱 -> 반복문 -> tr/td만들어서 return하는 걸 변수에 저장 -> 그 변수를 사용

import { useState } from "react";

const ChoiRSSecond = () => {
   const [ar, setAr] = useState([65456, 4564, 454, 123, 21]);

   const h2s = ar.map((a, i) => <h2>{a}</h2>);
   return <div>{h2s}</div>;
};

export default ChoiRSSecond;
