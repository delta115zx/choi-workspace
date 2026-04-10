import { useEffect } from "react";
import { useState } from "react";
import { useRef } from "react";
import io from "socket.io-client";

const socket = io("http://195.168.9.80:8888/");

const ChoiCanvasEx = () => {
   const [drawMode, setDrawMode] = useState(false);
   const paper = useRef();
   const [pen, setPen] = useState();
   const [startXY, setStartXY] = useState({ x: 0, y: 0 });

   useEffect(() => {
      socket.on("xy2", (xy2) => {
         pen.beginPath();
         pen.moveTo(xy2.sx, xy2.sy);
         pen.lineTo(xy2.ex, xy2.ey);
         pen.closePath();
         pen.stroke();
      });

      return () => {
         socket.off("xy2");
      };
   }, [pen]);

   useEffect(() => {
      // const pen = paper.current.getContext("2d")
      setPen(paper.current.getContext("2d"));
   }, []);

   const drawStart = (e) => {
      setDrawMode(true);
      setStartXY({ x: e.nativeEvent.offsetX, y: e.nativeEvent.offsetY });
   };

   const draw = (e) => {
      if (drawMode) {
         const endX = e.nativeEvent.offsetX;
         const endY = e.nativeEvent.offsetY;
         socket.emit("xy", {
            sx: startXY.x,
            sy: startXY.y,
            ex: endX,
            ey: endY,
         });
         // pen.beginPath();
         // pen.moveTo(startXY.x, startXY.y);
         // pen.lineTo(endX, endY);
         // pen.closePath();
         // pen.stroke();
         setStartXY({ x: e.nativeEvent.offsetX, y: e.nativeEvent.offsetY });
      }
   };

   const drawEnd = () => {
      setDrawMode(false);
   };

   return (
      <canvas
         ref={paper}
         style={{ border: "black solid 2px" }}
         width={300}
         height={300}
         onMouseDown={drawStart}
         onMouseMove={draw}
         onMouseUp={drawEnd}
      ></canvas>
   );
};

export default ChoiCanvasEx;
