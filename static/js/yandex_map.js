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

                    MyBalloonLayout = ymaps.templateLayoutFactory.createClass(
                        '<div class="popover top">' +
                        '<a class="close" href="#">&times;</a>' +
                        '<div class="arrow"></div>' +
                        '<div class="popover-inner">' +
                        '$[[options.contentLayout observeSize minWidth=235 maxWidth=300 maxHeight=350]]' +
                        '</div>' +
                        '</div>', {
                        /**
                         * Строит экземпляр макета на основе шаблона и добавляет его в родительский HTML-элемент.
                         * @see https://api.yandex.ru/maps/doc/jsapi/2.1/ref/reference/layout.templateBased.Base.xml#build
                         * @function
                         * @name build
                         */
                        build: function () {
                            this.constructor.superclass.build.call(this);

                            this._$element = $('.popover', this.getParentElement());

                            this.applyElementOffset();

                            this._$element.find('.close')
                                .on('click', $.proxy(this.onCloseClick, this));
                        },

                        /**
                         * Удаляет содержимое макета из DOM.
                         * @see https://api.yandex.ru/maps/doc/jsapi/2.1/ref/reference/layout.templateBased.Base.xml#clear
                         * @function
                         * @name clear
                         */
                        clear: function () {
                            this._$element.find('.close')
                                .off('click');

                            this.constructor.superclass.clear.call(this);
                        },

                        /**
                         * Метод будет вызван системой шаблонов АПИ при изменении размеров вложенного макета.
                         * @see https://api.yandex.ru/maps/doc/jsapi/2.1/ref/reference/IBalloonLayout.xml#event-userclose
                         * @function
                         * @name onSublayoutSizeChange
                         */
                        onSublayoutSizeChange: function () {
                            MyBalloonLayout.superclass.onSublayoutSizeChange.apply(this, arguments);

                            if(!this._isElement(this._$element)) {
                                return;
                            }

                            this.applyElementOffset();

                            this.events.fire('shapechange');
                        },

                        /**
                         * Сдвигаем балун, чтобы "хвостик" указывал на точку привязки.
                         * @see https://api.yandex.ru/maps/doc/jsapi/2.1/ref/reference/IBalloonLayout.xml#event-userclose
                         * @function
                         * @name applyElementOffset
                         */
                        applyElementOffset: function () {
                            this._$element.css({
                                left: -(this._$element[0].offsetWidth / 2),
                                top: -(this._$element[0].offsetHeight + this._$element.find('.arrow')[0].offsetHeight)
                            });
                        },

                        /**
                         * Закрывает балун при клике на крестик, кидая событие "userclose" на макете.
                         * @see https://api.yandex.ru/maps/doc/jsapi/2.1/ref/reference/IBalloonLayout.xml#event-userclose
                         * @function
                         * @name onCloseClick
                         */
                        onCloseClick: function (e) {
                            e.preventDefault();

                            this.events.fire('userclose');
                        },

                        /**
                         * Используется для автопозиционирования (balloonAutoPan).
                         * @see https://api.yandex.ru/maps/doc/jsapi/2.1/ref/reference/ILayout.xml#getClientBounds
                         * @function
                         * @name getClientBounds
                         * @returns {Number[][]} Координаты левого верхнего и правого нижнего углов шаблона относительно точки привязки.
                         */
                        getShape: function () {
                            if(!this._isElement(this._$element)) {
                                return MyBalloonLayout.superclass.getShape.call(this);
                            }

                            var position = this._$element.position();

                            return new ymaps.shape.Rectangle(new ymaps.geometry.pixel.Rectangle([
                                [position.left, position.top], [
                                    position.left + this._$element[0].offsetWidth,
                                    position.top + this._$element[0].offsetHeight + this._$element.find('.arrow')[0].offsetHeight
                                ]
                            ]));
                        },

                        /**
                         * Проверяем наличие элемента (в ИЕ и Опере его еще может не быть).
                         * @function
                         * @private
                         * @name _isElement
                         * @param {jQuery} [element] Элемент.
                         * @returns {Boolean} Флаг наличия.
                         */
                        _isElement: function (element) {
                            return element && element[0] && element.find('.arrow')[0];
                        }
                    })

                    var placemark = new ymaps.Placemark([events[i].fields.coordinates_latitude, events[i].fields.coordinates_longitude], {
                        // Зададим содержимое заголовка балуна.
                        balloonContentHeader: '<h3 class="popover-title"><a href = "/events/' + events[i].pk + '">' + events[i].fields.name + '</a></h3>',
                        // Зададим содержимое основной части балуна.
                        balloonContentBody: '<div class="map-body-container">' +
                            '<div><span class="map-direction">Старшее поколение</span></div>' +
                            '<div><span>' + events[i].fields.address + '</span>' +
                            '' + date_start + ' - ' + date_end + '</div>' +
                            '</div>',
                        // Зададим содержимое нижней части балуна.
                        balloonContentFooter: 'Информация предоставлена:<br/>' + events[i].fields.name,
                        // Зададим содержимое всплывающей подсказки.
                        hintContent: events[i].fields.name
                    }, {
                        balloonShadow: false,
                        balloonLayout: MyBalloonLayout,
                        balloonPanelMaxMapArea: 0,
                        preset: 'islands#redIcon'
                    });

                    myMap.geoObjects.add(placemark);
                }
            }
        }
    }
});
