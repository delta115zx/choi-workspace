import { Link, useNavigate, useSearchParams } from "react-router-dom";

const ChoiP5 = () => {
   // 요청파라메터스타일로 넘어오는 값
   const [menu, setMenu] = useSearchParams();
   const n = useNavigate(); // JS소스로 이동

   return (
      <>
         <h1>P5</h1>
         메뉴명 : {menu.get("namee")}
         <br />
         가격 : {menu.get("pricee")}
         <hr />
         <Link to={"/p6.go?title=삼국지&price=10000"}>P6으로</Link>
         <br />
         <Link to={"/p6.go?title=파이썬&price=20000"}>P6으로</Link>
         <br />
         <button
            onDoubleClick={() => {
               n("/p6.go?title=리액트&price=30000");
               // n(-2); 2번뒤로
            }}
         >
            P6으로
         </button>
      </>
   );
};

export default ChoiP5;
