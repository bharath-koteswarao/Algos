var table = document.getElementsByClassName("problems")[0];
for (var i = 0; i < table.rows.length; i++) {
    var x = table.rows[i].insertCell(0);
    x.innerHTML = i;
}