let teamElement = document.getElementById("team-name");

teamElement.addEventListener("mouseover", (event) => {
    let profiles = document.getElementsByClassName('profile_icon');
    console.log(profiles)
    for (let profile of profiles) {
        profile.style.animation="bubble-up 2s infinite";
    }
})