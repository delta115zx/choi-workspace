import { useState } from "react";

const ChoiRSFirst = () => {
   const [numbers, setNumbers] = useState([123, 65, 38, 100, 10, 50]);

   // 필터링
   //   배열 차례대로 탐색하면서 데이터 하나 만날때마다 콜백함수
   //   콜백함수속에서 조건문 써서 true값 리턴되는것만 살아남음
   // 배열명.filter((값) => {});
   //    numbers.filter((n) => {
   //       if (n % 2 === 0) {
   //          return true;
   //       } else {
   //          return false;
   //       }
   //    });

   const numbers2 = numbers.filter((n) => n % 2 === 0);

   // const numbers3 = numbers2.sort(); // 정렬(글자, 오름차순)
   // 정확하게 이해x, bubbleSort스러운 느낌
   const numbers3 = numbers2.sort((n1, n2) => {
      if (n1 > n2) {
         return -1; // 앞의 값이 더 클때 1 : 오름차순
                  // 앞의 값이 더 클때 -1 : 내림차순
      }
      return 1;
   });// 정렬(숫자/객체, 내림차순)

   const marquees = numbers3.map((n, i) => (
      <marquee behavior="alternate">{n}</marquee>
   ));
   return <div>{marquees}</div>;
};

export default ChoiRSFirst;
