import axios from "axios";
import { Link } from "react-router-dom";

const ChoiP3 = () => {
   const showProduct = () => {
      axios
         .get(
            `http://195.168.9.80:7777/product.get?jwt=${sessionStorage.getItem(
               "productInfo"
            )}`
         )
         .then((res) => {
            alert(res.data.name + " : " + res.data.price);
         });
   };

   return (
      <>
         <h1>P3</h1>
         <button onClick={showProduct}>등록한거 확인</button>
         <hr />
         <Link to={"/p4.go/홍길동/30"}>P4로</Link>
         <br />
         <Link to={"/p4.go/김길동/20"}>P4로</Link>
         <br />
         <a href="/p4.go/이길동/10">P4로</a>
      </>
   );
};

export default ChoiP3;
