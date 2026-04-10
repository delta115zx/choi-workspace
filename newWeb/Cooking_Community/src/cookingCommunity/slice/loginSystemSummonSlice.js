import { createSlice } from "@reduxjs/toolkit";

const initialState = {
   top: -400,
   opacity: 0,
};

const loginSystemSummonSlice = createSlice({
   name: "fdzz",
   initialState,
   reducers: {
      summon: (cur) => {
         if (cur.top === -400) {
            cur.top = 0;
            cur.opacity = 1;
         } else {
            cur.top = -400;
            cur.opacity = 0;
         }
      },
      hide: (cur) => {
         cur.top = -400;
         cur.opacity = 0;
      },
   },
});

export const { summon, hide } = loginSystemSummonSlice.actions;

export default loginSystemSummonSlice.reducer;
