import { Link, useParams } from "react-router-dom";

const Choip4 = () => {
   const student = useParams(); // 주소스타일로 넘어오는 값
   return (
      <>
         <h1>P4</h1>
         이름 : {student.namee}
         <br />
         나이 : {student.agee}
         <hr />
         <Link to={"/p5.go?namee=짜장면&pricee=6000"}>P5로</Link>
         <br />
         <Link to={"/p5.go?namee=짬뽕&pricee=6500"}>P5로</Link>
      </>
   );
};

export default Choip4;
