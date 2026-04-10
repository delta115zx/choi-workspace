// 노란배경색, 파란글자색 기본값:blue useState
// 검정배경색, 흰글자색 기본값:white useReducer
// 쓸때마다 글자색바뀌게

import { useReducer, useState } from "react";

const changeInput2 = (state, payload) => {
   return { ...state, color: payload.target.value };
};

// useEffect : 생성자
const ChoiHookThird = () => {
   const [input1Css, setInput1Css] = useState({
      backgroundColor: "yellow",
      color: "blue",
   });

   const [input2Css, setInput2Css] = useReducer(changeInput2, {
      color: "white",
      backgroundColor: "black",
   });

   // main.jsx에 StrictMode
   //       yarn dev -> 개발중
   //           확인차 두번씩
   //           개발중일때도 두번씩 되는거 안하려면 StrictMode삭제
   //       yarn build -> 서버에 올려서 서비스 시작
   //           StrictMode가 있어도 한번만

   //    useEffect(() => {
   //       alert("ㅋ");
   //    }); // ChoiHookThird가 렌더링될때마다(처음시작, 글자적히고, css가바뀌고)

   //    useEffect(() => {
   //       alert("ㅋ");
   //    }, []); // ChoiHookThird가 처음 렌더링될때

   //    useEffect(() => {
   //       alert("ㅋ");
   //    }, [input1Css]); // ChoiHookThird가 처음 렌더링될때 + input1Css값 바뀔때

   //    useEffect(() => {
   //       alert("ㅋ");

   //       return () => {
   //          alert("ㅎ");
   //       }; // ChoiHookThird가 화면상에서 사라질 때 (소멸자 같은)
   //    }, []);

   return (
      <>
         <input
            style={input1Css}
            value={input1Css.color}
            onChange={(e) => {
               setInput1Css({ ...input1Css, color: e.target.value });
            }}
         />{" "}
         <br />
         <input
            style={input2Css}
            value={input2Css.color}
            onChange={setInput2Css}
         />
      </>
   );
};

export default ChoiHookThird;
