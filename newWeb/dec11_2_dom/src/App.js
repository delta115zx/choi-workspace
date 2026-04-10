import "./App.css";
import ChoiPropsFifth from "./choiProps/choiPropsFifth";
import ChoiPropsFirst from "./choiProps/choiPropsFirst";
import ChoiPropsFourth from "./choiProps/choiPropsFourth";
import ChoiPropsSecond from "./choiProps/choiPropsSecond";
import ChoiPropsThird from "./choiProps/choiPropsThird";

// <태그명 속성명="값">텍스트</종료태그>

// props(properties)

function App() {
   return (
      <>
         <ChoiPropsFirst namee="홍길동" agee="30" />
         <ChoiPropsFirst namee="김길동" agee="20" />
         <hr />
         <hr />
         <ChoiPropsSecond name="초코파이" price="5000" />
         <ChoiPropsSecond name="빼빼로" price="3000" />
         <hr />
         <ChoiPropsThird namee="마우스" pricee="5000" />
         <ChoiPropsThird namee="키보드" pricee="15000" />
         <hr />
         <ChoiPropsFourth cpu="i7-1234" ram="32" hdd="500" />
         <ChoiPropsFourth cpu="i5-4567" ram="16" hdd="250" />
         <hr />
         <ChoiPropsFifth>홍길동</ChoiPropsFifth>
         <ChoiPropsFifth>김길동</ChoiPropsFifth>
      </>
   );
}

export default App;
