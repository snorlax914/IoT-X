const time = document.getElementById("time");
const photoes = document.querySelectorAll(".photo")
const photo_times = document.querySelectorAll(".photo_time")
const filePath = 'C:\\Users\\User\\Desktop\\iot\\server'
var index = 0

function setClock() {
    const now = new Date();
    time.innerHTML = `${now.getHours().toString().padStart(2, "0")} : ${now.getMinutes().toString().padStart(2, "0")} : ${now.getSeconds().toString().padStart(2, "0")}`;
}

function setImg() {
    var query = new Date().getTime()
    var newSrc = index.toString() + '.jpg?' + query
    console.log(photoes[index].src)
    photoes[index].src = newSrc
    console.log(photoes[index].src)
    console.log("#" + index + " has changed to " + index + ".jpg")
    index += 1
    if(index == 6) {
        index = 0
    }
    loadFile("fire.txt?" + query);
}

function loadFile(filePath) {
    var result = null;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", filePath, false);
    xmlhttp.send();
    if (xmlhttp.status==200) {
        result = xmlhttp.responseText;
    }
    console.log(result);
    if(result == "1") {
        console.log("fire")
        document.body.style.backgroundColor = "#800000";
    }
}

setInterval(setClock, 1000)
setInterval(setImg, 2000)