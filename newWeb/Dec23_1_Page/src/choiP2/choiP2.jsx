import { useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

const ChoiP2 = () => {
   const [product, setProduct] = useState({ name: "", price: "" });
   const productChange = (e) => {
      setProduct({ ...product, [e.target.name]: e.target.value });
   };

   const productReg = () => {
      axios
         .get(
            `http://195.168.9.80:7777/product.reg?name=${product.name}&price=${product.price}`
         )
         .then((res) => {
            sessionStorage.setItem("productInfo", res.data.token);
            setProduct({ name: "", price: "" });
         });
   };
   return (
      <>
         <h1>P2</h1>
         품명 :{" "}
         <input name="name" value={product.name} onChange={productChange} />
         <br />
         가격 :{" "}
         <input name="price" value={product.price} onChange={productChange} />
         <br />
         <button onClick={productReg}>등록</button>
         <hr />
         <Link to="/p3.go">P3로</Link>
      </>
   );
};

export default ChoiP2;
