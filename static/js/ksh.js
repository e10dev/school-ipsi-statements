const CHART_COLORS = {
    red: 'rgb(255, 99, 132)',
    orange: 'rgb(255, 159, 64)',
    yellow: 'rgb(255, 205, 86)',
    green: 'rgb(75, 192, 192)',
    blue: 'rgb(54, 162, 235)',
    purple: 'rgb(153, 102, 255)',
    grey: 'rgb(201, 203, 207)'
};

const BACKGROUND_COLORS = {
    red: 'rgba(255, 99, 132, 0.2)',
    orange: 'rgba(255, 159, 64, 0.2)',
    yellow: 'rgba(255, 205, 86, 0.2)',
    green: 'rgba(75, 192, 192, 0.2)',
    blue: 'rgba(54, 162, 235, 0.2)',
    purple: 'rgba(153, 102, 255, 0.2)',
    grey: 'rgba(201, 203, 207, 0.2)'
};

const CUSTOM_COLORS = {
    indigo: 'rgb(39, 49, 100)',
    skyblue: 'rgb(97, 214, 255)',
    grey: 'rgb(217, 217, 217)'
};

const CUSTOM_BACKGROUND_COLORS = {
    indigo: 'rgba(39, 49, 100, 0.7)',
    skyblue: 'rgba(97, 214, 255, 0.7)',
    grey: 'rgba(242, 246, 255, 0.7)'
};

const totalizer = {
    id: 'totalizer',
  
    beforeUpdate: chart => {
      let totals = {}
      let utmost = 0
  
      chart.data.datasets.forEach((dataset, datasetIndex) => {
        if (chart.isDatasetVisible(datasetIndex)) {
          utmost = datasetIndex
          dataset.data.forEach((value, index) => {
            totals[index] = (totals[index] || 0) + value
          })
        }
      })
  
      chart.$totalizer = {
        totals: totals,
        utmost: utmost
      }
    }
  }

window.onload = () => {
    var totalChart = new Chart(
        document.getElementById('totalChart').getContext('2d'), {
            type: 'bar',
            data: {
                labels: ["모집인원", "관심인원", "상담인원"],
                datasets: [{
                    label: "인원",
                    backgroundColor: [
                        CUSTOM_COLORS.indigo,
                        CUSTOM_COLORS.skyblue,
                        CUSTOM_COLORS.grey
                    ],
                    borderWidth: 1,
                    data: totals,
                }],
            },
            plugins: [ChartDataLabels],
            options: {
                responsive: false,
                indexAxis: 'y',
                scales: {
                    x: {
                        ticks: {
                            color: '#000'
                        }
                    },
                    y: {
                        ticks: {
                            color: '#000'
                        }
                    }
                },
                layout: {
                    padding: 20
                },
                plugins: {
                    legend: {
                        display: false,
                    },
                    datalabels: {
                        color: 'black',
                        anchor: 'end',
                        align: 'end',
                        offset: 5,
                        padding: 5,
                        borderWidth: 1,
                        formatter:function(value, context) {
                            return value + "명";
                        }
                    }
                },
            }
    });



    var topschoolChart = new Chart(
        document.getElementById('topschoolChart'), {
            type: 'bar',
    
            data: {
                labels: schoolIdx,
                datasets: [{
                    axis: 'y',
                    label: "인원",
                    fill: false,
                    backgroundColor: [
                        CUSTOM_COLORS.indigo,
                        CUSTOM_COLORS.skyblue,
                        CUSTOM_COLORS.skyblue,
                        CUSTOM_COLORS.skyblue,
                        CUSTOM_COLORS.skyblue,
                        CUSTOM_COLORS.skyblue,
                        CUSTOM_COLORS.skyblue,
                        CUSTOM_COLORS.skyblue,
                        CUSTOM_COLORS.skyblue,
                        CUSTOM_COLORS.skyblue,
                    ],
                    data: schoolData,
                }]
            },
            plugins: [ChartDataLabels],
            options: {
                responsive: false,
                scales: {
                    x: {
                        ticks: {
                            color: '#000'
                        }
                    },
                    y: {
                        ticks: {
                            color: '#000'
                        }
                    }
                },
                layout: {
                    padding: {
                        top: 50
                    }
                },
                plugins: {
                    legend: {
                        display: false,
                    },
                    datalabels: {
                        color: 'black',
                        anchor: 'end',
                        align: 'end',
                        offset: 5,
                        padding: 5,
                        borderWidth: 1,
                        formatter:function(value, context) {
                            return value + "명";
                        }
                    }
                }
            }
    });




    var interestseltApprChart = new Chart(
        document.getElementById('interestseltApprChart'), {
            type: 'doughnut',
    
            data: {
                labels: Object.keys(interestseltAppr),
                datasets: [{
                    label: 'test',
                    data: Object.values(interestseltAppr),
                    backgroundColor: [
                        CUSTOM_COLORS.indigo,
                        CUSTOM_COLORS.skyblue,
                        CUSTOM_COLORS.grey
                    ],
                    hoverOffset: 4
                }]
            },
            plugins: [ChartDataLabels],
    
            options: {
                responsive: false,
                plugins: {
                    legend: {
                        display: true,
                        position: 'right'
                    },
                    datalabels: {
                        color: 'black',
                        anchor: 'end',
                        align: 'end',
                        offset: 5,
                        borderWidth: 1,
                        formatter:function(value, context) {
                            var total = 0;
                            for (var i = 0; i < context.dataset.data.length; i++)
                                total += context.dataset.data[i];
                            return Math.round((value / total)*100) + '%';
                        }
                    }
                },
                layout: {
                    padding: 20
                }
            }
    });




    var cnslAplyChart = new Chart(
        document.getElementById('cnslAplyChart'), {
            type: 'line',
    
            data: {
                labels: cnslAplyData[0],
                datasets: [
                    {
                        label: '상담인원',
                        data: cnslAplyData[2],
                        borderColor: [CUSTOM_COLORS.indigo],
                        backgroundColor: [CUSTOM_COLORS.indigo],
                    },
                    {
                        label: '지원예정인원',
                        data: cnslAplyData[3],
                        borderColor: [CUSTOM_COLORS.skyblue],
                        backgroundColor: [CUSTOM_COLORS.skyblue],
                    }
                ]
            },
            plugins: [ChartDataLabels],
            options: {
                responsive: false,
                elements: {
                    line: {
                        tension: 0.4
                    }
                },
                layout: {
                    padding: {
                        top: 20
                    }
                },
                scales: {
                    x: {
                        ticks: {
                            color: '#000'
                        }
                    },
                    y: {
                        ticks: {
                            color: '#000'
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: true,
                        position: 'bottom'
                    },
                    datalabels: {
                        color: 'black',
                        anchor: 'end',
                        align: 'end',
                        offset: 5,
                        borderWidth: 1,
                        formatter:function(value, context) {
                            return value + "명";
                        }
                    }
                }
            }
    });




    // 0: idx, 1: 관심인원, 2: 모집인원-관심인원, 3: 모집인원
    var majorChart1 = new Chart(
        document.getElementById('majorChart1'), {
            type: 'bar',
    
            data: {
                labels: majorData1[0],
                datasets: [
                    {
                        label: '관심인원',
                        backgroundColor: [CUSTOM_COLORS.skyblue],
                        data: majorData1[1],
                        categoryPercentage: 1.0,
                        barPercentage: 0.7
                    },
                    {
                        label: '모집인원',
                        backgroundColor: [CUSTOM_COLORS.indigo],
                        data: majorData1[2],
                        categoryPercentage: 1.0,
                        barPercentage: 0.7
                    }
                ]
            },
            plugins: [ChartDataLabels, totalizer],
            options: {
                indexAxis: 'y',
                layout: {
                    padding: {
                        right: 20
                    }
                },
                plugins: {
                    legend: {
                        display: false,
                    },
                    datalabels: {
                        color: 'black',
                        anchor: 'end',
                        align: 'end',
                        offset: 5,
                        borderWidth: 1,
                        formatter:function(value, context) {
                            const total = context.chart.$totalizer.totals[context.dataIndex];
                            return (total - value) + "명 / " + total + "명";
                        },
                        display: function(context) {
                            return context.datasetIndex === context.chart.$totalizer.utmost;
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                var label = context.dataset.label || '';

                                if (label) {
                                    label += ': ';
                                }
                                label += context.dataset.label == "관심인원" ? context.parsed.x + "명" : context.chart.$totalizer.totals[context.dataIndex] + "명";
                                return label;
                            }
                        }
                    }
                },
                responsive: false,
                scales: {
                    x: {
                        min: 0,
                        stacked: true,
                        ticks: {
                            color: '#000',
                        }
                    },
                    y: {
                        stacked: true,
                        ticks: {
                            color: '#000',
                            callback: function(value, index) {
                                labelValue = this.getLabelForValue(value);
                                return labelValue.length >= 17 ? labelValue.split(' ')[1] : labelValue;
                            }
                        }
                    }
                },
            }
    });

	




    var majorChart2 = new Chart(
        document.getElementById('majorChart2'), {
            type: 'bar',
    
            data: {
                labels: majorData2[0],
                datasets: [
                    {
                        label: '관심인원',
                        backgroundColor: [CUSTOM_COLORS.skyblue],
                        data: majorData2[1],
                        categoryPercentage: 1.0,
                        barPercentage: 0.5
                    },
                    {
                        label: '모집인원',
                        backgroundColor: [CUSTOM_COLORS.indigo],
                        data: majorData2[2],
                        categoryPercentage: 1.0,
                        barPercentage: 0.5
                    }
                ]
            },
            plugins: [ChartDataLabels, totalizer],
            options: {
                indexAxis: 'y',
                layout: {
                    padding: {
                        right: 70
                    }
                },
                plugins: {
                    legend: {
                        display: false,
                    },
                    datalabels: {
                        color: 'black',
                        anchor: 'end',
                        align: 'end',
                        offset: 5,
                        borderWidth: 1,
                        formatter:function(value, context) {
                            const total = context.chart.$totalizer.totals[context.dataIndex];
                            return (total - value) + "명 / " + total + "명";
                        },
                        display: function(context) {
                            return context.datasetIndex === context.chart.$totalizer.utmost;
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                var label = context.dataset.label || '';

                                if (label) {
                                    label += ': ';
                                }
                                label += context.dataset.label == "관심인원" ? context.parsed.x + "명" : context.chart.$totalizer.totals[context.dataIndex] + "명";
                                return label;
                            }
                        }
                    }
                },
                responsive: false,
                scales: {
                    x: {
                        min: 0,
                        stacked: true,
                        ticks: {
                            color: '#000',
                        }
                    },
                    y: {
                        stacked: true,
                        ticks: {
                            color: '#000',
                            callback: function(value, index) {
                                labelValue = this.getLabelForValue(value);
                                return labelValue.length >= 17 ? labelValue.split(' ')[1] : labelValue;
                            }
                        }
                    }
                },
            }
    });
}