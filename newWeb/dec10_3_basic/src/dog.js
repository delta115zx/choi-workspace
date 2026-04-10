import React, { useState } from "react";

const Dog = () => {
   const [name, setName] = useState("몰라");
   const [age, setAge] = useState(0);

   const changeAge = (e) => {
      setAge(e.target.value);
   };

   const showInfo = () => {
      alert(name);
      alert(age);
   };

   return (
      <>
         <h1>{name}</h1>
         <h1>{age}</h1>
         이름 :{" "}
         <input
            value={name}
            onChange={(e) => {
               setName(e.target.value);
            }}
         />{" "}
         <br />
         나이 : <input value={age} onChange={changeAge} /> <br />
         <button onClick={showInfo}>출력</button>
      </>
   );
};

export default Dog;
