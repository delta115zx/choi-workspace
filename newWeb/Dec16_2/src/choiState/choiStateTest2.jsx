import { useEffect } from "react";
import { useState } from "react";

// 중간 렌더링 없이, 바뀐 state값 바로 사용
const ChoiStateTest2 = () => {
   const [no, setno] = useState(0);

   useEffect(() => {
      if (no !== 0) {
         alert(no);
      }
   }, [no]);

   return (
      <button
         onClick={() => {
            setno(no + 1);
         }}
      >
         버튼
      </button>
   );
};

export default ChoiStateTest2;
