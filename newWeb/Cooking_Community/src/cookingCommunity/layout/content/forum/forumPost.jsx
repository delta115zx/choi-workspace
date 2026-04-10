/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable react-hooks/set-state-in-effect */
/* eslint-disable react-refresh/only-export-components */ /* eslint-disable react-hooks/globals */
import axios from "axios";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import io from "socket.io-client";
import { EditSummon, setContent } from "../../../slice/forumPostEditFormSlice";
import w from "./img/write.png";
import c from "./img/delete.png";
import ForumPostEditForm from "./forumPostEditForm";
import ForumPostReply from "./forumPostReply";
import { isEmpty } from "../member/choiValidCheckerReact";

const socket = io("http://195.168.9.80:9999/");
export let setReplys2;

const ForumPost = (props) => {
   const d = useDispatch();
   let btnTd = null;
   // let txtTd = null;
   const loginMember = useSelector((s) => s.ms.loginMember);
   const [postCSS, setPostCSS] = useState({ opacity: 1 });
   const [txtCSS, setTxtCSS] = useState({ opacity: 1 });
   const [replyTxt, setReplyTxt] = useState("");
   const [replys, setReplys] = useState([]);
   // const page = useSelector((s) => s.fps.page);

   // const replyDOM = replys.map((r, i) => (
   //    <ForumPostReply
   //       no={r.no}
   //       writer={r.writer}
   //       date={r.date}
   //       color={r.color}
   //       r_p_no={r.r_p_no}
   //    >
   //       {r.txt}
   //    </ForumPostReply>
   // ));

   const replyDOM = replys.map((r, i) => {
      return (
         <ForumPostReply
            no={r.no}
            writer={r.writer}
            date={r.date}
            color={r.color}
         >
            {" "}
            {r.txt}
         </ForumPostReply>
      );
   });

   // const [editTxt, setEditTxt] = useState("");

   // const changeEditTxt = (e) => {
   //    setEditTxt(e.target.value);
   // };
   const changeReplyTxt = (e) => {
      setReplyTxt(e.target.value);
   };

   const summonPostEditForm = () => {
      d(
         setContent({ no: props.no, writer: props.writer, txt: props.children })
      );
      d(EditSummon());
   };

   const hidePost = () => {
      setPostCSS({ opacity: 0 });
   };
   const showPost = () => {
      setPostCSS({ opacity: 1 });
   };
   const hideTxt = () => {
      setTxtCSS({ opacity: 0 });
   };
   const showTxt = () => {
      setTxtCSS({ opacity: 1 });
   };

   // const showAndHideTxt = () => {
   //    if (txtCSS.opacity === 1) {
   //       hideTxt();
   //    } else if (txtCSS.opacity === 0) {
   //       showTxt();
   //    }
   // };

   const deletePost = () => {
      if (confirm("삭제?")) {
         axios
            .get(`http://localhost:7777/post.delete?no=${props.no}`)
            .then((res) => {
               alert(res.data.result);
               socket.emit("postChange");
            });
      }
   };

   setReplys2 = () => {
      setReplys(props.replys);
   };

   // const getReply = () => {
   //    axios
   //       .get(`http://localhost:7777/reply.get?r_p_no=${props.no}`)
   //       .then((res) => {
   //          setReplys(res.data.result);
   //       });
   // };

   const writeReply = () => {
      if (isValid) {
         axios
            .get(
               `http://localhost:7777/reply.write?writer=${sessionStorage.getItem(
                  "loginMember"
               )}&color=${props.color}&txt=${replyTxt}&r_p_no=${props.no}`
            )
            .then((res) => {
               alert(res.data.result);
               setReplyTxt("");
               socket.emit("postChange");
            });
      }
   };

   // const editPost = () => {
   //    axios
   //       .get(
   //          `http://localhost:7777/post.edit?no=${
   //             props.no
   //          }&txt=${JSON.stringify(editTxt)}`
   //       )
   //       .then((res) => {
   //          alert(res.data.result);
   //          showTxt();
   //          socket.emit("postChange");
   //       });
   // };

   const isValid = () => {
      if (isEmpty(replyTxt)) {
         alert("댓글?");
         return false;
      }
      return true;
   };

   useEffect(() => {
      setReplys(props.replys);
   });

   // useEffect(() => {
   //    setReplys(props.replys);
   // }, [page]);

   if (loginMember === undefined) {
      btnTd = null;
   } else if (loginMember.id === props.writer) {
      btnTd = (
         <td align="right">
            <img
               src={w}
               onMouseEnter={hideTxt}
               onMouseLeave={showTxt}
               onClick={summonPostEditForm}
            />
            &nbsp;&nbsp;&nbsp;&nbsp;
            <img
               src={c}
               onMouseEnter={hidePost}
               onMouseLeave={showPost}
               onClick={deletePost}
            />
         </td>
      );
   }

   // if (txtCSS.opacity === 1) {
   //    txtTd = (
   //       <td className="txtTd" style={txtCSS}>
   //          {props.children}
   //       </td>
   //    );
   // }  else if (txtCSS.opacity === 0) {
   //    txtTd = (
   //       <td className="txtTd">
   //          <textarea
   //             name="editTxt"
   //             className="editTxt"
   //             onChange={changeEditTxt}
   //          ></textarea>
   //          <img src={w} onClick={editPost} />
   //       </td>
   //    );
   // }
   return (
      <>
         <ForumPostEditForm />
         <table className="aForumPost" border={1} style={postCSS}>
            <tr>
               <td
                  className="titleTd"
                  style={{ backgroundColor: "#" + props.color + "99" }}
               >
                  <table className="titleTdTbl">
                     <tr>
                        <td>
                           <table>
                              <tr>
                                 <td className="writerTd">{props.writer}</td>
                              </tr>
                           </table>
                        </td>
                        {btnTd}
                     </tr>
                  </table>
               </td>
            </tr>
            <tr>
               <td className="contentTd">
                  <table className="contentTdTbl">
                     <tr>
                        <td
                           rowSpan={3}
                           align="center"
                           className="imgTd"
                           style={{
                              borderRight: "#" + props.color + "88 solid 3px",
                           }}
                        >
                           <img
                              src={`http://localhost:7777/member.info.photo.get?file=${props.photo}`}
                           />
                        </td>
                        <td align="left" className="dateTd">
                           {props.date}
                        </td>
                     </tr>
                     <tr>
                        <td className="txtTd" style={txtCSS}>
                           {props.children}
                        </td>
                     </tr>
                     <tr>
                        <td className="replyTd">
                           {replyDOM}
                           <table className="aForumPostReply">
                              <tr>
                                 <td
                                    className="writer"
                                    style={{ color: "#" + props.color }}
                                 >
                                    {loginMember.id}
                                 </td>
                                 <td className="txt">
                                    <input
                                       value={replyTxt}
                                       onChange={changeReplyTxt}
                                       placeholder="댓글"
                                       autoComplete="off"
                                    />
                                 </td>
                                 <td>
                                    <button onClick={writeReply}>쓰기</button>
                                 </td>
                              </tr>
                           </table>
                        </td>
                     </tr>
                  </table>
               </td>
            </tr>
         </table>
      </>
   );
};

export default ForumPost;
