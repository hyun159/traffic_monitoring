function openCctv(cctvId) {
    console.log("openCctv 호출:", cctvId);

    fetch(`http://127.0.0.1:8000/cctv/${cctvId}`)
        .then(response => response.json())
        .then(data => {
            console.log("API 응답:", data);
            window.open(data.cctvurl, "_blank");
        })
        .catch(error => {
            console.error("에러 발생:", error);
        });
}


// 장유 IC
const button1 = document.getElementById("cctv-button-1");
console.log("button1:", button1);

button1.addEventListener("click", function() {
    console.log("장유IC 버튼 클릭");
    openCctv(1);
});


// 김해 응달교
const button2 = document.getElementById("cctv-button-2");
console.log("button2:", button2);

button2.addEventListener("click", function() {
    console.log("응달교 버튼 클릭");
    openCctv(2);
});


// 부산 사상 종점 나들목
const button3 = document.getElementById("cctv-button-3");

button3.addEventListener("click", function() {
    console.log("부산 사상 나들목 버튼 클릭");
    openCctv(3);
});
