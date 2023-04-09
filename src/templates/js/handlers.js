const enableEventHandlers = data => {

    document.querySelector('#featuresOptions').onchange = e => {

        const { value: property, text: label } = e.target.selectedOptions[0]

        const newData = herramientas.map(herramienta => data[property])

        updateChartData('featuresChart', newData, label)
    }
}