import { useState } from "react";
import "./player.css"

// class
const PlayerBBS = () => {
   // memberVar
   const [player, setPlayer] = useState({
      name: "",
      nickname: "",
   });
   const [players, setPlayers] = useState([]);
   const playersTr = players.map((p, i) => {
      return (
         <tr
            className="dataTr"
            onClick={() => {
               delPlayer(p);
            }}
         >
            <td align="center">{p.name}</td>
            <td align="center">{p.nickname}</td>
         </tr>
      );
   });

   // method
   const changePlayer = (e) => {
      setPlayer({ ...player, [e.target.name]: e.target.value });
   };

   const delPlayer = (p) => {
      setPlayers(players.filter((pp) => p.name !== pp.name));
   };

   const regPlayer = () => {
      // JS배열에 추가
      //    배열[인덱스] = 값;
      //    배열.push(값) : 추가
      //    배열.concat(값) : 추가해서 추가된 배열을 리턴
      setPlayers(players.concat(player));
      setPlayer({ name: "", nickname: "" });
   };
   return (
      <div id="playerRegArea">
         선수이름 :{" "}
         <input
            name="name"
            className="txtType"
            value={player.name}
            onChange={changePlayer}
         />
         <br />
         닉네임 :{" "}
         <input
            name="nickname"
            className="txtType"
            value={player.nickname}
            onChange={changePlayer}
         />
         <br />
         <button onClick={regPlayer}>등록</button>
         <hr />
         <table id="playerBBSTbl" border={1}>
            <tr>
               <th>선수이름</th>
               <th>닉네임</th>
            </tr>
            {playersTr}
         </table>
      </div>
   );
};

export default PlayerBBS;
