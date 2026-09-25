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

async function loadJson(file){
    const response = await fetch('/static/translated.json');
    const data = await response.json();
    console.log("Loaded data:", data)
    myDisplayer(data);
}

// loadJson("translated.json");

function myDisplayer(data) {
    const original = Object.keys(data);
    const newer = Object.values(data);
    
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
    

    
}

async function calling(event){
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
}

function loadTrans(){
    loadJson("translated.json");
}
