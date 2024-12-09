import { initUtils } from '@telegram-apps/sdk';
import WebApp from './WebApp'
import {
    showToast,
} from 'vant'

export const handleCopyInviteLink = () => {
    const user = WebApp.initDataUnsafe.user!
    navigator.clipboard
        // .writeText(process.env.NEXT_PUBLIC_BOT_USERNAME ? `https://t.me/${BOT_USERNAME}/${APP_URL_SHORT_NAME}?startapp=kentId${getUserTelegramId(userTelegramInitData) || ""}` : "https://t.me/clicker_game_news")
        .writeText(`${CONFIG.inviteUrl}?startapp=tg-${user.id}`)
        // .writeText(`https://t.me/sheep_app_bot?startapp=tg-${user.id}`)
        .then(() => {
            showToast({ type: 'success', message: 'Invite link copied to clipboard!' });
        })
        .catch(err => {
            console.error('Failed to copy text: ', err);
            showToast({ type: 'fail', message: 'Failed to copy link. Please try again.' });
        });
};

export const handleInviteFriend = () => {
    const user = WebApp.initDataUnsafe.user!
    const inviteLink = `${CONFIG.inviteUrl}?startapp=tg-${user.id}`;
    // const inviteLink = `https://t.me/sheep_app_bot?startapp=tg-${user.id}`;

    // TODO: 分享文案
    // const shareText = `🎮 Join me in Bull's Back: Earn, and Win! 🏆\n🚀 Let's play and earn together!`;
    const shareText = `${CONFIG.inviteText}`;
    console.log('shareText', shareText)

    try {
        const utils = initUtils();
        const fullUrl = `https://t.me/share/url?url=${encodeURIComponent(inviteLink)}&text=${encodeURIComponent(shareText)}`;
        utils.openTelegramLink(fullUrl);
    } catch (error) {
        console.error('Error opening Telegram link:', error);
        showToast({ type: 'fail', message: 'Failed to open sharing dialog. Please try again.' });

        // Fallback: copy the invite link to clipboard
        navigator.clipboard.writeText(inviteLink)
            .then(() => showToast({ type: 'success', message: 'Invite link copied to clipboard instead' }))
            .catch(() => showToast({ type: 'fail', message: 'Failed to share or copy invite link' }));
    }
};


export const handleShareText = () => {
    const user = WebApp.initDataUnsafe.user!
    const inviteLink = `${CONFIG.inviteUrl}?startapp=tg-${user.id}`;
    // const inviteLink = `https://t.me/sheep_app_bot?startapp=tg-${user.id}`;

    // TODO: 分享文案
    // const shareText = `🎮 Join me in Sheep: Earn, and Win! 🏆%0a🚀 Let's play and earn together!`;
    const shareText = `${CONFIG.inviteText}`;

    return shareText + "%0a" + inviteLink
}

type TelegramWindow = Window & typeof globalThis & {
    Telegram?: {
        WebApp?: {
            HapticFeedback: {
                impactOccurred: (style: 'light' | 'medium' | 'heavy') => void;
            };
        };
    };
};

export function triggerHapticFeedback(
    telegramWebApp: TelegramWindow | Window = window,
    style: 'light' | 'medium' | 'heavy' = 'medium'
) {
    if (!telegramWebApp) return;

    const vibrationEnabled = localStorage.getItem('vibrationEnabled') !== 'false';
    if (!vibrationEnabled) return;

    const hapticFeedback = (telegramWebApp as TelegramWindow).Telegram?.WebApp?.HapticFeedback;
    if (hapticFeedback?.impactOccurred) {
        hapticFeedback.impactOccurred(style);
    }
}

export const handleClickLink = (link: string | URL | undefined, target: any) => {
    triggerHapticFeedback(window);
    window.open(link, target);  //'_blank'
}
