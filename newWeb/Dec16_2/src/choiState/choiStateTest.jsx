import { useState } from "react";

// React : JavaScript OOP Library + VDOM
//    화면전환 잦은 사이트에 유리 + JavaScript 
//      -> 비동기식 추구(결과가 나올때까지 기다리지x)
//      -> state변경한거 바로 반영안하고, 다음 렌더링때 반영
const ChoiStateTest = () => {
   const [no, setno] = useState(0);

   return (
      <button
         onClick={() => {
            setno(no + 1); // state값 변경
            // 화면에 뭐 그렸나
            alert(no);// 13번줄의 state값 변경 끝나기전에 이쪽으로(비동기식)
         }}
      >
         버튼
      </button>
   );
};

export default ChoiStateTest;
