import axios from "axios";
import { useState } from "react";

const ChoiAJAXPOST2 = () => {
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
      // POST
      //    axios.post(주소, FormData객체, {headers:{이름:값, 이름:값, ...}}).then(콜백함수);
      // 보안강화 POST
      //    axios.post(주소, FormData객체, {headers:{이름:값, 이름:값, ...}, {withCredentials:true}}).then(콜백함수);
      axios
         .post("http://195.168.9.80:7777/calculate.do3", fd, {
            withCredentials: true,
         })
         .then((res) => {
            setResult(res.data)
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

export default ChoiAJAXPOST2;
