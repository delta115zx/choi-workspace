const MyBtns = () => {
   const showAlert = () => {
      alert("ㅎㅎㅎ");
   };

   return (
      <>
         <button
            onClick={() => {
               alert("ㅋㅋ");
            }}
         >
            눌러
         </button>
         <button onClick={showAlert}>눌러2</button>
         <button onClick={showAlert}>눌러3</button>
      </>
   );
};

export default MyBtns;
