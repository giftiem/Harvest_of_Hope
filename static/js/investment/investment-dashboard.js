/*! For license information please see investment-dashboard.js.LICENSE.txt */
"use strict";
document.addEventListener("DOMContentLoaded", (function() {
    window.randomScalingFactor = function() {
        return Math.round(20 * Math.random())
    };
    var a = document.getElementById("areachartblue1").getContext("2d"),
        t = a.createLinearGradient(0, 0, 0, 110);
    t.addColorStop(0, "rgba(0, 73, 232, 1)"), t.addColorStop(1, "rgba(0, 73, 232, 0)");
    var o = {
            type: "bar",
            data: {
                labels: ["1", "2", "3", "4", "5", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"],
                datasets: [{
                    label: "# of Votes",
                    data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()],
                    radius: 0,
                    backgroundColor: t,
                    borderColor: "#015EC2",
                    borderWidth: 0,
                    borderRadius: 4,
                    fill: !0,
                    tension: .5
                }]
            },
            options: {
                maintainAspectRatio: !1,
                plugins: {
                    legend: {
                        display: !1
                    },
                    tooltip: {
                        enabled: !0
                    }
                },
                scales: {
                    y: {
                        display: !1,
                        beginAtZero: !0
                    },
                    x: {
                        display: !1
                    }
                }
            }
        },
        n = new Chart(a, o);
    setInterval((function() {
        o.data.datasets.forEach((function(a) {
            a.data = a.data.map((function() {
                return randomScalingFactor()
            }))
        })), n.update()
    }), 3e3);
    var r = document.getElementById("summarychart").getContext("2d"),
        e = r.createLinearGradient(0, 0, 0, 280);
    e.addColorStop(0, "rgba(0, 73, 232, 0.85)"), e.addColorStop(1, "rgba(0, 73, 232, 0)");
    var d = {
            type: "line",
            data: {
                labels: ["10:30", "11:00", "11:30", "12:00", "12:30", "01:00", "01:30"],
                datasets: [{
                    label: "# of Votes",
                    data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()],
                    radius: 0,
                    backgroundColor: e,
                    borderColor: "#5840ef",
                    borderWidth: 2,
                    fill: !0,
                    tension: .5
                }]
            },
            options: {
                animation: !0,
                maintainAspectRatio: !1,
                plugins: {
                    legend: {
                        display: !1
                    }
                },
                scales: {
                    y: {
                        display: !0,
                        beginAtZero: !0
                    },
                    x: {
                        grid: {
                            display: !0
                        },
                        display: !0,
                        beginAtZero: !0
                    }
                }
            }
        },
        i = new Chart(r, d);
    setInterval((function() {
        d.data.datasets.forEach((function(a) {
            a.data = a.data.map((function() {
                return randomScalingFactor()
            }))
        })), i.update()
    }), 3e3);
    var c = document.getElementById("doughnutchart").getContext("2d");
    new Chart(c, {
        type: "doughnut",
        data: {
            labels: ["Daily Vages", "Cancelled Bookings", "Oxygen", "Manpower", "Medical Facilities"],
            datasets: [{
                label: "Expense categories",
                data: [40, 35, 15, 25, 20],
                backgroundColor: ["#6faa00", "#ffc107", "#fd7e14", "#0049e8", "#becede"],
                borderWidth: 0
            }]
        },
        options: {
            responsive: !0,
            cutout: 80,
            tooltips: {
                position: "nearest",
                yAlign: "bottom"
            },
            plugins: {
                legend: {
                    display: !1,
                    position: "top"
                },
                title: {
                    display: !1,
                    text: "Chart.js Doughnut Chart"
                }
            },
            layout: {
                padding: 0
            }
        }
    })
}));