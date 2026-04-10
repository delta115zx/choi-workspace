import { Route, Routes } from "react-router-dom";
import "./App.css";
import CookingCommunityMain from "./cookingCommunity/cookingCommunityMain";
import Forum from "./cookingCommunity/layout/content/forum/forum";
import Home from "./cookingCommunity/layout/content/home/home";
import MemberInfo from "./cookingCommunity/layout/content/member/memberInfo";
import SignUpFormEx from "./cookingCommunity/layout/content/member/signUpFormex";

function App() {
   return (
      <Routes>
         <Route element={<CookingCommunityMain />}>
            <Route path="/" element={<Home />} />
            <Route path="/signup.go" element={<SignUpFormEx />} />
            <Route path="/memberinfo.go" element={<MemberInfo />} />
            <Route path="/forum.go" element={<Forum />} />
         </Route>
      </Routes>
   );
}

export default App;
