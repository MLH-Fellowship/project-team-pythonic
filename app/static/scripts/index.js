function profilePopup() {
    let profiles = document.getElementsByClassName('profile_icon');
    for (let profile of profiles) {
        profile.classList.add("bubble-up");
    }
}

function setup() {
    let teamElement = document.getElementById("team-name");
    let viewportWidth = window.innerWidth;
    if (viewportWidth < 900) {
        profilePopup();    
    }
    teamElement.addEventListener("mouseover", profilePopup);    
}

setup();