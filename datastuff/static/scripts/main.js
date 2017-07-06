// Image switcher code

var myImage = document.querySelector('img');

myImage.onclick = function () {
    var mySrc = myImage.getAttribute('src');
    if (mySrc === 'static/imgs/wat.jpg') {
        myImage.setAttribute('src', 'static/imgs/wat2.jpg');
    } else {
        myImage.setAttribute('src', 'static/imgs/wat.jpg');
    }
    myImage.width = 604;
    myImage.height = 404;
}

// Personalized welcome message code

var myButton = document.querySelector('button');
var myHeading = document.querySelector('h1');

function setUserName() {
    var myName = prompt('Please enter your name.');
    localStorage.setItem('name', myName);
    myHeading.innerHTML = 'Hi, ' + myName;
}

if (!localStorage.getItem('name')) {
    setUserName();
} else {
    var storedName = localStorage.getItem('name');
    myHeading.innerHTML = 'Hi, ' + storedName;
}

myButton.onclick = function () {
    setUserName();
}