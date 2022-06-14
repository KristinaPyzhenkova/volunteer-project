let event = new Vue({
    el: '#event_modal',
    data: {
        menuEvent: false,
    },
    methods: {
        openEvent: function(){
            if (this.menuEvent) {
                this.menuEvent = false
            } else {
                this.menuEvent = true
            }
        }
    }
});
