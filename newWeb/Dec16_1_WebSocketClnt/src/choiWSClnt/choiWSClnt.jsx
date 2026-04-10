// 라이브러리 설치
//      yarn add ???

import { useState } from "react";
import { useEffect } from "react";
import io from "socket.io-client";
// 1) index.html에 Node.js웹소켓 js파일 넣고...
// 2) Node.js에 있는 socket.io클라이언트라이브러리
//      yarn add socket.io-client@2

// react.js만 html에 넣고
// Node.js -> yarn -> vite를 써서 프로젝트 만들고
const ChoiWSClnt = () => {
   const [socket, setSocket] = useState();

   useEffect(() => {
      // var socket = io.connect("http://195.168.9.80:9999/");
      // socket.emit("test", "ㅋㅋㅋ")
      setSocket(io("http://195.168.9.80:9999/"));
   }, []);

   return (
      <>
         <button
            onClick={() => {
               socket.emit("test", "abcd");
               socket.on("test22", (msg) => {
                  alert(msg);
               });
            }}
         >
            전송
         </button>
      </>
   );
};

export default ChoiWSClnt;
