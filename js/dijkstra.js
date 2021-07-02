function dijkstra (graph, start, target) {
    console.log("\n Алгоритм Дийктрсы \n\n");
    var inf = 1000;
    var distance = {}
    var prev = {}
    var unvisited = Object.keys(graph)
    
    for (var i = 0; i<unvisited.length; i++){
        distance[unvisited[i]] = inf;
        prev[unvisited[i]] = null;    
    }
    //console.log(unvisited);
    //console.log(distance);
    //console.log(prev);
    distance[start] = 0;
    while (unvisited.length != 0) {
        current = function () {
            var min = 1000, vertex;
            for (var i = 0; i < unvisited.length; i++) {
                if (distance[unvisited[i]] < min) {
                    min = distance[unvisited[i]];
                    vertex = unvisited[i]
                }
            }
            return vertex;
        } ()
        unvisited.splice(unvisited.indexOf(current), 1)
        //console.log(unvisited);
        var pairs = parallel([Object.keys(graph[current]), Object.values(graph[current])])
        pairs.forEach((pair, i) => {
            var vertex = pair[0];
            var weight = pair[1];
            var alt = distance[current] + weight;
            if (alt < distance[vertex]) {
                distance[vertex] = alt;
				prev[vertex] = current;
                //console.log(prev)
            }
        })        
    }
    var shortest = []
    var temp = target;
    while (temp != start) {
        shortest.push(prev[temp]);
        temp = prev[temp];
    }
    shortest.push(target);
    // shortest.reverse();
    // shortest.push(target);
    // console.log("\n\n");
    // console.log(shortest);
    // console.log("\n\n");
    console.log(distance);
    console.log("\n\n\n");
    return [shortest, distance];
}

function parallel(arrays) {
    return arrays[0].map(function(_,i){
        return arrays.map(function(array){return array[i]})
    });
}

function convertToGraph(data) {
    var graph = {}
    var names = []
    for (var k = 0; k < data.nodes.length; k++){
        names.push(data.nodes[k].name);
    }
    for (var i = 0; i < data.nodes.length; i++) {
        var current = data.nodes[i];
        //console.log(current);
        var edges = {}
        for (var n = 0; n < data.links.length; n++){
            if (data.links[n].source == current.id) {
                edges[names[data.links[n].target - 1]] = data.links[n].value;
                
            }
            else if (data.links[n].target == current.id){
                edges[names[data.links[n].source - 1]] = data.links[n].value;
            }
        }
        //console.log(edges);
        graph [current.name] = edges;
    }
    //console.log(graph["Приморская"])
    //console.log(names)
    return graph;
}
