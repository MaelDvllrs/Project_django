
window.addEventListener("load",function() {
    let listAudio = document.getElementsByTagName("audio");
    let listAddPlaylistBtn = document.querySelectorAll(".add_playlist_container_btn");
    let listAddPlaylistContainer = document.querySelectorAll(".add_playlist_container");

    for (i_audio = 0; i_audio < listAudio.length; i_audio++) {
        listAddPlaylistBtn[i_audio].setAttribute("id", "AddPlaylistBtn_" + i_audio);
        listAddPlaylistContainer [i_audio].setAttribute("id", "Container_AddPlaylistBtn_" + i_audio);
    }
})


function addPlaylistContener(audio_class){
            audio = document.querySelector("." + audio_class);
            audio_id = audio.id;
            let add_playlist_contener = document.getElementById("Container_AddPlaylistBtn_" + audio_id);

            if (add_playlist_contener.style.display === "none" || add_playlist_contener.style.display === ''){
                add_playlist_contener.style.display = "block";
            }
            else {
                add_playlist_contener.style.display = "none";
            }

        }