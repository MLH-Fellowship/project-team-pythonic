// Executes the popup effect to display profile bubbles and description text
function profilePopup() {
    let profiles = document.getElementsByClassName('profile_icon');
    for (let profile of profiles) {
        profile.classList.add("bubble-up");
    }
    let description = document.getElementById('herosubfont');
    description.classList.add("fade-in-and-drop");
}

// Setup function for loading the necessary listeners
function setup() {
    let teamElement = document.getElementById("team-name");
    let viewportWidth = window.innerWidth;
    if (viewportWidth < 900) {
        profilePopup();
    }
    teamElement.addEventListener("mouseover", profilePopup);
    textFlicker();
}

// Function for adding a text flicker animation for the landing page description
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

    // This function executes the flickering given a certain interval
    let wordflick = function () {
        setInterval(function () {
            // If animation is moving forwards, continue adding letters
            if (forwards) {
                if (offset >= words[i].length) {
                    ++skip_count;
                    // Flips the status of the animation (now running backwards)
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

// Set up listeners on document load
setup();