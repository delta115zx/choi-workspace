import PropTypes from "prop-types";

const ChoiPropsThird = (props) => {
   return (
      <div>
         품명 : {props.namee}
         <br />
         가격 : {props.pricee}
      </div>
   );
};

ChoiPropsThird.propTypes = {
   namee: PropTypes.string.isRequired, // 글자만 필수로
   pricee: PropTypes.number, // pt시리즈
};

export default ChoiPropsThird;
