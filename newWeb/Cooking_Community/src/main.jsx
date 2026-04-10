import { BrowserRouter } from "react-router-dom";
import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import App from "./App.jsx";
import "./index.css";
import { configureStore } from "@reduxjs/toolkit";
import loginSystemSummonSlice from "./cookingCommunity/slice/loginSystemSummonSlice.js";
import memberSlice from "./cookingCommunity/slice/memberSlice.js";
import forumPostEditFormSlice from "./cookingCommunity/slice/forumPostEditFormSlice.js";
import forumPageSlice from "./cookingCommunity/slice/forumPageSlice.js";

const CCStore = configureStore({
   reducer: {
      lsss: loginSystemSummonSlice,
      ms: memberSlice,
      fpefs: forumPostEditFormSlice,
      fps: forumPageSlice,
   },
});

createRoot(document.getElementById("root")).render(
   <Provider store={CCStore}>
      <BrowserRouter>
         <App />
      </BrowserRouter>
   </Provider>
);
