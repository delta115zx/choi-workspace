import "./App.css";
import ChoiInput from "./choiInputttt/choiInput";

// jQuery.js : JavaScript 편하게 사용하게 해주는 라이브러리
// react.js : JavaScript OOP 라이브러리
// html에 react.js만 넣고 + 어떤 서버든 업로드만 하면

// Node.js의 yarn이라는 툴 도움받아서
//  프로젝트 만들떄
//    yarn create react-app 프로젝트이름
//  원래 프로젝트 실행
//    react-scripts start
//  yarn이라는 툴 도움받는 중이니
//    yarn start -> package.json에 scripts.start에 있는 명령어가 실행
//  포트번호(개발PC -> 그닥 의미는 없음)
//    package.json에 scripts.start 수정
//      set PORT=???? && react-scripts start

function App() {
   return <ChoiInput />;
}

export default App;
