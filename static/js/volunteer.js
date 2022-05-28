let modal = new Vue({
    el: '#modalCert',
    data: {
        isModal: false,
        src: ''
    },
    methods: {
        openModal: function(src){
            if (this.isModal) {
                this.isModal = false
            } else {
                this.isModal = true
                this.src = src
            }
        }
    }
});
