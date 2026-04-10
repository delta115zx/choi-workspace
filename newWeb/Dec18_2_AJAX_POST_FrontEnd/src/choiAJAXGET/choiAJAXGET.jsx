import axios from "axios";
import { useState } from "react";

const ChoiAJAXGET = () => {
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

   const calc = () => {
      axios
         .get(`http://195.168.9.80:7777/calculate.do?x=${xy.x}&y=${xy.y}`)
         .then((res) => {
            setResult(res.data);
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

export default ChoiAJAXGET;
