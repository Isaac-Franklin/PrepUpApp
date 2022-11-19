const dashboardbtn = document.querySelector('.dashboardbtn')
const profilebtn = document.querySelector('.profilebtn').classList.remove('active')
const interviewschedule = document.querySelector('.interviewschedulebtn').classList.add('active')
const materialsbtn = document.querySelector('.materialsbtn').classList.remove('active')
const roomsbtn = document.querySelector('.roomsbtn').classList.remove('active')
const interviewscore = document.querySelector('.interviewscore').classList.remove('active')


// dashboardbtn.classList.add('active')

let arrinterviewer = [];
let interviewer = document.querySelectorAll('.suggestedinterviewers')
const numberofcandidate = document.querySelector('.numberofcandidate h1 strong')
let selectedinterviewer = document.querySelector('.selectedinterviewer strong')
const specificinterviewer = document.querySelectorAll('.showspecificuser h1').innerHTML
const specificinterviewerinner = document.querySelectorAll('.showspecificuser p')
arrinterviewer.push(interviewer)
let suggestedlist = arrinterviewer[0];
console.log('====================================');
console.log(suggestedlist);
console.log(suggestedlist.length);
console.log('====================================');
numberofcandidate.innerHTML = suggestedlist.length
let purArr = [];
purArr.push(specificinterviewer)
console.log('====================================');
// console.log(purArr[0][0])
// console.log(JSON.stringify(purArr[0]))
// console.log(purArr[0])
// console.log(typeof (purArr[0]))
console.log('====================================');

async function getInterviewer(arr) {
    // get random index value
    const randomIndex = await Math.floor(Math.random() * arr.length);

    // get random item
    const item = await arr[randomIndex].innerHTML;
    const data = await JSON.stringify(item)
    console.log(item)
    // console.log(purArr[0][0])
    for (let i = 0; i < purArr.length; i++) {
        const element = purArr[i];
        // const newElement = JSON.stringify(element)
        // console.log(newElement)
        console.log()
        // console.log(typeof (elemen

        console.log(item)
        console.log(typeof (item))
        if (item === element) {
            specificinterviewerinner.innerHTML = 'item'
            console.log('We got a match!');
        } else {
            console.log('We DID NOT get a match!');
        }
    }
    return item,
        selectedinterviewer.innerHTML = item
}
getInterviewer(suggestedlist)


let activateBtn = document.querySelector('.activateselection');
let InterviewerDIV = document.querySelector('.selectedinterviewer')
let loader = document.querySelector(".loader")
let selectedinterviewerproper = document.querySelector('.selectedinterviewerproper')
const showInterviewer = () => {
    loader.style.display = "block";
    selectedinterviewerproper.style.display = 'none'
    InterviewerDIV.style.display = "block"

    setTimeout(() => {
        loader.style.display = "none";
        InterviewerDIV.style.display = "block"
        selectedinterviewerproper.style.display = 'block'
    }, 1000)
}


activateBtn.addEventListener('click', showInterviewer)

const refreshbtn = document.querySelector('.refresh')

refreshbtn.addEventListener('click', () => {
    location.reload()
})

// -----------------------------------


const acceptevent = () => {
    mainSelectionDisplaySection.style.display = 'none'
    acceptSection.style.display = 'block'
    acceptDisplayinner.style.display = 'block'
}

const accepted = document.querySelector('.accept')
const acceptDisplayinner = document.querySelector('.acceptDisplayinner')
accepted.addEventListener('click', acceptevent)
const mainSelectionDisplaySection = document.querySelector('.displaySelectedInterviewer')
const acceptSection = document.querySelector('.acceptDisplay')
