// useReducer : 멤버변수 + 멤버변수 값 바꿀수있는 메소드(setter)
//            + setter에 변화(기능추가같은...)
//            + 소스정리

import { useReducer } from "react";

// def doFlagGame():
//      print("ㅋㅋㅋ")

// class choiHookSecond:
//      def __init__(self):
//          self.history = "시작"
//      def setHistory(self):
//          doFlagGame()

// setter역할 할 함수(기존 state값, setter에 넣어준 값)
// 바꿀 state값 리턴
const doFlagGame = (curStateee, payloaddd) => {
   //    alert(curStateee);
   //    alert(payloaddd);
   return curStateee + " -> " + payloaddd.whatt + " " + payloaddd.doo;
};

const ChoiHookSecond = () => {
   // const [멤버변수, setter메소드명] = useReducer(setter역할할함수명, 기본값);
   // setter메소드(setHistory)를 호출하면 setter역할함수(doFlagGame)가 실행
   const [history, setHistory] = useReducer(doFlagGame, "시작");
   return (
      <>
         <h1>{history}</h1>
         <button
            onClick={() => {
               setHistory({ whatt: "청기", doo: "올려" });
            }}
         >
            청기올려
         </button>
         <button
            onClick={() => {
               setHistory({ whatt: "청기", doo: "내려" });
            }}
         >
            청기내려
         </button>
         <button
            onClick={() => {
               setHistory({ whatt: "백기", doo: "올려" });
            }}
         >
            백기올려
         </button>
         <button
            onClick={() => {
               setHistory({ whatt: "백기", doo: "내려" });
            }}
         >
            백기내려
         </button>
      </>
   );
};

export default ChoiHookSecond;
