import { useDispatch } from "react-redux";
import { sizeDownn, sizeUpp } from "../choiSizeSlice";

// dispatcher : state를 바꿔줄 존재
const ChoiBtns = () => {
   const d = useDispatch();

   return (
      <>
         <button
            onClick={() => {
               d(sizeUpp()); // d(slice쪽 reducer함수)
            }}
         >
            크게
         </button>
         <button
            onClick={() => {
               d(sizeDownn());
            }}
         >
            작게
         </button>
      </>
   );
};

export default ChoiBtns;
