function profilePopup() {
    let profiles = document.getElementsByClassName('profile_icon');
    for (let profile of profiles) {
        profile.classList.add("bubble-up");
    }
    let description = document.getElementById('herosubfont');
    description.classList.add("fade-in-and-drop");
}

function setup() {
    let teamElement = document.getElementById("team-name");
    let viewportWidth = window.innerWidth;
    if (viewportWidth < 900) {
        profilePopup();
    }
    teamElement.addEventListener("mouseover", profilePopup);
    textFlicker();
}

function textFlicker() {
    // Define values for the wordFlick function
    let words = ['Aspiring Production Engineers', 'MLH Fellows', 'Python Enthusiasts'],
        part,
        i = 0,
        offset = 0,
        len = words.length,
        forwards = true,
        skip_count = 0,
        skip_delay = 15,
        speed = 70;

    let wordflick = function () {
        setInterval(function () {
            if (forwards) {
                if (offset >= words[i].length) {
                    ++skip_count;
                    if (skip_count == skip_delay) {
                        forwards = false;
                        skip_count = 0;
                    }
                }
            } else {
                if (offset == 0) {
                    forwards = true;
                    i++;
                    offset = 0;
                    if (i >= len) {
                        i = 0;
                    }
                }
            }
            part = words[i].substring(0, offset);
            if (skip_count == 0) {
                if (forwards) {
                    offset++;
                } else {
                    offset--;
                }
            }
            document.getElementById('herosubfont').innerHTML = part;
        }, speed);
    };
    wordflick();
}

setup();