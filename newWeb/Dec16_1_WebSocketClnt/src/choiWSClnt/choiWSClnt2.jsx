import { useEffect } from "react";
import { useState } from "react";
import io from "socket.io-client";
const ChoiWSClnt2 = () => {
   // const [멤버변수, setter메소드] = useState(기본값);
   const [txt, setTxt] = useState(""); // 단순글자값

   // const [socket, setSocket] = useState(io("http://195.168.9.80:9999/")); // 함수 호출
   // 문제는 없는데
   //   React측에서 함수호출(시간이 걸리는)같은거 비추
   //   -> 시간이 걸려서 state 초기값 세팅되고 -> 느려지니
   //   -> useEffect활용 권장

   const [socket, setSocket] = useState();

   useEffect(() => {
      setSocket(io("http://195.168.9.80:9999/"));

      socket.on("test22", (msg) => {
         alert(msg);
      });
   }, []);

   // 이 시점은 소켓 연결되기 전
   // socket.on("test22", (msg) => {
   // alert(msg);
   // });

   return (
      <>
         <input
            value={txt}
            onChange={(e) => {
               setTxt(e.target.value);
            }}
         />
         <button
            onClick={() => {
               socket.emit("test", txt);
               setTxt("");
            }}
         >
            전송
         </button>
      </>
   );
};

export default ChoiWSClnt2;
