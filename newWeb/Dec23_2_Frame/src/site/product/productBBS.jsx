import { useState } from "react";
import "./product.css";

const ProductBBS = () => {
   const [product, setProduct] = useState({
      name: "",
      price: "",
   });

   const changeProduct = (e) => {
      setProduct({ ...product, [e.target.name]: e.target.value });
   };

   const showProduct = () => {
      alert(product.name);
      alert(product.price);
      setProduct({ name: "", price: "" });
   };
   return (
      <div id="productRegArea">
         품명 :{" "}
         <input
            className="txtType"
            name="name"
            value={product.name}
            onChange={changeProduct}
         />
         <br />
         가격 :{" "}
         <input
            className="txtType"
            name="price"
            value={product.price}
            onChange={changeProduct}
         />
         <br />
         <button onClick={showProduct}>등록</button>
      </div>
   );
};

export default ProductBBS;
