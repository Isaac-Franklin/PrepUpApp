const opennav = document.querySelector('.hamburger')
const closenav = document.querySelector('.hamburger2')
const navsection = document.querySelector('.responsivenav')


opennav.addEventListener('click', () => {
    navsection.style.display = 'block',
        opennav.style.display = 'none',
        closenav.style.display = 'block'

})


closenav.addEventListener('click', () => {
    navsection.style.display = 'none',
        opennav.style.display = 'block',
        closenav.style.display = 'none'
})