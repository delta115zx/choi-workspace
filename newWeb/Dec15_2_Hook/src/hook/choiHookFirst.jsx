// React : JavaScript OOP Lib + VDOM(변화 잦은 사이트에 유리)
//      객체를 만들려면 class가 필요
//      React측에서 class보다는 함수 사용을 권장

import { useState } from "react";

// 객체(class)
//      속성(멤버변수)
//      행동(메소드)
//      객체가 만들어질때 어쩌고(생성자)
//      -> 함수에 저런게 있을수 있나 - x
//      -> React측에서 hook이라는걸 제공해줘서, 저런 느낌 나게

// useState : 멤버변수 + 멤버변수 값 바꿀수있는 메소드(setter)
//      class ChoiHookFirst:
//          def __init__(self, btnCnt):
//              self.btnCnt = btnCnt
//          def setBtnCnt(self, btnCnt):
//              self.btnCnt = btnCnt

const ChoiHookFirst = () => {
    // const [멤버변수, setter메소드명] = useState(기본값);
   const [btnCnt, setBtnCnt] = useState(0);

   const changeCnt = () => {
      let curCnt = btnCnt;
      setBtnCnt(curCnt + 1);
   };

   return (
      <>
         <h1>버튼 누른 횟수 : {btnCnt}</h1>
         <button onClick={changeCnt}>버튼</button>
      </>
   );
};

export default ChoiHookFirst;
