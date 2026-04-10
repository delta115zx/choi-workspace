import axios from "axios";
import { useEffect, useRef, useState } from "react";
import io from "socket.io-client";
import { isEmpty, isNotNum } from "../choi/choiValidCheckerReact";
import mmc from "./menu.module.css";

// export 어쩌고 -> 여러개 export
//      import {어쩌고, ...} from "경로";
// export default 저쩌고 -> 저쩌고만 export
//      import 저쩌고 from "경로";

const socket = io("http://195.168.9.80:9999/");

// class
const MenuBBS2 = () => {
   // 멤버변수
   const [menu, setMenu] = useState({
      name: "",
      price: "",
      desc: "",
   });
   const [menus, setMenus] = useState([]);
   const menuTrs = menus.map((m, i) => {
      return (
         <tr
            onClick={() => {
               deleteMenu(m.name);
            }}
         >
            <td>{m.name}</td>
            <td>{m.price}</td>
            <td>{m.desc}</td>
         </tr>
      );
   });
   const [page, setPage] = useState(1);
   const [pages, setPages] = useState([]);
   const pagesSpans = pages.map((p, i) => {
      return (
         <span
            onClick={() => {
               setPage(p); // page state바꿈 1 -> 3
               // getMenu(); // 비동기식이라 이 시점의 page state값은 여전히 1
            }}
         >
            &nbsp;{p}&nbsp;
         </span>
      );
   });

   const menuInput = useRef({});
   //메소드
   const changeMenu = (e) => {
      setMenu({ ...menu, [e.target.name]: e.target.value });
   };

   const deleteMenu = (name) => {
      if (confirm("?")) {
         axios
            .get(`http://195.168.9.80:7777/menu.delete?name=${name}`)
            .then((res) => {
               alert(res.data.result);
               if (res.data.result === "삭제 성공") {
                  socket.emit("updated", "delete");
               }
            });
      }
   };

   const getMenu = () => {
      axios
         .get(`http://195.168.9.80:7777/menu.get?pageNo=${page}`)
         .then((res) => {
            setMenus(res.data.menus);
            // res.data.pageCount 4 -> [1,2,3,4]
            const ar = [];
            for (let i = 1; i <= res.data.pageCount; i++) {
               ar.push(i);
            }
            setPages(ar);
         });
   };
   const regMenu = () => {
      if (isValid()) {
         axios
            .get(
               `http://195.168.9.80:7777/menu.reg?name=${menu.name}&price=${menu.price}&desc=${menu.desc}`
            )
            .then((res) => {
               alert(res.data.result);
               if (res.data.result === "등록 성공") {
                  socket.emit("updated", "reg");
               }
            });
         setMenu({ name: "", price: "", desc: "" });
      }
   };

   const isValid = () => {
      if (isEmpty(menu.name)) {
         alert("메뉴명?");
         menuInput.current.name.value = "";
         menuInput.current.name.focus();
         return false;
      }
      if (isEmpty(menu.price) || menu.price < 0 || isNotNum(menu.price)) {
         alert("메뉴가격?");
         menuInput.current.price.value = "";
         menuInput.current.price.focus();
         return false;
      }
      if (isEmpty(menu.desc)) {
         alert("메뉴설명?");
         menuInput.current.desc.value = "";
         menuInput.current.desc.focus();
         return false;
      }
      return true;
   };
   // 생성자
   useEffect(() => {
      socket.on("updatedSrv", (msg) => {
         getMenu();
      });

      return () => {
         socket.off("updatedSrv");
      };
   }, []);

   useEffect(() => {
      getMenu();
   }, [page]);

   return (
      <>
         메뉴명 :{" "}
         <input
            ref={(thisInput) => (menuInput.current.name = thisInput)}
            className={mmc.txtTypeInput}
            value={menu.name}
            onChange={changeMenu}
            name="name"
            maxLength={30}
         />{" "}
         <br />
         가격 :{" "}
         <input
            ref={(thisInput) => (menuInput.current.price = thisInput)}
            className={mmc.txtTypeInput}
            value={menu.price}
            onChange={changeMenu}
            name="price"
            maxLength={5}
         />{" "}
         <br />
         설명 :{" "}
         <input
            ref={(thisInput) => (menuInput.current.desc = thisInput)}
            className={mmc.txtTypeInput}
            value={menu.desc}
            onChange={changeMenu}
            name="desc"
            maxLength={100}
         />{" "}
         <br />
         <button onClick={regMenu}>등록</button>
         <hr />
         <table border={1}>
            <tr>
               <th>메뉴</th>
               <th>가격</th>
               <th>설명</th>
            </tr>
            {menuTrs}
            <tr>
               <td align="center" colSpan={3}>
                  {pagesSpans}
               </td>
            </tr>
         </table>
         <hr />
      </>
   );
};

export default MenuBBS2;
