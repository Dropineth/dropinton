import WebApp from '@twa-dev/sdk'

if (process.env.NODE_ENV === 'development') {
    WebApp.initDataUnsafe.user = {
        id: 1,
        first_name: 'Tester',
        last_name: '',
        username: 'tester',
        language_code: 'zh-hans',
        is_premium: true,
    }
    WebApp.openLink = (url: string) => {
        open(url, '_blank')
    }
    WebApp.openTelegramLink = (url: string) => {
        open(url, '_blank')
    }
}

WebApp.expand();

export default WebApp
