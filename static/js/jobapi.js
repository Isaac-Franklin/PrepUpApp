
console.log("working");
var details;
const loader = document.querySelector(".loader img");
const proxy = "https://cors-anywhere.herokuapp.com/";
await fetch(`${proxy}http://arbeitnow.com/api/job-board-api`)
    .then((response) => response.json())
    .then((data) => {
        details = data.data;
    });

function titleLenght(title, limit = 20) {
    let newTitle = [];
    if (title.lenght > limit) {
        title.split(" ").reduce((total, word) => {
            if (total + word.lenght <= limit) {
                newTitle.push(word);
            }
            return `${newTitle.join(" ")}...`;
        }, 0);
    } else {
        return title;
    }
}

function insertJobData(details) {
    for (let i = 0; i < details.length - 65; i++) {
        const element = details[i];
        let data = element;
        // loader.style.display = "none";
        const jobDetails =
            `<div class='jobdetails'> <h4>Company Name: ${data.company_name}</h4><h3>Job Title: ${data.title}</h3><p>Location: ${data.location}</p><p>Remote: ${data.remote}</p><a href=${data.url}><button>Apply Here</button></a></div>`


        // <div class='jobdetails'>
        //                             <h4>Company Name: ${current.company_name}</h4>
        //                             <h3>Job Title: ${current.title}</h3>
        //                             <p>Location: ${current.location}</p>
        //                             <p>Remote: ${current.remote}</p>
        //                             <a href=${current.url}><button>Apply Here</button></a>
        //                         </div>

        //             `<div class="companyname"><h4>Company Name: ${data.company_name}</h4></div>
        // <div class="jobtitle">Job Title: ${data.title}</div>
        // <div class="jobdes"><h3></h3></div>
        // <div class="jobLocation"><p>Location: ${data.location}</p></div>
        // <div class="remote"><p>Remote: ${data.remote}</p></div>
        // <button class="joburl"><a href="${data.url}" target="_blank">Click Here To Apply</a></button><br><br>`;

        document
            .querySelector(".jobsapi")
            .insertAdjacentHTML("beforeend", jobDetails);
    }
}

insertJobData(details);
