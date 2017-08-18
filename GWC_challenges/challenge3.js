console.log("This prints in the console of the browser");

var loop = function(){
    for (i=0; i<7; i++){
        console.log ("I can do this!");
    }
};

loop();


// var color=['#FAEBD7','#7FFFD4','#FF7F50','#90EE90',"#DDA0DD"];
// var rand = color[Math.floor(Math.random() * color.length)];
// function changecolor(){
//   document.doucment.body.style.backgroundColor=color[rand];
// }



function changecolor(){
  document.body.style.backgroundColor=randomColors();
}

function randomColors(){
  return '#' + Math.floor(Math.random()* 16777215).toString(16);
}
