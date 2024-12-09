import { defineConfig } from 'vite'
import { viteExternalsPlugin } from 'vite-plugin-externals';
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        viteExternalsPlugin({
            dayjs: 'dayjs',
            vue: 'Vue',
            'vant': 'vant',
        }),
    ],
    build: {
        rollupOptions: {
            external: [
                'dayjs',
                'vant',
                'vue',
            ],
            output: {
                globals: {
                    dayjs: 'dayjs',
                    'vant': 'vant',
                    vue: 'Vue',
                },
            },
        },
    },
    server: {
        hmr: true,
        host: '0.0.0.0',
        port: 5173,
        proxy: {
            '/api': {
                target: 'http://localhost:18888',
                // target: 'http://ton.ai24h.cn:16666',
                changeOrigin: true
            },
        }
    }
})
