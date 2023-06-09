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

const ctx = document.getElementById('speedChart4');

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


// var densityCanvas = document.getElementById("speedChart4");

// Chart.defaults.global.defaultFontFamily = "Lato";
// Chart.defaults.global.defaultFontSize = 18;

// var densityData = {
//   label: 'Density of Planet (kg/m3)',
//   data: [5427, 5243, 5514, 3933, 1326, 687, 1271, 1638],
//   backgroundColor: 'rgba(0, 99, 132, 0.6)',
//   borderColor: 'rgba(0, 99, 132, 1)',
//   yAxisID: "y-axis-density"
// };
 
// var gravityData = {
//   label: 'Gravity of Planet (m/s2)',
//   data: [3.7, 8.9, 9.8, 3.7, 23.1, 9.0, 8.7, 11.0],
//   backgroundColor: 'rgba(99, 132, 0, 0.6)',
//   borderColor: 'rgba(99, 132, 0, 1)',
//   yAxisID: "y-axis-gravity"
// };
 
// var planetData = {
//   labels: ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
//   datasets: [densityData, gravityData]
// };
 
// var chartOptions = {
//   scales: {
//     xAxes: [{
//       barPercentage: 1,
//       categoryPercentage: 0.6
//     }],
//     yAxes: [{
//       id: "y-axis-density"
//     }, {
//       id: "y-axis-gravity"
//     }]
//   }
// };
 
// var barChart = new Chart(densityCanvas, {
//   type: 'bar',
//   data: planetData,
//   options: chartOptions
// });