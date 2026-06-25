    var visiblesidebar = document.getElementById("menu-section");
    var sidebar = document.querySelector(".menu-section");
    var isshow = false; 

    function visiblemenu()
    {
        if (isshow === false) {
            visiblesidebar.style.transform = "translateX(0px)"; // Show sidebar
            isshow = true;
        } else {
            visiblesidebar.style.transform = "translateX(-240px)"; // Hide sidebar
            isshow = false;
        }
    };


window.onload = function() {
  var slide = document.getElementById('slides');
  const element = 2;
  let currentindex = 0;
  var interval=2500;

  function OneByOne() {
    currentindex++;
    slide.style.transition = "transform 0.4s ease-in-out";
    slide.style.transform = 'translateX(-' + (currentindex * 800) +'px)';
     if (currentindex == element + 1) {
     slide.addEventListener("transitionend", () => {
        slide.style.transition = "none";
        currentindex= 0;
        slide.style.transform = "translateX(0)";
      }, { once: true });
    }
  }

  setInterval(OneByOne, interval);
}




var currentAudio = null;
var currentImage = null;
var images = document.getElementsByClassName("clickable-image");
var audios = document.querySelectorAll("audio");

// Loop through each image
for (var i = 0; i < images.length; i++) {
    images[i].onclick = function (){
        var audioId = this.getAttribute("data-audio").trim();
        var audio = document.getElementById(audioId);

        if (currentAudio === audio && !audio.paused) {
            audio.pause();
            audio.currentTime = 0;
            removeBorder(this);
            currentAudio = null;
            currentImage = null;
        }
        else {

            if (currentAudio !== null) {
                currentAudio.pause();
                currentAudio.currentTime = 0;
                removeBorder(currentImage);
            }

            currentAudio = audio;
            currentImage = this;
            audio.play();
            addBorder(this);

            // When the audio ends, remove highlight & play next
            audio.onended = function () {
                removeBorder(currentImage);
                playNextAudio(audio);
                currentAudio = null;
                currentImage = null;
            };
        }
    };
}

// Play next audio automatically
function NextAudioPlay(current) {
    var index = Array.from(audios).indexOf(current);
    var nextAudio = audios[index + 1];

    if (!nextAudio) {
        nextAudio = audios[0];
    }

    var nextImage = document.querySelector('.clickable-image[data-audio="' + nextAudio.id + '"]');

    removeBorder(currentImage); 
    currentAudio = nextAudio;
    currentImage = nextImage;

    nextAudio.play();
    addBorder(nextImage);

    nextAudio.onended = function () {
        NextAudioPlay(nextAudio);
    };
}

function addBorder(image) {  
    image.style.border = "3px solid #FF0590"; 
    image.style.width = "180px"; 
    image.style.height = "180px";
}

function removeBorder(image) {
    image.style.width = "150px"; 
    image.style.height = "150px";
    image.style.border="none";
}