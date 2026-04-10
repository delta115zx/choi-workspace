import { useState } from "react";
import "./product.css";

// class
const ProductBBS = () => {
   // memberVar
   const [product, setProduct] = useState({
      name: "",
      price: "",
   });
   const [products, setProducts] = useState([]);
   const productsTr = products.map((p, i) => {
      return (
         <tr
            className="dataTr"
            onClick={() => {
               delProduct(p);
            }}
         >
            <td>{p.name}</td>
            <td>{p.price}</td>
         </tr>
      );
   });

   // method
   const changeProduct = (e) => {
      setProduct({ ...product, [e.target.name]: e.target.value });
   };

   const delProduct = (p) => {
      setProducts(products.filter((pp) => p.name !== pp.name));
   };

   const regProduct = () => {
      // JS배열에 추가
      //    배열[인덱스] = 값;
      //    배열.push(값) : 추가
      //    배열.concat(값) : 추가해서 추가된 배열을 리턴
      setProducts(products.concat(product));
      setProduct({ name: "", price: "" });
   };
   return (
      <div id="productArea">
         품명 :{" "}
         <input
            name="name"
            className="txtType"
            value={product.name}
            onChange={changeProduct}
         />
         <br />
         가격 :{" "}
         <input
            name="price"
            className="txtType"
            value={product.price}
            onChange={changeProduct}
         />
         <br />
         <button onClick={regProduct}>등록</button>
         <hr />
         <table id="productBBSTbl" border={1}>
            <tr>
               <th>품명</th>
               <th>가격</th>
            </tr>
            {productsTr}
         </table>
      </div>
   );
};

export default ProductBBS;
