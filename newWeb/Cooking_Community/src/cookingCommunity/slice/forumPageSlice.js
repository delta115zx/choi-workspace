import { createSlice } from "@reduxjs/toolkit";

const initialState = {
   page: 1,
};

const forumPageSlice = createSlice({
   name: "fps",
   initialState,
   reducers: {
      setpage: (cur, act) => {
         cur.page = act.payload;
      },
   },
});

export const { setpage } = forumPageSlice.actions;

export default forumPageSlice.reducer;
