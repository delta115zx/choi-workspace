import axios from "axios";
import { useState } from "react";

const ProductBBS = () => {
   const [product, setProduct] = useState({ name: "", price: "" });

   const changeProduct = (e) => {
      setProduct({ ...product, [e.target.name]: e.target.value });
   };

   const productReg = () => {
      axios
         .get(
            `http://195.168.9.80:7777/product.reg?name=${product.name}&price=${product.price}`
         )
         .then((res) => {
            // sessionStorage : 브라우저 닫을때까지 쓸수있는 공간
            // -> 다른 페이지에서도 쓸수있게
            sessionStorage.setItem("myJWT", res.data.choiJWT); // 여기서는 복호화불가
            setProduct({ name: "", price: "" });
         });
   };

   const showProduct = () => {
      alert(sessionStorage.getItem("myJWT"));
   };

   const showProduct2 = () => {
      axios
         .get(
            `http://195.168.9.80:7777/product.get?jwt=${sessionStorage.getItem(
               "myJWT"
            )}`
         )
         .then((res) => {
            alert(JSON.stringify(res.data));
         });
   };

   const updateJWT = () => {
      axios
         .get(
            `http://195.168.9.80:7777/product.jwt.update?jwtt=${sessionStorage.getItem(
               "myJWT"
            )}`
         )
         .then((res) => {
            alert(JSON.stringify(res.data));
            sessionStorage.setItem("myJWT", res.data.choiJWT);
         });
   };

   const deleteJWT = () => {
      sessionStorage.removeItem("myJWT");
   };

   return (
      <>
         이름 :{" "}
         <input name="name" value={product.name} onChange={changeProduct} />{" "}
         <br />
         가격 :{" "}
         <input name="price" value={product.price} onChange={changeProduct} />
         <br />
         <button onClick={productReg}>JWT만들기</button>
         <button onClick={showProduct}>JWT확인하기</button>
         <button onClick={showProduct2}>JWT복호화하기</button>
         <button onClick={updateJWT}>JWT갱신하기</button>
         <button onClick={deleteJWT}>JWT삭제하기</button>
         <hr />
      </>
   );
};

export default ProductBBS;
