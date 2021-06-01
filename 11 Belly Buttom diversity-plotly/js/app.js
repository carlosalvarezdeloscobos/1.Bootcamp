//python -m http.server

// Loading data
let info = "samples.json";
const Json = d3.json(info);

//PART ONE TESTSUBJECT ID NO DROPDOWN
//   1.1 Select variables
var dropDown = d3.select("#selDataset");
dropDown.on("change", optionChanged);
var panelSelect = d3.select(".panel-body");

//   1.2 Extract names of dropdown values
Json.then((idNumber) => {
  var names = idNumber.names;
  selData(names);
});

//   1.3 Add option for dropdown
function selData(names) {
  var selector = d3.select("#selDataset");
  var option;

  names.forEach((name) => {
    option = selector.append("option").text(name).attr("value", name);
  });
}

// 1.4 Event handling
function optionChanged() {
  panelSelect.html("");
  var dropping = parseInt(dropDown.property("value"));
  Json.then((idNumber) => {
    var samples = idNumber.samples;
    var metaData = idNumber.metadata;

    //////////////////////////////////////
    // PART II DEMOGRAPHIC INFO
    // 2.1 adquire metadata
    metaData.forEach((meta) => {
      var metaInfo = meta.id;
      if (metaInfo == dropping) {
        Object.entries(meta).forEach(([key, value]) => {
          var option;
          option = panelSelect.append("p").text(` ${key}: ${value}`);
        });
        var freq = meta.wfreq;
      }
    });

    // 2.2 sample data
    samples.forEach((sample) => {
      var idSample = sample.id;
      if (idSample == dropping) {
        //Slicing first ten elements
        var otu_ids = sample.otu_ids.slice(0, 10);
        var otu_labels = sample.otu_labels.slice(0, 10);
        var sample_values = sample.sample_values.slice(0, 10);
        var list = [];
        for (var i = 0; i < otu_ids.length; i++) {
          var observation = {
            id: otu_ids[i],
            labels: otu_labels[i],
            value: sample_values[i],
          };
          list.push(observation);
        }
        //ordering the list
        var listForplot = list.sort((a, b) => a.value - b.value);

        // 2.3 passing function to the plot:
        plotBar(listForplot);
        plotBubble(listForplot);
      }
    });
  });
}
//////////////////////////////
// PART 3 PLOTTING

//bar chart
function plotBar(listForplot) {
  var y = listForplot.map((d) => "OTU " + String(d.id));
  //trace
  var traceBar = {
    x: listForplot.map((d) => d.value),
    y: y,
    type: "bar",
    orientation: "h",
    text: listForplot.map((d) => d.labels),
    marker: {
      color: "blue",
    },
  };
  //layout
  var layoutBar = {
    width: 500,
    height: 700,
    legend: {
      x: 0.06,
      y: 1,
      font: {
        size: 6,
      },
    },
    margin: {
      l: 100,
      r: 30,
      t: 30,
      b: 40,
    },
  };
  Plotly.newPlot("bar", [traceBar], layoutBar);
}

//bubble chart

function plotBubble(listForplot) {
  var traceBubble = {
    x: listForplot.map((d) => d.id),
    y: listForplot.map((d) => d.value),
    text: listForplot.map((d) => d.labels),
    mode: "markers",
    marker: {
      color: [
        "yellow",
        "green",
        "blue",
        "orange",
        "grey",
        "purple",
        "black",
        "pink",
        "white",
        "blue",
      ],
      opacity: [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],
      //color: listForplot.map((d) => d.id),
      size: listForplot.map((d) => d.value),
    },
  };
  var layoutBubble = {
    showlegend: false,
    height: 700,
    width: 1100,
    xaxis: { title: "OTU ID" },
  };

  Plotly.newPlot("bubble", [traceBubble], layoutBubble);
}
