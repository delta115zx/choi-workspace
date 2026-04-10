import axios from "axios";
import { useState } from "react";

// 동기식으로 -> async await
//    const getWeather = async () => {
//       // GET방식 AJAX
//       // axios.get(주소).then(콜백함수);
//       await axios
//          .get(
//             "https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr"
//          )
//          .then(() => {
//             alert("asd");
//          });
//       alert("zxc");
//    };

// jQuery : $.ajax(), $.getJSON(), ...
// React : AJAX관련 자체 메소드x -> vanillaJS의 AJAX를 활용
//          -> AJAX 라이브러리를 쓰자
//          -> axios
// yarn add axios
const ChoiAJAXFirst = () => {
   const [weather, setWeather] = useState({ d: "", t: "", h: "" });
   const getWeather = () => {
      // GET방식 AJAX
      // axios.get(주소).then(콜백함수);
      axios
         .get(
            "https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr"
         )
         .then((ress) => {
            // 응답내용 : ress.data
            // alert(JSON.stringify(ress.data));
            setWeather({
               d: ress.data.weather[0].description,
               t: ress.data.main.temp,
               h: ress.data.main.humidity,
            });
         });
   };
   return (
      <>
         <h1>날씨 : {weather.d}</h1>
         <h1>기온 : {weather.t}</h1>
         <h1>습도 : {weather.h}</h1>
         <button onClick={getWeather}>날씨 업데이트</button>
      </>
   );
};

export default ChoiAJAXFirst;
