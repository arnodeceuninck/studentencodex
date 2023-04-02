function mySearch() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("search-input");
  filter = input.value.toUpperCase();
  table = document.getElementById("search-table");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    var cols = tr[i].getElementsByTagName("td");

    // make a searchable string consisting of all columns
    var txt = "";
    for (var j = 0; j < cols.length; j++) {
        txt += cols[j].textContent || cols[j].innerText;
    }

    if (txt.toUpperCase().indexOf(filter) > -1) {
      tr[i].style.display = "";
    } else {
      tr[i].style.display = "none";
    }

  }
}