import './App.css';
import Clicker from './clicker';

// 개발끝난 React프로젝트
//      yarn build
//          -> build라는 폴더 생김
//          index.html단독실행은 불가
//          build폴더에 있는 것들을 어떤 웹서버든 업로드해야 작동

function App() {
  return (
    <>
      <Clicker />
      <hr />
      <Clicker />
    </>
  );
}

export default App;
