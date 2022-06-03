let teamElement = document.getElementById("team-name");

teamElement.addEventListener("mouseover", (event) => {
    let profiles = document.getElementsByClassName('profile_icon');
    for (let profile of profiles) {
        profile.classList.add("bubble-up");
    }
})