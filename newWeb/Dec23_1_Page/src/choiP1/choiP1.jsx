import { Link } from "react-router-dom";

const ChoiP1 = () => {
   return (
      <>
         <h1>P1</h1>
         <a href="p2.go">P2로</a>
         <br />
         <Link to={"/p2.go"}>P2로</Link>
      </>
   );
};

export default ChoiP1;
