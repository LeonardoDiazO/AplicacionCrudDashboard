var xmlhttp = new XMLHttpRequest();
var url = "http://localhost:4000/api/herramientas";
xmlhttp.open("GET", url, true);
xmlhttp.send();
xmlhttp.onreadystatechange = function() {
    if(this.readyState==4 && this.status==200){
        var data = JSON.parse(this.responseText);
        console.log(data);
    }
}

const ctx = document.getElementById('speedChart2');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
