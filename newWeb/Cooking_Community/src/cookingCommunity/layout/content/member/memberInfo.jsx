import axios from "axios";
import { useEffect, useRef, useState } from "react";
import { useSelector } from "react-redux";
import { logInCheck } from "../../../cookingCommunityMain";
import {
   isEmpty,
   isNotType,
   lessThen,
   notContains,
   notEqual,
} from "./choiValidCheckerReact";
import { useNavigate } from "react-router-dom";

const MemberInfo = () => {
   const loginMember = useSelector((s) => s.ms.loginMember);
   const [member, setMember] = useState({
      id: "",
      pw: "",
      pwCheck: "",
      name: "",
      postcode: "",
      address: "",
      detailAddress: "",
      photo: "",
   });
   const nav = useNavigate();
   const [photoURL, setPhotoURL] = useState();
   const memberFd = new FormData();
   memberFd.append("member", sessionStorage.getItem("loginMember"));
   memberFd.append("id", member.id);
   memberFd.append("pw", member.pw);
   memberFd.append("name", member.name);
   memberFd.append("postcode", member.postcode);
   memberFd.append("address", member.address);
   memberFd.append("detailAddress", member.detailAddress);
   memberFd.append("photo", member.photo);
   const memberInput = useRef({});

   const edit = () => {
      if (isValid()) {
         if (member.photo === "") {
            axios
               .post("http://localhost:7777/member.edit.nophoto", memberFd, {
                  headers: {
                     "Content-Type": "multipart/form-data",
                  },
                  withCredentials: "true",
               })
               .then((res) => {
                  alert(res.data.result);
                  if (res.data.result === "수정 성공") {
                     sessionStorage.setItem("loginMember", res.data.member);
                  }
                  logInCheck();
               });
         } else {
            axios
               .post("http://localhost:7777/member.edit", memberFd, {
                  headers: { "Content-Type": "multipart/form-data" },
                  withCredentials: "true",
               })
               .then((res) => {
                  alert(res.data.result);
                  if (res.data.result === "수정 성공") {
                     sessionStorage.setItem("loginMember", res.data.member);
                  }
                  logInCheck();
               });
         }
      }
   };

   const bye = () => {
      if (prompt("진짜 탈퇴할꺼면 탈퇴 입력") === "탈퇴") {
         axios
            .get(
               `http://localhost:7777/member.bye?member=${sessionStorage.getItem(
                  "loginMember"
               )}`
            )
            .then((res) => {
               alert(res.data.result);
               sessionStorage.removeItem("loginMember");
               logInCheck();
            });
      }
   };

   const changeMember = (e) => {
      if (e.target.name === "photo") {
         setMember({ ...member, photo: e.target.files[0] });
         if (e.target.files[0] !== undefined) {
            const reader = new FileReader();
            reader.readAsDataURL(e.target.files[0]);
            reader.onloadend = () => {
               setPhotoURL(reader.result);
            };
         } else {
            setMember({ ...member, photo: "" });
         }
      } else {
         setMember({ ...member, [e.target.name]: e.target.value });
      }
   };

   const isValid = () => {
      if (
         isEmpty(member.pw) ||
         notEqual(member.pw, member.pwCheck) ||
         lessThen(member.pw, 4) ||
         notContains(member.pw, "1234567890")
      ) {
         alert("pw?");
         setMember({ ...member, pw: "", pwCheck: "" });
         memberInput.current.pw.focus();
         return false;
      }
      if (isEmpty(member.name)) {
         alert("이름?");
         setMember({ ...member, name: "" });
         memberInput.current.name.focus();
         return false;
      }
      if (isEmpty(member.postcode) || isEmpty(member.detailAddress)) {
         alert("주소?");
         setMember({ ...member, postcode: "", address: "", detailAddress: "" });
         memberInput.current.detailAddress.focus();
         return false;
      }
      if (isEmpty(member.photo)) {
         return true;
      }
      if (
         isNotType(member.photo, "png") &&
         isNotType(member.photo, "gif") &&
         isNotType(member.photo, "jpg") &&
         isNotType(member.photo, "bmp")
      ) {
         alert("프사?");
         setMember({ ...member, photo: "" });
         memberInput.current.photo.value = "";
         return false;
      }
      return true;
   };
   const showAddrPopUp = () => {
      new window.daum.Postcode({
         oncomplete: function (data) {
            var addr = "";

            if (data.userSelectedType === "R") {
               addr = data.roadAddress;
            } else {
               addr = data.jibunAddress;
            }
            setMember({ ...member, address: addr, postcode: data.zonecode });
            document.getElementById("detailAddress").focus();
         },
      }).open();
   };

   useEffect(() => {
      if (loginMember.id === undefined) {
         nav("/")
      } else {
         setMember({
            ...loginMember,
            pwCheck: loginMember.pw,
            postcode: loginMember.address.split("㉾")[0],
            address: loginMember.address.split("㉾")[1],
            detailAddress: loginMember.address.split("㉾")[2],
            photo: "",
         });
         setPhotoURL(
            `http://localhost:7777/member.info.photo.get?file=${loginMember.photo}`
         );
      }
      return () => {};
   }, []);

   return (
      <table id="signUpFormTbl">
         <tr>
            <td>ID&nbsp;&nbsp; : &nbsp;&nbsp;{member.id}</td>
         </tr>
         <tr>
            <td>
               PW&nbsp;&nbsp; <br />
               <input
                  maxLength={10}
                  ref={(thisInput) => (memberInput.current.pw = thisInput)}
                  type="password"
                  name="pw"
                  value={member.pw}
                  onChange={changeMember}
                  autoComplete="off"
               />
            </td>
         </tr>
         <tr>
            <td>
               PW확인&nbsp;&nbsp; <br />
               <input
                  maxLength={10}
                  ref={(thisInput) => (memberInput.current.pwCheck = thisInput)}
                  type="password"
                  name="pwCheck"
                  value={member.pwCheck}
                  onChange={changeMember}
                  autoComplete="off"
               />
            </td>
         </tr>
         <tr>
            <td>
               이름&nbsp;&nbsp; <br />
               <input
                  maxLength={10}
                  ref={(thisInput) => (memberInput.current.name = thisInput)}
                  name="name"
                  value={member.name}
                  onChange={changeMember}
                  autoComplete="off"
               />
            </td>
         </tr>
         <tr>
            <td>생년월일 : {member.birthday}</td>
         </tr>
         <tr>
            <td>
               우편번호&nbsp;&nbsp; <br />
               <input
                  ref={(thisInput) =>
                     (memberInput.current.postcode = thisInput)
                  }
                  name="postcode"
                  id="postcode"
                  onClick={showAddrPopUp}
                  value={member.postcode}
                  onChange={changeMember}
                  autoComplete="off"
                  readOnly
               />
            </td>
         </tr>
         <tr>
            <td>
               주소&nbsp;&nbsp; <br />
               <input
                  ref={(thisInput) => (memberInput.current.address = thisInput)}
                  name="address"
                  id="address"
                  onClick={showAddrPopUp}
                  value={member.address}
                  onChange={changeMember}
                  autoComplete="off"
                  readOnly
               />
            </td>
         </tr>
         <tr>
            <td>
               상세주소&nbsp;&nbsp; <br />
               <input
                  ref={(thisInput) =>
                     (memberInput.current.detailAddress = thisInput)
                  }
                  name="detailAddress"
                  id="detailAddress"
                  value={member.detailAddress}
                  onChange={changeMember}
               />
            </td>
         </tr>
         <tr>
            <td>
               프로필사진&nbsp;&nbsp; <img src={photoURL} /> <br />
               <input
                  ref={(thisInput) => (memberInput.current.photo = thisInput)}
                  name="photo"
                  type="file"
                  onChange={changeMember}
               />
            </td>
         </tr>
         <tr>
            <td align="left">
               <button id="editBtn" onClick={edit}>
                  수정
               </button>
               <button id="byeBtn" onClick={bye}>
                  탈퇴
               </button>
            </td>
         </tr>
      </table>
   );
};

export default MemberInfo;
