$(function() {
    const plot_elem = document.getElementById('plot');

    const trace_names = {
        wheat_pp: 'Пшеница',
        coal_pp: 'Уголь',
        diamond_pp: 'Алмазы',
        exp_market: 'Опыт',
    };

    const layout = {
        xaxis: {
            title: 'Время'
        },
        yaxis: {
            title: 'Значение'
        }
    };

    var traces = [];
    var trace_indices_by_name = {};

    $.get('get-data', null, function(data) {
        $.each(data, function(type, values) {
            var dates = values.dates.map((val) => {
                var date = new Date(val);
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
            });

            var trace = {
                x: dates,
                y: values.values,
                type: 'scatter',
                name: trace_names[type]
            };

            trace_indices_by_name[type] = traces.length;
            traces.push(trace);
        });

        Plotly.plot(plot_elem, traces, layout);

        Plotly.restyle(plot_elem, 'visible', $('#wheat_pp_checkbox')[0].checked, trace_indices_by_name['wheat_pp']);
        Plotly.restyle(plot_elem, 'visible', $('#coal_pp_checkbox')[0].checked, trace_indices_by_name['coal_pp']);
        Plotly.restyle(plot_elem, 'visible', $('#diamond_pp_checkbox')[0].checked, trace_indices_by_name['diamond_pp']);
        Plotly.restyle(plot_elem, 'visible', $('#exp_market_checkbox')[0].checked, trace_indices_by_name['exp_market']);
    });

    $('#wheat_pp_checkbox').change(function() {
        Plotly.restyle(plot_elem, 'visible', this.checked, trace_indices_by_name['wheat_pp']);
    });
    $('#coal_pp_checkbox').change(function() {
        Plotly.restyle(plot_elem, 'visible', this.checked, trace_indices_by_name['coal_pp']);
    });
    $('#diamond_pp_checkbox').change(function() {
        Plotly.restyle(plot_elem, 'visible', this.checked, trace_indices_by_name['diamond_pp']);
    });
    $('#exp_market_checkbox').change(function() {
        Plotly.restyle(plot_elem, 'visible', this.checked, trace_indices_by_name['exp_market']);
    });
});