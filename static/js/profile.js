
function showSection(sectionId) {
    let sections = document.querySelectorAll('.section');
    sections.forEach(sec => sec.classList.remove('active'));

    document.getElementById(sectionId).classList.add('active');

    // update URL
    window.location.hash = sectionId;
}

window.onload = function () {
    let section = window.location.hash.replace('#', '') || 'watch';

    showSection(section);
}

function saveProfile() {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    alert("Profile Updated!\nUsername: " + username);
}

window.onload = function () {
    let section = window.location.hash.replace('#', '') || 'watching';

    showSection(section);
}

