import { useSelector } from "react-redux"

const ChoiH2 = () => {
  const text = useSelector((st) => st.cts);
  return (
    <h2>{text.text}</h2>
  )
}

export default ChoiH2