import { createSlice } from "@reduxjs/toolkit";

const initialState = {
   text: "ㅋㅋㅋ",
};

const choiTextSlice = createSlice({
   name: "ctssss",
   initialState,
   reducers: {
      setText: (cur, ac) => {
         // ac.payload : dispatcher 쪽에서 보내준 값
         cur.text = ac.payload;
      },
   },
});

export const { setText } = choiTextSlice.actions;

export default choiTextSlice.reducer;
