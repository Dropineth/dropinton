import { createApp } from 'vue'
import { closeToast } from 'vant'
import './style.css'
import App from './App.vue'

(async () => {
    const request = await fetch('/api/config')
    window.CONFIG = await request.json()
    createApp(App).mount('#app')
    closeToast(true)
})()
