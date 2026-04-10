import { Navigate } from "react-router-dom";

const ChoiP7 = () => {
   if (Math.random() > 0.5) {
      return <Navigate to={"/p8.go"} replace />; // redirect(강제이동)
   }
   return <div>ChoiP7</div>;
};

export default ChoiP7;
