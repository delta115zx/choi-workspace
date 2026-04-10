import { useRef, useState } from "react";
import axios from "axios";

const ChoiFileUploadFirst = () => {
   const [photo, setPhoto] = useState({ title: "", file: "" });
   const photoFormData = new FormData();
   photoFormData.append("title", photo.title);
   photoFormData.append("file", photo.file);
   const [result, setResult] = useState({ title: "" });
   const fileInput = useRef(); // file타입 input은 value를 안쓰니

   const changePhoto = (e) => {
      // file타입 input의 value는 선택한 파일명
      // Back-End로파일명을 보내겠다? -> 파일을 보내야
      if (e.target.name === "title") {
         setPhoto({ ...photo, [e.target.name]: e.target.value });
      } else {
         setPhoto({ ...photo, [e.target.name]: e.target.files[0] });
      }
   };

   const uploadPhoto = () => {
      // 기존 인코딩 방식이 글자/숫자만 가능, 파일은 불가
      // -> 인코딩 방식을 mulitpart/form-data로 바꿔서
      axios
         .post("http://195.168.9.80:7777/file.upload", photoFormData, {
            headers: { "Content-Type": "multipart/form-data" },
            withCredentials: true,
         })
         .then((res) => {
            setResult(res.data);
            setPhoto({ title: "", file: "" });
            fileInput.current.value = "";
         });
   };

   return (
      <>
         제목 :{" "}
         <input value={photo.title} name="title" onChange={changePhoto} />{" "}
         <br />
         파일 :{" "}
         <input
            ref={fileInput}
            type="file"
            name="file"
            onChange={changePhoto}
         />
         <br />
         <button onClick={uploadPhoto}>업로드</button>
         <hr />
         업로드한 사진 제목 : {result.title}
         업로드한 사진 파일명 : {result.file}
         <img
            src={`http://195.168.9.80:7777/file.get?filename=${result.file}`}
         />
      </>
   );
};

export default ChoiFileUploadFirst;
