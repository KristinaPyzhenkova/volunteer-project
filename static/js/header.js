let user = new Vue({
    el: '#nav',
    data: {
        menuUser: false,
    },
    methods: {
        openMenu: function(){

            if (this.menuUser) {
                this.menuUser = false
            } else {
                this.menuUser = true
            }
        }
    }
});
