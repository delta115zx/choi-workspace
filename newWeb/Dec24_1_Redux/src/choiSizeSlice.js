// state : 상태
// reducer : 기존state값+action 넣어주면, state를 바꿔주는 함수
// action : 액션
// slice : reducer + action

// rxslice

import { createSlice } from "@reduxjs/toolkit";

const initialState = {
   fontSize: 30,
};

const choiSizeSlice = createSlice({
   name: "cssssss", // 대충 지어도(나중에 이 이름으로 안부름)
   initialState,
   reducers: {
      sizeUpp: (curStateee) => {
         curStateee.fontSize += 5;
      },
      sizeDownn: (cs) => {
         cs.fontSize -= 5;
      },
   },
});

export const { sizeUpp, sizeDownn } = choiSizeSlice.actions;

export default choiSizeSlice.reducer;
