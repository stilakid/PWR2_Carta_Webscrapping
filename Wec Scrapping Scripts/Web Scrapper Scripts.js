// Helper Functions

// Function for saving the reviews to a json file that gets downloaded.
(function(console){

    console.save = function(data, filename){

        if(!data) {
            console.error('Console.save: No data')
            return;
        }

        if(!filename) filename = 'console.json'

        if(typeof data === "object"){
            data = JSON.stringify(data, undefined, 4)
        }

        var blob = new Blob([data], {type: 'text/json'}),
            e    = document.createEvent('MouseEvents'),
            a    = document.createElement('a')

        a.download = filename
        a.href = window.URL.createObjectURL(blob)
        a.dataset.downloadurl =  ['text/json', a.download, a.href].join(':')
        e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
        a.dispatchEvent(e)
    }
})(console)

// Synchronous wait function
const wait = (ms) => {
    var start = Date.now(),
        now = start;
    while (now - start < ms) {
      now = Date.now();
    }
}


////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////

// Gets Links

// Loads all the links in the catalogue for a department.
let load_button = document.querySelector(".SearchResultsPage__LoadMoreButton-sc-1hyeqlm-3, hywauC");
let intervalID;
const func = () => {
    if (load_button.textContent == "Load more") {
        load_button.click();
    } else if (load_button.textContent == "No more results") {
        // Fetches all the links for the department
        let links = [];
        let search_results = document.querySelectorAll(".CourseResultCard__CourseTitle-sc-1l3zpr6-1 > a");
        for (let result of search_results) {
            let link = result.href;
            links.push(link);
        }
        console.save(links);
        clearInterval(intervalID);
    }
}
intervalID = setInterval(func, 5000);



////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////

// Gets Reviews
const get_reviews = () => {
    // Function that expands all the reviews.

    const func2 = () => {
        let but = document.querySelector("#pseudo_link");
        for (let i = 0; i < 250; i++) {
            //wait(10);
            if (but !== null) {
                but.click();
                but = document.querySelector("#pseudo_link");
            }
        }
        // dunno why but this works.
        // but = document.querySelector("#pseudo_link");
        // for (let i = 0; i < 250; i++) {
        //     //wait(10);
        //     but.click();
        // }

        // Function that fetches all the reviews
        let cards = document.querySelectorAll(".card .card-body");
        let reviews = [];
        for (let card of cards) {
            let review = card.querySelector("span");
            if (review !== null) {
                reviews.push(card.querySelector("span").textContent);
            }
        }
        console.save(reviews);
        got_review = true;
    }
    setTimeout(func2, 10000);


    // This does not work as on load only waits for HTML element and style and image resources. Dynamically added content won't be loaded, which is bad as Carta reviews are dynamically loaded.
    // window.onload = function() {
    //     let but = document.querySelector("#pseudo_link");
    //     for (let i = 0; i < 250; i++) {
    //         if (but !== null) {
    //             but.click();
    //             but = document.querySelector("#pseudo_link");
    //         }
    //     }

    //     // Function that fetches all the reviews
    //     let cards = document.querySelectorAll(".card .card-body");
    //     let reviews = [];
    //     for (let card of cards) {
    //         let review = card.querySelector("span");
    //         if (review !== null) {
    //             reviews.push(card.querySelector("span").textContent);
    //         }
    //     }
    //     console.save(reviews);
    //     got_review = true;

    // }


    // const func2 = () => {
    //     let but = document.querySelector("#pseudo_link");
    //     for (let i = 0; i < 1500; i++) {
    //         but.click();
    //     }
    //     // Function that fetches all the reviews
    //     let cards = document.querySelectorAll(".card .card-body");
    //     let reviews = [];
    //     for (let card of cards) {
    //         let review = card.querySelector("span");
    //         if (review !== null) {
    //             reviews.push(card.querySelector("span").textContent);
    //         }
    //     }
    //     console.save(reviews);
    //     clearInterval(intervalID);
    // }
    // let intervalID = setInterval(func2, 10000);
}






////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////

// Accesses Each Link
// Manually put links inside page_links after retrieving it above.
let page_links = [
    "https://carta-beta.stanford.edu/course/CS106B/1226",
    "https://carta-beta.stanford.edu/course/CS%20107/1226"

];
sessionStorage.setItem("links", JSON.stringify(page_links));

let got_review = false;

const main = () => {
    get_reviews();
    let data = sessionStorage.getItem("links");
    if (data === null) {
        console.log("No links loaded in sessionStorage");
    }
    else if (data === "[]") {
        console.log("session storage is empty");
    } else {
        let parsed_data = JSON.parse(data);
        let url = parsed_data[0];
        let new_data = parsed_data.slice(1);
        sessionStorage.setItem("links", JSON.stringify(new_data));
        setInterval( () => {
                if (got_review) {
                    window.location.href=url;
                }
            }
            , 1000);
    }
}



// To check if session storage is working properly
let data = JSON.parse(sessionStorage.getItem("links"));
data.length;


3770