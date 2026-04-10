import { useRef } from "react";
import { useState } from "react";
import { isEmpty, isNotType } from "./choiValidCheckerReact";
import axios from "axios";
import { useEffect } from "react";
import { useReducer } from "react";

const ChoiLoL = () => {
   const [allPageCount, setAllPageCount] = useState(1);
   const [page, setPage] = useState(1);
   const [player, setPlayer] = useState({ name: "", nickname: "", photo: "" });
   const playerInput = useRef({});

   const pFD = new FormData();
   pFD.append("name", player.name);
   pFD.append("nickname", player.nickname);
   pFD.append("photo", player.photo);

   const player2add = (cur, pay) => {
      return cur.concat(pay);
   };
   const [player2, setPlayer2] = useReducer(player2add, []);
   const playerTrs = player2.map((p, i) => {
      return (
         <tr
            onClick={() => {
               deletePlayer(p.name);
            }}
         >
            <td>{p.name}</td>
            <td>{p.nickname}</td>
            <td align="center">
               <img
                  style={{ maxWidth: 200 }}
                  src={`http://195.168.9.80:7777/photo.get?filename=${p.photo}`}
               />
            </td>
         </tr>
      );
   });

   const scrollEventtt = () => {
      const htmlHeight = document.documentElement.scrollHeight;
      const browserHeight = window.innerHeight;
      const scrollOffset = window.scrollY;
      const scrollOffsetBottom = scrollOffset + browserHeight;
      if (scrollOffsetBottom >= htmlHeight - 10) {
         setPage(page + 1);
      }
   };

   const deletePlayer = (name) => {
      if (confirm("?")) {
         axios
            .get(`http://195.168.9.80:7777/player.delete?name=${name}`)
            .then((res) => {
               alert(res.data.result);
            });
      }
   };

   const changePlayer = (e) => {
      if (e.target.name === "photo") {
         setPlayer({ ...player, photo: e.target.files[0] });
      } else {
         setPlayer({ ...player, [e.target.name]: e.target.value });
      }
   };

   const isValid = () => {
      if (isEmpty(player.name)) {
         alert("이름?");
         playerInput.current.name.focus();
         return false;
      }
      if (isEmpty(player.nickname)) {
         alert("닉네임?");
         playerInput.current.nickname.focus();
         return false;
      }
      if (
         isEmpty(player.photo) ||
         (isNotType(player.photo, "png") &&
            isNotType(player.photo, "gif") &&
            isNotType(player.photo, "jpg"))
      ) {
         alert("사진?");
         playerInput.current.photo.value = "";
         return false;
      }

      return true;
   };

   const regPlayer = () => {
      if (isValid()) {
         axios
            .post("http://195.168.9.80:7777/player.reg", pFD, {
               headers: { "Content-Type": "multipart/form-data" },
               withCredentials: true,
            })
            .then((res) => {
               alert(res.data.result);
            });
         setPlayer({ name: "", nickname: "", photo: "" });
         playerInput.current.photo.value = "";
         getPlayer();
      }
   };

   const getPlayer = () => {
      axios
         .get(`http://195.168.9.80:7777/player.get?pageNo=${page}`)
         .then((res) => {
            setPlayer2(res.data.player);
            setAllPageCount(res.data.pageCount);
            // setProducts(products.concat(res.data.products));
         });
   };

   useEffect(() => {
      // window.removeEventListener("scroll", scrollEventtt);
      if (page <= allPageCount) {
         getPlayer();
      }
      // window.addEventListener("scroll", scrollEventtt);
   }, [page]);

   useEffect(() => {
      window.addEventListener("scroll", scrollEventtt);

      return () => {
         window.removeEventListener("scroll", scrollEventtt);
      };
   }, [player2]);

   return (
      <>
         선수이름:{" "}
         <input
            ref={(thisInput) => {
               playerInput.current.name = thisInput;
            }}
            name="name"
            value={player.name}
            onChange={changePlayer}
         />{" "}
         <br />
         선수닉네임:{" "}
         <input
            ref={(thisInput) => {
               playerInput.current.nickname = thisInput;
            }}
            name="nickname"
            value={player.nickname}
            onChange={changePlayer}
         />{" "}
         <br />
         선수사진:{" "}
         <input
            ref={(thisInput) => {
               playerInput.current.photo = thisInput;
            }}
            type="file"
            name="photo"
            onChange={changePlayer}
         />{" "}
         <br />
         <button onClick={regPlayer}>등록</button>
         <hr />
         <table border={1}>
            <tr>
               <th>이름</th>
               <th>닉네임</th>
               <th>사진</th>
            </tr>
            {playerTrs}
         </table>
      </>
   );
};

export default ChoiLoL;
