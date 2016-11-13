
// http://blog.thomsonreuters.com/index.php/mobile-patent-suits-graphic-of-the-day/
var solved = [
    {type: "F", id: "S1"},
    {type: "F", id: "12"},
    {type: "F", id: "25"},
    {type: "F", id: "5L2"},
    {type: "F", id: "L25"},
]

var links = [
    {source: "START", target: "Junction_1", type: "Walk", id: "S1"},
    {source: "Junction_1", target: "Junction_2", type: "Train-B", id: "12"},
    {source: "Junction_1", target: "Junction_4", type: "Train-A", id: "14"},
    {source: "Junction_2", target: "END", type: "Walk", id: "2E"},
    {source: "Junction_2", target: "Junction_5", type: "Train-B", id: "25"},
    {source: "Junction_2", target: "Junction_3", type: "Train-E", id: "23"},
    {source: "Junction_3", target: "Junction_5", type: "Train-D", id: "35"},
    {source: "Junction_3", target: "LOC_1", type: "Walk", id: "3L1"},
    {source: "Junction_3", target: "Junction_4", type: "Train-B", id: "34"},
    {source: "Junction_4", target: "Junction_5", type: "Train-C", id: "45"},
    {source: "Junction_4", target: "Junction_7", type: "Train-A", id: "47"},
    {source: "Junction_4", target: "Junction_6", type: "Train-B", id: "46"},
    {source: "Junction_5", target: "Junction_3", type: "Train-B", id: "53"},
    {source: "Junction_5", target: "LOC_2", type: "Walk", id: "5L2"},
    {source: "Junction_6", target: "Junction_1", type: "Train-B", id: "61"},
    {source: "Junction_6", target: "LOC_3", type: "Walk", id: "6L3"},
    {source: "Junction_7", target: "Junction_3", type: "Train-A", id: "73"},
    {source: "Junction_7", target: "LOC_4", type: "Walk", id: "7L4"},
    {source: "LOC_1", target: "Junction_3", type: "Walk", id: "L13"},
    {source: "LOC_2", target: "Junction_5", type: "Walk", id: "L25"},
    {source: "LOC_3", target: "Junction_6", type: "Walk", id: "L36"},
    {source: "LOC_4", target: "Junction_7", type: "Walk", id: "L47"},
];

links.forEach(function(link){
   solved.forEach(function(unit){
       if(link.id == unit.id){
           link.solve = unit.type;
       }
   })
});

var nodes = {};

// Compute the distinct nodes from the links.
links.forEach(function(link) {
    link.source = nodes[link.source] || (nodes[link.source] = {name: link.source});
    link.target = nodes[link.target] || (nodes[link.target] = {name: link.target});
});

var width = 960,
    height = 500;

var force = d3.layout.force()
    .nodes(d3.values(nodes))
    .links(links)
    .size([width, height])
    .linkDistance(100)
    .charge(-400)
    .on("tick", tick)
    .start();

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

// Per-type markers, as they don't inherit styles.
svg.append("defs").selectAll("marker")
    .data(["Walk", "Train-A", "Train-B", "Trian-C", "Train-D", "Train-E"])
    .enter().append("marker")
    .attr("id", function(d) { return d; })
    .attr("viewBox", "0 -5 10 10")
    .attr("refX", 15)
    .attr("refY", -1.5)
    .attr("markerWidth", 6)
    .attr("markerHeight", 6)
    .attr("orient", "auto")
    .append("path")
    .attr("d", "M0,-5L10,0L0,5");

var path = svg.append("g").selectAll("path")
    .data(force.links())
    .enter().append("path")
    .attr("class", function(d) { return "link " + d.type + " " + d.solve; })
    .attr("marker-end", function(d) { return "url(#" + d.type + ")"; });

var circle = svg.append("g").selectAll("circle")
    .data(force.nodes())
    .enter().append("circle")
    .attr("r", 6)
    .call(force.drag);

var text = svg.append("g").selectAll("text")
    .data(force.nodes())
    .enter().append("text")
    .attr("x", 8)
    .attr("y", ".31em")
    .text(function(d) { return d.name; });

// Use elliptical arc path segments to doubly-encode directionality.
function tick() {
    path.attr("d", linkArc);
    circle.attr("transform", transform);
    text.attr("transform", transform);
}

function linkArc(d) {
    var dx = d.target.x - d.source.x,
        dy = d.target.y - d.source.y,
        dr = Math.sqrt(dx * dx + dy * dy);
    return "M" + d.source.x + "," + d.source.y + "A" + dr + "," + dr + " 0 0,1 " + d.target.x + "," + d.target.y;
}

function transform(d) {
    return "translate(" + d.x + "," + d.y + ")";
}

var table = svg.append("g").selectAll("table")
    .data(force.solved())
    .enter().append("table")
    .text(function(d) { return "link " + d.type + " " + d.solve; })