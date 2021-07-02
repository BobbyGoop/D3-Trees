var dataset = [20, 40, 60, 80, 100];

var w = 1000;
var h = 800;

var svg = d3
  .select(".container")
  .append("svg")
  .attr("width", w)
  .attr("height", h);

var circles = svg
  .selectAll("circle")
  .data(dataset)
  .enter()
  .append("circle")
  .attr("cx", function (d, i) {
    return i * 50 + d * 2;
  })
  .attr("cy", h / 2)
  .attr("r", function (d) {
    return d;
  })
  .attr("fill", function (d) {
    return "rgb(" + d * 10 + ", 140, 255)";
  })
  .attr("stroke", function (d) {
    return "rgb(0, 140, " + d * 10 + ")";
  })
  .attr("stroke-width", function (d) {
    return d / 2;
  });
