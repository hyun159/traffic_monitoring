

// cctv 버튼 
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


// traffic으로 5분 주기 api 갱신
function loadTraffic() {

    fetch("http://127.0.0.1:8000/traffic")
        .then(response => response.json())

        .then(data => {

            console.log("교통정보:", data);

            const trafficList = document.getElementById("traffic-list");

            // 기존 화면 데이터 삭제
            trafficList.innerHTML = "";

            // 백엔드에서 받은 리스트를 하나씩 처리
            data.forEach(item => {

                const trafficItem = document.createElement("div");

                trafficItem.innerHTML = `
                    <p>도로: ${item["도로"]}</p>
                    <p>방향: ${item["방향"]}</p>
                    <p>위치: ${item["위치"]}</p>
                    <p>평균 속력: ${item["평균 속력"]} km/h</p>
                    <p>예측 시간: ${item["날짜"]} ${item["시간"]}시</p>
                    <hr>
                `;

                trafficList.appendChild(trafficItem);
            });
        })

        .catch(error => {
            console.error("교통정보 요청 실패:", error);
        });
}
loadTraffic();

setInterval(loadTraffic, 5 * 60 * 1000);