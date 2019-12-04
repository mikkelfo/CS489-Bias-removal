var authorlist = document.querySelectorAll('[class="authors-info"]')
console.log(authorlist.length)
var i;
for (i = 0; i < authorlist.length; i++) {
    console.log(authorlist[i].innerHTML)
    authorlist[i].innerHTML = 'Author' + String(i+1);
    console.log(authorlist[i].innerHTML)
}

/*
This is to make it even better, if we get on a summary of eg 10 papers and we want to click on one of them without
looking on the authors
var authorlist1 = document.querySelectorAll('[class="author"]')
console.log(authorlist1.length)
var i;
for (i = 0; i < authorlist1.length; i++) {
    console.log(authorlist1[i].innerHTML)
    authorlist1[i].innerHTML = 'Author' + String(i+1);
    console.log(authorlist1[i].innerHTML)
}
*/