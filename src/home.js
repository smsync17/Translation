let count = 0;
let pressed = false;


alert("Hello! My external JavaScript is working!" + count);

function updateCount(){
    document.getElementById("count").innerHTML = count;
    if(count == 20 || count == -20){
        alert("YES, YOU REACHED " + count);
    }
}

function increaseCount(){
    count++;
    updateCount();
}

function decreaseCount(){
    count--;
    updateCount();
}

function resetCount(){
    count = 0;
    updateCount();
}

function saveCount(){
    localStorage.setItem("count", count);
}

function loadCount(){
    let saved = localStorage.getItem("count");
    if (saved != null){
        count = Number(saved);
    }
    updateCount();
}

function press(){
    if (pressed){
        document.getElementById("demo").innerHTML = "Why unpressed :(";
        pressed = false;
    }
    else{
        document.getElementById("demo").innerHTML = "Wow so pressed";
        pressed = true;
    }
    count = 0 - count;
    updateCount();
}

async function loadJson(file){
    const response = await fetch(file);
    const data = await response.json();
    console.log("Loaded data:", data)
    myDisplayer(data);
}

loadJson("translated.json");

function myDisplayer(data) {
    const original = Object.keys(data);
    const newer = Object.values(data);
    console.log(original)
    console.log(newer)
}


