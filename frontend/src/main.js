import { createApp } from 'vue'
import Vue from "vue"
import VueCookies from 'vue-cookies'
import App from './GamePage.vue'

Vue.use(VueCookies)

createApp(App).mount('#app')

