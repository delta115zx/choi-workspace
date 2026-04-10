import { useRef, useState } from "react";
import {
   containsHangul,
   isEmpty,
   isNotNum,
   isNotType,
   lessThen,
   notContains,
   notEqual,
} from "./choiValidCheckerReact";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const SignUpForm = () => {
   const [regInfo, setRegInfo] = useState({
      id: "",
      pw: "",
      pwCheck: "",
      name: "",
      jumin1: "",
      jumin2: "",
      postcode: "",
      address: "",
      detailAddress: "",
      photo: "",
      idChk: "no",
   });
   const [bfChkId, setBfChkId] = useState("");
   const regInput = useRef({});
   const nav = useNavigate();

   const regFD = new FormData();
   regFD.append("id", regInfo.id);
   regFD.append("pw", regInfo.pw);
   regFD.append("name", regInfo.name);
   regFD.append("jumin1", regInfo.jumin1);
   regFD.append("jumin2", regInfo.jumin2);
   regFD.append("postcode", regInfo.postcode);
   regFD.append("address", regInfo.address);
   regFD.append("detailAddress", regInfo.detailAddress);
   regFD.append("photo", regInfo.photo);

   const changeInput = (e) => {
      if (e.target.name === "photo") {
         setRegInfo({ ...regInfo, photo: e.target.files[0] });
      } else {
         setRegInfo({ ...regInfo, [e.target.name]: e.target.value });
      }
   };

   const idChk = () => {
      if (isEmpty(bfChkId) || lessThen(bfChkId, 4) || containsHangul(bfChkId)) {
         return alert("사용할수없는 ID입니다.");
      } else {
         axios.get(`http://localhost:7777/id.chk?id=${bfChkId}`).then((res) => {
            alert(res.data.result);
            if (res.data.result === "사용가능한 아이디 입니다") {
               setRegInfo({ ...regInfo, id: bfChkId, idChk: "ok" });
            } else setRegInfo({ ...regInfo, id: "", idChk: "no" });
         });
      }
   };

   const isValid = () => {
      if (
         isEmpty(regInfo.id) ||
         lessThen(regInfo.id, 4) ||
         containsHangul(regInfo.id)
      ) {
         alert("ID??");
         setRegInfo({ ...regInfo, id: "" });
         setBfChkId("");
         regInput.current.id.focus();
         return false;
      }
      if (
         isEmpty(regInfo.pw) ||
         containsHangul(regInfo.pw) ||
         notEqual(regInfo.pw, regInfo.pwCheck) ||
         lessThen(regInfo.pw, 4) ||
         notContains(regInfo.pw, "1234567890")
      ) {
         alert("PW??");
         setRegInfo({ ...regInfo, pw: "", pwCheck: "" });
         regInput.current.pw.focus();
         return false;
      }
      if (isEmpty(regInfo.name)) {
         alert("이름??");
         setRegInfo({ ...regInfo, name: "" });
         regInput.current.name.focus();
         return false;
      }
      if (
         isEmpty(regInfo.jumin1) ||
         isEmpty(regInfo.jumin2) ||
         lessThen(regInfo.jumin1, 6) ||
         isNotNum(regInfo.jumin1) ||
         isNotNum(regInfo.jumin2)
      ) {
         alert("주민번호?");
         setRegInfo({ ...regInfo, jumin1: "", jumin2: "" });
      }
      if (
         isEmpty(regInfo.postcode) ||
         isEmpty(regInfo.address) ||
         isEmpty(regInfo.detailAddress)
      ) {
         alert("주소??");
         setRegInfo({
            ...regInfo,
            postcode: "",
            address: "",
            detailAddress: "",
         });
         regInput.current.detailAddress.focus();
         return false;
      }
      if (
         isEmpty(regInfo.photo) ||
         (isNotType(regInfo.photo, "png") &&
            isNotType(regInfo.photo, "gif") &&
            isNotType(regInfo.photo, "jpg") &&
            isNotType(regInfo.photo, "bmp"))
      ) {
         alert("프로필사진??");
         setRegInfo({ ...regInfo, photo: "" });
         regInput.current.photo.value = "";
         return false;
      }
      if (regInfo.idChk !== "ok" || regInfo.id !== bfChkId) {
         alert("중복체크?");
         setRegInfo({ ...regInfo, id: "" });
         setBfChkId("");
         regInput.current.id.focus();
         return false;
      }
      return true;
   };

   const signUp = () => {
      if (isValid()) {
         axios
            .post("http://localhost:7777/sign.up", regFD, {
               headers: { "Content-Type": "multipart/form-data" },
               withCredentials: true,
            })
            .then((res) => {
               alert(res.data.result);
               if (res.data.result === "가입 성공") {
                  nav("/");
               }
            });
      }
   };

   const showAddrPopUp = () => {
      new window.daum.Postcode({
         oncomplete: function (data) {
            // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

            // 각 주소의 노출 규칙에 따라 주소를 조합한다.
            // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
            var addr = ""; // 주소 변수

            //사용자가 선택한 주소 타입에 따라 해당 주소 값을 가져온다.
            if (data.userSelectedType === "R") {
               // 사용자가 도로명 주소를 선택했을 경우
               addr = data.roadAddress;
            } else {
               // 사용자가 지번 주소를 선택했을 경우(J)
               addr = data.jibunAddress;
            }

            // 우편번호와 주소 정보를 해당 필드에 넣는다.
            setRegInfo({ ...regInfo, address: addr, postcode: data.zonecode });
            // 커서를 상세주소 필드로 이동한다.
            document.getElementById("detailAddress").focus();
         },
      }).open();
   };
   return (
      <>
         <table id="signUpFormTbl">
            <tr>
               <td>
                  ID&nbsp;&nbsp;
                  <br />
                  <input
                     maxLength={10}
                     ref={(thisInput) => {
                        regInput.current.id = thisInput;
                     }}
                     value={bfChkId}
                     onChange={(e) => {
                        setBfChkId(e.target.value);
                     }}
                     autoComplete="off"
                     autoFocus
                  />
                  <button onClick={idChk} id="idChkBtn">
                     ID중복체크
                  </button>
               </td>
            </tr>
            <tr>
               <td>
                  PW&nbsp;&nbsp; <br />
                  <input
                     maxLength={10}
                     ref={(thisInput) => {
                        regInput.current.pw = thisInput;
                     }}
                     type="password"
                     name="pw"
                     value={regInfo.pw}
                     onChange={changeInput}
                     autoComplete="off"
                  />
               </td>
            </tr>
            <tr>
               <td>
                  PW확인&nbsp;&nbsp; <br />
                  <input
                     maxLength={10}
                     ref={(thisInput) => {
                        regInput.current.pwCheck = thisInput;
                     }}
                     type="password"
                     name="pwCheck"
                     value={regInfo.pwCheck}
                     onChange={changeInput}
                     autoComplete="off"
                  />
               </td>
            </tr>
            <tr>
               <td>
                  이름&nbsp;&nbsp; <br />
                  <input
                     maxLength={10}
                     ref={(thisInput) => {
                        regInput.current.name = thisInput;
                     }}
                     name="name"
                     value={regInfo.name}
                     onChange={changeInput}
                     autoComplete="off"
                  />
               </td>
            </tr>
            <tr>
               <td>
                  주민번호&nbsp;&nbsp; <br />
                  <input
                     maxLength={6}
                     ref={(thisInput) => {
                        regInput.current.jumin1 = thisInput;
                     }}
                     name="jumin1"
                     className="jumin1Input"
                     placeholder="xxxxxx"
                     value={regInfo.jumin1}
                     onChange={changeInput}
                     autoComplete="off"
                  />
                  &nbsp; - &nbsp;
                  <input
                     maxLength={1}
                     ref={(thisInput) => {
                        regInput.current.jumin2 = thisInput;
                     }}
                     name="jumin2"
                     className="jumin2Input"
                     placeholder="x"
                     value={regInfo.jumin2}
                     onChange={changeInput}
                     autoComplete="off"
                  />
                  &nbsp;xxxxxx
               </td>
            </tr>
            <tr>
               <td>
                  우편번호&nbsp;&nbsp; <br />
                  <input
                     ref={(thisInput) => {
                        regInput.current.postcode = thisInput;
                     }}
                     name="postcode"
                     id="postcode"
                     onClick={showAddrPopUp}
                     value={regInfo.postcode}
                     onChange={changeInput}
                     autoComplete="off"
                     readOnly
                  />
               </td>
            </tr>
            <tr>
               <td>
                  주소&nbsp;&nbsp; <br />
                  <input
                     ref={(thisInput) => {
                        regInput.current.address = thisInput;
                     }}
                     name="address"
                     id="address"
                     onClick={showAddrPopUp}
                     value={regInfo.address}
                     onChange={changeInput}
                     autoComplete="off"
                     readOnly
                  />
               </td>
            </tr>
            <tr>
               <td>
                  상세주소&nbsp;&nbsp; <br />
                  <input
                     ref={(thisInput) => {
                        regInput.current.detailAddress = thisInput;
                     }}
                     name="detailAddress"
                     id="detailAddress"
                     value={regInfo.detailAddress}
                     onChange={changeInput}
                  />
               </td>
            </tr>
            <tr>
               <td>
                  프로필사진&nbsp;&nbsp; <br />
                  <input
                     ref={(thisInput) => {
                        regInput.current.photo = thisInput;
                     }}
                     name="photo"
                     id="signUpPhotoInput"
                     type="file"
                     onChange={changeInput}
                  />
               </td>
            </tr>
            <tr>
               <td align="center">
                  <button id="signUpBtn" onClick={signUp}>
                     회원가입
                  </button>
               </td>
            </tr>
         </table>
      </>
   );
};

export default SignUpForm;
