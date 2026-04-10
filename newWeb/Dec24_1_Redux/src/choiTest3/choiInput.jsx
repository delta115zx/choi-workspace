import { useDispatch, useSelector } from "react-redux";
import { setText } from "../choiTextSlice";

const ChoiInput = () => {
   const text = useSelector((st) => st.cts);
   const d = useDispatch();
   return (
      <input
         value={text.text}
         onChange={(e) => {
            d(setText(e.target.value));
         }}
      />
   );
};

export default ChoiInput;
