const opennav = document.querySelector('.openmenubtn')
const closenav = document.querySelector('.closemenubtn')
const navBar = document.querySelector('.respgeneral')

const showMenuBar = () => {
    navBar.style.display = "block"
}
const hideMenuBar = () => {
    navBar.style.display = "none"
}

opennav.addEventListener("click", showMenuBar)
closenav.addEventListener("click", hideMenuBar)