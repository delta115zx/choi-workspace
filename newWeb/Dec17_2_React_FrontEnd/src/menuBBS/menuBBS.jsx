import { useRef, useState } from "react";
import { isEmpty } from "../choi/choiValidCheckerReact";
import mmc from "./menu.module.css";

// export 어쩌고 -> 여러개 export
//      import {어쩌고, ...} from "경로";
// export default 저쩌고 -> 저쩌고만 export
//      import 저쩌고 from "경로";

const MenuBBS = () => {
   const [menu, setMenu] = useState({
      name: "",
      price: "",
      desc: "",
   });

   const nameInput = useRef();
   const priceInput = useRef();
   const descInput = useRef();

   const changeMenu = (e) => {
      setMenu({ ...menu, [e.target.name]: e.target.value });
   };
   const regMenu = () => {
      if (isValid()) {
         alert("AJAX출발");
      }
      //   alert(menu.name);
      //   alert(menu.price);
      //   alert(menu.desc);
   };

   const isValid = () => {
      if (isEmpty(menu.name)) {
         alert("메뉴명?");
         nameInput.current.vlaue = "";
         nameInput.current.focus();
         return false;
      }
      if (isEmpty(menu.price) || menu.price < 0) {
         alert("메뉴가격?");
         priceInput.current.vlaue = "";
         priceInput.current.focus();
         return false;
      }
      if (isEmpty(menu.desc)) {
         alert("메뉴설명?");
         descInput.current.vlaue = "";
         descInput.current.focus();
         return false;
      }
      return true;
   };

   return (
      <>
         메뉴명 :{" "}
         <input
            ref={nameInput}
            className={mmc.txtTypeInput}
            value={menu.name}
            onChange={changeMenu}
            name="name"
            maxLength={30}
         />{" "}
         <br />
         가격 :{" "}
         <input
            ref={priceInput}
            className={mmc.txtTypeInput}
            value={menu.price}
            onChange={changeMenu}
            name="price"
            maxLength={5}
         />{" "}
         <br />
         설명 :{" "}
         <input
            ref={descInput}
            className={mmc.txtTypeInput}
            value={menu.desc}
            onChange={changeMenu}
            name="desc"
            maxLength={100}
         />{" "}
         <br />
         <button onClick={regMenu}>등록</button>
         <hr />
         <table border={1}></table>
      </>
   );
};

export default MenuBBS;
