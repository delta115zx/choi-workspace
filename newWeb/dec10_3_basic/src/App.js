import "./App.css";
import Dog from "./dog";
import MyBtns from "./myBtns";
import MyH1 from "./myH1";
import MyH2 from "./myH2";
import MyTbl from "./MyTbl";

// vanillaJS/jQuery
//    html에서 특정부분만 수정이 일어나는게 아님
//        b1을 클릭하면 h1의 css(글자색)만 변경되는게 아님
//        다른 객체들은 가만히 있는데, h1글자색만 바뀌는거 - x
//    html페이지 전체를 새로 다 렌더링 -> 화면 자주 바뀌는 사이트면
// React
//    Facebook에서 만든
//    JavaScript OOP Library
//    Virtual DOM
//      소스 -> VDOM -> 화면
//        소스 바뀌면 VDOM에
//        VDOM에 변경사항만 화면에 반영 -> 화면 자주 바뀌는 사이트에 유리
//      화면 자주 바뀌지 않은 사이트면 -> VDOM때문에 컴퓨터자원많이, 느려지고

// JavaScript OOP Library
//    OOP구사함으로써 얻는 이득
//        이름/나이 속성있고, 짖기/정보출력 기능있는 개
//          소스 알아보기 편함
//          여러개 만들기 편함
//    => 설계가 중요

// public/index.html -> <div id="root"></div>
// public/index.css : body여백, 전체적인 규칙
// index.js : 설정 + index.html의 <div id="root"></div>에 App.js띄우기
// src/App.js : 실제로 작업
// src/App.css : 실제 디자인

function App() {
   return (
      <>
         <Dog />
         <MyH1 />
         <MyH2 />
         <MyH2 />
         <MyBtns />
         <MyTbl />
         <MyTbl />
         <MyTbl />
      </>
   );
}

export default App;
