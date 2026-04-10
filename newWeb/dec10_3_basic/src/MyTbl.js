import { useState } from "react";

// 이벤트처리
//      vanillaJS/jQuery
//          버튼을 눌렀을때
//          그 시점에 input에 써져있는 내용
//          을 출력

//      React
//          state(멤버변수)를 상시 업데이트
//          버튼을 눌렀을때
//          그 시점의 state값
//          을 출력

// JavaScript OOP Library
//      MyTbl 객체를 만들고싶었음 -> class만들고싶었음
//      -> React측에서 class보다는 함수를 권장
//      -> 멤버변수? 메소드?
//      -> React측에서 hook이라는걸 제공해서 함수를 클래스처럼 쓸수있게

const MyTbl = () => {
   // 멤버변수느낌 : useState
   // txt라는 멤버변수만들고, 기본값 ""
   // setTxt라는 메소드(txt값 바꿀떄)
   const [txt, setTxt] = useState("");

   // 메소드
   const showwww = () => {
      alert(txt);
   };

   const keyUpp = (e) => {
      // e.target : $(this)
      setTxt(e.target.value);
   };

   // input의 내용 : txt값
   // input에서 키보드 건들떄마다 txt값을 input에 쓴걸로
   return (
      <>
         <table border={1}>
            <tr>
               <td>
                  <input value={txt} onChange={keyUpp} />
               </td>
            </tr>
            <tr>
               <td>
                  <button onClick={showwww}>눌러</button>
               </td>
            </tr>
         </table>
      </>
   );
};

export default MyTbl;
