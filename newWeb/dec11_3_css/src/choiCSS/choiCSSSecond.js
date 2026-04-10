const ChoiCSSSecond = (props) => {
   const tblCss = {
      color: props.c,
      backgroundColor: props.bgc,
      width: props.w + "px",
      height: props.h + "px",
   };

   return (
      <>
         <table border={1} style={tblCss}>
            <tr>
               <td>{props.children}</td>
            </tr>
         </table>
      </>
   );
};

export default ChoiCSSSecond;
