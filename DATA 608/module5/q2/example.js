d3.csv("https://raw.githubusercontent.com/charleyferrari/CUNY_DATA_608/master/module5/js_examples/Hello%20World/data/presidents.csv", function(data){
    tabulate(data, ['Name', 'Height', 'Weight']);
});

// from http://bl.ocks.org/jfreels/6734025
function tabulate(data, columns) {
    var table = d3.select('#q1').append('table')
    var thead = table.append('thead')
    var	tbody = table.append('tbody');
    
    // append the header row
    thead.append('tr')
    .selectAll('th')
    .data(columns).enter()
    .append('th')
    .text(function (column) { return column; });

    // create a row for each object in the data
    var rows = tbody.selectAll('tr')
    .data(data)
    .enter()
    .append('tr');

    // create a cell in each row for each column
    var cells = rows.selectAll('td')
    .data(function (row) {
        return columns.map(function (column) {
        return {column: column, value: row[column]};
        });
    })
    .enter()
    .append('td')
    .text(function (d) { return d.value; });

  return table;
}

function getPrez(){
    d3.csv("https://raw.githubusercontent.com/charleyferrari/CUNY_DATA_608/master/module5/js_examples/Hello%20World/data/presidents.csv", function(presidents){
        var name = $("#president").val()
        var filtered = presidents.filter(president => president.Name == name)

        var message = "";
        switch (filtered.length) {
            case 0:
                message = "No results found."
                break

            case 1:
                prez = filtered[0]
                message = prez.Name + " " + prez.Height + " " + prez.Weight
                break

            default:
                message = "Please enter a valid name."
        }

        $('#q2').text(message);
    })   
}