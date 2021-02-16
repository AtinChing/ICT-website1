function onload(){
	document.body.background = '#fbfab2';
}

function colourin(id){
    id.style.fontWeight = "900";
}
function uncolourin(id){
    id.style.fontWeight = "400";
}
function setCase(){
   }
function draw(){

}
function changeLogo(logoLang){ // Logo lang is the language whose logo should be the picture.
    var logoPic = document.getElementById('logo');
    switch(logoLang){
        case "C#":
            logoPic.src = 'C%23Logo.png';

            break;
        case "Java":
            logoPic.src = 'JavaLogo.png';
            break;
        case "Cpp":
            logoPic.src = 'CppLogo.png';
            break;
        case "Python":
            logoPic.src = 'PythonLogo.png';
            break;
        case "TypeScript":
            logoPic.src = 'TSLogo.png';
            break;
    }
}
function setVideoPos(){
	document.getElementById("video").style.objectPosition = "3000 30%"
}