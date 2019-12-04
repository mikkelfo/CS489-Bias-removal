console.log(document.readyState);
console.log("dlacm");
//Remove Authors
var authorlist = document.querySelectorAll('[title="Author Profile Page"]')
console.log(authorlist.length)
var i;
for (i = 0; i < authorlist.length; i++) {
    console.log(authorlist[i].innerHTML)
    authorlist[i].innerHTML = 'Author' + String(i+1);
    console.log(authorlist[i].innerHTML)
}

//Remove Location

var location = document.querySelector('[title="Institutional Profile Page"]').innerHTML;
console.log(location.length)
/*
var j;
for (j = 0; i < location.length; i++) {
    console.log(location[i].innerHTML)
    location[i].innerHTML = 'Location' + String(i+1);
    console.log(location[i].innerHTML)
}*/


//Remove Organisation

/*
just notes
document.getElementsByClassName('mediumb-text')[0].innerHTML = 'LOL'
document.querySelector('[title="Author Profile Page"]').innerHTML = 'Author 1'
*/