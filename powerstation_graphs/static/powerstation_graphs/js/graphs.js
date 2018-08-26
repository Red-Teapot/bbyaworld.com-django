$(function() {
    var trace_names = {
        wheat_pp: 'Пшеница',
        coal_pp: 'Уголь',
        diamond_pp: 'Алмазы',
        exp_market: 'Опыт',
        buy: 'Покупка',
        sell: 'Продажа',
    };

    var layout = {
        xaxis: {
            title: 'Время'
        },
        yaxis: {
            title: 'Значение'
        }
    };

    function formatDate(date) {
        var result = '';

        var day = date.getDate();
        result += day < 10 ? '0' + day : day;
        result += '.';

        var month = date.getMonth() + 1;
        result += month < 10 ? '0' + month : month;
        result += '.';

        var year = date.getFullYear();
        result += year;

        return result;
    }

    function createPlot(plotType, dataTypes, data, title) {
        var traces = [];
        var traceIndicesByName = [];

        var plotDivId = 'plot_' + plotType;

        $('#plot').append($('<div id="' + plotDivId + '"></div>'));
        var plotDiv = document.getElementById(plotDivId);
        var checkboxForm = $(plotDiv).append('<form></form>');

        $.each(data, function(type, values) {
            if(!dataTypes.includes(type))
                return true;

            var dates = values.dates.map(function(val) {
                return formatDate(new Date(val));
            });

            var trace = {
                x: dates,
                y: values.values,
                type: 'scatter',
                name: trace_names[type]
            };

            traceIndicesByName[type] = traces.length;
            traces.push(trace);
        });

        layout.title = title;
        Plotly.plot(plotDiv, traces, layout);

        if(dataTypes.length > 1) {
            $.each(dataTypes, function(k) {
                var id = k;
                var label_text = k in trace_names ? trace_names[k] : k;
                
                var paragraph = $('<p></p>');
                var checkbox = $('<input type="checkbox" id="' + id + '" checked />');
                var label = $('<label for="' + id + '">' + label_text + '</label>');
    
                paragraph.append(checkbox);
                paragraph.append(label);
    
                checkbox.change(function() {
                    var id = this.id;
    
                    Plotly.restyle(plotDiv, 'visible', this.checked, traceIndicesByName[id]);
                });
    
                checkboxForm.append(paragraph);
            });
        }
    }

    var expTable = [ // Min, max, sell, buy
        [-Infinity, -1000, 1, 2],
        [-999, -500, 2, 4],
        [-499, -250, 4, 6],
        [-249, -100, 6, 8],
        [-99, -50, 10, 12],
        [-49, 0, 12, 14],

        [1, 49, 14, 16],
        [50, 99, 16, 18],
        [100, 249, 20, 24],
        [250, 499, 24, 30],
        [500, 999, 32, 38],
        [1000, 1999, 40, 48],
        [2000, 4999, 48, 64],
        [5000, 9999, 56, 80],
        [10000, Infinity, 64, 96]
    ];

    $.get('get-data', null, function(data) {

        createPlot('powerplants', ['wheat_pp', 'coal_pp', 'diamond_pp'], data, 'Электростанции');

        // Process exp market data
        var expMarketData = data.exp_market;
        var dates = expMarketData.dates;
        var sellData = [];
        var buyData = [];

        $.each(expMarketData.values, function(val) {
            for(var i = 0; i < expTable.length; i++) {
                var expEntry = expTable[i];

                if(val >= expEntry[0] && val <= expEntry[1]) {
                    sellData.push(expEntry[2]);
                    buyData.push(expEntry[3]);
                }
            }
        });

        createPlot('exp_market', ['buy', 'sell'], {
            sell: {
                dates: dates,
                values: sellData
            },
            buy: {
                dates: dates,
                values: buyData
            }
        }, 'Опыт');

    });
});