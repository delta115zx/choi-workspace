import axios from "axios";
import { useSelector } from "react-redux";
import io from "socket.io-client";

const socket = io("http://195.168.9.80:9999/");
const ForumPostReply = (props) => {
   const loginMember = useSelector((s) => s.ms.loginMember);
   let btntd = null;

   const deletePostReply = () => {
      if (confirm("삭제?")) {
         axios
            .get(`http://localhost:7777/reply.delete?no=${props.no}`)
            .then((res) => {
               alert(res.data.result);
               socket.emit("postChange");
            });
      }
   };
   if (loginMember.id === props.writer) {
      btntd = (
         <td>
            <button onClick={deletePostReply}>X</button>
         </td>
      );
   }
   return (
      <table className="aForumPostReply">
         <tr>
            <td className="writer" style={{ color: "#" + props.color }}>
               {props.writer}
            </td>
            <td className="txt">{props.children}</td>
            <td className="date">{props.date}</td>
            {btntd}
         </tr>
      </table>
   );
};

export default ForumPostReply;
