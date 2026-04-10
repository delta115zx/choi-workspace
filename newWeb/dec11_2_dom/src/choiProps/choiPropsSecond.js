const ChoiPropsSecond = (props) => {
   return (
      <>
         <h1>
            {props.price}원짜리 {props.name}
         </h1>
      </>
   );
};

ChoiPropsSecond.propTypes = {};

export default ChoiPropsSecond;
