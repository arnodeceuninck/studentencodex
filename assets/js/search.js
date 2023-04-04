function getSelectedCategory() {
  // <button type="button" class="btn btn-secondary" data-category="antwerpse" id="antwerpse-selector">Antwerpse Codex</button>
  //             <button type="button" class="btn btn-light" data-category="rodex_oud" id="rodex_oud-selector">Rodex (Oud)</button>

    // get the buttons
    var buttons = document.querySelectorAll('.btn-group button');
    // get the selected button
    var selectedButton = document.querySelector('.btn-group button.btn-secondary');
    // get the category of the selected button
    var selectedCategory = selectedButton.dataset.category;
    return selectedCategory;
}

function mySearch() {
    console.log("mySearch() called");
  // Declare variables
  var input, filter, table, tr, td, i, txtValue, category;
  input = document.getElementById("search-input");
  filter = input.value.toUpperCase();
  table = document.getElementById("search-table");
  tr = table.getElementsByTagName("tr");

  category = getSelectedCategory();

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    var cols = tr[i].getElementsByTagName("td");

    // if the row is not in the current category, hide it
    if (tr[i].dataset.category !== category) {
        tr[i].style.display = "none";
        continue;
    }

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