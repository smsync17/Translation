let count = 0;
let pressed = false;

alert("Need this to know I reloaded");

// function updateCount(){
//     document.getElementById("count").innerHTML = count;
//     if(count == 20 || count == -20){
//         alert("YES, YOU REACHED " + count);
//     }
// }

// function increaseCount(){
//     count++;
//     updateCount();
// }

// function decreaseCount(){
//     count--;
//     updateCount();
// }

// function resetCount(){
//     count = 0;
//     updateCount();
// }

// function saveCount(){
//     localStorage.setItem("count", count);
// }

// function loadCount(){
//     let saved = localStorage.getItem("count");
//     if (saved != null){
//         count = Number(saved);
//     }
//     updateCount();
// }

// function press(){
//     if (pressed){
//         document.getElementById("demo").innerHTML = "Why unpressed :(";
//         pressed = false;
//     }
//     else{
//         document.getElementById("demo").innerHTML = "Wow so pressed";
//         pressed = true;
//     }
//     count = 0 - count;
//     updateCount();
// }



// Fetch and display previously saved translations from static folder
async function loadJson(file){
    const response = await fetch('/static/translated.json');
    const data = await response.json();
    console.log("Loaded data:", data)
    myDisplayer(data);
}

// loadJson("translated.json");


// Display data in a two-column table (English phrase and Arabic translation)
function myDisplayer(data) {
    bi_gram = data['bigram_translations'];
    const original = Object.keys(bi_gram);
    const newer = Object.values(bi_gram);
    
    var tbody = document.getElementById('tbody');
    
    tbody.innerHTML = ""; 

    // Loop through to create  row
    var tr = "";
    for (var i = 0; i < newer.length; i++) {
        tr = "";
        tr += "<tr>";
        tr += "<td>" + original[i] + "</td>";
        tr += "<td>" + newer[i] + "</td>";
        tr += "</tr>";
        tbody.innerHTML += tr;
    }
    
    var tbody2 = document.getElementById('tbody2');
    similarity = data['phonetic_matches'];
    const second_pot = Object.keys(similarity);
    const counter = Object.values(similarity);

    tbody2.innerHTML = ""; 

    var tr2 = "";
    for (var i = 0; i < 10; i++) {
        tr2 = "";
        tr2 += "<tr>";
        tr2 += "<td>" + second_pot[i] + "</td>";
        tr2 += "<td>" + counter[i] + "</td>";
        tr2 += "</tr>";
        tbody2.innerHTML += tr2;
    }
    
}

// Handle file upload form submission, send to backend, and display results
async function calling(event){
    document.querySelector('.loader').removeAttribute('hidden');
    event.preventDefault();
    var input = document.querySelector('input[type="file"]');
    var data = new FormData();
    data.append('file', input.files[0]);

    const response = await fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: data
    });

    const json_data = await response.json();
    myDisplayer(json_data);
    document.querySelector('.loader').setAttribute('hidden', '');
}


// Enable submit button when a file is selected, disable when empty
function enableButton(){
    var input = document.querySelector('input[type="file"]');
    var button = document.querySelector('button[type="submit"]');
    if (input.files[0]){
        button.removeAttribute('disabled');
    }
    else{
        button.setAttribute('disabled',' ');
    }
}

// Load saved translations from static JSON file
function loadTrans(){
    loadJson("translated.json");
}
