import { Link, useSearchParams } from "react-router-dom";

const ChoiP6 = () => {
   const [book, setBook] = useSearchParams();
   return (
      <>
         <h1>P6</h1>
         책이름 : {book.get("title")}
         <br />
         가격 : {book.get("price")}
         <br />
         <Link to={"/p7.go"}>P7로</Link>
      </>
   );
};

export default ChoiP6;
