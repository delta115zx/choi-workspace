import { useEffect } from "react";
import cdtmc from "./cdt.module.css";

const ChoiDesignThird = () => {
   useEffect(() => {
      const h = 180;
      const w = 80;

      // alert("키는" + h + "cm고, 몸무게는 " + w + "kg다");
      // ` : backtick
      alert(`키는 ${h}cm고, 몸무게는 ${w}kg다`);

      return () => {};
   }, []);

   return (
      <div className={`${cdtmc.a} ${cdtmc.b} ${cdtmc.c}`}>ChoiDesignThird</div>
   );
};

export default ChoiDesignThird;
