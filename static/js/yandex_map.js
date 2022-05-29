let map = new Vue({
    el: '#map',
    data: {
        isOpen: true
    },
    methods: {
        loadMap: function(events){
            ymaps.ready(init);
            console.log(events)
            function init() {
                var myMap = new ymaps.Map('map', {
                    center: [55.751574, 37.573856],
                    zoom: 11,
                    controls: []
                }, {
                    searchControlProvider: 'yandex#search'
                });

                for (i=0; i < events.length; i++) {
                    date_start = new Date(events[i].fields.date_start)
                    date_start = date_start.toLocaleDateString() + ' ' + date_start.toLocaleTimeString()
                    date_end = new Date(events[i].fields.date_end)
                    date_end = date_end.toLocaleDateString() + ' ' + date_end.toLocaleTimeString()

                    var placemark = new ymaps.Placemark([events[i].fields.coordinates_latitude, events[i].fields.coordinates_longitude], {
                        // Зададим содержимое заголовка балуна.
                        balloonContentHeader: '<a href = "/events/' + events[i].pk + '">' + events[i].fields.name + '</a><br>' +
                            '<span class="description">Старшее поколение</span>',
                        // Зададим содержимое основной части балуна.
                        balloonContentBody: '<img src="' + events[i].fields.avatar_url + '" height="100" width="150"> <br><br> ' +
                            '<b>' + date_start + ' - ' + date_end + '</b> <br/>',
                        // Зададим содержимое нижней части балуна.
                        balloonContentFooter: 'Информация предоставлена:<br/>' + events[i].fields.name,
                        // Зададим содержимое всплывающей подсказки.
                        hintContent: events[i].fields.name
                    });

                    myMap.geoObjects.add(placemark);
                }
            }
        }
    }
});
