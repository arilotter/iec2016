
// http://blog.thomsonreuters.com/index.php/mobile-patent-suits-graphic-of-the-day/
var fastest = ['START', 'Junction 1', 'Junction 2', 'END'];
var cheapest = ['START', 'Junction 1', 'Junction 4', 'END'];

var links = [
    {source: 'START',      target: 'Junction 1', type: 'Walk',    },
    {source: 'Junction 1', target: 'Junction 2', type: 'Train-B', },
    {source: 'Junction 1', target: 'Junction 4', type: 'Train-A', },
    {source: 'Junction 2', target: 'END',        type: 'Walk',    },
    {source: 'Junction 2', target: 'Junction 5', type: 'Train-B', },
    {source: 'Junction 2', target: 'Junction 3', type: 'Train-E', },
    {source: 'Junction 3', target: 'Junction 5', type: 'Train-D', },
    {source: 'Junction 3', target: 'Location 1',      type: 'Walk'},
    {source: 'Junction 3', target: 'Junction 4', type: 'Train-B', },
    {source: 'Junction 4', target: 'Junction 5', type: 'Train-C', },
    {source: 'Junction 4', target: 'Junction 7', type: 'Train-A', },
    {source: 'Junction 4', target: 'Junction 6', type: 'Train-B', },
    {source: 'Junction 5', target: 'Junction 3', type: 'Train-B', },
    {source: 'Junction 5', target: 'Location 2',      type: 'Walk'},
    {source: 'Junction 6', target: 'Junction 1', type: 'Train-B', },
    {source: 'Junction 6', target: 'Location 3',      type: 'Walk'},
    {source: 'Junction 7', target: 'Junction 3', type: 'Train-A', },
    {source: 'Junction 7', target: 'Location 4',      type: 'Walk'},
    {source: 'Location 1',      target: 'Junction 3', type: 'Walk'},
    {source: 'Location 2',      target: 'Junction 5', type: 'Walk'},
    {source: 'Location 3',      target: 'Junction 6', type: 'Walk'},
    {source: 'Location 4',      target: 'Junction 7', type: 'Walk'},
];

links.forEach(link => {
  fastest.forEach((unit, index) => {
    if (link.source === fastest[index - 1] && link.target === unit) {
      link.solve = 'F';
    }
  });
  cheapest.forEach((unit, index) => {
    if (link.source === cheapest[index - 1] && link.target === unit) {
      link.solve += ' C';
    }
  });
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
    .on('tick', tick)
    .start();

var svg = d3.select('body').append('svg')
    .attr('width', width)
    .attr('height', height);

// Per-type markers, as they don't inherit styles.
svg.append('defs').selectAll('marker')
    .data(['Walk', 'Train-A', 'Train-B', 'Trian-C', 'Train-D', 'Train-E'])
    .enter().append('marker')
    .attr('id', function(d) { return d; })
    .attr('viewBox', '0 -5 10 10')
    .attr('refX', 15)
    .attr('refY', -1.5)
    .attr('markerWidth', 6)
    .attr('markerHeight', 6)
    .attr('orient', 'auto')
    .append('path')
    .attr('d', 'M0,-5L10,0L0,5');

var path = svg.append('g').selectAll('path')
    .data(force.links())
    .enter().append('path')
    .attr('class', function(d) { return 'link ' + d.type + ' ' + d.solve;})
    .attr('marker-end', function(d) { return 'url(#' + d.type + ')'; });

var circle = svg.append('g').selectAll('circle')
    .data(force.nodes())
    .enter().append('circle')
    .attr('r', 9)
    .call(force.drag);

var text = svg.append('g').selectAll('text')
    .data(force.nodes())
    .enter().append('text')
    .attr('x', 8)
    .attr('y', '.31em')
    .text(function(d) { return d.name; });

// Use elliptical arc path segments to doubly-encode directionality.
function tick() {
    path.attr('d', linkArc);
    circle.attr('transform', transform);
    text.attr('transform', transform);
}

function linkArc(d) {
    var dx = d.target.x - d.source.x,
        dy = d.target.y - d.source.y,
        dr = Math.sqrt(dx * dx + dy * dy);
    return 'M' + d.source.x + ',' + d.source.y + 'A' + dr + ',' + dr + ' 0 0,1 ' + d.target.x + ',' + d.target.y;
}

function transform(d) {
    return 'translate(' + d.x + ',' + d.y + ')';
}

var table = svg.append('g').selectAll('table')
    .data(force.solved())
    .enter().append('table')
    .text(function(d) { return 'link ' + d.type + ' ' + d.solve; })
