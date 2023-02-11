        let audio = new Audio();
        let audio_play = new Audio();
        let current_song;
        let audio_id;

        let btn_play;
        let btn_pause;
        let btn_play_bis;
        let btn_pause_bis;

        let i_audio

        let percent;
        let cover
        let title
        let submitter

        let total_time = 0;

        let type;

        function temps(secondes) {
             var retour='';
             if(secondes<0)
             {
                  retour='-';
                  secondes*=-1;
             }
             if(secondes>=3600)
             {
                  var heures=Math.floor(secondes/3600);
                  retour+=heures+'h ';
                  secondes-=heures*3600;
             }
             if(secondes>=60)
             {
                  var minutes=Math.floor(secondes/60);
                  retour+=minutes+'min ';
                  secondes-=minutes*60;
             }
             if(secondes>0)
             {
                  retour+=parseInt(secondes)+'s';
             }
             return retour;
        }

        window.addEventListener("load",function() {
            let listAudio = document.getElementsByTagName("audio");
            let listBtnPlay = document.getElementsByClassName("btn_play");
            let listBtnPause = document.getElementsByClassName("btn_pause");

            let listCoverAlbum = document.querySelectorAll("#cover_music");
            let listTitleMusic = document.querySelectorAll("#title_music");
            let listSubmitterMusic = document.querySelectorAll("#submitter_music");


            for (i_audio = 0; i_audio < listAudio.length; i_audio++) {

                listAudio[i_audio].setAttribute("id", i_audio);
                listBtnPlay[i_audio].setAttribute("id", "btn_play_" + (i_audio));
                listBtnPause[i_audio].setAttribute("id", "btn_pause_" + (i_audio));

                listCoverAlbum[i_audio].setAttribute("id", "cover_" + i_audio);
                listTitleMusic[i_audio].setAttribute("id", "title_" + i_audio);
                listSubmitterMusic[i_audio].setAttribute("id", "submitter_" + i_audio);

                total_time += listAudio[i_audio].duration;

            }
            document.querySelector("#time_total").innerHTML = temps(total_time);

            document.querySelector("#music_count").innerHTML = listAudio.length;
        })



        let listAudio = document.getElementsByTagName("audio");

        audio = listAudio[current_song];
        let progress_barre = document.querySelector(".barre");
        let volume_bar = document.getElementById("volume");

        let btn_play_control = document.getElementById("play");
        let btn_pause_control = document.getElementById("pause");



        function playAndPauseBis(){
            if(audio.paused){
                btn_play.style.display = "none";
                btn_pause.style.display = "block";

                btn_play_control.style.display = "none"
                btn_pause_control.style.display = "block"

                audio.play()
                console.log(audio)
            }
            else{
                btn_play.style.display = "block";
                btn_pause.style.display = "none";

                btn_play_control.style.display = "block"
                btn_pause_control.style.display = "none"

                audio.pause()
            }
        }

        function playAndPause(audio_class) {
            current_song = null;
            audio = null

            audio = document.querySelector("." + audio_class);
            audio_id = audio.id;
            btn_play = document.getElementById("btn_play_" + audio_id);
            btn_pause = document.getElementById("btn_pause_" + audio_id);

            if (audio.paused) {
                for (current_song = 0; current_song<listAudio.length;){
                    audio_play = listAudio[current_song];
                    if(audio_play.paused === false){
                        audio_play.pause();
                         if(audio_play.played){
                         }
                        btn_play_bis = document.getElementById("btn_play_" + audio_play.id);
                        btn_pause_bis = document.getElementById("btn_pause_" + audio_play.id);

                        btn_play_bis.style.display = "block";
                        btn_pause_bis.style.display = "none";

                    }
                    current_song++;
                }

                audio.play();

                btn_play.style.display = "none";
                btn_pause.style.display = "block";

                btn_play_control.style.display = "none"
                btn_pause_control.style.display = "block"

                cover = document.getElementById("cover_" + audio.id);
                title = document.getElementById("title_" + audio.id);
                submitter = document.getElementById("submitter_" + audio.id);

                document.getElementById("cover").src = cover.src;
                document.getElementById("title").textContent = title.textContent;
                document.getElementById("submitter").textContent = submitter.textContent;



                progress_barre.addEventListener("input", function (){
                    percent = Math.trunc(audio.duration * (this.value/100));
                    audio.currentTime = Math.trunc(audio.duration * (this.value/100));
                })

                audio.addEventListener("timeupdate", function() {
                    percent = (audio.currentTime / audio.duration) * 100;
                    progress_barre.value = percent;
                })



                volume_bar.addEventListener("input", function() {
                    audio.volume = this.value / 100;
                })

                current_song = parseInt(audio.id);
                audio.addEventListener("ended", playNext);
            }

            else {
                audio.pause();
                btn_play.style.display = "block";
                btn_pause.style.display = "none";

                btn_play_control.style.display = "block"
                btn_pause_control.style.display = "none"
            }
        }

        function playNext() {
            audio.pause()
            audio.currentTime = 0;
            btn_play.style.display = "block";
            btn_pause.style.display = "none";

            current_song++;
            if (current_song >= listAudio.length) {
                current_song = 0;
            }
            audio = listAudio[current_song];

            btn_play = document.getElementById("btn_play_" + current_song);
            btn_pause = document.getElementById("btn_pause_" + current_song);

            btn_play.style.display = "none";
            btn_pause.style.display = "block";

            cover = document.getElementById("cover_" + audio.id);
            title = document.getElementById("title_" + audio.id);
            submitter = document.getElementById("submitter_" + audio.id);

            document.getElementById("cover").src = cover.src;
            document.getElementById("title").textContent = title.textContent;
            document.getElementById("submitter").textContent = submitter.textContent;

            audio.play();

            audio.addEventListener("timeupdate", function() {
                    percent = (audio.currentTime / audio.duration) * 100;
                    progress_barre.value = percent;
            })

            progress_barre.addEventListener("click", function (event){
                    audio.currentTime = audio.duration * ((event.clientX - this.offsetLeft) / this.offsetWidth);
            })

            volume_bar.addEventListener("input", function() {
                    audio.volume = this.value / 100;
            })

            audio.addEventListener("ended", playNext);
        }


        function playBefore() {
            audio.pause();
            audio.currentTime = 0;
            btn_play.style.display = "block";
            btn_pause.style.display = "none";

            current_song = current_song - 1;
            if (current_song <= 0) {
                current_song = listAudio.length - 1;
            }

            console.log(current_song)

            audio = listAudio[current_song];

            btn_play = document.getElementById("btn_play_" + current_song);
            btn_pause = document.getElementById("btn_pause_" + current_song);

            btn_play.style.display = "none";
            btn_pause.style.display = "block";

            cover = document.getElementById("cover_" + audio.id);
            title = document.getElementById("title_" + audio.id);
            submitter = document.getElementById("submitter_" + audio.id);

            document.getElementById("cover").src = cover.src;
            document.getElementById("title").textContent = title.textContent;
            document.getElementById("submitter").textContent = submitter.textContent;

            audio.play();

            audio.addEventListener("timeupdate", function () {
                percent = (audio.currentTime / audio.duration) * 100;
                progress_barre.value = percent;
            })

            progress_barre.addEventListener("click", function (event) {
                audio.currentTime = audio.duration * ((event.clientX - this.offsetLeft) / this.offsetWidth);
            })

            volume_bar.addEventListener("input", function () {
                audio.volume = this.value / 100;
            })

            audio.addEventListener("ended", playNext);
        }

