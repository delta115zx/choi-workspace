import { useEffect } from "react";
import { useState } from "react";
import io from "socket.io-client";

// useEffect로 처리는 가능한데, socket이 바뀔때마다? socket이 안바뀌는데
// -> React state시스템 굳이 사용할 필요 없음
const socket = io("http://195.168.9.80:9999/");

const ChoiWDClnt3 = () => {
   const [msg, setMsg] = useState("");

   useEffect(() => {
      socket.on("test22", (msg22) => {
         alert(msg22);
      });

      return () => {
        socket.off("test22");
      };
   }, []);

   return (
      <>
         <input
            value={msg}
            onChange={(e) => {
               setMsg(e.target.value);
            }}
         />
         <button
            onClick={() => {
               socket.emit("test", msg);
               setMsg("");
            }}
         >
            전송
         </button>
      </>
   );
};

export default ChoiWDClnt3;
