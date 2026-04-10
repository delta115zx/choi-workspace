const ChoiEventFirst = () => {
   const test = (e) => {
      alert(e.target);
      alert(e.target.value);
      alert(e.target.name);
   };
   return (
      <>
         <input
            name="abc"
            onClick={(e) => {
               alert("누름");
            }}
            onChange={test}
         />
      </>
   );
};

export default ChoiEventFirst;
