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


const ctx = document.getElementById('speedChart6');

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


// var speedCanvas = document.getElementById("speedChart6");

// Chart.defaults.global.defaultFontFamily = "Lato";
// Chart.defaults.global.defaultFontSize = 18;

// var speedData = {
//   labels: ["0s", "10s", "20s", "30s", "40s", "50s", "60s"],
//   datasets: [{
//     label: "Car Speed (mph)",
//     data: [0, 59, 75, 20, 20, 55, 40],
//     lineTension: 0,
//     fill: false,
//     borderColor: 'orange',
//     backgroundColor: 'transparent',
//     borderDash: [5, 5],
//     pointBorderColor: 'orange',
//     pointBackgroundColor: 'rgba(255,150,0,0.5)',
//     pointRadius: 5,
//     pointHoverRadius: 10,
//     pointHitRadius: 30,
//     pointBorderWidth: 2,
//     pointStyle: 'rectRounded'
//   }]
// };

// var chartOptions = {
//   legend: {
//     display: true,
//     position: 'top',
//     labels: {
//       boxWidth: 80,
//       fontColor: 'black'
//     }
//   }
// };

// var lineChart = new Chart(speedCanvas, {
//   type: 'line',
//   data: speedData,
//   options: chartOptions
// });