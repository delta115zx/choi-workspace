import { useState } from "react";

// rafce
// 폴더명 : choiInputttt
// 파일명 : choiInput.js - 대문자로 시작하고 싶었는데, vscode자동완성이 안될때가 있어서
// 함수명 : ChoiInput - Java진영에서는 class명 대문자로 시작

// OOP -> class -> react가 함수를 권장해서 함수로 만들기는
// 했지만 사실상 class로 봐야

// Dog에 name이라는 속성(멤버변수)
// ChoiInput에 txt라는 state

const ChoiInput = () => {
   const [txt, setTxt] = useState("ㅋㅋㅋ");
   return (
      <>
         <h1>{txt}</h1>
         <input
            value={txt} // txt라는 state를 h1의 내용에 상시연동
            onChange={(e) => { // input 내용 바뀔때마다
               // e.target : 이벤트 발생한 객체($(this))
               setTxt(e.target.value); // 바뀐 그 내용을 txt에 상시연동
            }}
         />
         <button
            onClick={() => { // button 클릭했을때
               alert(txt); // 그 시점의 txt라는 state값 사용
            }}
         >
            출력
         </button>
      </>
   );
};

export default ChoiInput;
