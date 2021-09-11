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

window.onload = () => {
    var totalChart = new Chart(
        document.getElementById('totalChart'), {
            type: 'bar',
    
            data: {
                labels: ["모집인원", "관심인원", "상담인원"],
                datasets: [{
                    axis: 'y',
                    label: '인원',
                    backgroundColor: [
                        CUSTOM_COLORS.indigo,
                        CUSTOM_COLORS.skyblue,
                        CUSTOM_COLORS.grey
                    ],
                    borderWidth: 1,
                    data: totals
                }]
            },
            plugins: [ChartDataLabels],
            options: {
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
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
                        right: 50
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
                },
            }
    });





    var cnslRstChart = new Chart(
        document.getElementById('cnslRstChart'), {
            type: 'bar',
    
            data: {
                labels: ["지원예정", "등록예정", "지원미정", "타 대학관심"],
                datasets: [{
                    label: '인원',
                    backgroundColor: [
                        CUSTOM_COLORS.indigo,
                        CUSTOM_COLORS.skyblue,
                        CUSTOM_COLORS.grey,
                        CUSTOM_COLORS.grey
                    ],
                    borderWidth: 1,
                    data: cnslRstData
                }]
            },
            plugins: [ChartDataLabels],
            options: {
                responsive: true,
                maintainAspectRatio: false,
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
                },
            }
    });



    var schoolChart = new Chart(
        document.getElementById('schoolChart'), {
            type: 'bar',
    
            data: {
                labels: schoolIdx,
                datasets: [{
                    label: '인원',
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
                    borderWidth: 1,
                    data: schoolData
                }]
            },
            plugins: [ChartDataLabels],
            options: {
                responsive: true,
                maintainAspectRatio: false,
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
                },
            }
    });




    var seltAppr = new Chart(
        document.getElementById('seltAppr'), {
            type: 'pie',
    
            data: {
                labels: seltApprNmData[0],
                datasets: [{
                    label: '인원',
                    data: seltApprNmData[1],
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
                responsive: true,
                maintainAspectRatio: false,
                layout: {
                    padding: {
                        top: 20,
                        bottom: 20
                    }
                },
                plugins: {
                    legend: {
                        position: 'right',
                        display: true,
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
}
