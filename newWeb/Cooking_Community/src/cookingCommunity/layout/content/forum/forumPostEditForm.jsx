import { useDispatch, useSelector } from "react-redux";
import c from "./img/delete.png";
import w from "./img/write.png";
import { EditHide, setContent } from "../../../slice/forumPostEditFormSlice";
import axios from "axios";
import io from "socket.io-client";
import { isEmpty } from "../member/choiValidCheckerReact";

const socket = io("http://195.168.9.80:9999/");

const ForumPostEditForm = () => {
   const fpefCSS = useSelector((s) => s.fpefs.css);
   const content = useSelector((s) => s.fpefs.content);
   const d = useDispatch();

   const changeContent = (e) => {
      d(setContent({ ...content, txt: e.target.value }));
   };
   const hidePostEditForm = () => {
      d(EditHide());
   };

   const editPost = () => {
      if (isValid) {
         axios
            .get(
               `http://localhost:7777/post.edit?no=${
                  content.no
               }&txt=${JSON.stringify(content.txt)}`
            )
            .then((res) => {
               alert(res.data.result);
               socket.emit("postChange");
               d(EditHide());
            });
      }
   };

   const isValid = () => {
      if (isEmpty(content.txt)) {
         alert("?");
         return false;
      }
      return true;
   };

   return (
      <table id="ForumPostUpdateArea" style={fpefCSS}>
         <tr>
            <td align="center">
               <table id="forumPostUpdateForm">
                  <tr className="writerArea">
                     <td className="writer">{content.writer}</td>
                     <td align="right" className="closeImg">
                        <img src={c} onClick={hidePostEditForm} />
                     </td>
                  </tr>
                  <tr>
                     <td>
                        <textarea
                           value={content.txt}
                           onChange={changeContent}
                        />
                     </td>
                     <td id="imgTd" align="center" onClick={editPost}>
                        <img id="editImg" src={w} />
                     </td>
                  </tr>
               </table>
            </td>
         </tr>
      </table>
   );
};

export default ForumPostEditForm;
