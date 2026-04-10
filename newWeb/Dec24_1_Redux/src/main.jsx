import { configureStore } from "@reduxjs/toolkit";
import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import App from "./App.jsx";
import choiSizeSlice from "./choiSizeSlice.js";
import choiTextSlice from "./choiTextSlice.js";
import "./index.css";

// store에 등록된 slice만 사용가능
const choiStore = configureStore({
   reducer: {
      csss: choiSizeSlice, // csss로 호출해서 사용
      cts: choiTextSlice,
   },
});

createRoot(document.getElementById("root")).render(
   <Provider store={choiStore}>
      <App />
   </Provider>
);
