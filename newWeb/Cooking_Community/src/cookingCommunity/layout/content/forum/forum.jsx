/* eslint-disable react-hooks/globals */
/* eslint-disable react-refresh/only-export-components */
import axios from "axios";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import io from "socket.io-client";
import { setpage } from "../../../slice/forumPageSlice";
import { isEmpty, lessThen } from "../member/choiValidCheckerReact";
import ForumPost, { setReplys2 } from "./forumPost";
import s from "./img/search.png";
import w from "./img/write.png";

const socket = io("http://195.168.9.80:9999/");
export let getPost;

const Forum = () => {
   const [borderCSS, setBorderCSS] = useState({ border: "black solid 3px" });
   const [borderCSS2, setBorderCSS2] = useState({ backgroundColor: "white" });
   const [fontColorCSS, setFontColorCSS] = useState({
      color: "black",
      fontsize: "12pt",
   });
   const [post, setPost] = useState({ color: "000000", txt: "" });
   const [searchTxt, setSearchTxt] = useState("");

   // const post2add = (cur, pay) => {
   //    return cur.concat(pay);
   // };
   // const [posts, setPosts] = useReducer(post2add, []);

   const [allPageCount, setAllPageCount] = useState(1);
   const [posts, setPosts] = useState([]);

   const page = useSelector((s) => s.fps.page);
   const d = useDispatch();

   const postsDOM = posts.map((p, i) => {
      return (
         <ForumPost
            no={p.no}
            writer={p.writer}
            photo={p.photo}
            date={p.date}
            color={p.color}
            replys={p.replys}
         >
            {p.txt}
         </ForumPost>
      );
   });

   const changePost = (e) => {
      setPost({ ...post, [e.target.name]: e.target.value });
      if (e.target.name === "color") {
         setFontColorCSS({ ...fontColorCSS, color: "#" + e.target.value });
         setBorderCSS({ border: "#" + e.target.value + " solid 3px" });
         setBorderCSS2({ backgroundColor: "#" + e.target.value });
      }
   };

   getPost = () => {
      axios
         .get(
            `http://localhost:7777/post.get?searchTxt=${searchTxt}&pageNo=${page}`
         )
         .then((res) => {
            if (res.data.result === "조회 실패") {
               alert(res.data.result);
            } else {
               setPosts(res.data.result);
               // alert(JSON.stringify(res.data.result));
               setAllPageCount(res.data.pageCount);
            }
         });
   };

   const goPrevPage = () => {
      if (page > 1) {
         d(setpage(page - 1));
      }
   };

   const goNextPage = () => {
      if (page < allPageCount) d(setpage(page + 1));
   };

   const isValid = () => {
      if (isEmpty(post.color) || lessThen(post.color, 6) || isEmpty(post.txt)) {
         alert("?");
         setPost({ color: "000000", txt: "" });
         return false;
      }
      return true;
   };

   // const scrollEventtt = () => {
   //    const htmlHeight = document.documentElement.scrollHeight;
   //    const browserHeight = window.innerHeight;
   //    const scrollOffset = window.scrollY;
   //    const scrollOffsetBottom = scrollOffset + browserHeight;
   //    if (scrollOffsetBottom >= htmlHeight - 10) {
   //       setPage(page + 1);
   //    }
   // };

   // const searchPost = () => {
   //    axios
   //       .get(
   //          `http://localhost:7777/post.search?searchTxt=${searchTxt}&pageNo=${1}`
   //       )
   //       .then((res) => {
   //          setPosts(res.data.result);
   //          setAllPageCount(res.data.pageCount);
   //       });
   // };

   const writePost = () => {
      if (isValid()) {
         axios
            .get(
               `http://localhost:7777/post.write?color=${
                  post.color
               }&txt=${JSON.stringify(
                  post.txt
               )}&member=${sessionStorage.getItem("loginMember")}`
            )
            .then((res) => {
               alert(res.data.result);
               setPost({ color: "000000", txt: "" });
               setFontColorCSS({ ...fontColorCSS, color: "#000000" });
               setBorderCSS({ border: "#000000 solid black" });
               setBorderCSS2({ backgroundColor: "#000000" });
               socket.emit("postChange");
            });
      }
   };

   useEffect(() => {
      getPost();

      return () => {};
   }, [page]);

   useEffect(() => {
      socket.on("postChange2", () => {
         getPost();
      });

      return () => {
         socket.off("postChange2");
      };
   }, []);

   // useEffect(() => {
   //    window.addEventListener("scroll", scrollEventtt);

   //    return () => {
   //       window.removeEventListener("scroll", scrollEventtt);
   //    };
   // }, [posts]);

   return (
      <>
         {postsDOM}
         <div id="postPageL" onClick={goPrevPage}></div>
         <div id="postPageR" onClick={goNextPage}></div>
         <div id="postBlankArea"></div>
         <table id="siteForumSnWArea" style={borderCSS}>
            <tr>
               <td>
                  <input
                     id="searchInput"
                     value={searchTxt}
                     onChange={(e) => {
                        setSearchTxt(e.target.value);
                     }}
                     placeholder="검색"
                     onKeyUp={(e) => {
                        if (e.key === "Enter") {
                           getPost();
                           setSearchTxt("");
                        }
                     }}
                  />
               </td>
               <td>
                  <img id="searchImg" src={s} onClick={getPost} />
               </td>
            </tr>
            <tr>
               <td colSpan={2} style={borderCSS2}></td>
            </tr>
            <tr>
               <td style={fontColorCSS}>
                  &nbsp;&nbsp;#
                  <input
                     id="colorInput"
                     name="color"
                     style={fontColorCSS}
                     placeholder="RRGGBB"
                     value={post.color}
                     maxLength={6}
                     onChange={changePost}
                     autoComplete="off"
                  />
               </td>
            </tr>
            <tr>
               <td>
                  <textarea
                     id="writeInput"
                     name="txt"
                     value={post.txt}
                     onChange={changePost}
                     placeholder="글 내용"
                     autoComplete="off"
                  />
               </td>
               <td>
                  <img id="writeImg" src={w} onClick={writePost} />
               </td>
            </tr>
         </table>
      </>
   );
};

export default Forum;
