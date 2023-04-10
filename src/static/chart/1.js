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

const ctx = document.getElementById('speedChart1');

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


// var speedCanvas1 = document.getElementById("speedChart1");

// Chart.defaults.global.defaultFontFamily = "Lato";
// Chart.defaults.global.defaultFontSize = 18;

// var dataFirst = {
//     label: "Car A - Speed (mph)",
//     data: [0, 59, 75, 20, 20, 55, 40],
//     lineTension: 0,
//     fill: false,
//     borderColor: 'red'
//   };

// var dataSecond = {
//     label: "Car B - Speed (mph)",
//     data: [20, 15, 60, 60, 65, 30, 70],
//     lineTension: 0,
//     fill: false,
//   borderColor: 'blue'
//   };

// var speedData = {
//   labels: ["0s", "10s", "20s", "30s", "40s", "50s", "60s"],
//   datasets: [dataFirst, dataSecond]
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