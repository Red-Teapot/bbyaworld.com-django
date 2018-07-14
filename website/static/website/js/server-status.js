$(function() {
    $.get('/server-status', null, function(data) {
        $('#server-status-indicator').addClass(data['online'] ? 'on' : 'off');

        if(data['online']) {
            $('#server-players > *').remove();
            data['players']['list'].forEach(function(element, index, array) {
                var item = $(document.createElement('li'));
                item.addClass('item');

                var head = $(document.createElement('img'));
                head.attr('src', 'https://minotar.net/helm/' + element + '/32');

                var nickname = $(document.createTextNode(element));

                item.append(head);
                item.append(nickname);

                $('#server-players').append(item);
            });

            $('#server-players-count').text(data['players']['online']);
        }
    });
});
