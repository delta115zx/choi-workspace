import { useSelector } from "react-redux";

// subscriber : state를 사용할 존재
const ChoiH1 = () => {
   // (store) => store.store에 등록해놓은 그 이름
   const h1CSS = useSelector((st) => st.csss);
   const text = useSelector((st) => st.cts);

   return <h1 style={h1CSS}>{text.text}</h1>;
};

export default ChoiH1;
