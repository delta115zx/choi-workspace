import axios from "axios";
import { useState } from "react";

const ChoiAJAXSecond = () => {
   const [searchTxt, setSearchTxt] = useState("");
   const [books, setBooks] = useState([]);
   const bookTrs = books.map((b) => {
      return (
         <tr>
            <td>
               <img src={b.thumbnail} />
            </td>
            <td>
               {b.title} : {b.price}원
            </td>
         </tr>
      );
   });
   const getBook = () => {
      // GET방식 AJAX
      // axios.get(주소, {headers:{이름:값, 이름:값, ...}}).then(콜백함수);
      axios
         .get(`https://dapi.kakao.com/v3/search/book?query=${searchTxt},`, {
            headers: {
               Authorization: "KakaoAK 51d1ecd7656d567e9e263d69ff1ebbd4",
            },
         })
         .then((res) => {
            setBooks(res.data.documents);
         });
      setSearchTxt("");
   };
   return (
      <>
         <input
            value={searchTxt}
            onChange={(e) => {
               setSearchTxt(e.target.value);
            }}
         />{" "}
         <button onClick={getBook}>검색</button>
         <table border={1}>{bookTrs}</table>
      </>
   );
};

export default ChoiAJAXSecond;
