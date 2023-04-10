var xmlhttp = new XMLHttpRequest();
var url = "https://pokeapi.co/api/v2/pokemon/ditto";
xmlhttp.open("GET", url, true);
xmlhttp.send();
xmlhttp.onreadystatechange = function() {
    if(this.readyState==4 && this.status==200){
        var data = JSON.parse(this.responseText);
        console.log(data);
    }
}

const ctx = document.getElementById('speedChart3');

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


// var densityCanvas = document.getElementById("speedChart3");

// Chart.defaults.global.defaultFontFamily = "Lato";
// Chart.defaults.global.defaultFontSize = 18;

// var densityData = {
//   label: 'Density of Planets (kg/m3)',
//   data: [5427, 5243, 5514, 3933, 1326, 687, 1271, 1638],
//   backgroundColor: [
//     'rgba(0, 99, 132, 0.6)',
//     'rgba(30, 99, 132, 0.6)',
//     'rgba(60, 99, 132, 0.6)',
//     'rgba(90, 99, 132, 0.6)',
//     'rgba(120, 99, 132, 0.6)',
//     'rgba(150, 99, 132, 0.6)',
//     'rgba(180, 99, 132, 0.6)',
//     'rgba(210, 99, 132, 0.6)',
//     'rgba(240, 99, 132, 0.6)'
//   ],
//   borderColor: [
//     'rgba(0, 99, 132, 1)',
//     'rgba(30, 99, 132, 1)',
//     'rgba(60, 99, 132, 1)',
//     'rgba(90, 99, 132, 1)',
//     'rgba(120, 99, 132, 1)',
//     'rgba(150, 99, 132, 1)',
//     'rgba(180, 99, 132, 1)',
//     'rgba(210, 99, 132, 1)',
//     'rgba(240, 99, 132, 1)'
//   ],
//   borderWidth: 2,
//   hoverBorderWidth: 0
// };

// var chartOptions = {
//   scales: {
//     yAxes: [{
//       barPercentage: 0.5
//     }]
//   },
//   elements: {
//     rectangle: {
//       borderSkipped: 'left',
//     }
//   }
// };

// var barChart = new Chart(densityCanvas, {
//   type: 'horizontalBar',
//   data: {
//     labels: ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
//     datasets: [densityData],
//   },
//   options: chartOptions
// });