import PropTypes from "prop-types";

const ChoiPropsFourth = (props) => {
   return (
      <table border={1}>
         <tr>
            <td>CPU</td>
            <td>{props.cpu}</td>
         </tr>
         <tr>
            <td>RAM</td>
            <td>{props.ram}</td>
         </tr>
         <tr>
            <td>HDD</td>
            <td>{props.hdd}</td>
         </tr>
      </table>
   );
};

// isRequired : 자동완성
// 나머지는 소스 가독성 수준
// -> 잘 안쓰는 느낌
ChoiPropsFourth.propTypes = {
   cpu: PropTypes.string.isRequired,
   ram: PropTypes.number,
   hdd: PropTypes.number,
};

export default ChoiPropsFourth;
