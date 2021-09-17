var xobj = new XMLHttpRequest();
xobj.overrideMimeType("application/json");
xobj.open('GET', './resources/data.json', false);
xobj.send(null);
var data = JSON.parse(xobj.responseText)
console.log(data)

function rgbToHex(r, g, b) {
    return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
}

function toRGB(h) {
    let r = 0, g = 0, b = 0;

    // 3 digits
    if (h.length == 4) {
        r = "0x" + h[1] + h[1];
        g = "0x" + h[2] + h[2];
        b = "0x" + h[3] + h[3];

        // 6 digits
    } else if (h.length == 7) {
        r = "0x" + h[1] + h[2];
        g = "0x" + h[3] + h[4];
        b = "0x" + h[5] + h[6];
    }

    return "rgb(" + +r + ", " + +g + ", " + +b + ")";
}

var route = []
var width = "1600", height = "720"
var link, node;
var button = d3.select(".container")
    .append("button")
    .attr("class", "btn-execute")
    .text("Рассчитать маршрут")
    .on("click", function () {
        svg.selectAll(".node-result").remove();
        if (route.length > 2 || route.length <= 1) alert("Пожалуйста, выберите 2 точки")
        else {
            showShortest(route);
        }
        console.log(route);
    });
var infoField = d3.select("body")
    .append("p")
    .attr("class", "info")

var button = d3.select(".container")
    .append("button")
    .attr("class", "btn-clear")
    .text("Очистить")
    .on("click", () => {
        svg.selectAll(".node-result").remove();
        svg.selectAll(".node-origin")
            .attr("stroke", "none")
            .attr("checked", "false")
        route.splice(0)
        infoField.text("")
    })

var svg = d3.select(".container")
    .append("svg")
    .attr("width", width)
    .attr("height", height)

link = svg.selectAll(".link-origin")
    .data(data.links)
    .enter()
    .append("line")
    .attr("class", "link-origin")
    .attr("x1", function (l) {
        var sourceNode = data.nodes.filter(function (d, i) {
            return i + 1 == l.source
        })[0];
        d3.select(this).attr("y1", sourceNode.y);
        return sourceNode.x
    })
    .attr("x2", function (l) {
        var targetNode = data.nodes.filter(function (d, i) {
            return i + 1 == l.target
        })[0];
        console.log(targetNode)
        d3.select(this).attr("y2", targetNode.y);
        return targetNode.x
    })
    .attr("stroke", function (l) {
        var targetNode = data.nodes.filter(function (d, i) {
            return i + 1 == l.target
        })[0];
        return data.colors[targetNode.line]
    });

node = svg.selectAll(".node")
    .data(data.nodes)
    .enter()
    .append("g");

node.append("circle")
    .attr("class", "node-origin")
    .attr("r", 12)
    .style("fill", function (d, i) {

        return data.colors[d.line];
    })
    .attr("cx", function (d) {
        return d.x
    })
    .attr("cy", function (d) {
        return d.y
    })

    .attr("checked", "false")
    .on("click", function (event, d) {

        var nextColor = this.style.fill == toRGB(data.colors[d.line]) ? data.colors["shortest"] : data.colors[d.line];
        if (d3.select(this).attr("checked") == "false") {
            d3.select(this)
                .attrs({
                    "stroke": nextColor,
                    "stroke-width": "5px",
                    "checked": "true"
                });
            route.push(d.name);
        }
        else if (d3.select(this).attr("checked") == "true") {
            d3.select(this)
                .attr("stroke", "none")
                .attr("checked", "false");
            route.splice(route.indexOf(d.name), 1);
        }
    })

node.append("text")
    .attr("dx", function (d) {
        if (d.id == 3 || d.id == 4) return d.x + 26;
        return d.x + 14
    })
    .attr("dy", function (d) {
        if (d.id == 7 || d.id == 12 ||
            d.id == 13 || d.id == 15) return d.y + 15
        if (d.id == 10 || d.id == 14) return d.y
        else return d.y - 18
    })
    .style("font-size", "14px")
    .style("fill", function (d, i) {
        return data.colors[d.line];
    })
    .text(function (d) { return d.name; });



function showShortest(route) {
    var res = dijkstra(convertToGraph(data), route[0], route[1])
    var shortest = res[0], dist = res[1];
    pathData = []
    for (var i = 0; i < data.nodes.length; i++) {
        if (shortest.indexOf(data.nodes[i].name) != -1) {
            pathData.push(data.nodes[i])
        }
    }
    console.log(pathData);

    infoField.text(`Итоговое время: ${dist[route[1]]} мин`)
    var path = svg.selectAll(".node")
        .data(pathData)
        .enter()
        .append("g")
        .append("circle")
        .attr("class", "node-result")
        .attr("r", 6)
        .style("fill", data.colors["shortest"])
        .attr("cx", function (d) {
            return d.x
        })
        .attr("cy", function (d) {
            return d.y
        })
        .attr("stroke-linecap", "round")
        .attr("stroke-linejoin", "round")
        ;

    console.log("\n")
    var sources = shortest.slice(0, shortest.length - 1);
    var targets = shortest.slice(1);
    console.log(sources, targets)
}


