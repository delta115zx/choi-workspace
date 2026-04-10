import { useState } from "react";

const ChoiKeyboardEvent = () => {
   const [eventInfo, setEventInfo] = useState("");
   const [keyInfo, setKeyInfo] = useState("");

   return (
      <>
         <input
            onKeyDown={(e) => {
               setEventInfo("keydown");
               setKeyInfo(e.key);
            }}
            onKeyUp={(e) => {
               setEventInfo("keyup");
               setKeyInfo(e.key);
            }}
         />
         <h2>{eventInfo}</h2>
         <h2>{keyInfo}</h2>
      </>
   );
};

export default ChoiKeyboardEvent;
