let count = 0;
let pressed = false;

alert("Hello! My external JavaScript is working!" + count);

function updateCount(){
    document.getElementById("count").innerHTML = count;
}

function increaseCount(){
    count++;
    updateCount();
}

function decreaseCount(){
    count--;
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
}

