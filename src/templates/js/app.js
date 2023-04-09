Chart.defaults.color = '#fff'
Chart.defaults.borderColor = '#444'


const printCharts = () => {


    //data del DashBoard
    fetchCoastersData('http://127.0.0.1:4000/api/herramientas')
        .then(([ data ]) => {
            renderModelsChart(data)
            renderFeaturesChart(data)
            renderYearsChart(data)
            enableEventHandlers()
            console.log("Que tienes tu: "+data);
        })

    
}

const renderModelsChart = herramientas => {

    // en la grafica se ve reflejado los data
    const uniqueModels = [...new Set(data.map(data => data.model))]

    const data = {
        labels: uniqueModels,
        datasets: [{
            data: uniqueModels.map(currentModel => data.filter(data => data.model === currentModel). legend),
            borderColor: getDataColors(),
            backgroundColor: getDataColors(20)
        }]      
    }

    const options = { 
        Plugins: {
            legend: { position: 'left' }
        }
    }

    new Chart('modelsChart', {type: 'dougnut', data, options })
}


    const renderFeaturesChart = data => {
        
        const data = {
            labels: data.map(data => data.name ),
            datasets: [{
                label: 'Altura (m)',
                data: data.map(data => data.heigth),
                borderColor: getDataColors()[0],
                backgroundColor: getDataColors(20)[0]
            }]
        }

        const options = {
            Plugins: {
                legend: { display: false }
            },
            scales: {
                r:{
                    ticks: { display: false}
                }
            }
        }

     new Chart('featuresChart', {type: 'radar', data, options })

}

    const renderYearsChart = data => {
         // grafica de años depende el año de los data que vamos a hacer referencia  del año
         const years = ['1998-2000', '2001-2003', '2004-2006', '2007-2009' ]

        const data = {
             labels: years,
             datasets: [{
                data: getCoastersByYear(herramientas, years),
                tension: .5,
                borderColor: getDataColors()[1],
                backgroundColor: getDataColors(20)[1],
                fill: true,
                pointBorderWidth: 5

             }]
       }

       const options = {
            Plugins: {
                leyend:{ display: false }
            }
       }

       new Chart('yearsChart', { type: 'line', data, options })
}

printCharts()
