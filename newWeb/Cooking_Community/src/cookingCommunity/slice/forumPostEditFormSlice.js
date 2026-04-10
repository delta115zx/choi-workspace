import { createSlice } from "@reduxjs/toolkit";

const initialState = {
   css: {
      top: "-100%",
      left: "-100%",
   },
   content: {
      no: "",
      writer: "",
      txt: "",
   },
};

const forumPostEditFormSlice = createSlice({
   name: "fpefs",
   initialState,
   reducers: {
      EditSummon: (cur, act) => {
         cur.css = { top: 0, left: 0 };
      },
      EditHide: (cur, act) => {
         cur.css = { top: "-100%", left: "-100%" };
      },
      setContent: (cur, act) => {
         cur.content = {
            no: act.payload.no,
            writer: act.payload.writer,
            txt: act.payload.txt,
         };
      },
   },
});

export const { EditSummon, EditHide, setContent } =
   forumPostEditFormSlice.actions;

export default forumPostEditFormSlice.reducer;
