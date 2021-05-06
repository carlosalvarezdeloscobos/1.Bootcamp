// from data.js
var tableData = data;

// YOUR CODE HERE!

// Selecting the id which the button will be actionable
// related to de filter table bottom:
var filterBtn = d3.select("#filter-btn");
// space where the table request will be input
var tbody = d3.select("tbody");
// enter a date input value event
var inputDatetime = d3.select("#datetime");

//function
function dataSelection() {
  let inputValue = inputDatetime.node().value;
  // filter the infro from data.ja that matches the input value
  let filteredData = tableData.filter((day) => day.datetime === inputValue);

  // iterate over data.js from the value selected in "enter a date"
  filteredData.forEach((aliens) => {
    let row = tbody.append("tr");
    Object.entries(aliens).forEach(([key, value]) => {
      let cell = row.append("td");
      cell.text(value);
    });
  });
}

// Event handling  with the callback function runData
filterBtn.on("click", dataSelection);
