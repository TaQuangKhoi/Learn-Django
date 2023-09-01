let initFeather = setInterval(function () {
    if (feather !== undefined) {
        feather.replace()
        clearInterval(initFeather)
    }
}, 200)

function clickFolderItem(id) {
    disableActive()
    let folder = document.getElementById(id)
    folder.classList.add('active')
}

function disableActive() {
    let active = document.getElementsByClassName('active')
    for (let i = 0; i < active.length; i++) {
        active[i].classList.remove('active')
    }
}
