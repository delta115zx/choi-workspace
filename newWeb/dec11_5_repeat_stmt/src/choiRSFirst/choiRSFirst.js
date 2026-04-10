const ChoiRSFirst = () => {
   const ar = [65456, 4564, 454, 123, 21];
   const rsTest = () => {
      // 반복문속에서 변수 만드는거 자제
      // 기존 for, for-of, while, do-while
      let a;
      for (let i = 0; i < ar.length; i++) {
         // const a = ar[i]; 반복할때마다 변수만듦 -> 메모리...
         a = ar[i];
         alert(a);
      }
   };
   const rsTest2 = () => {
      // 배열.map((값, 인덱스)=>{}); : 배열을 탐색하면서 하나 만날때마다 콜백함수 호출
      ar.map((a, i) => {
         alert(i + ":" + a);
      });
   };
   return (
      <>
         <button onClick={rsTest}>반복문</button>
         <button onClick={rsTest2}>반복문2</button>
      </>
   );
};

export default ChoiRSFirst;
