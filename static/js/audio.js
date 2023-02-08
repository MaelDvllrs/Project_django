var btnLecture = document.getElementById()("button");
var btnPause = document.getElementById()("button");

lecteur = document.getElementById("");

function lecture() {
    lecteur.play();
}

function pause() {
    lecteur.pause();
}

function stop() {
    lecteur.pause();
    lecteur.currentTime = 0;
}