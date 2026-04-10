import { useEffect } from "react";
import { useState } from "react";
import { useRef } from "react";
import io from "socket.io-client";

const socket = io("http://195.168.9.80:8888/");

const ChoiCanvas = () => {
   const paper = useRef();
   const [pen, setPen] = useState({
      drawMode: false,
      startX: "",
      startY: "",
      endX: "",
      endY: "",
   });

   useEffect(() => {
      socket.on("xy2", (xyxy) => {
         pen.beginPath();
         pen.moveTo(xyxy.sx, xyxy.sy);
         pen.lineTo(xyxy.ex, xyxy.ey);
         pen.closePath();
         pen.stroke();
      });

      return () => {
         socket.off("xy2");
      };
   }, [pen]);

   useEffect(() => {
      setPen(paper.current.getContext("2d"));
      return () => {};
   }, []);

   return (
      <canvas
         ref={paper}
         style={{ border: "black solid 2px" }}
         width={300}
         height={300}
         onMouseDown={(e) => {
            setPen({
               ...pen,
               drawMode: true,
               startX: e.nativeEvent.offsetX,
               startY: e.nativeEvent.offsetY,
            });
         }}
         onMouseMove={(e) => {
            if (pen.drawMode) {
               setPen({
                  ...pen,
                  endX: e.nativeEvent.offsetX,
                  endY: e.nativeEvent.offsetY,
               });
               let data = {
                  sx: pen.startX,
                  sy: pen.startY,
                  ex: pen.endX,
                  ey: pen.endY,
               };
               socket.emit("xy", data);
               setPen({
                  ...pen,
                  startX: e.nativeEvent.clientX,
                  startY: e.nativeEvent.clientY,
               });
            }
         }}
         onMouseUp={() => {
            setPen({ ...pen, drawMode: false });
         }}
      ></canvas>
   );
};

export default ChoiCanvas;
