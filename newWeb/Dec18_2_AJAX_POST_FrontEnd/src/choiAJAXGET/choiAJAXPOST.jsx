import axios from "axios";
import { useState } from "react";

const ChoiAJAXPOST = () => {
   const [xy, setXy] = useState({ x: "", y: "" });
   const [result, setResult] = useState({
      hab: "",
      cha: "",
      gob: "",
      moks: "",
   });

   const changeXY = (e) => {
      setXy({ ...xy, [e.target.name]: e.target.value });
   };

   const fd = new FormData();
   fd.append("x", xy.x); // fd.append("요청파라메터명", 값);
   fd.append("y", xy.y);

   const calc = () => {
      // GET
      //    요청파라메터가 주소에 실려서 전달
      //    axios.get(주소요청param까지다포함된주소, {headers:{이름:값, 이름:값, ...}}).then(콜백함수);
      // POST
      //    요청파라메터가 내부적으로 전달
      //    GET방식보다 보안 우수
      //    주소에 실을수없는 파라메터(체크박스, 파일, ...)
      //    axios.post(주소, FormData객체, {headers:{이름:값, 이름:값, ...}}).then(콜백함수);
      axios.post("http://195.168.9.80:7777/calculate.do2", fd).then((res) => {
         alert(JSON.stringify(res.data));
      });
   };
   return (
      <>
         x: <input name="x" value={xy.x} onChange={changeXY} />
         <br />
         y: <input name="y" value={xy.y} onChange={changeXY} />
         <br />
         <button onClick={calc}>계산</button>
         <hr />합 : {result.hab} <br />차 : {result.cha} <br />곱 : {result.gob}{" "}
         <br />몫 : {result.moks} <br />
      </>
   );
};

export default ChoiAJAXPOST;
